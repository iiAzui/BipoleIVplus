extends Node
class_name UnitAI

@export var unit_grid: UnitGrid
@export var chapter_battle: ChapterBattle

# Retro AI: all enemies attack in the order defined in the original list
func retro_ai_all_enemies():
	for unit in unit_grid.enemy_units:
		await retro_ai(unit)
		await get_tree().create_timer(0.5).timeout

# Retro AI: enemy will first try to attack/support, then move, then attack/support
func retro_ai(acting_unit: PlacedUnit):
	print(acting_unit.unit.character.display_name, " is acting")
	
	
	var action: Dictionary
	
	# First try to use attack
	action = find_usable_skill(acting_unit, true, false)
	if action:
		await chapter_battle.use_skill(acting_unit, action["target"], action["skill"])
		return
		
	# Then try to use support
	action = find_usable_skill(acting_unit, false, true)
	if action:
		await chapter_battle.use_skill(acting_unit, action["target"], action["skill"])
		return
		
	# can't do anything more if already moved
	if acting_unit.moved:
		return
		
	# Then try to move
	var starting_coords: Vector2i = acting_unit.coords
	current_path.clear()
	current_path.append(starting_coords)
	optimal_directions = [Vector2i.RIGHT, Vector2i.LEFT, Vector2i.UP, Vector2i.DOWN]
	var steps_left: int = acting_unit.unit.speed
	while steps_left > 0:
		# If could not move in any direction, break the loop
		if not try_take_step(acting_unit):
			break
		steps_left -= 1
		
		# Then try again to use attack. if skill found, break loop
		action = find_usable_skill(acting_unit, true, false)
		if action:
			break
			
		# Then try again to use support. if skill found, break loop
		action = find_usable_skill(acting_unit, false, true)
		if action:
			break
	
	# Animate move to target move location
	await acting_unit.move_animation(current_path)
	acting_unit.moved = true
	
	# Use the action if one was found
	if action:
		await chapter_battle.use_skill(acting_unit, action["target"], action["skill"])
	
# used bewteen try_take_step calls to prevent backtracking during a move.
var current_path: Array[Vector2i]
var optimal_directions: Array[Vector2i]

# Try to take a step in a random direction. Prioritize moving towards a unit on the opposite team.
# Will not move onto tiles already on the current move path.
# Return true if a step was taken, as well as add that step to the current path
func try_take_step(acting_unit: PlacedUnit) -> bool:
	if acting_unit.moved:
		return false
	
	# Loop through targets, closest targets first
	var targets: Array[PlacedUnit] = unit_grid.enemy_units if acting_unit.allied else unit_grid.allied_units
	targets.sort_custom(func(a: PlacedUnit, b: PlacedUnit): return a.coords.distance_squared_to(acting_unit.coords) < b.coords.distance_squared_to(acting_unit.coords))
	
	if not targets.is_empty():
		print("closest target to ", acting_unit.unit.character.display_name, " is ", targets[0].unit.character.display_name)
	
	# Loop through possible directions in random order
	var directions: Array[Vector2i] = [Vector2i.RIGHT, Vector2i.LEFT, Vector2i.UP, Vector2i.DOWN]
	directions.shuffle()
	
	# Check each direction to see if there is a unit this way. If so, and the target tile is not occupied, move that way
	# Also, don't move this way if it's not an optimal direction. 
	# When taking a step in a direction, the opposite direction is removed from optimal directions
	for target_unit in targets:
		for direction: Vector2i in directions:
			if not direction in optimal_directions:
				continue
			if acting_unit.coords.distance_squared_to(target_unit.coords) > (acting_unit.coords + direction).distance_squared_to(target_unit.coords):
				if not chapter_battle.is_tile_impassable(acting_unit.coords + direction) and not (acting_unit.coords + direction) in current_path:
					unit_grid.move_unit(acting_unit.coords, acting_unit.coords + direction)
					current_path.append(acting_unit.coords)
					if acting_unit.coords.x == target_unit.coords.x or acting_unit.coords.y == target_unit.coords.y:
						optimal_directions.erase(-direction)
					print("stepped to ", acting_unit.coords, " via optimal")
					return true
	
		
					
	# If no direction with an enemy in that direction was chosen, try each of the directions again but without caring if there's an enemy unit that way.
	for direction: Vector2i in directions:
		if not chapter_battle.is_tile_impassable(acting_unit.coords + direction) and not (acting_unit.coords + direction) in current_path:
			unit_grid.move_unit(acting_unit.coords, acting_unit.coords + direction)
			current_path.append(acting_unit.coords)
			print("stepped to ", acting_unit.coords, " via forced")
			return true
				
	return false

# Try to use a skill on units in range. Return true if attacked, false if no valid target found.
func find_usable_skill(acting_unit: PlacedUnit, use_attacks: bool = true, use_supports: bool = true) -> Dictionary:
	# can't use skill if already used a skill this turn
	if acting_unit.attacked:
		return {}
		
	var possible_actions: Array
	
	for skill in acting_unit.unit.moves:
		if not use_attacks and skill.move_type == "Attack":
			continue
		elif not use_supports and skill.move_type == "Support":
			continue
			
		var targets: Array[PlacedUnit] = unit_grid.allied_units if (skill.move_type == "Attack") != acting_unit.allied else unit_grid.enemy_units
		for target_unit in targets:
			var range: int = abs(target_unit.coords.x - acting_unit.coords.x) + abs(target_unit.coords.y - acting_unit.coords.y)
			if range >= skill.min_range and range <= skill.max_range:
				# Damage dealt if attack, heal amount if support
				var damage: int
				if skill.move_type == "Attack":
					damage = skill.get_damage_dealt(acting_unit.unit, target_unit.unit)
					damage = min(damage, target_unit.unit.hp)
				else:
					damage = skill.get_heal_amount(acting_unit.unit, target_unit.unit)
					damage = min(damage, target_unit.unit.max_hp - target_unit.unit.hp)
				
				
				# Can use this skill on the target
				possible_actions.append({
					"skill": skill,
					"target": target_unit,
					"damage": damage
				})
	
	# sort by damage dealt/HP healed. Prioritize the skill that will deal the most damage or heal the most HP
	possible_actions.sort_custom(func(a, b): return a.damage > b.damage)
	
	if not possible_actions.is_empty():
		var action = possible_actions[0]
		if action["damage"] > 0:
			return action
		else:
			print("all possible attacks would deal 0 damage / heal 0 hp")
			return {}
	else:
		print("no possible attacks" if not use_supports else ("no possible supports" if not use_attacks else "no possible skills"))
		return {}

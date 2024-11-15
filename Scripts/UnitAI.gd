extends Node
class_name UnitAI

@export var unit_grid: UnitGrid
@export var chapter_battle: ChapterBattle

# Retro AI: all enemies attack in the order defined in the original list
func retro_ai_all_enemies():
	for unit in unit_grid.enemy_units:
		retro_ai(unit)
		await get_tree().create_timer(0.5).timeout

# Retro AI: enemy will first try to attack/support, then move, then attack/support
func retro_ai(acting_unit: PlacedUnit):
	# Try to use attacks first on units in range
	if await try_skill(acting_unit, true, false):
		return
		
	# Then try to use supports on units in range
	if await try_skill(acting_unit, false, true):
		return
		
	# Then try to move
	try_move(acting_unit)
		
	# Then try again to use attack
	if await try_skill(acting_unit, true, false):
		return
		
	# Then try again to use supports
	if await try_skill(acting_unit, false, true):
		return

# Try to move, prioritizing moving towards a unit on the opposite team.
# Returns the amount of tiles moved
func try_move(acting_unit: PlacedUnit) -> int:
	if acting_unit.moved:
		return false
		
	# Move in a random direction
	# Prioritize directions that have at least one unit on the opposite team
	
	var starting_coords: Vector2i = acting_unit.coords
	current_path.clear()
	current_path.append(starting_coords)
	var steps_left: int = acting_unit.unit.speed
	while steps_left > 0:
		# If could not move in any direction, break the loop
		if not try_take_step(acting_unit):
			break
		steps_left -= 1
		
	unit_grid.move_unit(starting_coords, acting_unit.coords)
		
	acting_unit.moved = true
	return acting_unit.unit.speed - steps_left
	
# used bewteen try_take_step calls to prevent backtracking during a move.
var current_path: Array[Vector2i]

# Try to take a step in a random direction. Prioritize moving towards a unit on the opposite team.
# Will not move onto tiles already on the current move path.
# Return true if a step was taken, as well as add that step to the current path
func try_take_step(acting_unit: PlacedUnit, ) -> bool:
	var targets: Array[PlacedUnit] = unit_grid.enemy_units if acting_unit.allied else unit_grid.allied_units
	var directions: Array[Vector2i] = [Vector2i.RIGHT, Vector2i.LEFT, Vector2i.UP, Vector2i.DOWN]
	directions.shuffle()
	
	# Check each direction to see if there is a unit this way. If so, and the target tile is not occupied, move that way
	for direction: Vector2i in directions:
		for target_unit in targets:
			if acting_unit.coords.distance_squared_to(target_unit.coords) > (acting_unit.coords + direction).distance_squared_to(target_unit.coords):
				if not chapter_battle.is_tile_impassable(acting_unit.coords + direction) and not (acting_unit.coords + direction) in current_path:
					acting_unit.coords = acting_unit.coords + direction
					current_path.append(acting_unit.coords)
					return true
					
	# If no direction with an enemy in that direction was chosen, try each of the directions again but without caring if there's an enemy unit that way.
	for direction: Vector2i in directions:
		if not chapter_battle.is_tile_impassable(acting_unit.coords + direction) and not (acting_unit.coords + direction) in current_path:
			acting_unit.coords = acting_unit.coords + direction
			current_path.append(acting_unit.coords)
			return true
				
	return false

# Try to use a skill on units in range. Return true if attacked, false if no valid target found.
func try_skill(acting_unit: PlacedUnit, use_attacks: bool = true, use_supports: bool = true) -> bool:
	# can't attack if already attacked
	if acting_unit.attacked:
		return false
		
	var possible_actions: Array
	
	for skill in acting_unit.unit.moves:
		if not use_attacks and skill.move_type == "Attack":
			return false
		elif not use_supports and skill.move_type == "Support":
			return false
			
		var targets: Array[PlacedUnit] = unit_grid.allied_units if (skill.move_type == "Attack") != acting_unit.allied else unit_grid.enemy_units
		for target_unit in targets:
			var range: int = abs(target_unit.coords.x - acting_unit.coords.x) + abs(target_unit.coords.y - acting_unit.coords.y)
			if range >= skill.min_range and range <= skill.max_range:
				# Damage dealt if attack, heal amount if support
				var damage: int
				if skill.move_type == "Attack":
					damage = skill.get_damage_dealt(acting_unit.unit, target_unit.unit)
				else:
					damage = skill.get_heal_amount(acting_unit.unit, target_unit.unit)
				damage = min(damage, target_unit.unit.hp)
				
				# Can use this skill on the target
				possible_actions.append({
					"skill": skill,
					"target": target_unit,
					"damage": damage
				})
	
	# Prioritize the skill that will deal the most damage or heal the most HP
	possible_actions.sort_custom(func(a, b): return a.damage > b.damage)
	print(possible_actions)
	
	if not possible_actions.is_empty():
		var action = possible_actions[0]
		await chapter_battle.use_skill(acting_unit, action["target"], action["skill"])
		return true
	else:
		return false

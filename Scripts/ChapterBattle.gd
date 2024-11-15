class_name ChapterBattle
extends Node3D

# If this is non-null, all the enemies from this CHapterPlacements objects will be placed when the battle begins
# Used to store placements in a file instead of a scene.
# this method of transfer works better for the retro files, 
# since I don't want to figure out how to make a whole scene based off that data
@export var placements: ChapterPlacements

@export var allied_unit_preview: UnitPreview
@export var enemy_unit_preview: UnitPreview
@export var damage_preview_panel: DamagePreviewPanel
@export var move_select_panel: MoveSelectPanel
@export var attack_button: Button

@export var unit_grid: UnitGrid
@export var map_cursor: MapCursor
@export var range_display_grid: Node3D
@export var move_path_line: Line2D
@export var attack_path_line: Line2D
@export var outgoing_hit_percent: Control
@export var incoming_hit_percent: Control
@export var outgoing_hit_percent_label: Label
@export var incoming_hit_percent_label: Label

@export var battle_camera: BattleCamera

const MOVE_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/MoveTileHighlight.tscn")
const ATTACK_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/AttackTileHighlight.tscn")
const SUPPORT_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/SupportTileHighlight.tscn")

const RETRO_WIDTH: int = 19
const RETRO_HEIGHT: int = 14

const TILE_SIZE: float = 64.0

var is_player_turn: bool = true

## Current coordinates of the player's cursor. Used for unit selection, move destination, attack target, etc.
var cursor_coords: Vector2i = Vector2i(-1, -1)

## Current selected unit for moving/attacking.
var unit_selected: PlacedUnit

## Current attack/support move selected for the unit selected.
var move_selected_index: int
var move_selected: Move

## The unit currently hovered by the cursor.
var hovered_unit: PlacedUnit

## Current cursor mode ("Select", "Move", "Attack")
var cursor_mode: CursorMode = CursorMode.SELECT
enum CursorMode {
	## Cursor selecting a unit to move/attack.
	SELECT,
	## Moving the unit
	MOVING,
	## Using an attack or support type move.
	ATTACKING
}

# The current tiles the selected unit can move to, as calculated from the last show_range call.
# Store the Vector2i coords as keys as the amount of moves left when moving to that tile.
var moveable_tiles: Dictionary

# Tiles that the player's skill cursor can move on. Contains the amount of skill range steps left as the value.
var skill_range_tiles: Dictionary

# Tiles that can be the destination of an attack or the player's current Attack type move. 
# Will not include tiles that require a range lower than the current move's min_range.
# Automatically added in spread_range if current range is within the current move or set of moves' min and max range.
var attackable_tiles: Dictionary

# Same as attackable_tiles but for support moves
var supportable_tiles: Dictionary

# DIsplayed range for the current move, or shared mix/max of all moves if no move selected yet
var displayed_min_attack_range: int
var displayed_max_attack_range: int

# used when recursively mapping out attack/support range
var lowest_attack_range: int = 99
var lowest_support_range: int = 99
var highest_attack_range: int = -1
var highest_support_range: int = -1

var move_range_iterations: int
var skill_range_iterations: int

## When in move/attack mode, the current tile path.
var current_path: Array[Vector2i]

func _ready() -> void:
	place_player_units()
	place_enemy_units()
	change_cursor_mode(CursorMode.SELECT)
	allied_unit_preview.display_unit(null)
	enemy_unit_preview.display_unit(null)
	move_cursor_to(Vector2i.ZERO)
	damage_preview_panel.hide()
	attack_button.hide()
	outgoing_hit_percent.hide()
	incoming_hit_percent.hide()
	
	#call_deferred("grab_focus")

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("Left"):
		move_cursor(Vector2i.LEFT)
	elif event.is_action_pressed("Right"):
		move_cursor(Vector2i.RIGHT)
	elif event.is_action_pressed("Up"):
		move_cursor(Vector2i.UP)
	elif event.is_action_pressed("Down"):
		move_cursor(Vector2i.DOWN)
	elif event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
			var space_state := get_world_3d().direct_space_state
			var cam := get_viewport().get_camera_3d()
			
			var origin = cam.project_ray_origin(event.position)
			var end = origin + cam.project_ray_normal(event.position) * 1000
			var query = PhysicsRayQueryParameters3D.create(origin, end)
			
			var result := space_state.intersect_ray(query)
		
			if result:
				var coords: Vector2i = round(Vector2i(result.position.x + 0.5, result.position.z + 0.5))
				if is_coords_in_bounds(coords):
					# Press the tile if it is already hovered when clicking it
					if coords == cursor_coords:
						on_tile_pressed()
					# Otherwise, hover the clicked tile
					else:
						move_cursor_to(coords)
		elif event.button_index == MOUSE_BUTTON_WHEEL_UP:
			prev_move()
		elif event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
			next_move()
	elif event.is_action_pressed("Esc"):
		if cursor_mode != CursorMode.SELECT:
			change_cursor_mode(CursorMode.SELECT)
			show_range(hovered_unit)
	elif event.is_action_pressed("Select"):
		on_tile_pressed()
	elif event.is_action_pressed("Move"):
		on_move_pressed()
	elif event.is_action_pressed("Skill"):
		on_skill_pressed()
	elif event.is_action_pressed("1"):
		select_move(0)
	elif event.is_action_pressed("2"):
		select_move(1)
	elif event.is_action_pressed("3"):
		select_move(2)
	elif event.is_action_pressed("4"):
		select_move(3)
	elif event.is_action_pressed("5"):
		select_move(4)
	elif event.is_action_pressed("6"):
		select_move(5)
	elif event.is_action_pressed("7"):
		select_move(6)
		
func on_move_pressed():
	if cursor_mode == CursorMode.MOVING:
		on_tile_pressed()
	else:
		if hovered_unit and hovered_unit.allied == is_player_turn and !hovered_unit.moved:
			unit_selected = hovered_unit
			change_cursor_mode(CursorMode.MOVING)
	
func on_skill_pressed():			
	if cursor_mode == CursorMode.ATTACKING:
		on_tile_pressed()
	else:
		if hovered_unit and hovered_unit.allied == is_player_turn and !hovered_unit.attacked:
			unit_selected = hovered_unit
			change_cursor_mode(CursorMode.ATTACKING)
		
func on_tile_pressed():
	if cursor_mode == CursorMode.SELECT and hovered_unit and hovered_unit.allied == is_player_turn:
		unit_selected = hovered_unit
		if hovered_unit:
			if !hovered_unit.moved:
				change_cursor_mode(CursorMode.MOVING)
			elif !hovered_unit.attacked:
				change_cursor_mode(CursorMode.ATTACKING)
	elif cursor_mode == CursorMode.MOVING:
		# if pressing tile outside of move range (or trying to move in place), return
		if not cursor_coords in moveable_tiles:
			move_cursor_to(unit_selected.coords)
			change_cursor_mode(CursorMode.SELECT)
			show_range(hovered_unit)
			return
			
		unit_grid.move_unit(unit_selected.coords, cursor_coords)
		unit_selected.moved = true
		hovered_unit = unit_selected
		change_cursor_mode(CursorMode.SELECT)
		show_range(hovered_unit)
	elif cursor_mode == CursorMode.ATTACKING:
		attack_pressed()
		
func attack_pressed():
	if cursor_mode != CursorMode.ATTACKING:
		printerr("attack somehow pressed while not in attack mode")
		return
	
	if not move_selected:
		auto_select_move()
		
	if not (cursor_coords in attackable_tiles) and not (cursor_coords in supportable_tiles):
		#move_cursor_to(unit_selected.coords)
		#hovered_unit = unit_selected
		#change_cursor_mode(CursorMode.SELECT)
		#show_range(hovered_unit)
		print("clicked outside of attackable/supportable tiles")
		return
		
	# If there isn't a unit here, return
	if not hovered_unit:
		#move_cursor_to(unit_selected.coords)
		#hovered_unit = unit_selected
		#change_cursor_mode(CursorMode.SELECT)
		#show_range(hovered_unit)
		print("no unit here")
		return
		
	if hovered_unit.allied != (move_selected.move_type == "Support"):
		#change_cursor_mode(CursorMode.SELECT)
		#show_range(hovered_unit)
		print("wrong unit select type for selected move")
		return
	
	if move_selected:
		## TODO: implement attacking, and selecting move for that matter
		var attacker: PlacedUnit = unit_selected
		var defender: PlacedUnit = hovered_unit
		var move: Move = move_selected
		unit_selected.moved = true # Cannot move after attack
		unit_selected.attacked = true
		print("used skill ", move_selected.display_name)
		
		hovered_unit = unit_selected
		select_move(-1)
		show_range(null)
		change_cursor_mode(CursorMode.SELECT)
		map_cursor.modulate = Color.TRANSPARENT
		
		battle_camera.combat_view(attacker, defender)
		await get_tree().create_timer(0.25).timeout
		
		# Skill
		var skill_damage: int = move.get_damage_dealt(attacker.unit, defender.unit)
		defender.unit.take_damage(skill_damage)
		await attack_animation(attacker, defender, move, skill_damage)
		await get_tree().create_timer(0.25).timeout
		
		if defender.unit.is_alive() and attacker.unit.is_alive() and unit_in_range(defender, attacker):
			var counter_damage: int = defender.unit.get_counter_damage(attacker.unit)
			if counter_damage > 0:
				defender.unit.take_damage(skill_damage)
				await attack_animation(defender, attacker, null, counter_damage)
				await get_tree().create_timer(0.25).timeout
			
		var followup_attacker: PlacedUnit
		var followup_defender: PlacedUnit
		if attacker.unit.speed > defender.unit.speed:
			followup_attacker = attacker
			followup_defender = defender
		elif attacker.unit.speed < defender.unit.speed:
			followup_attacker = defender
			followup_defender = attacker
			
		if followup_attacker and followup_attacker.unit.is_alive() and followup_defender.unit.is_alive() and unit_in_range(followup_attacker, followup_defender):
			var followup_damage: int = followup_attacker.unit.get_counter_damage(followup_defender.unit)
			if followup_damage > 0:
				followup_defender.unit.take_damage(followup_damage)
				await attack_animation(followup_attacker, followup_defender, null, followup_damage)
				await get_tree().create_timer(0.25).timeout
		
		await get_tree().create_timer(0.25).timeout
		battle_camera.standard_view()
		
		if not attacker.unit.is_alive():
			unit_grid.erase_unit(attacker.coords)
		if not defender.unit.is_alive():
			unit_grid.erase_unit(defender.coords)
		
		change_cursor_mode(CursorMode.SELECT)
		show_range(unit_selected)
	else:
		printerr("a move should be selected while in attack mode! there is none selected")
		
func attack_animation(attacker: PlacedUnit, target: PlacedUnit, move: Move, damage: int):
	await attacker.attack_animation(target, move, damage)

func place_player_units():
	if not SaveData.save:
		printerr("no save data loaded but trying to load units!")
		return
	
	# Spawn along the bottom row in retro mode.
	# Once non retro modes are added this will need new code
	var place_coords := Vector2i(0, 12)
	
	for i in len(SaveData.save.units):
		var unit: Unit = SaveData.save.units[i]
		var placed_unit: PlacedUnit = unit_grid.PLACED_UNIT_SCENE.instantiate()
		placed_unit.allied = true
		placed_unit.unit = unit
		unit_grid.place_unit(placed_unit, place_coords)
		
		place_coords.x += 1
		if place_coords.x >= ChapterBattle.RETRO_WIDTH:
			place_coords.x = 0
			place_coords.y += 1
		
func place_enemy_units():
	if not placements:
		printerr("no placements defined but trying to load placements from file!")
		return
		
	for i in len(placements.unit_names):
		var unit_name: String = placements.unit_names[i]
		var unit_coords: Vector2i = placements.unit_coords[i]
		var unit: Unit = ResourceLoader.load("res://Database/EnemyUnits/"+unit_name+".tres")
		var placed_unit: PlacedUnit = unit_grid.PLACED_UNIT_SCENE.instantiate()
		placed_unit.allied = false
		placed_unit.unit = unit
		unit_grid.place_unit(placed_unit, unit_coords)
		
		
func is_coords_in_bounds(coords: Vector2i):
	return coords.x >= 0 and coords.x < RETRO_WIDTH and coords.y >= 0 and coords.y < RETRO_HEIGHT
		
func move_cursor(offset: Vector2i):
	move_cursor_to(cursor_coords + offset)

func move_cursor_to(coords: Vector2i):
	if coords == cursor_coords:
		return
	
	cursor_coords = coords
	cursor_coords.x = clamp(cursor_coords.x, 0, RETRO_WIDTH-1)
	cursor_coords.y = clamp(cursor_coords.y, 0, RETRO_HEIGHT-1)
	#print("moved cursor to ", cursor_coords)
	map_cursor.position = Vector3(cursor_coords.x, 0.025, cursor_coords.y)
	
	hovered_unit = unit_grid.get_unit_at(cursor_coords)
	
	# For debugging
	if cursor_coords in skill_range_tiles:
		var hovered_tiles_left: int = skill_range_tiles[cursor_coords]
		#print("hovered tile steps left: ", hovered_tiles_left)
		#print("hover range: ", displayed_max_attack_range - hovered_tiles_left)
	
	if cursor_mode == CursorMode.SELECT:
		allied_unit_preview.display_unit(hovered_unit)
		show_range(hovered_unit)
	elif cursor_mode == CursorMode.MOVING or cursor_mode == CursorMode.ATTACKING:
		# When in attacking or moving, display any enemies hovered over on right, 
		# while moving/attacking unit is still displayed on left.
		if move_selected:
			display_hovered_skill_target()
		elif hovered_unit:
			enemy_unit_preview.display_unit(hovered_unit if hovered_unit and !hovered_unit.allied else null)
		
		var valid_range: Dictionary = moveable_tiles if cursor_mode == CursorMode.MOVING else skill_range_tiles
		if not (coords in valid_range or coords == unit_selected.coords):
			return
		
		# if cursor intersects itself, shrink path back to that position
		if cursor_coords in current_path:
			var last: Vector2i = current_path.pop_back()
			while last != cursor_coords:
				last = current_path.pop_back()
		
		# If moving farther than speed allows
		# recalculate the path to reach that tile with the minimum changes
		# also recalculate if path intersects itself	
		if len(current_path) > unit_selected.unit.speed:
			recalculate_path_to(cursor_coords)
		# simply add an adjacent point if the new point is adjacent to the last
		# allows click-drag or arrow keys to map out specific paths
		elif not current_path.is_empty() and abs(cursor_coords.x - current_path.back().x) + abs(cursor_coords.y - current_path.back().y) == 1:
			current_path.append(cursor_coords)
			refresh_path()
		# otherwise, just recalculate the path to the point
		else:
			recalculate_path_to(cursor_coords)

func display_hovered_skill_target():
	if (cursor_coords in attackable_tiles or cursor_coords in supportable_tiles) and hovered_unit and move_selected and hovered_unit.allied == (move_selected.move_type == "Support"):
		enemy_unit_preview.display_unit(hovered_unit)
		
		var skill_damage: int = move_selected.get_damage_dealt(unit_selected.unit, hovered_unit.unit)
		var counter_damage: int = hovered_unit.unit.get_counter_damage(unit_selected.unit)
		var ally_counter_damage: int = unit_selected.unit.get_counter_damage(hovered_unit.unit) 
		var enemy_counter_damage: int = hovered_unit.unit.get_counter_damage(unit_selected.unit)
		
		var damage_dealt: int = skill_damage
		var damage_taken: int = 0
		
		var outgoing_hit_chance: float = move_selected.get_hit_chance(unit_selected.unit, hovered_unit.unit)
		var incoming_hit_chance: float = move_selected.get_hit_chance(hovered_unit.unit, unit_selected.unit)
		
		outgoing_hit_percent_label.text = str(round(outgoing_hit_chance*100))+"%"
		incoming_hit_percent_label.text = str(round(incoming_hit_chance*100))+"%"
		
		var in_counter_range: bool = unit_in_range(unit_selected, hovered_unit)
		if in_counter_range:
			damage_taken += enemy_counter_damage
			
				
		damage_preview_panel.skill_preview.display(skill_damage, true)
		damage_preview_panel.counter_preview.display(enemy_counter_damage if in_counter_range else 0, false)
		
		if unit_selected.unit.speed > hovered_unit.unit.speed:
			damage_dealt += ally_counter_damage
			damage_preview_panel.followup_preview.display(ally_counter_damage, true)
		elif unit_selected.unit.speed < hovered_unit.unit.speed:
			damage_taken += enemy_counter_damage
			damage_preview_panel.followup_preview.display(enemy_counter_damage, false)
		else:
			damage_preview_panel.followup_preview.display(0, false)
		
		allied_unit_preview.display_damage_preview(unit_selected, damage_taken)
		enemy_unit_preview.display_damage_preview(hovered_unit, damage_dealt)
		damage_preview_panel.show()
		outgoing_hit_percent.show()
		incoming_hit_percent.show()
		attack_button.show()
		outgoing_hit_percent_label
	else:
		enemy_unit_preview.display_unit(null)
		damage_preview_panel.hide()
		attack_button.hide()
		outgoing_hit_percent.hide()
		incoming_hit_percent.hide()

func change_cursor_mode(mode: CursorMode):
	cursor_mode = mode
	if mode == CursorMode.SELECT:
		map_cursor.modulate = map_cursor.select_color
		select_move(-1)
		end_move_path()
		unit_selected = null
		allied_unit_preview.display_unit(hovered_unit)
		enemy_unit_preview.display_unit(null)
		move_select_panel.show_move(null)
		damage_preview_panel.hide()
		attack_button.hide()
		outgoing_hit_percent.hide()
		incoming_hit_percent.hide()
	elif mode == CursorMode.MOVING:
		map_cursor.modulate = map_cursor.move_color
		start_path()
		move_select_panel.show_move(null)
	elif mode == CursorMode.ATTACKING:
		map_cursor.modulate = map_cursor.attack_color
		# TODO: select by arrow keys, change selection by scroll wheel, may want to select via a menu
		start_path()
		select_move(0)
		display_hovered_skill_target()
		
	if move_path_line: move_path_line.visible = cursor_mode == CursorMode.MOVING
	if attack_path_line: attack_path_line.visible = cursor_mode == CursorMode.ATTACKING
	
func unit_in_range(attacker: PlacedUnit, defender: PlacedUnit) -> bool:
	var range: int = abs(defender.coords.x - attacker.coords.x) + abs(defender.coords.y - attacker.coords.y)
	print("target range: ", range)
	var in_counter_range: bool = false
	for move in hovered_unit.unit.moves:
		print(move.display_name, " range: ", move.min_range, "-", move.max_range)
		if range >= move.min_range and range <= move.max_range:
			return true
			
	return false
	
func auto_select_move():	
	# Loop through the moves until one can hit the target unit
	var attack_range_remaining: int = attackable_tiles[cursor_coords] if cursor_coords in attackable_tiles else -1
	var support_range_remaining: int = supportable_tiles[cursor_coords] if cursor_coords in supportable_tiles else -1
	
	for i in len(unit_selected.unit.moves):
		var move: Move = unit_selected.unit.moves[i]
		var range_remaining: int = attack_range_remaining if move.move_type == "Attack" else support_range_remaining
		var range_required: int = displayed_max_attack_range - range_remaining + 1
		print(move.display_name, " range required: ", range_required)
		if move.min_range <= range_required and move.max_range >= range_required:
			# select this move
			select_move(i)
			break
			
	# if a suitable skill was not found to hit this tile, return and move cursor back to selected unit
	if not move_selected:
		hovered_unit = unit_selected
		move_cursor_to(unit_selected.coords)
		change_cursor_mode(CursorMode.SELECT)
		return
	else:
		display_hovered_skill_target()
		# if a move was selected, don't immediately use the skill. 
		# return here and wait for another input for confirmation to use the auto selected skill.
		return
		
func select_move(move_index: int):
	if move_index < 0:
		move_selected_index = -1;
		move_selected = null
		move_select_panel.show_move(null)
		return
		
	if not unit_selected:
		# If move is selectable on the hovered unit in select mode, select the unit and the move and go straight into attack mode
		if cursor_mode == CursorMode.SELECT and hovered_unit and move_index < len(hovered_unit.unit.moves):
			unit_selected = hovered_unit
			change_cursor_mode(CursorMode.ATTACKING)
			await get_tree().process_frame
			
	# otherwise, if a unit is selected but the move index requested is outside its move list range, ignore the input
	elif move_index >= len(unit_selected.unit.moves):
		return
		
	if not unit_selected:
		return
	
	move_selected_index = move_index
	move_selected = unit_selected.unit.moves[move_index]
	print("selected move ", move_selected.display_name, " (slot ", move_index, ")")
	map_cursor.modulate = map_cursor.support_color if move_selected.move_type == "Support" else map_cursor.attack_color
	display_hovered_skill_target()
	
	show_range(unit_selected) # update range to not include move range in case havent moved yet
	move_select_panel.show_move(move_selected)
	if len(unit_selected.unit.moves) > 1:
		move_select_panel.show_arrows()
	else:
		move_select_panel.hide_arrows()
	
func next_move():
	if not unit_selected or len(unit_selected.unit.moves) < 2:
		return
	move_selected_index += 1
	if move_selected_index >= len(unit_selected.unit.moves):
		move_selected_index = 0
	elif move_selected_index < 0:
		move_selected_index = len(unit_selected.unit.moves) - 1
		
	select_move(move_selected_index)
	
func prev_move():
	if not unit_selected or len(unit_selected.unit.moves) < 2:
		return
	move_selected_index -= 1
	if move_selected_index >= len(unit_selected.unit.moves):
		move_selected_index = 0
	elif move_selected_index < 0:
		move_selected_index = len(unit_selected.unit.moves) - 1
		
	select_move(move_selected_index)
	
func start_path():
	current_path.clear()
	current_path.append(unit_selected.coords)
	refresh_path()

func refresh_path():
	if cursor_mode == CursorMode.MOVING:
		if move_path_line: 
			move_path_line.visible = true
			move_path_line.clear_points()
			for coords in current_path:
				move_path_line.add_point(coords * TILE_SIZE)
		if attack_path_line:
			attack_path_line.visible = false
	elif cursor_mode == CursorMode.ATTACKING:
		if move_path_line:
			move_path_line.visible = false
		if attack_path_line:
			attack_path_line.visible = true
			attack_path_line.clear_points()
			for coords in current_path:
				attack_path_line.add_point(coords * TILE_SIZE)
	else:
		if move_path_line: move_path_line.visible = false
		if attack_path_line: attack_path_line.visible = false
		
# Return tru ewhen a path is found
func recalculate_path_to(target_coords: Vector2i):
	current_path.clear()
	
	if cursor_mode == CursorMode.MOVING:
		search_for_path(unit_selected.coords, target_coords, unit_selected.unit.speed+1)
	elif cursor_mode == CursorMode.ATTACKING:
		search_for_path(unit_selected.coords, target_coords, displayed_max_attack_range+1)
	
	refresh_path()

func search_for_path(coords: Vector2i, target_coords: Vector2i, steps_left: int) -> bool:
	# Can't move here if not movable/attack (ignore if on starting tile)
	if not coords in (moveable_tiles if cursor_mode == CursorMode.MOVING else skill_range_tiles) and coords != unit_selected.coords:
		return false
	
	# "Take" the "step" for this possible path
	steps_left -= 1
	
	# Return true if the target position was reached
	if coords == target_coords:
		current_path.append(coords)
		return true
		
	# Can't take any more steps
	if steps_left == 0:
		return false
		
	# If there's not enough steps to reach the target position, return false
	var distance: int = abs(target_coords.x - coords.x) + abs(target_coords.y - coords.y)
	if distance > steps_left:
		return false
		
	# Add to the ongoing path, this will get cleared after all the directional checks and possible branching paths
	current_path.append(coords)
	
	# If any branches find the target successfully, return true to prevent popping back 
	# or checking any more unneccesary brnaches
	var right_first := coords.x < target_coords.x and coords.y <= target_coords.y
	if right_first:
		if search_for_path(coords + Vector2i.RIGHT, target_coords, steps_left): return true
	var left_first := coords.x > target_coords.x and coords.y >= target_coords.y
	if left_first:
		if search_for_path(coords + Vector2i.LEFT, target_coords, steps_left): return true
	var down_first := coords.y < target_coords.y and coords.x >= target_coords.x
	if down_first:
		if search_for_path(coords + Vector2i.DOWN, target_coords, steps_left): return true
	var up_first := coords.y > target_coords.y and coords.x <= target_coords.x
	if up_first:
		if search_for_path(coords + Vector2i.UP, target_coords, steps_left): return true
		
	if not right_first:
		if search_for_path(coords + Vector2i.RIGHT, target_coords, steps_left): return true
	if not left_first:
		if search_for_path(coords + Vector2i.LEFT, target_coords, steps_left): return true
	if not down_first:
		if search_for_path(coords + Vector2i.DOWN, target_coords, steps_left): return true
	if not up_first:
		if search_for_path(coords + Vector2i.UP, target_coords, steps_left): return true
		
	# If none of the branches reached the target, remove so the next branches can replace this
	current_path.pop_back()
	return false

func end_move_path():
	if move_path_line: move_path_line.visible = false

func show_range(unit: PlacedUnit):	
	for child in range_display_grid.get_children():
		child.queue_free()
		
	moveable_tiles.clear()
	skill_range_tiles.clear()
	attackable_tiles.clear()
	supportable_tiles.clear()
	
	if not unit or not unit.unit:
		return

	if move_selected:
		displayed_min_attack_range = move_selected.min_range
		displayed_max_attack_range = move_selected.max_range
		lowest_attack_range = move_selected.min_range if move_selected.move_type == "Attack" else 99
		lowest_support_range = move_selected.min_range if move_selected.move_type == "Support" else 99
		highest_attack_range = move_selected.max_range if move_selected.move_type == "Attack" else 0
		highest_support_range = move_selected.max_range if move_selected.move_type == "Support" else 0
	else:
		lowest_attack_range = 99
		lowest_support_range = 99
		highest_attack_range = -1
		highest_support_range = -1
		for move in unit.unit.moves:
			if move.move_type == "Attack":
				lowest_attack_range = min(lowest_attack_range, move.min_range)
				highest_attack_range = max(highest_attack_range, move.max_range)
			elif move.move_type == "Support":
				lowest_support_range = min(lowest_support_range, move.min_range)
				highest_support_range = max(highest_support_range, move.max_range)
				
		displayed_min_attack_range = min(lowest_attack_range, lowest_support_range)
		displayed_max_attack_range = max(highest_attack_range, highest_support_range)
		
	#print("attack range: ", lowest_attack_range, "-", highest_attack_range)
	#print("support range: ", lowest_support_range, "-", highest_support_range)
	#print("displayed range: ", displayed_min_attack_range, "-", displayed_max_attack_range)
	
	move_range_iterations = 0
	skill_range_iterations = 0
	spread_range(unit.coords, unit, 0 if unit.moved or cursor_mode == CursorMode.ATTACKING else unit.unit.speed)
	print("move range search iterations: ", move_range_iterations)
	print("skill range search iterations: ", skill_range_iterations)
	
	# can't move in place
	moveable_tiles.erase(unit.coords)
	
	# can't attack self
	attackable_tiles.erase(unit.coords)
	
	for coords in moveable_tiles.keys():
		place_highlight(MOVE_TILE_HIGHLIGHT, coords)
	
	for coords in attackable_tiles.keys():
		# Don't show the attack square if unit can move here, blue square should be shown instead
		if coords in moveable_tiles.keys():
			continue
			
		# If there is another unit here, don't show a red square if it's another ally here.
		# (Empty squares will still have a red square)
		var other_unit: PlacedUnit = unit_grid.get_unit_at(coords)
		if other_unit and other_unit.allied == unit.allied:
			continue
			
		place_highlight(ATTACK_TILE_HIGHLIGHT, coords)
		
	for coords in supportable_tiles.keys():
		# if player can move or attack here, don't show a support highlight
		if coords in moveable_tiles.keys():
			continue
		if coords in attackable_tiles.keys():
			continue
			
		# there has to be an ally here to show the supportable highlight
		var other_unit: PlacedUnit = unit_grid.get_unit_at(coords)
		if not other_unit or other_unit.allied == unit.allied:
			place_highlight(SUPPORT_TILE_HIGHLIGHT, coords)

		
func place_highlight(highlight_scene: PackedScene, coords: Vector2i):
	var highlight: Node3D = highlight_scene.instantiate()
	highlight.position = Vector3(coords.x, 0, coords.y);
	range_display_grid.add_child(highlight)
	
# Mark how many moves remaining at the coords, and spreads movable/attackable range to adjacent tiles
func spread_range(coords: Vector2i, unit: PlacedUnit, move_remaining: int):
	# Can't move on this tile if it is solid / there is a unit here
	# (ignore this if this tile is where the unit currently is)
	if is_tile_impassable(coords) and not (unit.coords == coords):
		return
	
	# If already marked as moveable, stop if unit can already reach this tile in fewer moves
	if moveable_tiles.has(coords) and moveable_tiles[coords] > move_remaining:
		return
		
	# Mark as a valid move location and mark the value as the moves it took to get here
	moveable_tiles[coords] = move_remaining
	move_range_iterations += 1
	
	# Spread attack range from this position that the unit can reach
	spread_attack_range(coords, unit, 0 if unit.attacked else displayed_max_attack_range)
	
	if move_remaining <= 0:
		return
	# Consume a move tile
	move_remaining -= 1
		
	# Try to spread move range to adjacent tiles
	spread_range(coords + Vector2i.UP, unit, move_remaining)
	spread_range(coords + Vector2i.RIGHT, unit, move_remaining)
	spread_range(coords + Vector2i.DOWN, unit, move_remaining)
	spread_range(coords + Vector2i.LEFT, unit, move_remaining)
	
func spread_attack_range(coords: Vector2i, unit: PlacedUnit, range_remaining: int):
	# stop if cursor is OOB
	if not is_coords_in_bounds(coords):
		return
		
	# if currently on this tile on or above min and on or below max,
	# mark as attackable/supportable
	var range = displayed_max_attack_range - range_remaining
	if range >= lowest_attack_range and range <= highest_attack_range and not (coords in attackable_tiles):
		attackable_tiles[coords] = true
	if range >= lowest_support_range and range <= highest_support_range and not (coords in supportable_tiles):
		supportable_tiles[coords] = true
	
	# If renaining range is above 500, considered infinite,
	# doesn't matter if this has been reached in fewer moves, all other tiles will be be reached either way.
	if range_remaining > 500:
		if skill_range_tiles.has(coords):
			return
	#else:
		## If already marked as attackable, stop if unit can already reach this tile in fewer moves
		#if skill_range_tiles.has(coords) and skill_range_tiles[coords] >= range_remaining:
			#return
		
	skill_range_tiles[coords] = range_remaining
	skill_range_iterations += 1
	
	if range_remaining <= 0:
		return
	range_remaining -= 1
	
	spread_attack_range(coords + Vector2i.UP, unit, range_remaining)
	spread_attack_range(coords + Vector2i.RIGHT, unit, range_remaining)
	spread_attack_range(coords + Vector2i.DOWN, unit, range_remaining)
	spread_attack_range(coords + Vector2i.LEFT, unit, range_remaining)
	
# Return true if this tile is either out of bounds or there is a solid tile here (for non retro mode).
func is_tile_solid(coords: Vector2i):
	return not is_coords_in_bounds(coords);
	
# True if the given tile is solid or there is a unit there (allied or enemy).
# Units can only move on non-solid tiles
func is_tile_impassable(coords: Vector2i):
	# If there is a solid tile here / coord is outside the map, return true
	if is_tile_solid(coords):
		return true
		
	# If there is a unit here return true
	if unit_grid.get_unit_at(coords):
		return true
	
	# otherwise this tile is open	
	return false

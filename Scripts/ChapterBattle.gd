class_name ChapterBattle
extends Control

# If this is non-null, all the enemies from this CHapterPlacements objects will be placed when the battle begins
# Used to store placements in a file instead of a scene.
# this method of transfer works better for the retro files, 
# since I don't want to figure out how to make a whole scene based off that data
@export var placements: ChapterPlacements

@onready var unit_grid: UnitGrid = $UnitGrid
@onready var map_cursor: MapCursor = $MapCursor
@onready var range_display_grid: Node2D = $RangeDisplayGrid
@onready var unit_preview: UnitPreview = $UnitPreview
@onready var move_path_line: Line2D = $MovePathLine
@onready var attack_path_line: Line2D = $AttackPathLine


const MOVE_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/MoveTileHighlight.tscn")
const ATTACK_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/AttackTileHighlight.tscn")
const SUPPORT_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/SupportTileHighlight.tscn")

const RETRO_WIDTH: int = 19
const RETRO_HEIGHT: int = 14

const TILE_SIZE: float = 64.0

var is_player_turn: bool = true

## Current coordinates of the player's cursor. Used for unit selection, move destination, attack target, etc.
var cursor_coords: Vector2i = Vector2i.ZERO

## Current selected unit for moving/attacking.
var unit_selected: PlacedUnit

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
var attackable_tiles: Dictionary

var highest_attack_range: int
var highest_support_range: int
var total_attack_range_span: int

var range_iterations: int
var range_attack_iterations: int

## When in move/attack mode, the current tile path.
var current_path: Array[Vector2i]

func _ready() -> void:
	place_player_units()
	place_enemy_units()
	
	#call_deferred("grab_focus")

func _input(event: InputEvent) -> void:
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
			event = unit_grid.make_input_local(event)
			var coords: Vector2i = round(event.position / TILE_SIZE)
			if is_coords_in_bounds(coords):
				move_cursor_to(coords)
	elif event.is_action_pressed("Esc"):
		change_cursor_mode(CursorMode.SELECT)
	elif event.is_action_pressed("Select"):
		on_tile_pressed()
					
		
func on_tile_pressed():
	if cursor_mode == CursorMode.SELECT and hovered_unit.allied == is_player_turn:
		unit_selected = hovered_unit
		if hovered_unit:
			if !hovered_unit.moved:
				change_cursor_mode(CursorMode.MOVING)
			elif !hovered_unit.attacked:
				change_cursor_mode(CursorMode.ATTACKING)
	elif cursor_mode == CursorMode.MOVING:
		# if in move mode and the current coords of the unit is selected, cancel the move
		if cursor_coords == unit_selected.coords:
			change_cursor_mode(CursorMode.SELECT)
			return
			
		# if pressing tile outside of move range, return
		if not cursor_coords in moveable_tiles:
			change_cursor_mode(CursorMode.SELECT)
			return
			
		unit_grid.move_unit(unit_selected.coords, cursor_coords)
		unit_selected.moved = true
		change_cursor_mode(CursorMode.SELECT)
		hovered_unit = unit_selected
		show_range(unit_selected)
	elif cursor_mode == CursorMode.ATTACKING:
		## TODO: implement attacking, and selecting move for that matter
		unit_selected.moved = true # Cannot move after attack
		unit_selected.attacked = true
		change_cursor_mode(CursorMode.SELECT)
		hovered_unit = unit_selected
		show_range(unit_selected)
		
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
	print("moved cursor to ", cursor_coords)
	map_cursor.position = cursor_coords * TILE_SIZE
	
	hovered_unit = unit_grid.get_unit_at(cursor_coords)
	
	if cursor_mode == CursorMode.SELECT:
		unit_preview.display_unit(hovered_unit)
		show_range(hovered_unit)
	elif cursor_mode == CursorMode.MOVING or cursor_mode == CursorMode.ATTACKING:
		var prevent_outside: Dictionary = moveable_tiles if cursor_mode == CursorMode.MOVING else attackable_tiles
		if not (coords in prevent_outside or coords == unit_selected.coords):
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

func change_cursor_mode(mode: CursorMode):
	cursor_mode = mode
	if mode == CursorMode.SELECT:
		map_cursor.modulate = map_cursor.select_color
		end_move_path()
	elif mode == CursorMode.MOVING:
		map_cursor.modulate = map_cursor.move_color
		start_path()
	elif mode == CursorMode.ATTACKING:
		map_cursor.modulate = map_cursor.attack_color
		start_path()
		
	move_path_line.visible = cursor_mode == CursorMode.MOVING
	attack_path_line.visible = cursor_mode == CursorMode.ATTACKING
	
	
func start_path():
	current_path.clear()
	current_path.append(unit_selected.coords)
	refresh_path()

func refresh_path():
	if cursor_mode == CursorMode.MOVING:
		move_path_line.visible = true
		attack_path_line.visible = false
		move_path_line.clear_points()
		for coords in current_path:
			move_path_line.add_point(coords * TILE_SIZE)
	elif cursor_mode == CursorMode.ATTACKING:
		move_path_line.visible = false
		attack_path_line.visible = true
		attack_path_line.clear_points()
		for coords in current_path:
			attack_path_line.add_point(coords * TILE_SIZE)
	else:
		move_path_line.visible = false
		attack_path_line.visible = false
		
# Return tru ewhen a path is found
func recalculate_path_to(target_coords: Vector2i):
	current_path.clear()
	
	if cursor_mode == CursorMode.MOVING:
		search_for_path(unit_selected.coords, target_coords, unit_selected.unit.speed+1)
	elif cursor_mode == CursorMode.ATTACKING:
		search_for_path(unit_selected.coords, target_coords, max(highest_attack_range, highest_support_range)+1)
	
	refresh_path()

func search_for_path(coords: Vector2i, target_coords: Vector2i, steps_left: int) -> bool:
	# Can't move here if not movable/attack (ignore if on starting tile)
	if not coords in (moveable_tiles if cursor_mode == CursorMode.MOVING else attackable_tiles) and coords != unit_selected.coords:
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
	move_path_line.visible = false

func show_range(unit: PlacedUnit):	
	for child in range_display_grid.get_children():
		child.queue_free()
		
	moveable_tiles.clear()
	attackable_tiles.clear()
	
	if not unit or not unit.unit:
		return
	
	# Total range of abilities is move amount plus range of highest range attack
	highest_attack_range = 0
	highest_support_range = 0
	for move in unit.unit.moves:
		if move.move_type == "Attack":
			highest_attack_range = max(highest_attack_range, move.range)
		elif move.move_type == "Support":
			highest_support_range = max(highest_support_range, move.range)
			
	total_attack_range_span = max(highest_attack_range, highest_support_range)
	
	range_iterations = 0
	range_attack_iterations = 0
	spread_range(unit.coords, unit, 0 if unit.moved else unit.unit.speed)
	print("range iterations: ", range_iterations)
	print("range attack iterations: ", range_attack_iterations)
	
	# can't move in place
	moveable_tiles.erase(unit.coords)
	
	# TODO: only show attack in place if move is a support move
	attackable_tiles.erase(unit.coords)
	
	
	for coords in moveable_tiles.keys():
		var highlight: Node2D = MOVE_TILE_HIGHLIGHT.instantiate()
		highlight.position = coords * TILE_SIZE
		range_display_grid.add_child(highlight)
		
	for coords in attackable_tiles.keys():
		# Don't show the attack square if unit can move here, blue swuare should be shown instead
		if coords in moveable_tiles.keys():
			continue
			
		var tiles_left: int = attackable_tiles[coords]
		var range_required: int = total_attack_range_span - tiles_left
			
		# Don't show the attack square if there is a unit here that is not the targe tof the current move.
		# TODO: change logic based on whether or not move is a support move, or add green tiles for supportable allies?
		var other_unit: PlacedUnit = unit_grid.get_unit_at(coords)
		
		# If there is indeed another unit here and they are on the same team, 
		# check if they're in support range and draw a green square if so
		if other_unit and other_unit.allied == unit.allied and highest_support_range >= range_required:
			var highlight: Node2D = SUPPORT_TILE_HIGHLIGHT.instantiate()
			highlight.position = coords * TILE_SIZE
			range_display_grid.add_child(highlight)
			
		# TODO: attack minimum and maximum range
		# Show attack range otherwise if not an ally here
		elif highest_attack_range >= range_required and (not other_unit or other_unit.allied != unit.allied):
			var highlight: Node2D = ATTACK_TILE_HIGHLIGHT.instantiate()
			highlight.position = coords * TILE_SIZE
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
	range_iterations += 1
	
	# Spread attack range from this position that the unit can reach
	spread_attack_range(coords, unit, 0 if unit.attacked else total_attack_range_span)
	
	if move_remaining <= 0:
		return
	# Consume a move tile
	move_remaining -= 1
		
	# Try to spread move range to adjacent tiles
	spread_range(coords + Vector2i.UP, unit, move_remaining)
	spread_range(coords + Vector2i.RIGHT, unit, move_remaining)
	spread_range(coords + Vector2i.DOWN, unit, move_remaining)
	spread_range(coords + Vector2i.LEFT, unit, move_remaining)
	
func spread_attack_range(coords: Vector2i, unit: PlacedUnit, attack_range_remaining: int):
	# stop if cursor is OOB
	if not is_coords_in_bounds(coords):
		return
	
	# If renaining range is above 500, considered infinite,
	# doesn't matter if this has been reached in fewer moves, all other tiles will be be reached either way.
	if attack_range_remaining > 500:
		if attackable_tiles.has(coords):
			return
	else:
		# If already marked as attackable, stop if unit can already reach this tile in fewer moves
		if attackable_tiles.has(coords) and attackable_tiles[coords] >= attack_range_remaining:
			return
		
	attackable_tiles[coords] = attack_range_remaining
	range_attack_iterations += 1
	
	if attack_range_remaining <= 0:
		return
	attack_range_remaining -= 1
	
	spread_attack_range(coords + Vector2i.UP, unit, attack_range_remaining)
	spread_attack_range(coords + Vector2i.RIGHT, unit, attack_range_remaining)
	spread_attack_range(coords + Vector2i.DOWN, unit, attack_range_remaining)
	spread_attack_range(coords + Vector2i.LEFT, unit, attack_range_remaining)
	
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

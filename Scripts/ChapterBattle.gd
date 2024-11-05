class_name ChapterBattle
extends Control

@onready var unit_grid: UnitGrid = $UnitGrid
@onready var map_cursor: Sprite2D = $MapCursor
@onready var range_display_grid: Node2D = $RangeDisplayGrid

const MOVE_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/MoveTileHighlight.tscn")
const ATTACK_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/AttackTileHighlight.tscn")
const SUPPORT_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/SupportTileHighlight.tscn")

const RETRO_WIDTH: int = 19
const RETRO_HEIGHT: int = 14

const TILE_SIZE: float = 64.0

## Current coordinates of the player's cursor. Used for unit selection, move destination, attack target, etc.
var cursor_coords: Vector2i = Vector2i.ZERO

## Current selected unit for moving/attacking.
var unit_selected: PlacedUnit

## The unit currently hovered by the cursor.
var hovered_unit: PlacedUnit

## Current cursor mode ("Select", "Move", "Attack")
var cursor_mode: String = "Select"

signal cursor_moved

func _ready() -> void:
	call_deferred("grab_focus")

func _input(event: InputEvent) -> void:
	if event.is_action_pressed("Left"):
		move_cursor(Vector2i.LEFT)
	if event.is_action_pressed("Right"):
		move_cursor(Vector2i.RIGHT)
	if event.is_action_pressed("Up"):
		move_cursor(Vector2i.UP)
	if event.is_action_pressed("Down"):
		move_cursor(Vector2i.DOWN)
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
			event = unit_grid.make_input_local(event)
			var coords: Vector2i = round(event.position / TILE_SIZE)
			if is_coords_in_bounds(coords):
				# If clicked on the already hovered unit
				if coords == cursor_coords and hovered_unit:
					unit_selected = hovered_unit
					if hovered_unit.moved:
						cursor_mode = "Move"
					else:
						cursor_mode = "Attack"
				else:
					move_cursor_to(coords)
		
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
	
	unit_selected
	
	hovered_unit = unit_grid.get_unit_at(cursor_coords)
	cursor_moved.emit()

# dictionary to store the Vector2i coords as keys and dummy values
var moveable_tiles: Dictionary
var attackable_tiles: Dictionary

var highest_attack_range: int
var highest_support_range: int
var total_attack_range_span: int

func show_range(unit: PlacedUnit):	
	for child in range_display_grid.get_children():
		child.queue_free()
		
	moveable_tiles.clear()
	attackable_tiles.clear()
	
	if not unit:
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
	
	spread_range(unit.coords, unit, unit.unit.speed)
	
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
			
		# Show attack range otherwise
		elif highest_attack_range >= range_required:
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
	
	# Spread attack range from this position that the unit can reach
	spread_attack_range(coords, unit, total_attack_range_span)
	
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
	
	# If already marked as attackable, stop if unit can already reach this tile in fewer moves
	if attackable_tiles.has(coords) and attackable_tiles[coords] > attack_range_remaining:
		return
		
	attackable_tiles[coords] = attack_range_remaining
	
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

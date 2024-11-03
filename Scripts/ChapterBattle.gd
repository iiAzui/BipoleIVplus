class_name ChapterBattle
extends Control

@onready var unit_grid: UnitGrid = $UnitGrid
@onready var map_cursor: Sprite2D = $MapCursor
@onready var range_display_grid: Node2D = $RangeDisplayGrid

const MOVE_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/MoveTileHighlight.tscn")

const RETRO_WIDTH: int = 19
const RETRO_HEIGHT: int = 14

const TILE_SIZE: float = 64.0

var cursor_coords: Vector2i = Vector2i.ZERO

var hovered_unit: PlacedUnit

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
			if is_coords_in_bounds(coords) and coords != cursor_coords:
				move_cursor_to(coords)
		
func is_coords_in_bounds(coords: Vector2i):
	return coords.x >= 0 and coords.x < RETRO_WIDTH and coords.y >= 0 and coords.y < RETRO_HEIGHT
		
func move_cursor(offset: Vector2i):
	move_cursor_to(cursor_coords + offset)

func move_cursor_to(coords: Vector2i):
	cursor_coords = coords
	cursor_coords.x = clamp(cursor_coords.x, 0, RETRO_WIDTH-1)
	cursor_coords.y = clamp(cursor_coords.y, 0, RETRO_HEIGHT-1)
	print("moved cursor to ", cursor_coords)
	map_cursor.position = cursor_coords * TILE_SIZE
	
	hovered_unit = unit_grid.get_unit_at(cursor_coords)
	cursor_moved.emit()

# dictionaries to store the Vector2i coords as keys and dummy values
var move_range: Dictionary
var attack_range: Dictionary

func show_range(unit: PlacedUnit):	
	for child in range_display_grid.get_children():
		child.queue_free()
		
	move_range.clear()
	attack_range.clear()
	
	if not unit:
		return
		
	print("showing range of ", unit.unit.character.display_name, " from coords ", unit.coords)
	
	spread_range(unit.coords, unit, 0 if unit.moved else unit.unit.speed)
	
	# can't move in place
	move_range.erase(unit.coords)
	
	for moveable_coords in move_range.keys():
		var highlight = MOVE_TILE_HIGHLIGHT.instantiate()
		highlight.position = moveable_coords * TILE_SIZE
		range_display_grid.add_child(highlight)
	
# Mark as movable/attackable, and spreads movable and attackable range to adjacent tiles
func spread_range(coords: Vector2i, unit: PlacedUnit, move_remaining: int):
	# Can't move on this tile if it is solid / there is a unit here
	# (ignore this if this tile is where the unit currently is)
	if is_tile_solid(coords) and not (unit.coords == coords):
		return
	
	# If already marked as moveable, stop if unit can already reach this tile in fewer moves
	if move_range.has(coords) and move_range[coords] > move_remaining:
		return
		
	# Mark as a valid move location and mark the value as the moves it took to get here
	print(coords, " reachable in ", move_remaining, " moves")
	move_range[coords] = move_remaining
	
	# If this was the last tile, cant move anymore
	move_remaining -= 1
	if move_remaining < 0:
		return
		
	spread_range(Vector2i(coords + Vector2i.UP), unit, int(move_remaining))
	spread_range(Vector2i(coords + Vector2i.RIGHT), unit, int(move_remaining))
	spread_range(Vector2i(coords + Vector2i.DOWN), unit, int(move_remaining))
	spread_range(Vector2i(coords + Vector2i.LEFT), unit, int(move_remaining))
	
# True if the given tile is solid or there is a unit there (allied or enemy).
# Units can only move on non-solid tiles
func is_tile_solid(coords: Vector2i):
	# If out of retro bounds return true
	if not is_coords_in_bounds(coords):
		return true
		
	# If there is a unit here return true
	if unit_grid.get_unit_at(coords):
		return true
	
	# otherwise this tile is open	
	return false

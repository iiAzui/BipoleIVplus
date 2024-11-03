class_name ChapterBattle
extends Control

@onready var unit_grid: UnitGrid = $UnitGrid
@onready var map_cursor: Sprite2D = $MapCursor

var cursor_coords: Vector2i = Vector2i.ZERO

var hovered_unit: PlacedUnit

signal cursor_moved

func _ready() -> void:
	call_deferred("grab_focus")

func _input(event: InputEvent) -> void:
	if event.is_action_pressed("ui_left"):
		move_cursor(Vector2i.LEFT)
	if event.is_action_pressed("ui_right"):
		move_cursor(Vector2i.RIGHT)
	if event.is_action_pressed("ui_up"):
		move_cursor(Vector2i.UP)
	if event.is_action_pressed("ui_down"):
		move_cursor(Vector2i.DOWN)

func move_cursor(offset: Vector2i):
	cursor_coords += offset
	cursor_coords.x = clamp(cursor_coords.x, 0, UnitGrid.RETRO_WIDTH-1)
	cursor_coords.y = clamp(cursor_coords.y, 0, UnitGrid.RETRO_HEIGHT-1)
	print("moved cursor to ", cursor_coords)
	map_cursor.position = cursor_coords * UnitGrid.TILE_SIZE
	
	hovered_unit = unit_grid.get_unit_at(cursor_coords)
	cursor_moved.emit()

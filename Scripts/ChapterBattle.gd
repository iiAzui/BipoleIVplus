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
	if event.is_action_pressed("Left"):
		move_cursor(Vector2i.LEFT)
	if event.is_action_pressed("Right"):
		move_cursor(Vector2i.RIGHT)
	if event.is_action_pressed("Up"):
		move_cursor(Vector2i.UP)
	if event.is_action_pressed("Down"):
		move_cursor(Vector2i.DOWN)
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT:
			event = unit_grid.make_input_local(event)
			var coords: Vector2i = round(event.position / unit_grid.TILE_SIZE)
			print(coords)
			if coords.x >= 0 and coords.x < unit_grid.RETRO_WIDTH and coords.y >= 0 and coords.y < unit_grid.RETRO_HEIGHT and coords != cursor_coords:
				move_cursor_to(coords)
		

func move_cursor(offset: Vector2i):
	move_cursor_to(cursor_coords + offset)

func move_cursor_to(coords: Vector2i):
	cursor_coords = coords
	cursor_coords.x = clamp(cursor_coords.x, 0, UnitGrid.RETRO_WIDTH-1)
	cursor_coords.y = clamp(cursor_coords.y, 0, UnitGrid.RETRO_HEIGHT-1)
	print("moved cursor to ", cursor_coords)
	map_cursor.position = cursor_coords * UnitGrid.TILE_SIZE
	
	hovered_unit = unit_grid.get_unit_at(cursor_coords)
	cursor_moved.emit()

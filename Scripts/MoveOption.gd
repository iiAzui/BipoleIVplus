class_name MoveOption
extends Control

@export var unselected_stylebox: StyleBox
@export var selected_stylebox: StyleBox
@export var move_name_label: Label

var move: Move

func setup(move: Move):
	self.move = move
	move_name_label.text = move.display_name

func _input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.is_released() and move:
		print("clicked move ", move.display_name)

func show_selected():
	add_theme_stylebox_override("panel", selected_stylebox)
	
func show_unselected():
	add_theme_stylebox_override("panel", unselected_stylebox)

class_name MoveSelectPanel
extends PanelContainer

@export var move_name_label: Label


func show_move(move: Move):
	if move:
		visible = true
		move_name_label.text = move.display_name
	else:
		visible = false

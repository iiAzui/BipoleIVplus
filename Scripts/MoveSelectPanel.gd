class_name MoveSelectPanel
extends PanelContainer

@export var move_name_label: Label
@export var prev_arrow: Button
@export var next_arrow: Button

func show_arrows():
	prev_arrow.visible = true
	next_arrow.visible = true
	
func hide_arrows():
	prev_arrow.visible = false
	next_arrow.visible = false

func show_move(move: Move):
	if move:
		visible = true
		move_name_label.text = move.display_name
	else:
		visible = false

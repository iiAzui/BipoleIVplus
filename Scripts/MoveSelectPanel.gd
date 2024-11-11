class_name MoveSelectPanel
extends PanelContainer

@export var moves_container: Node

const MOVE_OPTION = preload("res://Scenes/UI/MoveOption.tscn")

var selected_option: MoveOption

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func show_selected_move(index: int):
	if selected_option:
		selected_option.show_unselected()
		
	if index < 0:
		return
		
	var move_option: MoveOption = moves_container.get_child(index)
	if move_option:
		move_option.show_selected()
		selected_option = move_option

func display_moves(unit: PlacedUnit):
	selected_option = null
	
	if unit:
		visible = true
	else:
		visible = false	
		return
	
	for child in moves_container.get_children():
		child.queue_free()
	
	for move in unit.unit.moves:
		var move_option_display: MoveOption = MOVE_OPTION.instantiate() as MoveOption
		move_option_display.setup(move)
		move_option_display.show_unselected()
		moves_container.add_child(move_option_display)

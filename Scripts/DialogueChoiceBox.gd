class_name DialogueChoiceBox
extends PanelContainer

@export var choice_container: Node

var choices: Array[Dictionary] = []

const DIALOGUE_CHOICE = preload("res://Scenes/UI/DialogueChoice.tscn")

func _ready() -> void:
	hide()

func start_new_choice_prompt():
	choices.clear()
	for node in choice_container.get_children():
		node.queue_free()
	
func add_choice(text: String = "Recruit", on_select: Callable = func(): pass):
	var button: Button = DIALOGUE_CHOICE.instantiate() as Button
	choice_container.add_child(button)
	button.text = text
	button.pressed.connect(on_select)

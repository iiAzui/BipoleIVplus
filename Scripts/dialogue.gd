extends Control

@export var cutscene_name: String = "Chapter01"

@onready var dialogue_text: Label = $PanelContainer/MarginContainer/DialogueText
@onready var name_left: Label = $PanelContainer/MarginContainer/NameLeft
@onready var name_right: Label = $PanelContainer/MarginContainer/NameRight


var dialogue_lines: Array
var line_index: int

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	var dialogue_file = FileAccess.open("res://Cutscenes/"+cutscene_name+".json", FileAccess.READ)
	if not dialogue_file:
		printerr("cutscene not found: ", cutscene_name)
		return
	var json_string = dialogue_file.get_as_text()
	dialogue_file.close()
	var json = JSON.new()
	json.parse(json_string)
	dialogue_lines = json.data
	print(dialogue_lines)
	
	line_index = -1
	display_next_line()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_accept"):
		display_next_line()
	
func display_next_line():
	line_index += 1
	if line_index >= len(dialogue_lines):
		printerr("end of dialogue reached. this probably isnt intended, a new chapter or battle should have started by now")
		return
		
	var line: Dictionary = dialogue_lines[line_index]
	dialogue_text.text = line["text"] if line.has("text") else ""
	name_left.text = line["left"] if line.has("left") else ""
	name_right.text = line["right"] if line.has("right") else ""

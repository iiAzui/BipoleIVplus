extends Control

@export var cutscene_name: String = "Chapter01"

@onready var dialogue_text: Label = $PanelContainer/MarginContainer/DialogueText
@onready var name_left: Label = $PanelContainer/MarginContainer/NameLeft
@onready var name_right: Label = $PanelContainer/MarginContainer/NameRight
@onready var portrait_left: TextureRect = $PortraitLeft
@onready var portrait_right: TextureRect = $PortraitRight


# All current dialogue
var dialogue: Array

# Current branch based on conditionals, or the root dialogue list if not on a branch.
var current_branch: Array

# The path of dialogue line indexes to reach the current branch when combined with line_branch_stack to get the branch taken.
var line_index_stack: Array[int]
# The path of branch names to reach the current branch.
var line_branch_stack: Array[String]

# The line # of the current branch currently bring shown.
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
	dialogue = json.data
	print(dialogue)
	
	current_branch = dialogue
	
	line_index = -1
	display_next_line()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_accept"):
		display_next_line()
	
func display_next_line() -> void:
	line_index += 1
	if line_index >= len(current_branch):
		if line_index_stack.is_empty():
			printerr("end of dialogue reached. this probably isnt intended, a new chapter or battle should have started by now")
			return
	
		# retrace the steps to get back to the dialogue before the last branch was taken
		current_branch = dialogue
		for i in len(line_index_stack)-1:
			var index_of_next_branch = line_index_stack[i]
			var branch_name := line_branch_stack[i]
			var branch: Dictionary = current_branch[index_of_next_branch]
			current_branch = branch[branch_name]
			
		# go to the next line after the lbranch that is being exited
		# and remove the index and branch name from the branch path stack
		line_index = line_index_stack.pop_back() + 1
		line_branch_stack.pop_back()
		display_next_line()
		return
		
	var line: Dictionary = current_branch[line_index]
	
	# "condition" key signifies a branch start
	if line.has("condition"):
		var condition_is_true: bool = check_condition(line["condition"])
		var branch_name = "true" if condition_is_true else "false"
		if line.has(branch_name):
			current_branch = line[branch_name]
			line_index_stack.push_back(line_index)
			line_branch_stack.push_back(branch_name)
			line_index = -1
			display_next_line()
			return
			
	else:
		dialogue_text.text = line["text"] if line.has("text") else ""
		
		var left = line["left"] if line.has("left") else ""
		name_left.text = left
		set_portrait(portrait_left, left)
		
		var right = line["right"] if line.has("right") else ""
		name_right.text = right
		set_portrait(portrait_right, right)
		
		if not line.has("text"):
			display_next_line()
			return
		
	print("index stack: ", line_index_stack, ", branch stack: ", line_branch_stack, ", current line: ", line_index)

# Check if a condition is true. 
# If none of the checks fail, condition returns true.
# The moment any check fails, returns false
func check_condition(condition: Dictionary) -> bool:
	if condition.has("is_alive"):
		var characters: Array = condition["is_alive"]
		for character: String in characters:
			# TODO: check current party and see if this unit is alive, return false if not
			pass
		
	if condition.has("units_alive_greater"):
		var value = condition["units_alive_greater"]
		# TODO: check if there are more than value units alive, return false if not
		pass
		
	if condition.has("units_alive_equal"):
		var value = condition["units_alive_equal"]
		# TODO: check if there are exactly value units alive, return false if not
		pass
		
	# no condition returned false, so all conditions passed, return true
	return true

# The name of the portrait to set for the given portrait texture rect.
# Resource load will get it into memory if it needs to be loaded
func set_portrait(texture_rect: TextureRect, name: String):
	if not name or name == "":
		texture_rect.visible = false
		return
	
	var portrait_filename = "res://Portraits/"+name.to_lower()+"_big.png"
	if ResourceLoader.exists(portrait_filename, "Texture2D"):
		var portrait_texture: Texture2D = ResourceLoader.load(portrait_filename)
		texture_rect.texture = portrait_texture
		texture_rect.visible = true
	else:
		texture_rect.visible = false

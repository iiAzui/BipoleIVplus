extends Control
class_name Dialogue

@export var dialogue_text: Label
@export var name_left: Label
@export var name_right: Label
@export var portrait_left: TextureRect
@export var portrait_right: TextureRect
@export var color_background: ColorRect
@export var choices: DialogueChoiceBox

# TODO: probably want to move this to the save file
static var current_chapter: String = "Chapter01"

# All current dialogue
var dialogue: Array

# Current branch based on conditionals, or the root dialogue list if not on a branch.
var current_branch: Array

# The path of dialogue line indexes to reach the current branch when combined with line_branch_stack to get the branch taken.
static var line_index_stack: Array[int] = []
# The path of branch names to reach the current branch.
static var line_branch_stack: Array[String] = []

# The line # of the current branch currently bring shown.
static var line_index: int = -1

# True when the player is making a choice (recruitment, etc)
var choosing: bool = false

# True if currently skipping - will skip over all dialogue except conditionals and choices
var skipping: bool = false
var skip_timer: float = 0.0
const SKIP_DELAY: float = 0.05

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	play_cutscene()
	
func play_cutscene():
	load_cutscene_file()
	if not dialogue or dialogue.is_empty():
		return
		
	print("loaded cutscene for chapter ", current_chapter)
	print("line index stack: ", line_index_stack)
	print("line branch stack: ", line_branch_stack)
	print("line index: ", line_index)
	print("current branch: ", current_branch)
	
	display_next_line(false)
	
func load_cutscene_file():
	var dialogue_file = FileAccess.open("res://Database/Cutscenes/"+current_chapter+".json", FileAccess.READ)
	if not dialogue_file:
		dialogue = []
		printerr("cutscene not found: ", current_chapter)
		return
	var json_string = dialogue_file.get_as_text()
	dialogue_file.close()
	var json = JSON.new()
	json.parse(json_string)
	dialogue = json.data
	find_branch()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if skipping and not choosing:
		skip_timer += delta
		if skip_timer > SKIP_DELAY:
			skip_timer -= SKIP_DELAY
			display_next_line()
			
	
func _input(event: InputEvent) -> void:
	if not choosing:
		if event.is_action_pressed("ui_accept"):
			display_next_line()
		if event is InputEventMouseButton and event.is_released() and event.button_index == MOUSE_BUTTON_LEFT:
			display_next_line()
			
	if event.is_action_pressed("Skip"):
		skipping = !skipping
	
func display_next_line(close_current_line: bool = true) -> void:
	if line_index >= 0 and close_current_line:
		var line_being_closed = current_branch[line_index]
		if line_being_closed.has("battle"):
			get_tree().change_scene_to_file("res://Scenes/3DChapterBattle.tscn")
			return
		elif line_being_closed.has("startchapter"):
			var new_chapter: String = line_being_closed["startchapter"].replace(" ", "")
			if current_chapter == new_chapter:
				printerr("trying to reload back into current chapter!")
				return
			current_chapter = new_chapter
			line_index_stack.clear()
			line_branch_stack.clear()
			line_index = -1
			load_cutscene_file()
			play_cutscene()
			return
	
	line_index += 1
	if line_index >= len(current_branch):
		if line_index_stack.is_empty():
			printerr("end of dialogue reached. this probably isnt intended, a new chapter or battle should have started by now")
			return
	
		# retrace the steps to get back to the dialogue before the last branch was taken
		find_branch()
		
		# go to the next line after the lbranch that is being exited
		# and remove the index and branch name from the branch path stack
		line_index = line_index_stack.pop_back() + 1
		line_branch_stack.pop_back()
		display_next_line()
		return
		
	print("index stack: ", line_index_stack, ", branch stack: ", line_branch_stack, ", current line: ", line_index)
	var line: Dictionary = current_branch[line_index]
	
	# NOTE: may want to add actual backgrounds eventually instead of solid colors
	if line.has("bgcolor"):
		var bgcolor_string = line["bgcolor"]
		if bgcolor_string == "black":
			color_background.color = Color.BLACK
		elif bgcolor_string == "gray" or bgcolor_string == "grey":
			color_background.color = Color.DARK_GRAY
		elif bgcolor_string == "green":
			color_background.color = Color.DARK_GREEN
		else:
			printerr("unrecognzied background color: ", bgcolor_string)
			
	if line.has("recruitment_choice"):
		var unit_name: String = line["recruitment_choice"]
		var unit: Unit = ResourceLoader.load("res://Database/RecruitedUnits/"+unit_name+".tres", "Unit") as Unit
		if not unit:
			printerr("unit to recruit not found in Database/RecruitedUnits: ", unit_name)
			display_next_line()
			return
			
		choosing = true
		skipping = false
		choices.start_new_choice_prompt()
		line["text"] = "Recruit "+unit.character.display_name+"?"
		choices.add_choice("Recruit", choose_choice_option.bind("true"))
		choices.add_choice("Do not recruit", choose_choice_option.bind("false"))
		choices.show()
	
	# "condition" key signifies a branch start
	if line.has("condition"):
		var condition_is_true: bool = check_condition(line["condition"])
		var branch_name = "true" if condition_is_true else "false"
		enter_branch(branch_name)
			
	else:
		dialogue_text.text = line["text"] if line.has("text") else ""
		
		var left_character = try_get_character(line["left"] if line.has("left") else "")	
		var left_name_string = left_character.display_name if left_character else (line["name_left"] if line.has("name_left") else (line["left"] if line.has("left") else ""))
		name_left.text = left_name_string
		set_portrait(portrait_left, left_character.portrait if left_character else (get_portrait(line["left"]) if line.has("left") else null))
		
		var right_character = try_get_character(line["right"] if line.has("right") else "")	
		var right_name_string = right_character.display_name if right_character else (line["name_right"] if line.has("name_right") else (line["right"] if line.has("right") else ""))
		name_right.text = right_name_string
		set_portrait(portrait_right, right_character.portrait if right_character else (get_portrait(line["right"]) if line.has("right") else null))
		
		if not line.has("text"):
			display_next_line()
			return
		
func choose_choice_option(branch_name: String):
	choices.hide()
	choosing = false
	enter_branch(branch_name)
		
# Enter a new branch on the current line
func enter_branch(branch_name: String):
	if current_branch[line_index].has(branch_name):
		current_branch = current_branch[line_index][branch_name]
		line_index_stack.push_back(line_index)
		line_branch_stack.push_back(branch_name)
		line_index = -1
		display_next_line()
		return

func find_branch():
	current_branch = dialogue
	for i in len(line_index_stack)-1:
		var index_of_next_branch = line_index_stack[i]
		var branch_name := line_branch_stack[i]
		var branch: Dictionary = current_branch[index_of_next_branch]
		current_branch = branch[branch_name]
		print("index_of_next_branch: ", index_of_next_branch, ", branch_name: ", branch_name)

func try_get_character(name: String) -> Character:
	if ResourceLoader.exists("res://Database/Characters/"+name+".tres", "Character"):
		return ResourceLoader.load("res://Database/Characters/"+name+".tres", "Character")
	
	#print("could not get character of name ", name)
	return null
		

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

func get_portrait(name: String) -> Texture2D:
	if not name:
		return
	
	if ResourceLoader.exists("res://Sprites/Portraits/"+name.to_lower()+"_big.png", "Texture2D"):
		return ResourceLoader.load("res://Sprites/Portraits/"+name.to_lower()+"_big.png", "Texture2D")
		
	if ResourceLoader.exists("res://Sprites/Portraits/"+name.to_lower()+".png", "Texture2D"):
		return ResourceLoader.load("res://Sprites/Portraits/"+name.to_lower()+".png", "Texture2D")
	
	print("could not get portrait of name \"", name, "\"")
	return null

# The name of the portrait to set for the given portrait texture rect.
# Resource load will get it into memory if it needs to be loaded
func set_portrait(texture_rect: TextureRect, texture: Texture2D):
	if texture:
		texture_rect.texture = texture
		texture_rect.visible = true
	else:
		texture_rect.visible = false

extends Control


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func new_game():
	#TODO: actually make a new game
	Dialogue.current_chapter = "Prologue"
	get_tree().change_scene_to_file("res://Scenes/Dialogue.tscn")
	
func continue_game():
	#TODO: load game if one exists, if not this button should probably be disabled
	Dialogue.current_chapter = "Chapter01"
	get_tree().change_scene_to_file("res://Scenes/Dialogue.tscn")
	
func settings():
	pass

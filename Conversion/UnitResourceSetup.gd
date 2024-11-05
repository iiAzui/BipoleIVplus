@tool
extends EditorScript

# Called when the script is executed (using File -> Run in Script Editor).
func _run():
	# for each Unit resource, find the exported move names and hook them up to the correct Move resources.
	setup_units_in_dir("res://Database/RecruitedUnits")
	setup_units_in_dir("res://Database/EnemyUnits")
	
func setup_units_in_dir(dir_path: String):
	var dir = DirAccess.open(dir_path)
	for unit_name in dir.get_files():
		setup_unit(dir_path, unit_name.substr(0, len(unit_name)-5))
			
func setup_unit(dir_path: String, unit_name: String):
	var file_path: String = dir_path + "/" + unit_name + ".tres"
	var unit: Unit = ResourceLoader.load(file_path)
	if not unit:
		printerr("non-unit or invalid unit in folder: ", unit_name, ".tres")
		return
		
	print(unit_name, ": Setting up unit")
	
	unit.moves = []
	for i in len(unit.exported_move_names):
		var move_name: String = unit.exported_move_names[i]
		var move: Move = ResourceLoader.load("res://Database/Moves/"+move_name+".tres")
		if move:
			unit.moves.push_back(move)
			print("\t", move_name, " connected!")

	unit.move_unlocks = []
	unit.move_unlock_levels = []
	for i in len(unit.exported_move_unlock_names):
		var move_name: String = unit.exported_move_unlock_names[i]
		var move: Move = ResourceLoader.load("res://Database/Moves/"+move_name+".tres")
		if move:
			var unlock_level: int = unit.exported_move_unlock_levels[i]
			unit.move_unlocks.push_back(move)
			unit.move_unlock_levels.push_back(unlock_level)
			print("\t", move_name, " connected!")
	
	var character: Character = ResourceLoader.load("res://Database/Characters/"+unit.exported_character_name+".tres", "")
	if character:
		print("\tdisplay name: ", character.display_name)
		
		var portrait_sprite: Texture2D = ResourceLoader.load("res://Sprites/Portraits/"+unit.exported_portrait_name+".png", "Texture2D")
		if portrait_sprite:
			character.portrait = portrait_sprite
			
		var overworld_sprite: Texture2D = ResourceLoader.load("res://Sprites/Overworld/"+unit.exported_overworld_name+".png", "Texture2D")
		if overworld_sprite:
			character.overworld_sprite = overworld_sprite
			
		unit.character = character
		
		ResourceSaver.save(character)

	ResourceSaver.save(unit)

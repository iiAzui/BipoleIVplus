@tool
extends EditorScript

# Called when the script is executed (using File -> Run in Script Editor).
func _run():
	# for each Unit resource, find the exported move names and hook them up to the correct Move resources.
	setup_units_in_dir("res://Database/RecruitedUnits")
	
func setup_units_in_dir(dir_path: String):
	var dir = DirAccess.open(dir_path)
	for file_name in dir.get_files():
		setup_unit(dir_path + "/" + file_name)
			
func setup_unit(unit_path: String):
	var unit: Unit = ResourceLoader.load(unit_path)
	if not unit:
		printerr("not a unit: ", unit_path)
		return
		
	print(unit_path, ": Setting up unit")
	
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
			
	ResourceSaver.save(unit)

extends Node2D


static var PLACED_UNIT_SCENE: PackedScene = preload("res://Scenes/UI/PlacedUnit.tscn")

@onready var unit_grid: UnitGrid = $UnitGrid

func _ready() -> void:
	load_player_units()

func load_player_units():
	# Spawn along the bottom row in retro mode.
	# Once non retro modes are added this will need new code
	var place_coords := Vector2i(0, 12)
	
	for i in len(SaveData.save.units):
		var unit: Unit = SaveData.save.units[i]
		var placed_unit: PlacedUnit = PLACED_UNIT_SCENE.instantiate()
		placed_unit.unit = unit
		unit_grid.add_child(placed_unit)
		unit_grid.place_unit(placed_unit, place_coords)
		
		place_coords.x += 1
		if place_coords.x >= unit_grid.RETRO_WIDTH:
			place_coords.x = 0
			place_coords.y += 1

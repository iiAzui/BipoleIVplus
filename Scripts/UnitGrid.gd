class_name UnitGrid
extends Node2D

#Contains all units in a dictionary. key is coordinates, value is the PlacedUnit
# to get a unit at (x, y), use the key of Vector2i(x, y)
var grid: Dictionary

const PLACED_UNIT_SCENE: PackedScene = preload("res://Scenes/UI/PlacedUnit.tscn")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	grid = {}
	
	# Get all units already in this scene and initialize them in the grid array based on their node position
	for unit: PlacedUnit in get_children():
		# if child is not a unit then the typecast to Unit will make it null, so skip it if null
		if not unit:
			continue

		var grid_relative_position = unit.position / ChapterBattle.TILE_SIZE
		print(grid_relative_position)
		var grid_coords := Vector2i(round(grid_relative_position.x), round(grid_relative_position.y))
		place_unit(unit, grid_coords)
		
	# Place player units from party
	load_player_units()
		
func load_player_units():
	# Spawn along the bottom row in retro mode.
	# Once non retro modes are added this will need new code
	var place_coords := Vector2i(0, 12)
	
	for i in len(SaveData.save.units):
		var unit: Unit = SaveData.save.units[i]
		var placed_unit: PlacedUnit = PLACED_UNIT_SCENE.instantiate()
		placed_unit.allied = true
		placed_unit.unit = unit
		add_child(placed_unit)
		place_unit(placed_unit, place_coords)
		
		place_coords.x += 1
		if place_coords.x >= ChapterBattle.RETRO_WIDTH:
			place_coords.x = 0
			place_coords.y += 1

func get_unit_at(coords: Vector2i):
	return grid.get(coords, null)
		
func place_unit(unit: PlacedUnit, coords: Vector2i):
	grid[coords] = unit
	unit.position = coords * ChapterBattle.TILE_SIZE
	unit.coords = coords
	print("placed ", unit.name, " at ", coords)

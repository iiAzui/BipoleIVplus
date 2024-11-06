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

func get_unit_at(coords: Vector2i):
	return grid.get(coords, null)
		
func place_unit(unit: PlacedUnit, coords: Vector2i):
	grid[coords] = unit
	unit.coords = coords
	unit.position = coords * ChapterBattle.TILE_SIZE
	add_child(unit)
	print("placed ", unit.name, " at ", coords)
	
func move_unit(from: Vector2i, to: Vector2i):
	var unit: PlacedUnit = grid[from]
	grid[from] = null
	grid[to] = unit
	unit.coords = to
	unit.position = to * ChapterBattle.TILE_SIZE
	print("moved ", unit.name, " from ", from, " to ", to)

class_name UnitGrid
extends Node2D

#Contains all units in a dictionary. key is coordinates, value is the PlacedUnit
# to get a unit at (x, y), use the key of Vector2i(x, y)
var grid: Dictionary

const RETRO_WIDTH: int = 14
const RETRO_HEIGHT: int = 19

const TILE_SIZE: float = 64.0

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	grid = {}
	
	# Get all units already in this scene and initialize them in the grid array based on their node position
	for unit: PlacedUnit in get_children():
		# if child is not a unit then the typecast to Unit will make it null, so skip it if null
		if not unit:
			continue

		var grid_relative_position = unit.position / TILE_SIZE
		print(grid_relative_position)
		var grid_coords := Vector2i(round(grid_relative_position.x), round(grid_relative_position.y))
		place_unit(unit, grid_coords)
		
func place_unit(unit: PlacedUnit, coords: Vector2i):
	grid[coords] = unit
	unit.position = Vector2(coords.x*TILE_SIZE, coords.y*TILE_SIZE)
	print("placed ", unit.name, " at ", coords)

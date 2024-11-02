extends Node2D

#Contains all units in a flattened 2d array format.
# to get a unit at (x, y), call grid[y*width + x]
var grid: Array[Unit]

# values might change in non retro mode. for now, keeping these as constants
const width: int = 14
const height: int = 19

const TILE_SIZE: float = 64.0

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	# Setup the grid
	grid = []
	grid.resize(width * height)
	
	# Get all units already in this scene and initialize them in the grid array based on their node position
	for unit: Unit in get_children():
		# if child is not a unit then the typecast to Unit will make it null, so skip it if null
		if not unit:
			continue

		var grid_relative_position = unit.position / TILE_SIZE
		print(grid_relative_position)
		var x = round(grid_relative_position.x)
		var y = round(grid_relative_position.y)
		place_unit(unit, x, y)
		
func place_unit(unit: Unit, x: int, y: int):
	grid[y*width + x] = unit
	unit.position = Vector2(x*TILE_SIZE, y*TILE_SIZE)
	print("placed ", unit.name, " at ", x, ", ", y)

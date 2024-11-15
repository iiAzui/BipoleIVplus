class_name UnitGrid
extends Node3D

@export var use_3d: bool = false

#Contains all units in a dictionary. key is coordinates, value is the PlacedUnit
# to get a unit at (x, y), use the key of Vector2i(x, y)
var grid: Dictionary

# Allied units that are still alive
var allied_units: Array[PlacedUnit] = []
# Enemy units that are still alive
var enemy_units: Array[PlacedUnit] = []

const PLACED_UNIT_SCENE: PackedScene = preload("res://Scenes/UI/PlacedUnit.tscn")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	grid = {}
	allied_units.clear()
	enemy_units.clear()
	
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
	set_unit_coords(unit, coords)
	add_child(unit)
	if unit.allied:
		allied_units.append(unit)
	else:
		enemy_units.append(unit)
	print("placed ", unit.name, " at ", coords)
	
func move_unit(from: Vector2i, to: Vector2i):
	var unit: PlacedUnit = grid[from]
	grid[from] = null
	grid[to] = unit
	set_unit_coords(unit, to)
	print("moved ", unit.name, " from ", from, " to ", to)

func erase_unit(coords: Vector2i):
	if coords in grid:
		var unit = grid[coords]
		allied_units.erase(unit)
		enemy_units.erase(unit)
		grid[coords].queue_free()
		grid.erase(coords)
	

func set_unit_coords(unit: PlacedUnit, coords: Vector2i):
	unit.coords = coords
	unit.position = Vector3(coords.x, unit.position.y, coords.y)

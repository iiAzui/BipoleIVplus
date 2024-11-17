class_name RangeDisplayGrid
extends Node3D

# Key = coords (Vector2i), value = RangeTileHighlight (sprite3D)
var grid: Dictionary

const RANGE_TILE_HIGHLIGHT: PackedScene = preload("res://Scenes/UI/RangeTileHighlight.tscn")

@export var move_color := Color.BLUE
@export var attack_color := Color.RED
@export var support_color := Color.GREEN
@export var danger_zone_color := Color.DARK_RED

func _ready():
	grid = {}
	
	# will work in retro, will need to be reworked for when maps are added in non retro to cover all non-solid tiles.
	for y in ChapterBattle.RETRO_HEIGHT:
		for x in ChapterBattle.RETRO_WIDTH:
			var coords := Vector2i(x, y)
			var highlight: Sprite3D = RANGE_TILE_HIGHLIGHT.instantiate()
			add_child(highlight)
			grid[coords] = highlight
			highlight.position = Vector3(x, 0, y);
			highlight.visible = false

func show_highlight(coords: Vector2i, highlight_color: Color):
	if coords in grid:
		var highlight: Sprite3D = grid[coords]
		highlight.visible = true
		highlight.modulate = highlight_color
	else:
		printerr("coords ", coords, " not found in grid")

func clear():
	for highlight in grid.values():
		highlight.visible = false

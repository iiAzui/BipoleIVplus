class_name MainScene
extends Control

@onready var unit_preview: UnitPreview = $UnitPreview

# TODO: load chapter from save file
@onready var battle: ChapterBattle = $Chapter01

func _ready() -> void:
	battle.cursor_moved.connect(show_hovered_unit)
	
func show_hovered_unit():
	if battle.hovered_unit:
		unit_preview.visible = true
		unit_preview.display_unit(battle.hovered_unit)
	else:
		unit_preview.visible = false
	battle.show_range(battle.hovered_unit)

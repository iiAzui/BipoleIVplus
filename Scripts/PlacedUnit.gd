@tool
class_name PlacedUnit
extends Node2D

@export var unit: Unit:
	set(value):
		if unit:
			unit.character_changed.disconnect(update_unit_visual)
			
		unit = value
		update_unit_visual()
		
		if unit:
			unit.max_hp = unit.hp
			unit.character_changed.connect(update_unit_visual)
			

@onready var sprite: Sprite2D = $Sprite2D

func _enter_tree() -> void:
	update_unit_visual()

func _ready() -> void:
	update_unit_visual()

# for editor reflecting current unit
func update_unit_visual():
	if unit and unit.character:
		$Sprite2D.texture = unit.character.overworld_sprite
	else:
		$Sprite2D.texture = null

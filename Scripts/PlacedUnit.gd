@tool
class_name PlacedUnit
extends Node2D

@export var unit: Unit:
	set(value):
		if unit:
			unit.character_changed.disconnect(on_unit_changed)
			
		unit = value
		on_unit_changed()
		
		if unit:
			unit.character_changed.connect(on_unit_changed)
			

@onready var sprite: Sprite2D = $Sprite2D

# for editor reflecting current unit
func on_unit_changed():
	if unit and unit.character:
		sprite.texture = unit.character.overworld_sprite
	else:
		sprite.texture = null

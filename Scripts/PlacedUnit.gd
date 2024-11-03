@tool
class_name PlacedUnit
extends Node2D

@onready var health_bar: TextureProgressBar = $HealthBar
@onready var level_label: Label = $LevelBackground/LevelLabel

@export var unit: Unit:
	set(value):
		if unit:
			unit.character_changed.disconnect(update_unit_visual)
			unit.level_changed.disconnect(update_unit_visual)
			
		unit = value
		if is_node_ready():
			update_unit_visual()
		
		if unit:
			unit.max_hp = unit.hp
			unit.character_changed.connect(update_unit_visual)
			unit.level_changed.connect(update_unit_visual)
			

@onready var sprite: Sprite2D = $Sprite2D

func _enter_tree() -> void:
	if Engine.is_editor_hint():
		update_unit_visual()

func _ready() -> void:
	update_unit_visual()

# for editor reflecting current unit
func update_unit_visual():
	if unit and unit.character:
		$Sprite2D.texture = unit.character.overworld_sprite
		health_bar.value = unit.hp
		health_bar.max_value = unit.max_hp
		level_label.text = str(unit.level)

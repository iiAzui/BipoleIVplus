@tool
class_name PlacedUnit
extends Node2D

@onready var health_bar: TextureProgressBar = $HealthBar
@onready var level_label: Label = $LevelBackground/LevelLabel

const HEALTH_BAR_PLAYER = preload("res://Sprites/UI/HealthBarPlayer.tres")
const HEALTH_BAR_ENEMY = preload("res://Sprites/UI/HealthBarEnemy.tres")

# True if in the player's party, false if this is an enemy unit fighting the player
var allied: bool = false

# True if the unit has moved yet during their turn. 
# Can only move once per turn and cannot move after using a move.
var moved: bool = false

# true if unit has already used their attack during their turn.
var attacked: bool = false

# Current coords on the map. Should always mirror the key that it has in UnitGrid's grid dictionary.
# (UnitGrid should manage this value closely)
var coords: Vector2i

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

func _ready() -> void:
	update_unit_visual()

# for editor reflecting current unit
func update_unit_visual():
	if unit and unit.character:
		$Sprite2D.texture = unit.character.overworld_sprite
		if health_bar:
			health_bar.value = unit.hp
			health_bar.max_value = unit.max_hp
			health_bar.texture_progress = HEALTH_BAR_PLAYER if allied else HEALTH_BAR_ENEMY
			level_label.text = str(unit.level)

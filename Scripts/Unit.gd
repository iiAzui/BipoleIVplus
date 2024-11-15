@tool
class_name Unit
extends Resource

signal character_changed
@export var character: Character:
	set(value):
		character = value
		character_changed.emit()

@export var moves: Array[Move]
@export var move_unlocks: Array[Move]
@export var move_unlock_levels: Array[int]

# USED ONLY FOR IMPORTING FROM PYTHON CONVERSION
@export_storage var exported_move_names: Array[String]
@export_storage var exported_move_unlock_names: Array[String]
@export_storage var exported_move_unlock_levels: Array[int]

@export_storage var exported_portrait_name: String
@export_storage var exported_overworld_name: String
@export_storage var exported_character_name: String
@export_storage var exported_x: int
@export_storage var exported_y: int

@export_subgroup("Stats")
signal level_changed
@export var level: int = 1:
	set(value):
		level = value
		level_changed.emit()

@export var hp: int = 20
@export var attack: int = 10 # Influences attack damage
@export var defense: int = 10 # Influences damages taken from physical attacks
@export var resistance: int = 10 # Influences damage taken from magic attacks
@export var agility: int = 10 # Influences the change of getting hit by an attack, and the change of you hitting your attack
@export var accuracy: int = 10
@export var speed: int = 10 # The amount of tiles this unit can move
@export var exp_reward: int = 100 # EXP given when defeated. Enemy units can also level up if they defeat your units.

@export_subgroup("Traits")
@export_enum("Physical", "Magic") var primary_type: String = "Physical"
@export var traits: Array[String]
@export var unit_class: String
@export var class_change: String
@export var class_change_level: int

@export_subgroup("Growths")
@export var hp_growth: Vector2i = Vector2i(50, 1)
@export var atk_growth: Vector2i = Vector2i(50, 1)
@export var def_growth: Vector2i = Vector2i(50, 1)
@export var res_growth: Vector2i = Vector2i(50, 1)
@export var agl_growth: Vector2i = Vector2i(50, 1)
@export var acr_growth: Vector2i = Vector2i(50, 1)

var max_hp: int
var exp: int = 0 # Level up every 100 EXP

func _init() -> void:
	print("init ", resource_name)
	
func take_damage(damage: int):
	hp = max(0, hp - damage)
	
func get_counter_damage(target: Unit) -> int:
	var def_or_res: int = target.defense if primary_type == "Physical" else target.resistance
	return max(0, int(attack * 1.25 - def_or_res / 2.0))

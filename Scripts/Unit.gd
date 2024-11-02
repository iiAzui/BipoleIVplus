class_name Unit
extends Node2D

@export var display_name: String
@export var attack_range: int
@export_enum("Physical", "Magical") var primary_type: String
@export var hp: int = 20

@export var attacks: Array
@export var supports: Array

@export_subgroup("Stats")
@export var atk: int # Influences attack damage
@export var def: int # Influences damage taken from physical attacks
@export var res: int # Influences damage taken from magic attacks
@export var agl: int # Influences the change of getting hit by an attack, and the change of you hitting your attack
@export var acr: int
@export var spd: int # The amount of tiles this unit can move
@export var exp_reward: int # EXP given when defeated. Enemy units can also level up if they defeat your units.



# TODO: Growths

var max_hp: int
var exp: int = 0 # Level up every 100 EXP

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	max_hp = hp


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

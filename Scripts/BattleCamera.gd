# NOTE: controls the node3d that camera is parented under, not the camera directly

class_name BattleCamera
extends Node3D

@export var camera: Camera3D
@export var standard_distance: float = 22.25
@export var combat_distance: float = 15
@export var standard_fov: float = 45.0
@export var center_position: Vector3 = Vector3(9, 0, 6.5)
@onready var offset_direction: Vector3 = (camera.global_position - global_position).normalized()

var start_position: Vector3
var target_position: Vector3
var target_fov: float

var current_duration: float = 0.25
var current_t: float = 0.0

func _ready() -> void:
	start_position = camera.global_position
	standard_view()
	current_t = current_duration

func _process(delta: float) -> void:
	current_t = move_toward(current_t, current_duration, delta)
	camera.global_position = lerp(start_position, target_position, current_t / current_duration)
	
func standard_view():
	start_position = camera.global_position
	target_position = center_position + offset_direction * standard_distance
	current_t = 0.0

func combat_view(attacker: PlacedUnit, defender: PlacedUnit):
	start_position = camera.global_position
	var map_center: Vector3 = center_position + offset_direction * standard_distance
	var combat_center: Vector3 = (attacker.global_position + defender.global_position) / 2.0 + offset_direction * combat_distance;
	target_position = lerp(map_center, combat_center, 0.5)
	current_t = 0.0

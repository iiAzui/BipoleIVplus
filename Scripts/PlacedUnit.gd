@tool
class_name PlacedUnit
extends Node3D

@export var health_bar: TextureProgressBar
@export var level_label: Label
@export var sprite_3d: Sprite3D

const HEALTH_BAR_PLAYER = preload("res://Sprites/UI/HealthBarPlayer.tres")
const HEALTH_BAR_ENEMY = preload("res://Sprites/UI/HealthBarEnemy.tres")
const DAMAGE_POPUP = preload("res://Scenes/UI/DamagePopup.tscn")

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

func _ready() -> void:
	update_unit_visual()

# for editor reflecting current unit
func update_unit_visual():
	if unit and unit.character:
		if not sprite_3d:
			sprite_3d = $Sprite3D
		sprite_3d.texture = unit.character.overworld_sprite
		if health_bar:
			health_bar.value = unit.hp
			health_bar.max_value = unit.max_hp
			health_bar.texture_progress = HEALTH_BAR_PLAYER if allied else HEALTH_BAR_ENEMY
			level_label.text = str(unit.level)

# if move is null this is probably a generic attack (counter attack / follow up)
func attack_animation(target: PlacedUnit, move: Move, damage: int):
	var start_point: Vector3 = global_position
	var attack_point: Vector3 = lerp(global_position, target.global_position, 0.5)
	await get_tree().create_tween().tween_property(self, "global_position", attack_point, 0.125).finished
	target.damage_animation(damage)
	await get_tree().create_timer(0.125).timeout
	await get_tree().create_tween().tween_property(self, "global_position", start_point, 0.25).finished

func damage_animation(damage: int):
	var popup: DamagePopup = DAMAGE_POPUP.instantiate() as DamagePopup
	add_child(popup)
	popup.animate(self, damage)
	# just use whatever value is already in the health bar to use to animate bewteen old and new value
	animate_health_bar(health_bar.value, unit.hp) 
	await get_tree().create_tween().tween_property(sprite_3d, "modulate", Color(1, 0.5, 0.5), 0.125).finished
	await get_tree().create_timer(0.125).timeout
	await get_tree().create_tween().tween_property(sprite_3d, "modulate", Color.WHITE, 0.25).finished
	
func animate_health_bar(old_health: int, new_health: int):
	health_bar.value = old_health
	await get_tree().create_tween().tween_property(health_bar, "value", new_health, 0.25)

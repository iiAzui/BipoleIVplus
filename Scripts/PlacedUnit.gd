@tool
class_name PlacedUnit
extends Node3D

@export var health_bar: TextureProgressBar
@export var health_before_damage_bar: TextureProgressBar
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

var shader_mat: ShaderMaterial

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
	shader_mat = sprite_3d.material_override as ShaderMaterial
	update_unit_visual()

# for editor reflecting current unit
func update_unit_visual():
	if unit and unit.character:
		if not sprite_3d:
			sprite_3d = $Sprite3D
		sprite_3d.texture = unit.character.overworld_sprite
		if shader_mat:
			if allied:
				shader_mat.set_shader_parameter("acted", attacked)
			shader_mat.set_shader_parameter("texture_albedo", unit.character.overworld_sprite)
		if health_bar:
			health_bar.value = unit.hp
			health_bar.max_value = unit.max_hp + 1
			health_before_damage_bar.max_value = unit.max_hp
			health_bar.texture_progress = HEALTH_BAR_PLAYER if allied else HEALTH_BAR_ENEMY
			health_before_damage_bar.texture_progress = HEALTH_BAR_PLAYER if allied else HEALTH_BAR_ENEMY
			level_label.text = str(unit.level)

func display_damage_preview(incoming_damage: int):
	health_before_damage_bar.value = unit.hp if incoming_damage > 0 else 0
	health_bar.value = max(0, unit.hp - incoming_damage)

func move_animation(path: Array[Vector2i]):
	if len(path) == 0:
		printerr("trying to do move anim with empty path list")
		return
		
	position = Vector3(path[0].x, 0, path[0].y)
	for i in len(path)-1:
		var next_point = path[i+1]
		var next_position := Vector3(next_point.x, 0, next_point.y)
		await get_tree().create_tween().tween_property(self, "position", next_position, 0.25/float(unit.speed)).finished;

# if move is null this is probably a generic attack (counter attack / follow up)
func attack_animation(target: PlacedUnit, move: Move, damage: int, miss: bool):
	var start_point: Vector3 = global_position
	var attack_point: Vector3 = lerp(global_position, target.global_position, 0.2 if move and move.move_type == "Support" else 0.5)
	await get_tree().create_tween().tween_property(self, "global_position", attack_point, 0.125).finished
	target.damage_animation(damage, move, miss, move and move.move_type == "Support")
	await get_tree().create_timer(0.125).timeout
	await get_tree().create_tween().tween_property(self, "global_position", start_point, 0.25).finished

func damage_animation(damage: int, move: Move, miss: bool, is_heal: bool = false):
	# just use whatever value is already in the health bar to use to animate bewteen old and new value
	var modulate_color: Color = Color(0, 0.9, 0) if is_heal else Color(0.9, 0, 0)
	
	shader_mat.set_shader_parameter("overlay_color", modulate_color)
	
	var popup: DamagePopup = DAMAGE_POPUP.instantiate() as DamagePopup
	add_child(popup)
	popup.animate(self, damage, miss)
	animate_health_bar(health_bar.value, unit.hp)
	
	if miss:
		pass
	else:
		get_tree().create_tween().tween_method(set_overlay_blend, 0.5, 0, 0.4)
	
func take_damage_with_animation(damage: int):
	unit.take_damage(damage)
	await damage_animation(damage, null, false, false)
	
func death_animation():
	shader_mat.set_shader_parameter("overlay_color", Color.BLACK)
	set_overlay_blend(0)
	get_tree().create_tween().tween_method(set_overlay_blend, 0, 1, 0.5)
	await get_tree().create_timer(0.75).timeout
	queue_free()
	
func set_overlay_blend(value: float):
	#print(value)
	shader_mat.set_shader_parameter("overlay_blend", value)
	
func animate_health_bar(old_health: int, new_health: int):
	health_bar.value = old_health
	await get_tree().create_tween().tween_property(health_bar, "value", new_health, 0.25)

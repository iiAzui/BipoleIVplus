class_name UnitPreview
extends PanelContainer

@export var display_name_label: Label
@export var portrait_texture_rect: TextureRect
@export var health_label: Label
@export var health_bar: TextureProgressBar
@export var level_label: Label
@export var exp_label: Label
@export var exp_bar: TextureProgressBar
@export var atk_label: Label
@export var def_label: Label
@export var res_label: Label
@export var spd_label: Label
@export var agl_label: Label
@export var acr_label: Label

const HEALTH_BAR_PLAYER = preload("res://Sprites/UI/HealthBarPlayer.tres")
const HEALTH_BAR_ENEMY = preload("res://Sprites/UI/HealthBarEnemy.tres")

func display_unit(placed_unit: PlacedUnit):
	if not placed_unit:
		modulate.a = 0
		return
	var unit = placed_unit.unit
	if not unit:
		printerr(placed_unit, " doesn't have any unit stats! (this might be bad)")
		modulate.a = 0
		return
	modulate.a = 1
		
	display_name_label.text = unit.character.display_name if unit.character else "Unit"
	portrait_texture_rect.texture = unit.character.portrait if unit.character else null
	
	health_label.text = "%d/%d" % [unit.hp, unit.max_hp]
	health_bar.max_value = unit.max_hp
	health_bar.value = unit.hp
	health_bar.texture_progress = HEALTH_BAR_PLAYER if placed_unit.allied else HEALTH_BAR_ENEMY
	
	level_label.text = "Lv %d" % unit.level
	const xp_until_next: int = 100 # might change in non retro mode, not sure
	exp_label.text = "%d/%d EXP" % [unit.exp, xp_until_next]
	exp_bar.value = unit.exp
	exp_bar.max_value = xp_until_next
	
	atk_label.text = str(unit.attack)
	def_label.text = str(unit.defense)
	res_label.text = str(unit.resistance)
	spd_label.text = str(unit.speed)
	agl_label.text = str(unit.agility)
	acr_label.text = str(unit.accuracy)

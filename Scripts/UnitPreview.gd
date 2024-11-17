class_name UnitPreview
extends PanelContainer

@export var display_name_label: Label
@export var portrait_texture_rect: TextureRect
@export var health_bar: TextureProgressBar
@export var health_before_damage_bar: TextureProgressBar
@export var level_label: Label
@export var exp_display: StatDisplay
@export var exp_bar: TextureProgressBar
@export var hp_display: StatDisplay
@export var atk_display: StatDisplay
@export var def_display: StatDisplay
@export var res_display: StatDisplay
@export var spd_display: StatDisplay
@export var agl_display: StatDisplay
@export var acr_display: StatDisplay

@export var levelup_notification: Control

const HEALTH_BAR_PLAYER = preload("res://Sprites/UI/HealthBarPlayer.tres")
const HEALTH_BAR_ENEMY = preload("res://Sprites/UI/HealthBarEnemy.tres")

func _ready() -> void:
	levelup_notification.hide()

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
	
	hp_display.label.text = "%d/%d" % [unit.hp, unit.max_hp]
	health_bar.max_value = unit.max_hp
	health_bar.value = unit.hp
	health_bar.texture_progress = HEALTH_BAR_PLAYER if placed_unit.allied else HEALTH_BAR_ENEMY
	
	health_before_damage_bar.max_value = unit.max_hp
	health_before_damage_bar.value = unit.hp
	health_before_damage_bar.texture_progress = HEALTH_BAR_PLAYER if placed_unit.allied else HEALTH_BAR_ENEMY
	
	level_label.text = "Lv %d" % unit.level
	const xp_until_next: int = 100 # might change in non retro mode, not sure
	exp_display.label.text = "%d/%d" % [unit.exp, xp_until_next]
	exp_bar.value = unit.exp
	exp_bar.max_value = xp_until_next
	
	atk_display.label.text = str(unit.attack)
	def_display.label.text = str(unit.defense)
	res_display.label.text = str(unit.resistance)
	spd_display.label.text = str(unit.speed)
	agl_display.label.text = str(unit.agility)
	acr_display.label.text = str(unit.accuracy)
	
	levelup_notification.hide()
	exp_display.hide_growth()
	hp_display.hide_growth()
	atk_display.hide_growth()
	def_display.hide_growth()
	res_display.hide_growth()
	agl_display.hide_growth()
	acr_display.hide_growth()
	
func display_damage_preview(placed_unit: PlacedUnit, incoming_damage: int):
	health_before_damage_bar.value = placed_unit.unit.hp
	health_bar.value = max(0, placed_unit.unit.hp - incoming_damage)

func show_exp_gain(amount: int):
	exp_display.show_growth(amount)

func show_levelup(stat_gains: Array[int]):
	levelup_notification.show()
	var disps: Array[StatDisplay] = [hp_display, atk_display, def_display, res_display, agl_display, acr_display]
	for i in 6:
		disps[i].show_growth(stat_gains[i])

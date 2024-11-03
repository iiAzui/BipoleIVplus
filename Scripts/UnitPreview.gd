class_name UnitPreview
extends PanelContainer

@onready var display_name_label: Label = $MarginContainer/VBoxContainer/DisplayNameLabel
@onready var portrait_texture_rect: TextureRect = $MarginContainer/VBoxContainer/PortraitPanelContainer/TextureRect
@onready var health_label: Label = $MarginContainer/VBoxContainer/HealthContainer/HealthLabel
@onready var health_bar: TextureProgressBar = $MarginContainer/VBoxContainer/HealthContainer/HealthBar
@onready var level_label: Label = $MarginContainer/VBoxContainer/LevelContainer/LevelLabel
@onready var exp_label: Label = $MarginContainer/VBoxContainer/LevelContainer/EXPLabel
@onready var exp_bar: TextureProgressBar = $MarginContainer/VBoxContainer/LevelContainer/EXPBar

const HEALTH_BAR_PLAYER = preload("res://Sprites/UI/HealthBarPlayer.tres")
const HEALTH_BAR_ENEMY = preload("res://Sprites/UI/HealthBarEnemy.tres")

func display_unit(placed_unit: PlacedUnit):
	var unit = placed_unit.unit
	display_name_label.text = unit.character.display_name
	portrait_texture_rect.texture = unit.character.portrait
	
	health_label.text = "%d/%d" % [unit.hp, unit.max_hp]
	health_bar.max_value = unit.max_hp
	health_bar.value = unit.hp
	health_bar.texture_progress = HEALTH_BAR_PLAYER if placed_unit.allied else HEALTH_BAR_ENEMY
	
	level_label.text = "Lv %d" % unit.level
	const xp_until_next: int = 100 # might change in non retro mode, not sure
	exp_label.text = "%d/%d EXP" % [unit.exp, xp_until_next]
	exp_bar.value = unit.exp
	exp_bar.max_value = xp_until_next

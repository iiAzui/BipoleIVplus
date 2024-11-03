class_name UnitPreview
extends PanelContainer

@onready var display_name_label: Label = $MarginContainer/VBoxContainer/DisplayNameLabel
@onready var portrait_texture_rect: TextureRect = $MarginContainer/VBoxContainer/PortraitPanelContainer/TextureRect
@onready var health_label: Label = $MarginContainer/VBoxContainer/PanelContainer/HealthLabel
@onready var health_bar: TextureProgressBar = $MarginContainer/VBoxContainer/PanelContainer/HealthBar

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

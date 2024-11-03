class_name UnitPreview
extends PanelContainer

@onready var display_name_label: Label = $MarginContainer/VBoxContainer/DisplayNameLabel
@onready var portrait_texture_rect: TextureRect = $MarginContainer/VBoxContainer/PortraitPanelContainer/TextureRect
@onready var health_label: Label = $MarginContainer/VBoxContainer/HealthLabel
@onready var health_bar: TextureProgressBar = $MarginContainer/VBoxContainer/HealthBar

func display_unit(unit: Unit):
	display_name_label.text = unit.character.display_name
	portrait_texture_rect.texture = unit.character.portrait
	health_label.text = "%d/%d" % [unit.hp, unit.max_hp]
	health_bar.max_value = unit.max_hp
	health_bar.value = unit.hp

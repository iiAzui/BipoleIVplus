class_name StatDisplay
extends Control

@export var label: Label
@export var growth_label: Label

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	growth_label.hide()

func show_growth(amount: int):
	if amount > 0:
		growth_label.show()
		growth_label.text = "+"+str(amount)
	else:
		growth_label.hide()

func hide_growth():
	growth_label.hide()

class_name DamagePreview
extends PanelContainer

@export var damage_label: Label

# Outgoing if going from allied to target unit.
# Incoming if going from target to allied unit.
func display(damage: int, outgoing: bool):
	if damage > 0:
		visible = true
		damage_label.text = str(damage)
		damage_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT if outgoing else HORIZONTAL_ALIGNMENT_LEFT
	else:
		visible = false

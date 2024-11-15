extends Sprite3D
class_name DamagePopup

@export var damage_label: Label

func animate(unit: PlacedUnit, damage: int):
	global_position = unit.global_position
	damage_label.text = str(damage)
	modulate = Color.WHITE
	await get_tree().create_tween().tween_property(damage_label, "global_position", damage_label.global_position + Vector2.UP * 40, 0.5).finished
	await get_tree().create_timer(0.25).timeout
	await get_tree().create_tween().tween_property(self, "modulate", Color(1,1,1,0), 0.25).finished
	queue_free()

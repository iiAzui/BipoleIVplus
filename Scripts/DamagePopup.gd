extends Control
class_name DamagePopup

@export var damage_label: Label

func animate(unit: PlacedUnit, damage: int, miss: bool):
	position = get_viewport().get_camera_3d().unproject_position(unit.global_position)
	damage_label.text = "MISS" if miss else str(damage)
	modulate = Color.WHITE
	await get_tree().create_tween().tween_property(self, "position", position + Vector2.UP * 75, 0.2).finished
	await get_tree().create_timer(0.3).timeout
	await get_tree().create_tween().tween_property(self, "modulate", Color(1,1,1,0), 0.125).finished
	queue_free()

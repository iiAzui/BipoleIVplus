class_name MoveUnlock
extends Resource

@export var level: int
@export var move: Move

func _init(level: int = 0, move: Move = null) -> void:
	self.level = level
	self.move = move

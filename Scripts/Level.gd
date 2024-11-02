extends Node

const CHAR := preload("res://Charcters.tscn")

func _ready() -> void:
	var partynum = 0
	for i in len(Globals.Party):
		var cindex = Globals.Names.find(Globals.Party[partynum])
		var Char = CHAR.instantiate()
		add_child(Char)
		Char.name = Globals.Names[cindex]
		Char.position = Globals.Spawns[partynum]
		Char.get_node("Sprite").texture = load(Globals.Por[cindex][1])
		partynum += 1

func _on_cursor_body_entered(body: Node2D) -> void:
	var bname = body.name
	var bindex = Globals.Party.find(bname)
	print(bname, bindex)
	get_node("LeftPlayerRightEnemy/LeftOnHover").visible = true
	get_node("LeftPlayerRightEnemy/LeftOnHover/Por").texture = load(Globals.Por[bindex][0])
func _on_cursor_body_exited(body: Node2D) -> void:
	get_node("LeftPlayerRightEnemy/LeftOnHover").visible = false

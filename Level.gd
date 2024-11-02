extends Node

var c1
var c2
var c3
var c4
var c5
var c6

func _ready() -> void:
	c1 = Globals.Names.find(Globals.Party[0])
	
	#get_node("C1/Sprite2D").texture = load(small[0])

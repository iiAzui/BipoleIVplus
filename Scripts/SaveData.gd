class_name SaveData
extends Resource

# TODO: implement saving and loading from file
static var save: SaveData = load("res://Database/TestingSaveData.tres")

# All living units.
@export var units: Array[Unit]

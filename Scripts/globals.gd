extends Node




var ProtonBio = "Proton is from Nolavillia, though he grew up in Bipole and was raised by Scien.\nHe now serves under the Territory of Static as a high-ranking knight alongside\n Scien and the Elemental Offense Squad."
var ProtonPath = "res://Portraits/proton_big.png"
var ProtonPathS = "res://Sprites/proton_small.png"

var p1 = 1
var p2 = 2
var p3 = 3
var p4 = 4
var p5 = 5
var p6 = 6


var NAME = ["0","Proton","Quest","Scien","Romra"]
var NumName = [0,1,2,3,4]
var LVLEXP = ["0",[1,0],[1,0],[1,0],[1,0]]
var ATKDEFRES = ["0",[10,8,6],"Quest","Scien","Romra"]
var SPDAGLACR = ["0",[4,4,13],"Quest","Scien","Romra"]

var A1 = ["0","Slice","Quest","Scien","Romra"]
var A2 = ["0","","Quest","Scien","Romra"]
var A3 = ["0","","Quest","Scien","Romra"]
var A4 = ["0","","Quest","Scien","Romra"]

var S1 = ["0","N/A","Quest","Scien","Romra"]
var S2 = ["0","","Quest","Scien","Romra"]
var S3 = ["0","","Quest","Scien","Romra"]
var S4 = ["0","","Quest","Scien","Romra"]

var T1 = ["0","Physical Primary","Quest","Scien","Romra"]
var T2 = ["0","Xuir","Quest","Scien","Romra"]
var T3 = ["0","Knight","Quest","Scien","Romra"]
var T4 = ["0","","Quest","Scien","Romra"]

var Class = ["0","Xuir Knight","Quest","Scien","Romra"]
var HP = ["0",[30,30],"Quest","Scien","Romra"]

var ATKHPDEF = ["0",[[60,1],[60,3],[70,1]],"Quest","Scien","Romra"]
var RESAGLACR = ["0",[[35,1],[40,1],[60,1]],"Quest","Scien","Romra"]

var Bio = ["0",str(ProtonBio),"Quest","Scien","Romra"]

var EXPTHING = ["0",2,"Quest","Scien","Romra"]
var Portrait = ["0",str(ProtonPath),"Quest","Scien","Romra"]
var Sprite = ["0",str(ProtonPathS),"Quest","Scien","Romra"]





var Party = ["Proton","Rhys", "Justin"]

var Names = ["Proton","Justin", "Rhys"]

var Spawns = [Vector2(-552,224),Vector2(-520,224),Vector2(-490,224)]

var Por = [
	["res://Portraits/proton_big.png","res://Sprites/proton_small.png"],
	["res://Portraits/azure_big.png","res://Sprites/azure_small.png"],
	["res://Portraits/azure_big.png","res://Sprites/azure_small.png"]
]
var ClassBioTraits = [
	#[Class, Bio, [Trait1, Trait2, 0]]
	["N/A", "N/A",["N/A",0]],
	["Xuir Knight", "Proton is from Nolavillia, though he grew up in Bipole and was raised by Scien.\nHe now serves under the Territory of Static as a high-ranking knight alongside \nScien and the Elemental Offense Squad.", ["Xuir","Knight","Physical Primary",0] ]
]

var LevelExpExpNeeded = [
	# [Level, [Exp, neededExp]]
	[0,[0,0]],
	[1, [0,2]] #Proton
]

var MovesNums = [
	#[[atc1, atc2], [sup1, sup2]]
	[[0],[0]],
	[[1],[0]]
]

var Attacks = [
	#[Name, Range, Damage / Healing (-), effect]
	["N/A",0,0,0]
]

var Supports = [
	#[Name, Range, Damage / Healing (-), effect]
	["N/A",0,0,0]
]

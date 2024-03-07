extends Node2D

#func _ready():
	#if true == true:
		#%Name.text = "Proton"
		#%LVLEXP.text = "Level: 1 EXP: 0"
		#%ATKDEFRES.text = "ATK: 10 DEF: 8 RES: 6"
		#%SPDAGLACR.text = "SPD: 4 AGL: 4 ACR: 13"
		#if true == true:
			#%A1.text = "Slice"
			#%A2.text = ""
			#%A3.text = ""
			#%A4.text = ""
		#if true == true:
			#%S1.text = "N/A"
			#%S2.text = ""
			#%S3.text = ""
			#%S4.text = ""
		#if true == true:
			#%T1.text = "Physical Primary"
			#%T2.text = "Xuir"
			#%T3.text = "Knight"
			#%T4.text = ""
		#%Class.text = "Class: Xuir Knight"
		#%HP.text = "HP: 30/30"
		#if true == true:
			#%ATKHPDEF.text = "ATK: [60,1] HP: [70,3] DEF: [70,1]"
			#%RESAGLACR.text = "RES: [35,1] AGL: [40,1] ACR: [60,1]"
		#if true == true:
			#%Bio.text = "Proton is from Nolavillia, though he grew up in Bipole and was raised by Scien.\nHe now serves under the Territory of Static as a high-ranking knight alongside\n Scien and the Elemental Offense Squad."
		#%EXPTHING.text = "Chapter EXP Level Determinant: 2"
		#%Portrait.texture = load("res://Portraits/proton_big.png")
		
#func clear():
	#%Name.text = ""
	#%LVLEXP.text = ""
	#%ATKDEFRES.text = ""
	#%SPDAGLACR.text = ""
	#if true == true:
		#%A1.text = ""
		#%A2.text = ""
		#%A3.text = ""
		#%A4.text = ""
	#if true == true:
		#%S1.text = ""
		#%S2.text = ""
		#%S3.text = ""
		#%S4.text = ""
	#if true == true:
		#%T1.text = ""
		#%T2.text = ""
		#%T3.text = ""
		#%T4.text = ""
	#%Class.text = ""
	#%HP.text = ""
	#if true == true:
		#%ATKHPDEF.text = ""
		#%RESAGLACR.text = ""
	#if true == true:
		#%Bio.text = ""
	#%EXPTHING.text = ""
	#%Portrait.texture = load("res://Portraits/selection.png") 

func _on_area_2d_body_entered(body):
	if body.name == "Proton":
		%Name.text = "Proton"
		%LVLEXP.text = "Level: 1 EXP: 0"
		%ATKDEFRES.text = "ATK: 10 DEF: 8 RES: 6"
		%SPDAGLACR.text = "SPD: 4 AGL: 4 ACR: 13"
		if true == true:
			%A1.text = "Slice"
			%A2.text = ""
			%A3.text = ""
			%A4.text = ""
		if true == true:
			%S1.text = "N/A"
			%S2.text = ""
			%S3.text = ""
			%S4.text = ""
		if true == true:
			%T1.text = "Physical Primary"
			%T2.text = "Xuir"
			%T3.text = "Knight"
			%T4.text = ""
		%Class.text = "Class: Xuir Knight"
		%HP.text = "HP: 30/30"
		if true == true:
			%ATKHPDEF.text = "ATK: [60,1] HP: [70,3] DEF: [70,1]"
			%RESAGLACR.text = "RES: [35,1] AGL: [40,1] ACR: [60,1]"
		if true == true:
			%Bio.text = "Proton is from Nolavillia, though he grew up in Bipole and was raised by Scien.\nHe now serves under the Territory of Static as a high-ranking knight alongside\n Scien and the Elemental Offense Squad."
		%EXPTHING.text = "Chapter EXP Level Determinant: 2"
		%Portrait.texture = load("res://Portraits/proton_big.png") 
	else:
		pass

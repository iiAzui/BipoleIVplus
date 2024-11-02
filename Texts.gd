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
			#%S3.text = "" d
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

#func _on_area_2d_body_entered(body):
	#%Texts.visible = true
	#%TextsNormal.visible = false
	#if body.NumName == 1:
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
	#if body.name != "Enemy":
		#var num =  body.NumName
		#%Name.text = Globals.NAME[num]
		#%LVLEXP.text = "Level: " + str(Globals.LVLEXP[num][0]) + " EXP: " + str(Globals.LVLEXP[num][1])
		#%ATKDEFRES.text = "ATK: " + str(Globals.ATKDEFRES[num][0]) + " DEF: " + str(Globals.ATKDEFRES[num][1]) + " RES: " + str(Globals.ATKDEFRES[num][2])
		#%SPDAGLACR.text = "SPD: " + str(Globals.SPDAGLACR[num][0]) + " AGL: " + str(Globals.SPDAGLACR[num][1]) + " ACL: " + str(Globals.SPDAGLACR[num][2])
		#if true == true:
			#%A1.text = str(Globals.A1[num])
			#%A2.text = str(Globals.A2[num])
			#%A3.text = str(Globals.A3[num])
			#%A4.text = str(Globals.A4[num])
		#if true == true:
			#%S1.text = str(Globals.S1[num])
			#%S2.text = str(Globals.S2[num])
			#%S3.text = str(Globals.S3[num])
			#%S4.text = str(Globals.S4[num])
		#if true == true:
			#%T1.text = str(Globals.T1[num])
			#%T2.text = str(Globals.T2[num])
			#%T3.text = str(Globals.T3[num])
			#%T4.text = str(Globals.T4[num])
		#%Class.text = "Class: " + Globals.Class[num]
		#%HP.text = "HP: " + str(Globals.HP[num][0]) + "/" + str(Globals.HP[num][1])
		#if true == true:
			#%ATKHPDEF.text = "ATK: " + str(Globals.NAME[num])
			#%RESAGLACR.text = "RES: " + str(Globals.NAME[num])
		#if true == true:
			#%ATKHPDEF.text = "ATK: [" + str(Globals.ATKHPDEF[num][0][0]) +", "+str(Globals.ATKHPDEF[num][0][1]) + "] HP: [" + str(Globals.ATKHPDEF[num][1][0]) +", "+str(Globals.ATKHPDEF[num][1][1]) + "] DEF: []" + str(Globals.ATKHPDEF[num][2][0]) +", "+str(Globals.ATKHPDEF[num][2][1]) + "]"
			#%RESAGLACR.text = "RES: [" + str(Globals.RESAGLACR[num][0][0]) +", "+str(Globals.RESAGLACR[num][0][1]) + "] AGL: [" + str(Globals.RESAGLACR[num][1][0]) +", "+str(Globals.RESAGLACR[num][1][1]) + "] ACR: []" + str(Globals.RESAGLACR[num][2][0]) +", "+str(Globals.RESAGLACR[num][2][1]) + "]"
		#if true == true:
			#%Bio.text = str(Globals.Bio[num])
		#%EXPTHING.text = "Chapter EXP Level Determinant: " + str(Globals.EXPTHING[num])
		#%Portrait.texture = load(str(Globals.Portrait[num]))
#
#func _on_area_2d_body_exited(body):
	#%Texts.visible = false
	#%TextsNormal.visible = true
	#%P1HP.text = "HP: "+ str(Globals.HP[1][0]) + "/" + str(Globals.HP[1][1])
	#%P1Class.text = "Class: "+ str(Globals.Class[1])
	#%P1Level.text = "Lvl: "+ str(Globals.LVLEXP[1][0])
	#%P1A1.text = "Atk. 1: "+ str(Globals.A1[1])
	#%P1S1.text = "Sup. 1: "+ str(Globals.S1[1])
	#%P1Sprite.texture = load(str(Globals.Sprite[1]))

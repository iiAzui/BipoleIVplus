instant_level_ups = []

def InstantLevelUp(unit, amount):
    instant_level_ups.append({"unit": unit.DisplayName, "amount": amount})


# import turtle
# import screensetup
# import units
# import time
# import statprint
# import moves
# import random
# import cutscenes
# import difficulty
# import os
# current_directory = os.getcwd()
# import math

# GameFont = "Gamepixies"
# import oscheck
# FontMul = oscheck.TextMul

# waitspeed = 0.5 #1

# currentlydoingsomething = False

# turtle.register_shape(current_directory+"/Sprites/selection.gif")
# Selection = turtle.Turtle()
# Selection.shape(current_directory+"/Sprites/selection.gif")
# Selection.penup()
# Selection.pensize(15)
# Selection.speed(0)
# Selection.goto(-650,-300)

# TextboxMaker = turtle.Turtle()
# TextboxMaker.hideturtle()
# TextboxMaker.penup()
# TextboxMaker.speed(0)

# turtle.register_shape(current_directory+"/Sprites/enemyselection.gif")
# PotentialLocation = turtle.Turtle()
# PotentialLocation.shape(current_directory+"/Sprites/enemyselection.gif")
# PotentialLocation.hideturtle()
# PotentialLocation.penup()
# PotentialLocation.speed(0)

# ViewingUnit = None
# SelectedUnit = None

# MoveChoseNo = 0
# MoveToPerfrom = None
# TargetUnit = None
# DamageDelt = 0
# HitPercent = 0

# Status = 0 #0 is when normal, 1 is when moving unit, 2 is when attacking, 3 is when in combat screen (i don't think this is actually used), 4 is when supporting, 5 during enemy phase, 6 is when not in battle, 7 is while selecting neutral info, 8 is while selecting attack info, 9 is while selecting support info

# MoveLeft = 0

# TimeWasterSelectionVer = turtle.Turtle()
# TimeWasterSelectionVer.penup()
# TimeWasterSelectionVer.speed(1)
# TimeWasterSelectionVer.hideturtle()

# ControlsPrinter = turtle.Turtle()
# ControlsPrinter.penup()
# ControlsPrinter.hideturtle()
# ControlsPrinter.speed(0)
# ControlsPrinter.goto(-675,-330)
# ControlsPrinter.fillcolor("white")
# ControlsPrinter.begin_fill()
# ControlsPrinter.goto(40,-330)
# ControlsPrinter.goto(65,-352.5)
# ControlsPrinter.goto(-660,-352.5)
# ControlsPrinter.end_fill()

# ControlsPrinter.goto(-650,-351)
# ControlsPrinter.write("Q = Move  W = Attack  E = Support  R = Info  P = End Turn  Space = Cancel",False, align="left",font=(GameFont, round(20*FontMul)))

# ActionStatusPrinter = turtle.Turtle()
# ActionStatusPrinter.hideturtle()
# ActionStatusPrinter.penup()
# ActionStatusPrinter.speed(0)

# turtle.register_shape(current_directory+"/Sprites/acted.gif")
# turtle.register_shape(current_directory+"/Sprites/moved.gif")


# def InstantLevelUp(unittolevelup,levels):
#     for num in range(levels):
#         unittolevelup.Level += 1
#         if unittolevelup.ATKGrowth[0] >= random.randint(1,100):
#             unittolevelup.ATK += random.randint(1,unittolevelup.ATKGrowth[1])
#         if unittolevelup.HPGrowth[0] >= random.randint(1,100):
#             unittolevelup.MaxHP += random.randint(1,unittolevelup.HPGrowth[1])
#         if unittolevelup.DEFGrowth[0] >= random.randint(1,100):
#             unittolevelup.DEF += random.randint(1,unittolevelup.DEFGrowth[1])
#         if unittolevelup.RESGrowth[0] >= random.randint(1,100):
#             unittolevelup.RES += random.randint(1,unittolevelup.RESGrowth[1])
#         if unittolevelup.AGLGrowth[0] >= random.randint(1,100):
#             unittolevelup.AGL += random.randint(1,unittolevelup.AGLGrowth[1])
#         if unittolevelup.ACRGrowth[0] >= random.randint(1,100):
#             unittolevelup.ACR += random.randint(1,unittolevelup.ACRGrowth[1])
#         if len(unittolevelup.AttackUnlocks) != 0:
#             for unlock in unittolevelup.AttackUnlocks:
#                 print(unlock[1],unittolevelup.Level)
#                 if unlock[1] == unittolevelup.Level:
#                     print("Unlocked", unlock[0].CombatName)
#                     unittolevelup.Attacks.append(unlock[0])
#         if len(unittolevelup.SupportUnlocks) != 0:
#             for unlock in unittolevelup.SupportUnlocks:
#                 print(unlock[1],unittolevelup.Level)
#                 if unlock[1] == unittolevelup.Level:
#                     print("Unlocked", unlock[0].CombatName)
#                     unittolevelup.Supports.append(unlock[0])
#         if len(unittolevelup.ClassChange) != 0:
#             for unlock in unittolevelup.ClassChange:
#                 print(unlock[1])
#                 if unlock[1] == unittolevelup.Level:
#                     print("Promoting to", unlock[0])
#                     unittolevelup.UnitClass = unlock[0]

# def DisableDirectionals():
#     (screensetup.BattleScreen).onkey(None, "Up")
#     (screensetup.BattleScreen).onkey(None, "Down")
#     (screensetup.BattleScreen).onkey(None, "Right")
#     (screensetup.BattleScreen).onkey(None, "Left")

# def EnableDirectionals():
#     (screensetup.BattleScreen).onkey(UpInputed, "Up")
#     (screensetup.BattleScreen).onkey(DownInputed, "Down")
#     (screensetup.BattleScreen).onkey(RightInputed, "Right")
#     (screensetup.BattleScreen).onkey(LeftInputed, "Left")

# def DisableKeys():
#     (screensetup.BattleScreen).onkey(None, "Up")
#     (screensetup.BattleScreen).onkey(None, "Down")
#     (screensetup.BattleScreen).onkey(None, "Right")
#     (screensetup.BattleScreen).onkey(None, "Left")
#     (screensetup.BattleScreen).onkey(None, "space")
#     (screensetup.BattleScreen).onkey(None, "q")
#     (screensetup.BattleScreen).onkey(None, "w")
#     (screensetup.BattleScreen).onkey(None, "e")
#     (screensetup.BattleScreen).onkey(None,"r")
#     (screensetup.BattleScreen).onkey(None, "p")
#     (screensetup.BattleScreen).onkey(None, "1")
#     (screensetup.BattleScreen).onkey(None, "2")
#     (screensetup.BattleScreen).onkey(None, "3")
#     (screensetup.BattleScreen).onkey(None, "4")
#     (screensetup.BattleScreen).onkey(None, "5")
#     (screensetup.BattleScreen).onkey(None, "6")
#     (screensetup.BattleScreen).onkey(None, "7")
#     (screensetup.BattleScreen).onkey(None, "o")

# def DisableNumKeys():
#     (screensetup.BattleScreen).onkey(None, "1")
#     (screensetup.BattleScreen).onkey(None, "2")
#     (screensetup.BattleScreen).onkey(None, "3")
#     (screensetup.BattleScreen).onkey(None, "4")
#     (screensetup.BattleScreen).onkey(None, "5")
#     (screensetup.BattleScreen).onkey(None, "6")
#     (screensetup.BattleScreen).onkey(None, "7")

# def DisableNonDirectionals():
#     (screensetup.BattleScreen).onkey(None, "q")
#     (screensetup.BattleScreen).onkey(None, "w")
#     (screensetup.BattleScreen).onkey(None, "e")
#     (screensetup.BattleScreen).onkey(None, "p")
#     (screensetup.BattleScreen).onkey(None, "1")
#     (screensetup.BattleScreen).onkey(None, "2")
#     (screensetup.BattleScreen).onkey(None, "3")
#     (screensetup.BattleScreen).onkey(None, "4")
#     (screensetup.BattleScreen).onkey(None, "5")
#     (screensetup.BattleScreen).onkey(None, "6")
#     (screensetup.BattleScreen).onkey(None, "7")

# def DefaultInputs():
#     screensetup.BattleScreen.tracer(1)
#     (screensetup.BattleScreen).onkey(UpInputed, "Up")
#     (screensetup.BattleScreen).onkey(DownInputed, "Down")
#     (screensetup.BattleScreen).onkey(RightInputed, "Right")
#     (screensetup.BattleScreen).onkey(LeftInputed, "Left")
#     (screensetup.BattleScreen).onkey(CancelAction, "space")
#     (screensetup.BattleScreen).onkey(MoveUnit, "q")
#     (screensetup.BattleScreen).onkey(ChooseAttack, "w")
#     (screensetup.BattleScreen).onkey(ChooseSupport,"e")
#     (screensetup.BattleScreen).onkey(ChooseInfo1,"r")
#     (screensetup.BattleScreen).onkey(EndTurn,"p")

#     (screensetup.BattleScreen).onkey(None, "1")
#     (screensetup.BattleScreen).onkey(None, "2")
#     (screensetup.BattleScreen).onkey(None, "3")
#     (screensetup.BattleScreen).onkey(None, "4")
#     (screensetup.BattleScreen).onkey(None, "5")
#     (screensetup.BattleScreen).onkey(None, "6")
#     (screensetup.BattleScreen).onkey(None, "7")

#     TextboxMaker.clear()

# def ConfirmMove():
#     global SelectedUnit
#     global Status
#     if SelectedUnit.TurtleName.pos() != Selection.pos():
#         print("Confirm Move")
#         DisableDirectionals()
#         SelectedUnit.TurtleName.goto(Selection.pos())
#         Selection.penup()
#         Selection.clear()
#         Status = 0
#         SelectedUnit.HasMoved = True
#         ActionStatusPrinter.goto(SelectedUnit.TurtleName.pos())
#         ActionStatusPrinter.shape(current_directory+"/Sprites/moved.gif")
#         SelectedUnit.MoveStamp = ActionStatusPrinter.stamp()
#         SelectedUnit = None
#         ViewingUnit = None
#         DefaultInputs()
#         (screensetup.BattleScreen).onkey(MoveUnit, "q")
#     else:
#         print("You cannot move 0 tiles")

# def MoveUnit():
#     global ViewingUnit
#     global SelectedUnit
#     global Status
#     global MoveLeft
#     screensetup.BattleScreen.tracer(1)
#     if ViewingUnit.HasMoved == False:
#         if ViewingUnit in units.UnitsAlive:
#             DisableKeys()
#             (screensetup.BattleScreen).onkey(CancelAction, "space")
#             LocationToGoTo = ViewingUnit.TurtleName.pos()
#             #print(LocationToGoTo)
#             Selection.goto(LocationToGoTo)
#             SelectedUnit = ViewingUnit
#             Status = 1
#             EnableDirectionals()
#             Selection.pencolor("blue")
#             Selection.pendown()
#             MoveLeft = int(ViewingUnit.SPD)
#             (screensetup.BattleScreen).onkey(ConfirmMove, "q")

# def CancelAction():
#     global ViewingUnit
#     global SelectedUnit
#     global Status
#     DisableKeys()
#     Status = 0
#     SelectedUnit = None
#     Selection.penup()
#     Selection.clear()
#     if ViewingUnit != None:
#         Selection.goto(ViewingUnit.TurtleName.pos())
#     #(screensetup.BattleScreen).onkey(MoveUnit, "q")
#     DefaultInputs()

# def UpInputed():
#     global MoveLeft
#     global Status
#     if Status == 0:
#         statprint.CanPrint = True
#         DisableDirectionals()
#         if Selection.ycor() < 350:
#             Selection.goto(Selection.xcor(),Selection.ycor()+50)
#             print(Selection.xcor(),Selection.ycor())
#             CheckUnitOnTile()
#         EnableDirectionals()
#     elif Status == 1 or Status ==2 or Status == 4:
#         UnitIsThere = False
#         statprint.CanPrint = True
#         DisableDirectionals()
#         if Selection.ycor() < 350:
#             if MoveLeft > 0: #CHANGE THIS TO 0 REE------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                 for unit in units.UnitsAlive:
#                     if (unit.TurtleName.xcor(), unit.TurtleName.ycor()) == (Selection.xcor(), Selection.ycor() + 50) and Status == 1:
#                         UnitIsThere = True
#                 for unit in units.EnemyUnitsAlive:
#                     if (unit.TurtleName.xcor(), unit.TurtleName.ycor()) == (Selection.xcor(), Selection.ycor() + 50) and Status == 1:
#                         UnitIsThere = True
#                 if UnitIsThere == False:
#                     Selection.goto(Selection.xcor(),Selection.ycor()+50)
#                     print(Selection.xcor(),Selection.ycor())
#                     MoveLeft -= 1
#         EnableDirectionals()

# def DownInputed():
#     global MoveLeft
#     global Status
#     DisableDirectionals()
#     statprint.CanPrint = True
#     if Status == 0:
#         if Selection.ycor() > -300:
#             Selection.goto(Selection.xcor(),Selection.ycor()-50)
#             print(Selection.xcor(),Selection.ycor())
#             CheckUnitOnTile()
#     elif Status == 1 or Status == 2 or Status == 4:
#         UnitIsThere = False
#         statprint.CanPrint = True
#         DisableDirectionals()
#         if Selection.ycor() > -300:
#             if MoveLeft > 0:
#                 for unit in units.UnitsAlive:
#                     if (unit.TurtleName.xcor(), unit.TurtleName.ycor()) == (Selection.xcor(), Selection.ycor()-50) and Status == 1:
#                         UnitIsThere = True
#                 for unit in units.EnemyUnitsAlive:
#                     if (unit.TurtleName.xcor(), unit.TurtleName.ycor()) == (Selection.xcor(), Selection.ycor()-50) and Status == 1:
#                         UnitIsThere = True
#                 if UnitIsThere == False:
#                     Selection.goto(Selection.xcor(),Selection.ycor()-50)
#                     print(Selection.xcor(),Selection.ycor())
#                     MoveLeft -= 1
#     EnableDirectionals()

# def RightInputed():
#     global MoveLeft
#     global Status
#     DisableDirectionals()
#     statprint.CanPrint = True
#     if Status == 0:
#         if Selection.xcor() < 250:
#             Selection.goto(Selection.xcor()+50,Selection.ycor())
#             print(Selection.xcor(),Selection.ycor())
#             CheckUnitOnTile()
#     elif Status == 1 or Status == 2 or Status == 4:
#         UnitIsThere = False
#         statprint.CanPrint = True
#         DisableDirectionals()
#         if Selection.xcor() < 250:
#             if MoveLeft > 0:
#                 for unit in units.UnitsAlive:
#                     if (unit.TurtleName.xcor(), unit.TurtleName.ycor()) == (Selection.xcor()+50, Selection.ycor()) and Status == 1:
#                         UnitIsThere = True
#                 for unit in units.EnemyUnitsAlive:
#                     if (unit.TurtleName.xcor(), unit.TurtleName.ycor()) == (Selection.xcor()+50, Selection.ycor()) and Status == 1:
#                         UnitIsThere = True
#                 if UnitIsThere == False:
#                     Selection.goto(Selection.xcor()+50,Selection.ycor())
#                     print(Selection.xcor(),Selection.ycor())
#                     MoveLeft -= 1
#     EnableDirectionals()

# def LeftInputed():
#     global MoveLeft
#     global Status
#     DisableDirectionals()
#     statprint.CanPrint = True
#     if Status == 0:
#         if Selection.xcor() > -650:
#             Selection.goto(Selection.xcor()-50,Selection.ycor())
#             print(Selection.xcor(),Selection.ycor())
#             CheckUnitOnTile()
#     elif Status == 1 or Status == 2 or Status == 4:
#         UnitIsThere = False
#         statprint.CanPrint = True
#         DisableDirectionals()
#         if Selection.xcor() > -650:
#             if MoveLeft > 0:
#                 for unit in units.UnitsAlive:
#                     if (unit.TurtleName.xcor(), unit.TurtleName.ycor()) == (Selection.xcor()-50, Selection.ycor()) and Status == 1:
#                         UnitIsThere = True
#                 for unit in units.EnemyUnitsAlive:
#                     if (unit.TurtleName.xcor(), unit.TurtleName.ycor()) == (Selection.xcor()-50, Selection.ycor()) and Status == 1:
#                         UnitIsThere = True
#                 if UnitIsThere == False:
#                     Selection.goto(Selection.xcor()-50,Selection.ycor())
#                     print(Selection.xcor(),Selection.ycor())
#                     MoveLeft -= 1
    
#     EnableDirectionals()

# def CheckUnitOnTile():
#     global ViewingUnit
#     print(Selection.pos())
#     for unit in units.UnitsAlive:
#         if unit.TurtleName.pos() == Selection.pos():
#             ViewingUnit = unit
#             statprint.setselected(ViewingUnit,cutscenes.ChapterLevel)
#     for unit in units.EnemyUnitsAlive:
#         if unit.TurtleName.pos() == Selection.pos():
#             ViewingUnit = unit
#             statprint.setselected(ViewingUnit,cutscenes.ChapterLevel)

# def MakeTextSquare():
#     TextboxMaker.goto(-600,-100)
#     TextboxMaker.pendown()
#     TextboxMaker.fillcolor("white")
#     TextboxMaker.begin_fill()
#     TextboxMaker.goto(-600,150)
#     TextboxMaker.goto(200,150)
#     TextboxMaker.goto(200,-100)
#     TextboxMaker.goto(-600,-100)
#     TextboxMaker.end_fill()
#     TextboxMaker.penup()

# def MakeInstructionText(big,small1,small2,small3,small4):
#     screensetup.BattleScreen.tracer(0)
#     MakeTextSquare()
#     TextboxMaker.penup()
#     TextboxMaker.goto(-200,75)
#     TextboxMaker.write(big,False, align="center",font=(GameFont, round(40*FontMul), "bold"))
#     TextboxMaker.goto(-200,25)
#     TextboxMaker.write(small1,False, align="center",font=(GameFont, round(20*FontMul), "normal"))
#     TextboxMaker.goto(-200,0)
#     TextboxMaker.write(small2,False, align="center",font=(GameFont, round(20*FontMul), "normal"))
#     TextboxMaker.goto(-200,-25)
#     TextboxMaker.write(small3,False, align="center",font=(GameFont, round(20*FontMul), "normal"))
#     TextboxMaker.goto(-200,-50)
#     TextboxMaker.write(small4,False, align="center",font=(GameFont, round(20*FontMul), "normal"))
#     screensetup.BattleScreen.tracer(1)

# def OnePortrait(portrait):
#     TextboxMaker.goto(-525,75)
#     TextboxMaker.shape(portrait)
#     TextboxMaker.stamp()

# def TwoPortrait(portrait1,portrait2):
#     OnePortrait_Protrait = portrait1
#     OnePortrait(OnePortrait_Protrait)
#     TextboxMaker.goto(125,75)
#     TextboxMaker.shape(portrait2)
#     TextboxMaker.stamp()

# def AttackDamage():
#     global MoveToPerfrom
#     global SelectedUnit
#     global TargetUnit
#     global DamageDelt
#     if MoveToPerfrom.HasExtra == True and MoveToPerfrom.Extra in TargetUnit.Traits:
#         print("Move is extra effective!")
#         if MoveToPerfrom.MoveType == "Physical":
#             DamageDelt = round(((SelectedUnit.ATK * MoveToPerfrom.PWR) - (TargetUnit.DEF / 2)) * MoveToPerfrom.ExtraMul)
#         else:
#             DamageDelt = round(((SelectedUnit.ATK * MoveToPerfrom.PWR) - (TargetUnit.RES / 2)) * MoveToPerfrom.ExtraMul)
#     else:
#         if MoveToPerfrom.MoveType == "Physical":
#             DamageDelt = round((SelectedUnit.ATK * MoveToPerfrom.PWR) - (TargetUnit.DEF / 2))
#         else:
#             DamageDelt = round((SelectedUnit.ATK * MoveToPerfrom.PWR) - (TargetUnit.RES / 2))
#     if DamageDelt < 0:
#         DamageDelt = 0
#     SelectedUnit.CurrentHP -= MoveToPerfrom.HPCost

# def CounterDamage():
#     global MoveToPerfrom
#     global SelectedUnit
#     global TargetUnit
#     global DamageDelt
#     if TargetUnit.PrimaryType == "Physical":
#         DamageDelt = round( (TargetUnit.ATK * 1.25) - (SelectedUnit.DEF / 2))
#     else:
#         DamageDelt = round( (TargetUnit.ATK * 1.25) - (SelectedUnit.RES / 2))
#     if DamageDelt < 0:
#         DamageDelt = 0

# def FollowupDamage():
#     global MoveToPerfrom
#     global SelectedUnit
#     global TargetUnit
#     global DamageDelt
#     if SelectedUnit.PrimaryType == "Physical":
#         DamageDelt = round( (SelectedUnit.ATK * 1.25) - (TargetUnit.DEF / 2))
#     else:
#         DamageDelt = round( (SelectedUnit.ATK * 1.25) - (TargetUnit.RES / 2))
#     if DamageDelt < 0:
#         DamageDelt = 0

# def CalculateAttackHitPercent():
#     global SelectedUnit
#     global TargetUnit
#     global MoveToPerfrom
#     global HitPercent
#     #HitPercent = ((SelectedUnit.AGL*MoveToPerfrom.HIT)/TargetUnit.AGL)*((TargetUnit.AGL*TargetUnit.SPD)-(MoveToPerfrom.HIT-SelectedUnit.SPD)) #((a!AGL*a!HIT)/e!AGL)*((e!AGL*e!SPD)-(a!HIT-a!SPD))
#     #HitPercent = ((SelectedUnit.AGL*MoveToPerfrom.HIT)-TargetUnit.AGL)*10
#     HitPercent = ((SelectedUnit.ACR*MoveToPerfrom.HIT)-TargetUnit.AGL)*10

# def CalculateCounterHitPercent():
#     global SelectedUnit
#     global TargetUnit
#     global MoveToPerfrom
#     global HitPercent
#     ##HitPercent = (TargetUnit.AGL*1.5)-(SelectedUnit.AGL)
#     #if TargetUnit.AGL*TargetUnit.SPD > SelectedUnit.AGL*SelectedUnit.SPD:
#         ##HitPercent = 80+((TargetUnit.AGL*TargetUnit.SPD)/SelectedUnit.AGL)-((SelectedUnit.AGL*SelectedUnit.SPD)-TargetUnit.SPD)
#         ##HitPercent = ((TargetUnit.AGL*1.5)-SelectedUnit.AGL)*10
#         #HitPercent = ((TargetUnit.ACR*1)-SelectedUnit.AGL)*10
#     #else:
#         ##HitPercent = ((TargetUnit.AGL*TargetUnit.SPD)/SelectedUnit.AGL)*((SelectedUnit.AGL*SelectedUnit.SPD)-TargetUnit.SPD) - 20
#         ##HitPercent = ((TargetUnit.AGL*1.5)-SelectedUnit.AGL+2)*10
#         #HitPercent = ((TargetUnit.ACR*1)-SelectedUnit.AGL+2)*10
#     ##HitPercent = (TargetUnit.AGL*TargetUnit.SPD)-(SelectedUnit.AGL)
#     HitPercent = ((TargetUnit.ACR*1)-SelectedUnit.AGL)*10

# def CalculateFollowUpHitPercent():
#     global SelectedUnit
#     global TargetUnit
#     global MoveToPerfrom
#     global HitPercent
#     ##HitPercent = ((SelectedUnit.AGL*1.5)/TargetUnit.AGL)*((TargetUnit.AGL*TargetUnit.SPD)-(1.5-SelectedUnit.SPD)) #((a!AGL*a!HIT)/e!AGL)*((e!AGL*e!SPD)-(a!HIT-a!SPD))
#     #if SelectedUnit.AGL*SelectedUnit.SPD > TargetUnit.AGL*TargetUnit.SPD:
#         ##HitPercent = 80+((SelectedUnit.AGL*SelectedUnit.SPD)/TargetUnit.AGL)-((TargetUnit.AGL*TargetUnit.SPD)-SelectedUnit.SPD)
#         ##HitPercent = ((SelectedUnit.AGL*1.5)-TargetUnit.AGL)*10
#         #HitPercent = ((SelectedUnit.ACR*1)-TargetUnit.AGL)*10
#     #else:
#         ##HitPercent = (((SelectedUnit.AGL*SelectedUnit.SPD)/TargetUnit.AGL)*((TargetUnit.AGL*TargetUnit.SPD)-SelectedUnit.SPD))/2
#         ##HitPercent = ((SelectedUnit.AGL*1.5)-TargetUnit.AGL+2)*10
#         #HitPercent = ((SelectedUnit.ACR*1)-TargetUnit.AGL+2)*10
#     HitPercent = ((SelectedUnit.ACR*1)-TargetUnit.AGL)*10

# def AttackingStats():
#     global SelectedUnit
#     global TargetUnit
#     global HitPercent
#    #CalculateAttackHitPercent()
#     TextboxMaker.goto(-475,75)
#     thingtoprint = "HP: " + str(SelectedUnit.CurrentHP)
#     TextboxMaker.write(thingtoprint,False, align="left",font=(GameFont, round(20*FontMul), "bold"))
#     TextboxMaker.goto(-200,75)
#     thingtoprint = "Hit%: " + str(HitPercent)
#     TextboxMaker.write(thingtoprint,False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#     TextboxMaker.goto(75,75)
#     thingtoprint = "HP: " + str(TargetUnit.CurrentHP)
#     TextboxMaker.write(thingtoprint,False, align="right",font=(GameFont, round(20*FontMul), "bold"))

# def CounteringStats():
#     global SelectedUnit
#     global TargetUnit
#     global HitPercent
#     #CalculateCounterHitPercent()
#     TextboxMaker.goto(-475,75)
#     thingtoprint = "HP: " + str(SelectedUnit.CurrentHP)
#     TextboxMaker.write(thingtoprint,False, align="left",font=(GameFont, round(20*FontMul), "bold"))
#     TextboxMaker.goto(-200,75)
#     thingtoprint = "Hit%: " + str(HitPercent)
#     TextboxMaker.write(thingtoprint,False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#     TextboxMaker.goto(75,75)
#     thingtoprint = "HP: " + str(TargetUnit.CurrentHP)
#     TextboxMaker.write(thingtoprint,False, align="right",font=(GameFont, round(20*FontMul), "bold"))

# def AttackPrint1(): #The Initial Attack
#     global HitPercent
#     global DamageDelt
#     global waitspeed

#     global Status
#     if Status != 5:
#         ActionStatusPrinter.goto(SelectedUnit.TurtleName.pos())
#         ActionStatusPrinter.shape(current_directory+"/Sprites/acted.gif")
#         SelectedUnit.ActStamp = ActionStatusPrinter.stamp()

#     if difficulty.Difficulty != "Insane" and difficulty.Difficulty != "Ultimate":
#         screensetup.BattleScreen.tracer(0)
#         MakeTextSquare()
#         TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#         CalculateAttackHitPercent()
#         AttackDamage()
#         TextboxMaker.goto(-200,-25)
#         RandomNum1to100 = random.randint(1,100)

#         if HitPercent >= RandomNum1to100:
#             #print(str(HitPercent) + " >= " + str(RandomNum1to100))
#             TargetUnit.CurrentHP -= DamageDelt
#             printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.CombatName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         else: 
#             #print(str(HitPercent) + " < " + str(RandomNum1to100))
#             printthisthing = SelectedUnit.DisplayName + " missed!"
#             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         AttackingStats()
#         screensetup.BattleScreen.tracer(0)
#         if CheckIfDead() != True:
#             if Status != 5:
#                 (screensetup.BattleScreen).onkey(AttackPrint2, "space")
#             else:
#                 time.sleep(waitspeed)
#                 AttackPrint2()
#         else:
#             pass
#     else:
#         if SelectedUnit in units.UnitsAlive:
#             screensetup.BattleScreen.tracer(0)
#             CheckIfDead()
#             MakeTextSquare()
#             CounterDamage()
#             CalculateCounterHitPercent()
#             TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#             distancebetweenunits = TargetUnit.TurtleName.distance(SelectedUnit.TurtleName.pos())
#             print("Distance between units", distancebetweenunits)
#             TextboxMaker.goto(-200,-25)
#             longestrange = 0
#             isone = False
#             isinfinite = False
#             for attack in TargetUnit.Attacks:
#                 print("moverange:",attack.MoveRange)
#                 if attack.MoveRange == "Infinite":
#                     isinfinite = True
#                 elif attack.MoveRange == 1:
#                     isone = True
#                 elif attack.MoveRange > longestrange:
#                     longestrange = attack.MoveRange
#             print("Is counter range infinite",isinfinite)
#             print("Can counter at 1 range:", isone)
#             print("Longest non infinite/one range:",longestrange)
#             if isinfinite == True or (isone == True and distancebetweenunits == 50) or (distancebetweenunits <= (longestrange*50) and distancebetweenunits != 50):
#                 if HitPercent >= random.randint(1,100):
#                     SelectedUnit.CurrentHP -= DamageDelt
#                     printthisthing = str((TargetUnit.DisplayName, "counters and deals", DamageDelt,"to",SelectedUnit.DisplayName))
#                     TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#                 else: 
#                     printthisthing = TargetUnit.DisplayName + " missed!"
#                     TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             else:
#                 printthisthing = TargetUnit.DisplayName + " is out of their attack range and cannot attack!"
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             CounteringStats()
#             screensetup.BattleScreen.tracer(0)
#             if CheckIfDead() != True:
#                 if Status != 5:
#                     (screensetup.BattleScreen).onkey(AttackPrint2, "space")
#                 else:
#                     time.sleep(waitspeed)
#                     AttackPrint2()
#             else:
#                 pass
#         else:
#             screensetup.BattleScreen.tracer(0)
#             MakeTextSquare()
#             TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#             CalculateAttackHitPercent()
#             AttackDamage()
#             TextboxMaker.goto(-200,-25)
#             RandomNum1to100 = random.randint(1,100)

#             if HitPercent >= RandomNum1to100:
#                 #print(str(HitPercent) + " >= " + str(RandomNum1to100))
#                 TargetUnit.CurrentHP -= DamageDelt
#                 printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.CombatName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             else: 
#                 #print(str(HitPercent) + " < " + str(RandomNum1to100))
#                 printthisthing = SelectedUnit.DisplayName + " missed!"
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             AttackingStats()
#             screensetup.BattleScreen.tracer(0)
#             if CheckIfDead() != True:
#                 if Status != 5:
#                     (screensetup.BattleScreen).onkey(AttackPrint2, "space")
#                 else:
#                     time.sleep(waitspeed)
#                     AttackPrint2()
#             else:
#                 pass

# def AttackPrint2(): #The Enemy Followup Attack
#     global HitPercent
#     global DamageDelt
#     global waitspeed
#     (screensetup.BattleScreen).onkey(None, "space")
#     if difficulty.Difficulty != "Insane" and difficulty.Difficulty != "Ultimate": 
#         screensetup.BattleScreen.tracer(0)
#         CheckIfDead()
#         MakeTextSquare()
#         CounterDamage()
#         CalculateCounterHitPercent()
#         TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#         distancebetweenunits = TargetUnit.TurtleName.distance(SelectedUnit.TurtleName.pos())
#         print("Distance between units", distancebetweenunits)
#         TextboxMaker.goto(-200,-25)
#         longestrange = 0
#         isone = False
#         isinfinite = False
#         for attack in TargetUnit.Attacks:
#             print("moverange:",attack.MoveRange)
#             if attack.MoveRange == "Infinite":
#                 isinfinite = True
#             elif attack.MoveRange == 1:
#                 isone = True
#             elif attack.MoveRange > longestrange:
#                 longestrange = attack.MoveRange
#         print("Is counter range infinite",isinfinite)
#         print("Can counter at 1 range:", isone)
#         print("Longest non infinite/one range:",longestrange)
#         if isinfinite == True or (isone == True and distancebetweenunits == 50) or (distancebetweenunits <= (longestrange*50) and distancebetweenunits != 50):
#             if HitPercent >= random.randint(1,100):
#                 SelectedUnit.CurrentHP -= DamageDelt
#                 printthisthing = str((TargetUnit.DisplayName, "counters and deals", DamageDelt,"to",SelectedUnit.DisplayName))
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             else: 
#                 printthisthing = TargetUnit.DisplayName + " missed!"
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         else:
#             printthisthing = TargetUnit.DisplayName + " is out of their attack range and cannot attack!"
#             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         CounteringStats()
#         screensetup.BattleScreen.tracer(0)
#         if CheckIfDead() != True:
#             if Status != 5:
#                 (screensetup.BattleScreen).onkey(AttackPrint3, "space")
#             else:
#                 time.sleep(waitspeed)
#                 AttackPrint3()
#         else:
#             pass
#     else:
#         if SelectedUnit not in units.UnitsAlive:
#             screensetup.BattleScreen.tracer(0)
#             CheckIfDead()
#             MakeTextSquare()
#             CounterDamage()
#             CalculateCounterHitPercent()
#             TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#             distancebetweenunits = TargetUnit.TurtleName.distance(SelectedUnit.TurtleName.pos())
#             print("Distance between units", distancebetweenunits)
#             TextboxMaker.goto(-200,-25)
#             longestrange = 0
#             isone = False
#             isinfinite = False
#             for attack in TargetUnit.Attacks:
#                 print("moverange:",attack.MoveRange)
#                 if attack.MoveRange == "Infinite":
#                     isinfinite = True
#                 elif attack.MoveRange == 1:
#                     isone = True
#                 elif attack.MoveRange > longestrange:
#                     longestrange = attack.MoveRange
#             print("Is counter range infinite",isinfinite)
#             print("Can counter at 1 range:", isone)
#             print("Longest non infinite/one range:",longestrange)
#             if isinfinite == True or (isone == True and distancebetweenunits == 50) or (distancebetweenunits <= (longestrange*50) and distancebetweenunits != 50):
#                 if HitPercent >= random.randint(1,100):
#                     SelectedUnit.CurrentHP -= DamageDelt
#                     printthisthing = str((TargetUnit.DisplayName, "counters and deals", DamageDelt,"to",SelectedUnit.DisplayName))
#                     TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#                 else: 
#                     printthisthing = TargetUnit.DisplayName + " missed!"
#                     TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             else:
#                 printthisthing = TargetUnit.DisplayName + " is out of their attack range and cannot attack!"
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             CounteringStats()
#             screensetup.BattleScreen.tracer(0)
#             if CheckIfDead() != True:
#                 if Status != 5:
#                     (screensetup.BattleScreen).onkey(AttackPrint3, "space")
#                 else:
#                     time.sleep(waitspeed)
#                     AttackPrint3()
#             else:
#                 pass
#         else:
#             screensetup.BattleScreen.tracer(0)
#             MakeTextSquare()
#             TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#             CalculateAttackHitPercent()
#             AttackDamage()
#             TextboxMaker.goto(-200,-25)
#             RandomNum1to100 = random.randint(1,100)

#             if HitPercent >= RandomNum1to100:
#                 #print(str(HitPercent) + " >= " + str(RandomNum1to100))
#                 TargetUnit.CurrentHP -= DamageDelt
#                 printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.CombatName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             else: 
#                 #print(str(HitPercent) + " < " + str(RandomNum1to100))
#                 printthisthing = SelectedUnit.DisplayName + " missed!"
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             AttackingStats()
#             screensetup.BattleScreen.tracer(0)
#             if CheckIfDead() != True:
#                 if Status != 5:
#                     (screensetup.BattleScreen).onkey(AttackPrint3, "space")
#                 else:
#                     time.sleep(waitspeed)
#                     AttackPrint3()
#             else:
#                 pass



#     # (screensetup.BattleScreen).onkey(None, "space")
#     # CheckIfDead()
#     # MakeTextSquare()
#     # CounterDamage()
#     # CalculateCounterHitPercent()
#     # TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#     # #distancebetweenunits = TargetUnit.TurtleName.distance(SelectedUnit.TurtleName.xcor(),SelectedUnit.TurtleName.ycor())
#     # distancebetweenunits = TargetUnit.TurtleName.distance(SelectedUnit.TurtleName.pos())
#     # TextboxMaker.goto(-200,-25)
#     # isinfinity = False
#     # not1 = False
#     # is1 = False
#     # biggestnumber = -1
#     # for num in TargetUnit.Attacks:
#     #     num = num.MoveRange
#     #     if str(num) == "Infinite":
#     #         isinfinity = True
#     #         num = 99999999999999
#     #         print("Countering has Infinite Range")
#     #     elif num != 1:
#     #         not1 = True
#     #         if num > biggestnumber:
#     #             num = biggestnumber
#     #         print("Countering has", num ,"Range")
#     #     else:
#     #         is1 = True
#     #         if num > biggestnumber:
#     #             num = biggestnumber
#     #         print("Countering has 1 Range")
#     # print("IsInfinity:", str(isinfinity))
#     # print("Not1:", str(not1))
#     # print("Is1:", str(is1))
#     # if ((distancebetweenunits/50) == 1 and is1 == True) or (not1 == True and distancebetweenunits <= (biggestnumber*50)+1 and distancebetweenunits != 50) or (isinfinity == True): #(distancebetweenunits/50) in TargetUnit.AttackRange:
#     #     if HitPercent >= random.randint(1,100):
#     #         SelectedUnit.CurrentHP -= DamageDelt
#     #         printthisthing = str((TargetUnit.DisplayName, "counters and deals", DamageDelt,"to",SelectedUnit.DisplayName))
#     #         TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     #     else: 
#     #         printthisthing = TargetUnit.DisplayName + " missed!"
#     #         TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     # else:
#     #     printthisthing = TargetUnit.DisplayName + " is out of their attack range and cannot attack!"
#     #     TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     # CounteringStats()
#     # if CheckIfDead() != True:
#     #     if Status != 5:
#     #         (screensetup.BattleScreen).onkey(AttackPrint3, "space")
#     #     else:
#     #         time.sleep(waitspeed)
#     #         AttackPrint3()
#     # else:
#     #     pass

# def AttackPrint3():
#     global HitPercent
#     global DamageDelt
#     global TargetUnit
#     global SelectedUnit
#     global HitPercent
#     global waitspeed
#     screensetup.BattleScreen.tracer(0)
#     (screensetup.BattleScreen).onkey(None, "space")
#     CheckIfDead()
#     MakeTextSquare()
#     CounterDamage()
#     CalculateCounterHitPercent()
#     TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#     distancebetweenunits = TargetUnit.TurtleName.distance(SelectedUnit.TurtleName.pos())
#     print("Distance between units", distancebetweenunits)
#     TextboxMaker.goto(-200,-25)
#     longestrange = 0
#     isone = False
#     isinfinite = False
#     if TargetUnit.AGL > SelectedUnit.AGL:
#         isone = False
#         isinfinite = False
#         for attack in TargetUnit.Attacks:
#             print("moverange:",attack.MoveRange)
#             if attack.MoveRange == "Infinite":
#                 isinfinite = True
#             elif attack.MoveRange == 1:
#                 isone = True
#             elif attack.MoveRange > longestrange:
#                 longestrange = attack.MoveRange
#         print("Is counter range infinite",isinfinite)
#         print("Can counter at 1 range:", isone)
#         print("Longest non infinite/one range:",longestrange)
#         if isinfinite == True or (isone == True and distancebetweenunits == 50) or (distancebetweenunits <= (longestrange*50) and distancebetweenunits != 50):
#             if HitPercent >= random.randint(1,100):
#                 SelectedUnit.CurrentHP -= DamageDelt
#                 printthisthing = str((TargetUnit.DisplayName, "counters and deals", DamageDelt,"to",SelectedUnit.DisplayName))
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             else: 
#                 printthisthing = TargetUnit.DisplayName + " missed!"
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         else:
#             printthisthing = TargetUnit.DisplayName + " is out of their attack range and cannot attack!"
#             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         CounteringStats()
#         screensetup.BattleScreen.tracer(1)
#         if CheckIfDead() != True:
#             if Status != 5:
#                 (screensetup.BattleScreen).onkey(EndCombat1, "space")
#             else:
#                 time.sleep(waitspeed)
#                 EndCombat1()
#         else:
#             pass
#     elif SelectedUnit.AGL > TargetUnit.AGL:
#         isone = False
#         isinfinite = False
#         for attack in SelectedUnit.Attacks:
#             print("moverange:",attack.MoveRange)
#             if attack.MoveRange == "Infinite":
#                 isinfinite = True
#             elif attack.MoveRange == 1:
#                 isone = True
#             elif attack.MoveRange > longestrange:
#                 longestrange = attack.MoveRange
#         print("Is counter range infinite",isinfinite)
#         print("Can counter at 1 range:", isone)
#         print("Longest non infinite/one range:",longestrange)
#         if isinfinite == True or (isone == True and distancebetweenunits == 50) or (distancebetweenunits <= (longestrange*50) and distancebetweenunits != 50):
#             if HitPercent >= random.randint(1,100):
#                 TargetUnit.CurrentHP -= DamageDelt
#                 printthisthing = str((SelectedUnit.DisplayName, "counters and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#             else: 
#                 printthisthing = SelectedUnit.DisplayName + " missed!"
#                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         else:
#             printthisthing = SelectedUnit.DisplayName + " is out of their attack range and cannot attack!"
#             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         CounteringStats()
#         screensetup.BattleScreen.tracer(1)
#         if CheckIfDead() != True:
#             if Status != 5:
#                 (screensetup.BattleScreen).onkey(EndCombat1, "space")
#             else:
#                 time.sleep(waitspeed)
#                 EndCombat1()
#         else:
#             pass
#     else:
#         printthisthing = "Neither can attack"
#         TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#         screensetup.BattleScreen.tracer(1)
#         if CheckIfDead() != True:
#             if Status != 5:
#                 (screensetup.BattleScreen).onkey(EndCombat1, "space")
#             else:
#                 time.sleep(waitspeed)
#                 EndCombat1()
#         else:
#             pass

#     # distancebetweenunits = TargetUnit.TurtleName.distance(SelectedUnit.TurtleName.xcor(),SelectedUnit.TurtleName.ycor())
#     # print(SelectedUnit.DisplayName)
#     # if SelectedUnit.AGL > TargetUnit.AGL:
#     #     isinfinity = False
#     #     not1 = False
#     #     is1 = False
#     #     biggestnumber = 0
#     #     for num in SelectedUnit.Attacks:
#     #         num = num.MoveRange
#     #         if str(num) == "Infinite":
#     #             isinfinity = True
#     #             num = 99999999999999
#     #             print("Countering has Infinite Range")
#     #         elif num != 1:
#     #             not1 = True
#     #             if num > biggestnumber:
#     #                 num = biggestnumber
#     #             print("Countering has", num ,"Range")
#     #         else:
#     #             is1 = True
#     #             if num < biggestnumber:
#     #                 num = biggestnumber
#     #             print("Countering has 1 Range")
#     #     print("IsInfinity:", str(isinfinity))
#     #     print("Not1:", str(not1))
#     #     print("Is1:", str(is1))
#     #     if ((distancebetweenunits/50) == 1 and is1 == True) or (not1 == True and distancebetweenunits <= (biggestnumber*50)+1 and distancebetweenunits != 50) or (isinfinity == True):
#     #         CalculateFollowUpHitPercent() #CHANGE THIS ------------------------------------------------------
#     #         if HitPercent >= random.randint(1,100):
#     #             FollowupDamage()
#     #             TargetUnit.CurrentHP -= DamageDelt
#     #             TextboxMaker.goto(-200,-25)
#     #             printthisthing = str((SelectedUnit.DisplayName, "followed up with an attack and dealt", DamageDelt,"to",TargetUnit.DisplayName))
#     #             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     #         else: 
#     #             TextboxMaker.goto(-200,-25)
#     #             printthisthing = SelectedUnit.DisplayName + " missed!"
#     #             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     #         AttackingStats()
#     #     else:
#     #         TextboxMaker.goto(-200,-25)
#     #         printthisthing = SelectedUnit.DisplayName + " is out of their range!"
#     #         TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     #         AttackingStats()
#     # elif SelectedUnit.AGL < TargetUnit.AGL:
#     #     isinfinity = False
#     #     not1 = False
#     #     is1 = False
#     #     biggestnumber = 0
#     #     for num in TargetUnit.Attacks:
#     #         num = num.MoveRange
#     #         if str(num) == "Infinite":
#     #             isinfinity = True
#     #             num = 99999999999999
#     #             print("Countering has Infinite Range")
#     #         elif num != 1:
#     #             not1 = True
#     #             if num > biggestnumber:
#     #                 num = biggestnumber
#     #             print("Countering has", num ,"Range")
#     #         else:
#     #             is1 = True
#     #             if num < biggestnumber:
#     #                 num = biggestnumber
#     #             print("Countering has 1 Range")
#     #     print("IsInfinity:", str(isinfinity))
#     #     print("Not1:", str(not1))
#     #     print("Is1:", str(is1))
#     #     if ((distancebetweenunits/50) == 1 and is1 == True) or (not1 == True and distancebetweenunits <= (biggestnumber*50)+1 and distancebetweenunits != 50) or (isinfinity == True):
#     #         CalculateCounterHitPercent()
#     #         if HitPercent >= random.randint(1,100):
#     #             CounterDamage()
#     #             SelectedUnit.CurrentHP -= DamageDelt
#     #             TextboxMaker.goto(-200,-25)
#     #             printthisthing = str((TargetUnit.DisplayName, "followed up with an attack and dealt", DamageDelt,"to",SelectedUnit.DisplayName))
#     #             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     #             AttackingStats()
#     #         else:
#     #             TextboxMaker.goto(-200,-25)
#     #             printthisthing = str((TargetUnit.DisplayName, "missed their counter attack!"))
#     #             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     #             AttackingStats()
#     #     else:
#     #         TextboxMaker.goto(-200,-25)
#     #         printthisthing = str((TargetUnit.DisplayName, "is out of their attack range and cannot attack!"))
#     #         TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, 20, "bold"))
#     #         AttackingStats()
#     # else: 
#     #     TextboxMaker.goto(-200,-25)
#     #     print("AGL is equal")
#     #     printthisthing = "Neither can followup"
#     #     TextboxMaker.write(printthisthing,False, align="center",font=(GameFont, 20, "bold"))
#     # if CheckIfDead() != True:
#     #     SelectedUnit.EXP += 10
#     #     TargetUnit.EXP += 10
#     #     if Status != 5:
#     #         (screensetup.BattleScreen).onkey(EndCombat1, "space")
#     #     else:
#     #         time.sleep(waitspeed)
#     #         EndCombat1()
#     # else:
#     #     pass

# def SupportPrint():
#     global Status
#     if Status != 5:
#         ActionStatusPrinter.goto(SelectedUnit.TurtleName.pos())
#         ActionStatusPrinter.shape(current_directory+"/Sprites/acted.gif")
#         SelectedUnit.ActStamp = ActionStatusPrinter.stamp()

#     screensetup.BattleScreen.tracer(0)
#     MakeTextSquare()
#     TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#     AmountToHeal = round(SelectedUnit.ATK*MoveToPerfrom.PWR)
#     TargetUnit.CurrentHP += AmountToHeal
#     if TargetUnit.CurrentHP > TargetUnit.MaxHP:
#         TargetUnit.CurrentHP = TargetUnit.MaxHP
#     SelectedUnit.CurrentHP -= MoveToPerfrom.HPCost

#     print(MoveToPerfrom.CombatName)

#     TextboxMaker.goto(-475,75)
#     thingtoprint = "HP: " + str(SelectedUnit.CurrentHP)
#     TextboxMaker.write(thingtoprint,False, align="left",font=(GameFont, round(20*FontMul), "bold"))
#     TextboxMaker.goto(75,75)
#     thingtoprint = "HP: " + str(TargetUnit.CurrentHP)
#     TextboxMaker.write(thingtoprint,False, align="right",font=(GameFont, round(20*FontMul), "bold"))
#     TextboxMaker.goto(-200,-25)
#     printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.CombatName, "and", TargetUnit.DisplayName,"recovers",AmountToHeal,"HP"))
#     TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
    
#     if difficulty.Difficulty == "Ultimate":
#         if SelectedUnit.Level < cutscenes.ChapterLevel:
#             SelectedUnit.EXP += random.randint(15,20)
#         else:
#             SelectedUnit.EXP += random.randint(5,15)
#     else:
#         SelectedUnit.EXP += random.randint(15,20)
#     (screensetup.BattleScreen).onkey(EndCombat1, "space")

# def LevelUp(unittolevelup):
#     global waitspeed
#     (screensetup.BattleScreen).onkey(None, "space")
#     unittolevelup.Level += 1
#     if unittolevelup.ATKGrowth[0] >= random.randint(1,100):
#         unittolevelup.ATK += random.randint(1,unittolevelup.ATKGrowth[1])
#     if unittolevelup.HPGrowth[0] >= random.randint(1,100):
#         unittolevelup.MaxHP += random.randint(1,unittolevelup.HPGrowth[1])
#     if unittolevelup.DEFGrowth[0] >= random.randint(1,100):
#         unittolevelup.DEF += random.randint(1,unittolevelup.DEFGrowth[1])
#     if unittolevelup.RESGrowth[0] >= random.randint(1,100):
#         unittolevelup.RES += random.randint(1,unittolevelup.RESGrowth[1])
#     if unittolevelup.AGLGrowth[0] >= random.randint(1,100):
#         unittolevelup.AGL += random.randint(1,unittolevelup.AGLGrowth[1])
#     if unittolevelup.ACRGrowth[0] >= random.randint(1,100):
#         unittolevelup.ACR += random.randint(1,unittolevelup.ACRGrowth[1])
#     MakeTextSquare()
#     OnePortrait(unittolevelup.Portrait)
#     TextboxMaker.goto(-200,-25)
#     printthisthing = "[" + unittolevelup.DisplayName + " has leveled up!]\n" + random.choice(unittolevelup.LevelQuotes)
#     TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#     if len(unittolevelup.AttackUnlocks) != 0:
#         for unlock in unittolevelup.AttackUnlocks:
#             print(unlock[1],unittolevelup.Level)
#             if unlock[1] == unittolevelup.Level:
#                 print("Unlocked", unlock[0].CombatName)
#                 unittolevelup.Attacks.append(unlock[0])
#     if len(unittolevelup.SupportUnlocks) != 0:
#         for unlock in unittolevelup.SupportUnlocks:
#             print(unlock[1],unittolevelup.Level)
#             if unlock[1] == unittolevelup.Level:
#                 print("Unlocked", unlock[0].CombatName)
#                 unittolevelup.Supports.append(unlock[0])
#     if len(unittolevelup.ClassChange) != 0:
#         for unlock in unittolevelup.ClassChange:
#             print(unlock[1])
#             if unlock[1] == unittolevelup.Level:
#                 print("Promoting to", unlock[0])
#                 unittolevelup.UnitClass = unlock[0]
#     if Status != 5:
#         (screensetup.BattleScreen).onkey(EndCombat1, "space")
#     else:
#         time.sleep(waitspeed)
#         EndCombat1()

# def EndCombat1():
#     global SelectedUnit
#     screensetup.BattleScreen.tracer(1)
#     (screensetup.BattleScreen).onkey(None, "space")
#     if SelectedUnit.EXP >= 100:
#         SelectedUnit.EXP -= 100
#         #(screensetup.BattleScreen).onkey(EndCombat2, "space")
#         LevelUp(SelectedUnit)
#     else:
#         EndCombat2()

# def EndCombat2():
#     (screensetup.BattleScreen).onkey(None, "space")
#     global TargetUnit
#     if TargetUnit.EXP >= 100:
#         TargetUnit.EXP -= 100
#         #(screensetup.BattleScreen).onkey(EndCombat3, "space")
#         LevelUp(TargetUnit)
#     else:
#         EndCombat3()

# def EndCombat3():
#     global Status
#     global SelectedUnit
#     global TargetUnit
#     global currentlydoingsomething
#     if units.Proton in units.UnitsAlive or units.XuirMan in units.UnitsAlive:
#         if Status != 5:
#             (screensetup.BattleScreen).onkey(None, "space")
#             (screensetup.BattleScreen).onkey(None, "space")
#             TextboxMaker.clear()
#             Status = 0
#             SelectedUnit.HasMoved = True
#             SelectedUnit.HasActioned = True
#             TargetUnit = None
#             SelectedUnit = None
#             CancelAction()
#             DefaultInputs()
#         else:
#             TextboxMaker.clear()
#             TargetUnit = None
#             SelectedUnit = None
#             currentlydoingsomething = False
#             print("Attack finished, currentlydoingsomething =", currentlydoingsomething)
#     else:
#         print("Proton has been defeated")
#         MakeTextSquare()
#         TextboxMaker.goto(-200,-25)
#         TextboxMaker.write("Game Over\nProton has been defeated",False, align="center",font=(GameFont, round(20*FontMul), "bold"))
        
# def CheckIfDead():
#     (screensetup.BattleScreen).onkey(None, "space")
#     global SelectedUnit
#     global TargetUnit
#     global ViewingUnit

#     ChapterLevel = cutscenes.ChapterLevel

#     if SelectedUnit.CurrentHP <= 0:
#         if SelectedUnit.MoveStamp != None:
#             print("has MoveStamp")
#             print(SelectedUnit.MoveStamp)
#             ActionStatusPrinter.clearstamp(SelectedUnit.MoveStamp)
#             SelectedUnit.MoveStamp = None
#         else:
#             print("no MoveStamp")
#         if SelectedUnit.ActStamp != None:
#             print("has ActStamp")
#             print(SelectedUnit.ActStamp)
#             ActionStatusPrinter.clearstamp(SelectedUnit.ActStamp)
#             SelectedUnit.ActStamp = None
#         else:
#             print("no ActStamp")
#         MakeTextSquare()
#         TextboxMaker.goto(-200,-25)
#         printthisthing = SelectedUnit.DisplayName + " has been defeated."
#         TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
        
#         if TargetUnit.Level > ChapterLevel*2:
#             exp_earned = math.ceil(SelectedUnit.EXPReward*0.1)
#             print("x0.1")
#         elif TargetUnit.Level > ChapterLevel*1.5:
#             exp_earned = math.ceil(SelectedUnit.EXPReward*0.25)
#             print("x0.25")
#         elif TargetUnit.Level > ChapterLevel:
#             exp_earned = math.ceil(SelectedUnit.EXPReward*0.5)
#             print("x0.5")
#         elif TargetUnit.Level < ChapterLevel*0.35:
#             exp_earned = SelectedUnit.EXPReward*2
#             print("x2")
#         elif TargetUnit.Level < ChapterLevel*0.5:
#             exp_earned = math.ceil(SelectedUnit.EXPReward*1.75)
#             print("x1.75")
#         elif TargetUnit.Level < ChapterLevel*0.75:
#             exp_earned = math.ceil(SelectedUnit.EXPReward*1.5)
#             print("x1.5")
#         else:
#             exp_earned = SelectedUnit.EXPReward
#             print("x1")

#         if difficulty.Difficulty == "Easy":
#             TargetUnit.EXP += math.ceil(exp_earned*1.5)
#         elif difficulty.Difficulty == "Standard":
#             TargetUnit.EXP += exp_earned
#         elif difficulty.Difficulty == "Hard":
#             TargetUnit.EXP += math.ceil(exp_earned*0.75)
#         elif difficulty.Difficulty == "Insane":
#             TargetUnit.EXP += math.ceil(exp_earned*0.75)
#         elif difficulty.Difficulty == "Ultimate":
#             TargetUnit.EXP += math.ceil(exp_earned*0.5)
        
#         if SelectedUnit in units.UnitsAlive:
#             units.UnitsAlive.remove(SelectedUnit)
#         elif SelectedUnit in units.EnemyUnitsAlive:
#             units.EnemyUnitsAlive.remove(SelectedUnit)
#         SelectedUnit.TurtleName.hideturtle()
#         SelectedUnit.TurtleName.goto(-10000,-10000)
#         ViewingUnit = None
#         if Status != 5:
#             (screensetup.BattleScreen).onkey(EndCombat1, "space")
#         else:
#             time.sleep(2.5)
#             EndCombat1()
#         return True

#     elif TargetUnit.CurrentHP <= 0:
#         MakeTextSquare()
#         TextboxMaker.goto(-200,-25)
#         printthisthing = TargetUnit.DisplayName + " has been defeated."
#         TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))

#         if SelectedUnit.Level > ChapterLevel*2:
#             exp_earned = math.ceil(TargetUnit.EXPReward*0.1)
#             print("x0.1")
#         elif SelectedUnit.Level > ChapterLevel*1.5:
#             exp_earned = math.ceil(TargetUnit.EXPReward*0.25)
#             print("x0.25")
#         elif SelectedUnit.Level > ChapterLevel:
#             exp_earned = math.ceil(TargetUnit.EXPReward*0.5)
#             print("x0.5")
#         elif SelectedUnit.Level < ChapterLevel*0.35:
#             exp_earned = TargetUnit.EXPReward*2
#             print("x2")
#         elif SelectedUnit.Level < ChapterLevel*0.5:
#             exp_earned = math.ceil(TargetUnit.EXPReward*1.75)
#             print("x1.75")
#         elif SelectedUnit.Level < ChapterLevel*0.75:
#             exp_earned = math.ceil(TargetUnit.EXPReward*1.5)
#             print("x1.5")
#         else:
#             exp_earned = TargetUnit.EXPReward
#             print("x1")

#         if difficulty.Difficulty == "Easy":
#             SelectedUnit.EXP += math.ceil(exp_earned*1.5)
#         elif difficulty.Difficulty == "Standard":
#             SelectedUnit.EXP += exp_earned
#         elif difficulty.Difficulty == "Hard":
#             SelectedUnit.EXP += math.ceil(exp_earned*0.75)
#         elif difficulty.Difficulty == "Insane":
#             SelectedUnit.EXP += math.ceil(exp_earned*0.75)
#         elif difficulty.Difficulty == "Ultimate":
#             SelectedUnit.EXP += math.ceil(exp_earned*0.5)

#         if TargetUnit in units.UnitsAlive:
#             units.UnitsAlive.remove(TargetUnit)
#         elif TargetUnit in units.EnemyUnitsAlive:
#             units.EnemyUnitsAlive.remove(TargetUnit)
#         TargetUnit.TurtleName.hideturtle()
#         TargetUnit.TurtleName.goto(-10000,-10000)
#         ViewingUnit = None
#         if Status != 5:
#             (screensetup.BattleScreen).onkey(EndCombat1, "space")
#         else:
#             time.sleep(2.5)
#             EndCombat1()
#         return True

# def ConfirmAttack():
#     global MoveToPerfrom
#     global SelectedUnit
#     global TargetUnit
#     global DamageDelt
#     DisableKeys()
#     EnemyIsThere = False
#     for enemy in units.EnemyUnitsAlive:
#         if Selection.pos() == enemy.TurtleName.pos():
#             EnemyIsThere = True
#             TargetUnit = enemy
#     print("Enemy there " + str(EnemyIsThere))
#     if MoveToPerfrom.HPCost >= SelectedUnit.CurrentHP:
#         print("Not enough HP to perform this move")
#         SelectedUnit = None
#         Status = 0
#         CancelAction()
#     else:
#         if EnemyIsThere == True:
#             #print(MoveToPerfrom.DisplayName)
#             print(Selection.distance(SelectedUnit.TurtleName.pos()))
#             if MoveToPerfrom.MoveRange == "Infinite":
#                 print("Move has Infinite Range (cord range)")
#             else:
#                 print("Move has", MoveToPerfrom.MoveRange * 50, "Range (cord range)")

#             if MoveToPerfrom.MoveRange == "Infinite":
#                 print("Infinite Range")
#                 DisableKeys()
#                 MakeTextSquare()
#                 TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                 #AttackDamage()
#                 #printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.DisplayName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                 #AttackPrint1(((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",","")))
#                 AttackPrint1()
#             elif MoveToPerfrom.MoveRange == 1:
#                 print("Close Range")
#                 if Selection.distance(SelectedUnit.TurtleName.pos()) == MoveToPerfrom.MoveRange * 50:
#                     DisableKeys()
#                     MakeTextSquare()
#                     TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                     #AttackDamage()
#                     #printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.DisplayName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                     #AttackPrint1(((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",","")))
#                     AttackPrint1()
#                 else:
#                     SelectedUnit = None
#                     Status = 0
#                     CancelAction()
#             else:
#                 print("Long Range")
#                 if Selection.distance(SelectedUnit.TurtleName.pos()) != 50:
#                     DisableKeys()
#                     MakeTextSquare()
#                     TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                     #AttackDamage()
#                     #printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.DisplayName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                     #AttackPrint1(((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",","")))
#                     AttackPrint1()
#                 else:
#                     SelectedUnit = None
#                     Status = 0
#                     CancelAction()
#         else:
#             SelectedUnit = None
#             Status = 0
#             CancelAction()

# def ConfirmSupport():
#     global MoveToPerfrom
#     global SelectedUnit
#     global TargetUnit
#     global DamageDelt
#     DisableKeys()
#     AllyIsThere = False
#     for ally in units.UnitsAlive:
#         if Selection.pos() == ally.TurtleName.pos():
#             AllyIsThere = True
#             TargetUnit = ally
#     print("Ally there " + str(AllyIsThere))
#     if MoveToPerfrom.HPCost >= SelectedUnit.CurrentHP:
#         print("Not enough HP to perform this support")
#         SelectedUnit = None
#         Status = 0
#         CancelAction()
#     else:
#         if AllyIsThere == True:
#             #print(MoveToPerfrom.DisplayName)
#             print(Selection.distance(SelectedUnit.TurtleName.pos()))
#             if MoveToPerfrom.MoveRange == "Infinite":
#                 print("Support has Infinite Range (cord range)")
#             else:
#                 print("Support has", MoveToPerfrom.MoveRange * 50, "Range (cord range)")

#             if MoveToPerfrom.MoveRange == "Infinite":
#                 print("Infinite Range")
#                 DisableKeys()
#                 MakeTextSquare()
#                 TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                 #AttackDamage()
#                 #printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.DisplayName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                 #AttackPrint1(((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",","")))
#                 SupportPrint()
#             elif MoveToPerfrom.MoveRange == 1:
#                 print("Close Range")
#                 if Selection.distance(SelectedUnit.TurtleName.pos()) == MoveToPerfrom.MoveRange * 50:
#                     DisableKeys()
#                     MakeTextSquare()
#                     TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                     #AttackDamage()
#                     #printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.DisplayName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                     #AttackPrint1(((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",","")))
#                     SupportPrint()
#                 else:
#                     SelectedUnit = None
#                     Status = 0
#                     CancelAction()
#             else:
#                 print("Long Range")
#                 if Selection.distance(SelectedUnit.TurtleName.pos()) != 50:
#                     DisableKeys()
#                     MakeTextSquare()
#                     TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                     #AttackDamage()
#                     #printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.DisplayName, "and deals", DamageDelt,"to",TargetUnit.DisplayName))
#                     #AttackPrint1(((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",","")))
#                     SupportPrint()
#                 else:
#                     SelectedUnit = None
#                     Status = 0
#                     CancelAction()
#         else:
#             SelectedUnit = None
#             Status = 0
#             CancelAction()

# def Chose1():
#     global MoveChoseNo
#     global MoveLeft
#     global Status
#     global MoveToPerfrom
#     if Status == 2:
#         if len(SelectedUnit.Attacks) >= 1:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "1")
#             MoveChoseNo = 1
#             (screensetup.BattleScreen).onkey(ConfirmAttack, "w")
#             Status = 2
#             if (SelectedUnit.Attacks[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Attacks[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             Selection.pencolor("red")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No move in slot")
#     elif Status == 4:
#         if len(SelectedUnit.Supports) >= 1:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "1")
#             MoveChoseNo = 1
#             (screensetup.BattleScreen).onkey(ConfirmSupport, "e")
#             Status = 4
#             if (SelectedUnit.Supports[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Supports[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             Selection.pencolor("light green")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No support in slot")
#     elif Status == 8:
#         if len(SelectedUnit.Attacks) >= 1:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 1
#             InfoModePrint(SelectedUnit.Attacks[MoveChoseNo-1])
#     elif Status == 9:
#         if len(SelectedUnit.Supports) >= 1:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 1
#             InfoModePrint(SelectedUnit.Supports[MoveChoseNo-1])

# def Chose2():
#     global MoveChoseNo
#     global MoveLeft
#     global Status
#     global MoveToPerfrom
#     if Status == 2:
#         if len(SelectedUnit.Attacks) >= 2:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "2")
#             MoveChoseNo = 2
#             (screensetup.BattleScreen).onkey(ConfirmAttack, "w")
#             Status = 2
#             if (SelectedUnit.Attacks[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Attacks[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             Selection.pencolor("red")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No move in slot")
#     elif Status == 4:
#         if len(SelectedUnit.Supports) >= 2:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "2")
#             MoveChoseNo = 2
#             (screensetup.BattleScreen).onkey(ConfirmSupport, "e")
#             Status = 4
#             if (SelectedUnit.Supports[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Supports[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             Selection.pencolor("light green")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No support in slot")
#     elif Status == 8:
#         if len(SelectedUnit.Attacks) >= 2:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 2
#             InfoModePrint(SelectedUnit.Attacks[MoveChoseNo-1])
#     elif Status == 9:
#         if len(SelectedUnit.Supports) >= 2:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 2
#             InfoModePrint(SelectedUnit.Supports[MoveChoseNo-1])

# def Chose3():
#     global MoveChoseNo
#     global MoveLeft
#     global Status
#     global MoveToPerfrom
#     if Status == 2:
#         if len(SelectedUnit.Attacks) >= 3:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "3")
#             MoveChoseNo = 3
#             (screensetup.BattleScreen).onkey(ConfirmAttack, "w")
#             Status = 2
#             if (SelectedUnit.Attacks[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Attacks[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             Selection.pencolor("red")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No move in slot")
#     elif Status == 4:
#         if len(SelectedUnit.Supports) >= 3:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "2")
#             MoveChoseNo = 3
#             (screensetup.BattleScreen).onkey(ConfirmSupport, "e")
#             Status = 4
#             if (SelectedUnit.Supports[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Supports[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             Selection.pencolor("light green")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No support in slot")
#     elif Status == 8:
#         if len(SelectedUnit.Attacks) >= 3:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 3
#             InfoModePrint(SelectedUnit.Attacks[MoveChoseNo-1])
#     elif Status == 9:
#         if len(SelectedUnit.Supports) >= 3:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 3
#             InfoModePrint(SelectedUnit.Supports[MoveChoseNo-1])

# def Chose4():
#     global MoveChoseNo
#     global MoveLeft
#     global Status
#     global MoveToPerfrom
#     if Status == 2:
#         if len(SelectedUnit.Attacks) >= 4:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "4")
#             MoveChoseNo = 4
#             (screensetup.BattleScreen).onkey(ConfirmAttack, "w")
#             Status = 2
#             if (SelectedUnit.Attacks[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Attacks[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             Selection.pencolor("red")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No move in slot")
#     elif Status == 4:
#         if len(SelectedUnit.Supports) >= 4:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "2")
#             MoveChoseNo = 4
#             (screensetup.BattleScreen).onkey(ConfirmSupport, "e")
#             Status = 4
#             if (SelectedUnit.Supports[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Supports[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             Selection.pencolor("light green")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No support in slot")
#     elif Status == 8:
#         if len(SelectedUnit.Attacks) >= 4:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 4
#             InfoModePrint(SelectedUnit.Attacks[MoveChoseNo-1])
#     elif Status == 9:
#         if len(SelectedUnit.Supports) >= 4:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 4
#             InfoModePrint(SelectedUnit.Supports[MoveChoseNo-1])

# def Chose5():
#     global MoveChoseNo
#     global MoveLeft
#     global Status
#     global MoveToPerfrom
#     if Status == 2:
#         if len(SelectedUnit.Attacks) >= 5:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "5")
#             MoveChoseNo = 5
#             (screensetup.BattleScreen).onkey(ConfirmAttack, "w")
#             Status = 2
#             if (SelectedUnit.Attacks[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Attacks[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#             Selection.pencolor("red")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No move in slot")

#     # So, how's your day been? I've been coding Bipole IV: Liberation of Xuir all day and it's starting to get boring.

#     # I feel like I'm supposed to put something interesting here, just in case someone actually looks at the code.

#     # Nah, I'm going to talk about oatmeal.

#     # I haven't eaten any oatmeal today.

#     # Have you?

#     # ...

#     # If you responded to that, you're stupid.

#     # You literally responded to a comment (comments, actually) in a game file.

#     # But why would anyone even be looking through the game files?

#     # That's kind of weird.

#     # If you're reading this, you probably messed up somewhere in your life.

#     # Please do something else apart from looking at the internal files for Bipole IV: Liberation of Xuir.

#     # You could be doing literally anything else with your life.

#     # Okay, now I'm starting to feel stupid.

#     # No one's going to even read this.

#     # Why am I even writing this?

#     # Why do I feel the *need* to write this?

#     # Eh, whatever.

#     # If this game somehow becomes popular, someone might find this and post it to Reddit or something idk.

#     # Wouldn't that be wacky?

#     # 01010100 01101000 01100101 00100000 01110100 01101001 01101101 01100101 01101100 01101001 01101110 01100101 00100000 01110011 01101000 01100001 01101100 01101100 00100000 01101110 01101111 01110100 00100000 01100010 01100101 00100000 01100100 01101001 01110011 01110100 01110101 01110010 01100010 01100101 01100100

#     # 01010100 01101000 01100101 00100000 01011000 01110101 01101001 01110010 00100000 01010111 01110010 01100001 01110100 01101000 00100000 01101101 01110101 01110011 01110100 00100000 01101110 01101111 01110100 00100000 01100010 01100101 00100000 01110101 01101110 01101100 01100101 01100001 01110011 01101000 01100101 01100100

#     # Moment.

#     # Now get a life and do something else.

#     # Or visit infinityjka.itch.io, that's also an option that should be considered.

#     # But if your looking through the files of Bipole IV: Liberation of Xuir, then you're probably already dedicated enough to the series to have played the rest of the games.

#     # Apart from mabye Bipole XXI: Trials [The First Chapter], I don't think anyone wants to or ever will play that game.

#     # I don't recommend playing it either.

#     # Honestly, one of the worst canon Bipole games.

#     # Or canon for now. It probably won't be canon if I ever get around to finishing Bipole II: Trials.

#     # You know what, I should probably stop wasting my time on this and actually start coding Bipole.

#     # Writing this was a suprisngly effective method of procrastination, I've already wasted like 20 minutes.

#     # But I think I'm going to go back to coding.

#     # Chapter 27c isn't going to code itself (or mabye it will, but probably not).

#     # -infinityJKA

#     elif Status == 4:
#         if len(SelectedUnit.Supports) >= 5:
#             TextboxMaker.clear()
#             (screensetup.BattleScreen).onkey(None, "2")
#             MoveChoseNo = 5
#             (screensetup.BattleScreen).onkey(ConfirmSupport, "e")
#             Status = 4
#             if (SelectedUnit.Supports[MoveChoseNo - 1]).MoveRange != "Infinite":
#                 MoveLeft = SelectedUnit.Supports[MoveChoseNo - 1].MoveRange
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             else:
#                 MoveLeft = 999999
#                 MoveToPerfrom = SelectedUnit.Supports[MoveChoseNo - 1]
#             Selection.pencolor("light green")
#             Selection.pendown()
#             EnableDirectionals()
#             DisableNumKeys()
#         else:
#             print("No support in slot")
#     elif Status == 8:
#         if len(SelectedUnit.Attacks) >= 5:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 5
#             InfoModePrint(SelectedUnit.Attacks[MoveChoseNo-1])
#     elif Status == 9:
#         if len(SelectedUnit.Supports) >= 5:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 5
#             InfoModePrint(SelectedUnit.Supports[MoveChoseNo-1])

# def Chose6():
#     global MoveChoseNo
#     global MoveLeft
#     global Status
#     global MoveToPerfrom
#     if len(SelectedUnit.Attacks) >= 6 and Status == 2:
#         TextboxMaker.clear()
#         (screensetup.BattleScreen).onkey(None, "6")
#         MoveChoseNo = 6
#         (screensetup.BattleScreen).onkey(ConfirmAttack, "w")
#         Status = 2
#         if (SelectedUnit.Attacks[MoveChoseNo - 1]).MoveRange != "Infinite":
#             MoveLeft = SelectedUnit.Attacks[MoveChoseNo - 1].MoveRange
#             MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#         else:
#             MoveLeft = 999999
#             MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#         Selection.pencolor("red")
#         Selection.pendown()
#         EnableDirectionals()
#         DisableNumKeys()
#     elif Status == 2:
#         print("No move in slot")
#     elif Status == 8:
#         if len(SelectedUnit.Attacks) >= 6:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 6
#             InfoModePrint(SelectedUnit.Attacks[MoveChoseNo-1])

# def Chose7():
#     global MoveChoseNo
#     global MoveLeft
#     global Status
#     global MoveToPerfrom
#     if len(SelectedUnit.Attacks) >= 7 and Status == 2:
#         TextboxMaker.clear()
#         (screensetup.BattleScreen).onkey(None, "7")
#         MoveChoseNo = 7
#         (screensetup.BattleScreen).onkey(ConfirmAttack, "w")
#         Status = 2
#         if (SelectedUnit.Attacks[MoveChoseNo - 1]).MoveRange != "Infinite":
#             MoveLeft = SelectedUnit.Attacks[MoveChoseNo - 1].MoveRange
#             MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#         else:
#             MoveLeft = 999999
#             MoveToPerfrom = SelectedUnit.Attacks[MoveChoseNo - 1]
#         Selection.pencolor("red")
#         Selection.pendown()
#         EnableDirectionals()
#         DisableNumKeys()
#     elif Status == 2:
#         print("No move in slot")
#     elif Status == 8:
#         if len(SelectedUnit.Attacks) >= 7:
#             TextboxMaker.clear()
#             DisableKeys()
#             MoveChoseNo = 7
#             InfoModePrint(SelectedUnit.Attacks[MoveChoseNo-1])

# def ChooseAttack():
#     global Status
#     global SelectedUnit
#     global ViewingUnit
#     screensetup.BattleScreen.tracer(1)
#     if ViewingUnit != None and ViewingUnit in units.ListOfPlayableUnits:
#         if ViewingUnit.HasActioned == False:
#             DisableKeys()
#             MakeInstructionText("Attack Mode","Use the num keys to select an attack or press space to exit attack mode","The num key to press is the placement of the attack from the top of the list","After choosing a move, select the target and press w to perform the move","Use info mode (r) to check move stats")
#             Selection.goto(ViewingUnit.TurtleName.pos())
#             (screensetup.BattleScreen).onkey(CancelAction, "space")
#             SelectedUnit = ViewingUnit
#             Status = 2
#             (screensetup.BattleScreen).onkey(Chose1, "1")
#             (screensetup.BattleScreen).onkey(Chose2, "2")
#             (screensetup.BattleScreen).onkey(Chose3, "3")
#             (screensetup.BattleScreen).onkey(Chose4, "4")
#             (screensetup.BattleScreen).onkey(Chose5, "5")
#             (screensetup.BattleScreen).onkey(Chose6, "6")
#             (screensetup.BattleScreen).onkey(Chose7, "7")

# def ChooseSupport():
#     global Status
#     global SelectedUnit
#     global ViewingUnit
#     screensetup.BattleScreen.tracer(1)
#     if ViewingUnit != None and ViewingUnit in units.ListOfPlayableUnits:
#         if ViewingUnit.HasActioned == False:
#             DisableKeys()
#             MakeInstructionText("Support Mode","Use the num keys to select a support or press space to exit support mode","The num key to press is the placement of the support from the top of the list","After choosing a support, select the target and press e to perform the support","Use info mode (r) to check move stats")
#             Selection.goto(ViewingUnit.TurtleName.pos())
#             (screensetup.BattleScreen).onkey(CancelAction, "space")
#             SelectedUnit = ViewingUnit
#             Status = 4
#             (screensetup.BattleScreen).onkey(Chose1, "1")
#             (screensetup.BattleScreen).onkey(Chose2, "2")
#             (screensetup.BattleScreen).onkey(Chose3, "3")
#             (screensetup.BattleScreen).onkey(Chose4, "4")
#             (screensetup.BattleScreen).onkey(Chose5, "5")
#             (screensetup.BattleScreen).onkey(Chose6, "6")
#             (screensetup.BattleScreen).onkey(Chose7, "7")

# def ChooseInfo1():
#     global Status
#     global SelectedUnit
#     global ViewingUnit
#     screensetup.BattleScreen.tracer(1)
#     if ViewingUnit != None:
#         DisableKeys()
#         MakeInstructionText("Info Mode",("Checking: " + ViewingUnit.DisplayName),"Press w to check an attack","Press e to check a support","Press space to cancel")
#         Selection.goto(ViewingUnit.TurtleName.pos())
#         (screensetup.BattleScreen).onkey(CancelAction, "space")
#         SelectedUnit = ViewingUnit
#         Status = 7
#         (screensetup.BattleScreen).onkey(ChooseInfo2, "w")
#         (screensetup.BattleScreen).onkey(ChooseInfo3, "e")

# def ChooseInfo2():
#     global Status
#     global SelectedUnit
#     global ViewingUnit
#     screensetup.BattleScreen.tracer(1)
#     if ViewingUnit != None:
#         DisableKeys()
#         MakeInstructionText("Info Mode",("Checking: " + ViewingUnit.DisplayName),"Press the corresponding number key to the attack that you want to check","The num key to press is the placement of the attack from the top of the list","Press space to cancel")
#         Selection.goto(ViewingUnit.TurtleName.pos())
#         (screensetup.BattleScreen).onkey(CancelAction, "space")
#         SelectedUnit = ViewingUnit
#         Status = 8
#         (screensetup.BattleScreen).onkey(Chose1, "1")
#         (screensetup.BattleScreen).onkey(Chose2, "2")
#         (screensetup.BattleScreen).onkey(Chose3, "3")
#         (screensetup.BattleScreen).onkey(Chose4, "4")
#         (screensetup.BattleScreen).onkey(Chose5, "5")
#         (screensetup.BattleScreen).onkey(Chose6, "6")
#         (screensetup.BattleScreen).onkey(Chose7, "7")

# def ChooseInfo3():
#     global Status
#     global SelectedUnit
#     global ViewingUnit
#     screensetup.BattleScreen.tracer(1)
#     if ViewingUnit != None:
#         DisableKeys()
#         MakeInstructionText("Info Mode",("Checking: " + ViewingUnit.DisplayName),"Press the corresponding number key to the support that you want to check","The num key to press is the placement of the support from the top of the list","Press space to cancel")
#         Selection.goto(ViewingUnit.TurtleName.pos())
#         (screensetup.BattleScreen).onkey(CancelAction, "space")
#         SelectedUnit = ViewingUnit
#         Status = 9
#         (screensetup.BattleScreen).onkey(Chose1, "1")
#         (screensetup.BattleScreen).onkey(Chose2, "2")
#         (screensetup.BattleScreen).onkey(Chose3, "3")
#         (screensetup.BattleScreen).onkey(Chose4, "4")
#         (screensetup.BattleScreen).onkey(Chose5, "5")

# def InfoModePrint(movetoinfo):
#     DisableKeys()
#     if movetoinfo in moves.ListOfAttacks:
#         if movetoinfo.HasExtra == True:
#             MakeInstructionText(movetoinfo.DisplayName,("Type: " + movetoinfo.MoveType),("Range: " + str(movetoinfo.MoveRange)),("PWR: " + str(movetoinfo.PWR) + " | HIT: " + str(movetoinfo.HIT)),(str(movetoinfo.ExtraMul) + "x damage to " + movetoinfo.Extra))
#         else:
#             MakeInstructionText(movetoinfo.DisplayName,("Type: " + movetoinfo.MoveType),("Range: " + str(movetoinfo.MoveRange)),("PWR: " + str(movetoinfo.PWR) + " | HIT: " + str(movetoinfo.HIT)),"No Extra")
#     else:
#         MakeInstructionText(movetoinfo.DisplayName,("Type: " + movetoinfo.MoveType),("Range: " + str(movetoinfo.MoveRange)),("PWR: " + str(movetoinfo.PWR)),"")
#     (screensetup.BattleScreen).onkey(CancelAction, "space")

# def EndTurn():
#     global Status
#     global SelectedUnit
#     global TargetUnit
#     global MoveToPerfrom
#     global currentlydoingsomething
#     global waitspeed
#     if Status == 0 and SelectedUnit == None:
#         DisableKeys()

#         for unit in units.UnitsAlive:
#             unit.MoveStamp = None
#             unit.ActStamp = None
#         ActionStatusPrinter.clear()

#         screensetup.BattleScreen.tracer(1)
#         currentlydoingsomething = False
#         Status = 5
#         SelectedUnit = None
#         TargetUnit = None
#         print("End Turn")
#         PotentialLocation.showturtle()
#         for enemy in units.EnemyUnitsAlive:
#             time.sleep(0.2)
#             PotentialLocation.goto(enemy.TurtleName.pos())
#             hasdoneaction = False
#             hassupports = False
#             hasattacks = False
#             moveleft = enemy.SPD
#             ViewingUnit = enemy.TurtleName
#             if len(enemy.Supports) != 0:
#                 hassupports = True
#                 print(enemy.DisplayName,"has support(s)")
#             if len(enemy.Attacks) != 0:
#                 hasattacks = True
#                 print(enemy.DisplayName,"has attacks(s)")
#             if hassupports == True:
#                 for support in enemy.Supports:
#                     if enemy.CurrentHP > support.HPCost and hasdoneaction == False:
#                         rangedist = support.MoveRange
#                         supis1 = False
#                         supisinfin = False
#                         if rangedist == 1:
#                             supis1 = True
#                             print(enemy.DisplayName,support.CombatName,"Range 1 True")
#                         elif rangedist == "Infinite":
#                             supisinfin = True
#                             print(enemy.DisplayName,support.CombatName,"Range infinite True")
#                         else:
#                             print(enemy.DisplayName,support.CombatName,"is not 1 Range or Infinite Range")
#                         listofpossiblehealingtargets = []
#                         for otherenemy in units.EnemyUnitsAlive:
#                             if otherenemy != enemy:
#                                 if rangedist == "Infinite" and otherenemy.CurrentHP < otherenemy.MaxHP:
#                                     listofpossiblehealingtargets.append(otherenemy)
#                                     print(otherenemy.DisplayName,"is a possible support target (infinite range) for", enemy.DisplayName)
#                                 elif rangedist != "Infinite" and enemy.TurtleName.distance(otherenemy.TurtleName) <= (rangedist*50) and enemy.TurtleName.distance(otherenemy.TurtleName) != 50:
#                                     if otherenemy.CurrentHP < otherenemy.MaxHP:
#                                         listofpossiblehealingtargets.append(otherenemy)
#                                         print(otherenemy.DisplayName,"is a possible support target (>1 range) for", enemy.DisplayName)
#                                 elif rangedist != "Infinite" and enemy.TurtleName.distance(otherenemy.TurtleName) == 50 and otherenemy.CurrentHP < otherenemy.MaxHP:
#                                     listofpossiblehealingtargets.append(otherenemy)
#                                     print(otherenemy.DisplayName,"is a possible support target (1 range) for", enemy.DisplayName)
#                         prioritysuptarget = None
#                         prioritysuptargethpdifference = 0
#                         if len(listofpossiblehealingtargets) > 0:
#                             for target in listofpossiblehealingtargets:
#                                 if (target.MaxHP - target.CurrentHP) > prioritysuptargethpdifference:
#                                     prioritysuptarget = target
#                                     prioritysuptargethpdifference = (target.MaxHP - target.CurrentHP)
#                                     print(prioritysuptarget.DisplayName,"is now the target for support")
#                                 elif (target.MaxHP - target.CurrentHP) == prioritysuptargethpdifference:
#                                     if target.MaxHP > prioritysuptarget.MaxHP:
#                                         prioritysuptarget = target
#                                         prioritysuptargethpdifference = (target.MaxHP - target.CurrentHP)
#                                         print(prioritysuptarget.DisplayName,"is now the target for support")
#                         if prioritysuptarget != None and hasdoneaction == False:
#                             while currentlydoingsomething == True:
#                                 print("Another action is happening right now, delaying action")
#                                 time.sleep(1)
#                             currentlydoingsomething = True
#                             print("Now supporting", prioritysuptarget.DisplayName)
#                             hasdoneaction = True
#                             SelectedUnit = enemy
#                             TargetUnit = prioritysuptarget
#                             MoveToPerfrom = support
#                             print(MoveToPerfrom.CombatName)
#                             MakeTextSquare()
#                             TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                             AmountToHeal = round(SelectedUnit.ATK*MoveToPerfrom.PWR)
#                             TargetUnit.CurrentHP += AmountToHeal
#                             if TargetUnit.CurrentHP > TargetUnit.MaxHP:
#                                 TargetUnit.CurrentHP = TargetUnit.MaxHP
#                             SelectedUnit.CurrentHP -= MoveToPerfrom.HPCost
#                             TextboxMaker.goto(-475,75)
#                             thingtoprint = "HP: " + str(SelectedUnit.CurrentHP)
#                             TextboxMaker.write(thingtoprint,False, align="left",font=(GameFont, round(20*FontMul), "bold"))
#                             TextboxMaker.goto(75,75)
#                             thingtoprint = "HP: " + str(TargetUnit.CurrentHP)
#                             TextboxMaker.write(thingtoprint,False, align="right",font=(GameFont, round(20*FontMul), "bold"))
#                             TextboxMaker.goto(-200,-25)
#                             printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.CombatName, "and", TargetUnit.DisplayName,"recovers",AmountToHeal,"HP"))
#                             TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#                             time.sleep(waitspeed)
#                             TextboxMaker.clear()
#                             TargetUnit = None
#                             SelectedUnit = None
#                             currentlydoingsomething = False
                            
#                         else:
#                             print("No support targets within range")
#             if hasattacks == True and hasdoneaction == False:
#                 print("Checking for attack target")
#                 for attack in enemy.Attacks:
#                     if enemy.CurrentHP > attack.HPCost and hasdoneaction == False:
#                         rangedist = attack.MoveRange
#                         attackis1 = False
#                         attackisinfin = False
#                         if rangedist == 1:
#                             attackis1 = True
#                             print(enemy.DisplayName,attack.CombatName,"Range 1 True")
#                         elif rangedist == "Infinite":
#                             attackisinfin = True
#                             print(enemy.DisplayName,attack.CombatName,"Range infinite True")
#                         else:
#                             print(enemy.DisplayName,attack.CombatName,"is not 1 Range or Infinite Range")
#                         listofpossibleattacktargets = []
#                         for attacktarget in units.UnitsAlive:
#                             if rangedist == "Infinite":
#                                 listofpossibleattacktargets.append(attacktarget)
#                                 print(attacktarget.DisplayName,"is a possible attack (inf range) target for", enemy.DisplayName)
#                             elif rangedist == 1 and enemy.TurtleName.distance(attacktarget.TurtleName) == 50:
#                                 listofpossibleattacktargets.append(attacktarget)
#                                 print(attacktarget.DisplayName,"is a possible attack (range 1) target for", enemy.DisplayName)
#                             elif rangedist != "Infinite" and enemy.TurtleName.distance(attacktarget.TurtleName) <= (rangedist*50) and enemy.TurtleName.distance(attacktarget.TurtleName) != 50:
#                                 listofpossibleattacktargets.append(attacktarget)
#                                 print(attacktarget.DisplayName,"is a possible attack (range > 1) target for", enemy.DisplayName)
#                         priorityattacktarget = None
#                         priorityattacktargethpdifference = 0
#                         highestdamage = -1
#                         targettoattack = None
#                         if len(listofpossibleattacktargets) > 0:
#                             for target in listofpossibleattacktargets:
#                                 damage = 0
#                                 if attack.HasExtra == True and attack.Extra in target.Traits:
#                                     if attack.MoveType == "Physical":
#                                         damage = round(((enemy.ATK * attack.PWR) - (target.DEF / 2)) * attack.ExtraMul)
#                                     else:
#                                         damage = round(((enemy.ATK * attack.PWR) - (target.RES / 2)) * attack.ExtraMul)
#                                 else:
#                                     if attack.MoveType == "Physical":
#                                         damage = round((enemy.ATK * attack.PWR) - (target.DEF / 2))
#                                     else:
#                                         damage = round((enemy.ATK * attack.PWR) - (target.RES / 2))
#                                 if damage < 0:
#                                     damage = 0
#                                 print("Potential Damage:", damage)
#                                 if damage > highestdamage:
#                                     print(target.DisplayName, "is now the target")    
#                                     highestdamage = damage
#                                     targettoattack = target
#                             print("currentlydoingsomething =", currentlydoingsomething)
#                             while currentlydoingsomething == True:
#                                 print("Another action is happening right now, delaying action")
#                                 time.sleep(2)
#                                 pass
#                             currentlydoingsomething = True
#                             hasdoneaction = True
#                             print(targettoattack.DisplayName,"will now be attacked")
#                             SelectedUnit = enemy
#                             TargetUnit = targettoattack
#                             MoveToPerfrom = attack
#                             MakeTextSquare()
#                             TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                             AttackPrint1()
#             if hasdoneaction == False:
#                 print("Preparing to move")
#                 PotentialLocation.goto(enemy.TurtleName.pos())
#                 cantgoto = []
#                 whichdirection = 0
#                 cantmoveto = None
#                 whichdirection = None
#                 for x in range(enemy.SPD):
#                     movedtile = False
#                     while hasdoneaction == False and movedtile == False:
#                         whichdirection = random.randint(1,4)
#                         print("previous", cantmoveto, "now",whichdirection)
#                         if whichdirection != cantmoveto:
#                             if whichdirection == 1:
#                                 PotentialLocation.goto(PotentialLocation.xcor()+50,PotentialLocation.ycor())
#                                 movedir = "right"
#                             elif whichdirection == 2:
#                                 PotentialLocation.goto(PotentialLocation.xcor()-50,PotentialLocation.ycor())
#                                 movedir = "left"
#                             elif whichdirection == 3:
#                                 PotentialLocation.goto(PotentialLocation.xcor(),PotentialLocation.ycor()+50)
#                                 movedir = "up"
#                             elif whichdirection == 4:
#                                 PotentialLocation.goto(PotentialLocation.xcor(),PotentialLocation.ycor()-50)
#                                 movedir = "down"
#                             issomeonealreadythere = False
#                             for unit in units.UnitsAlive:
#                                 if unit.TurtleName.pos() == PotentialLocation.pos():
#                                     issomeonealreadythere = True
#                             for unit in units.EnemyUnitsAlive:
#                                 if unit.TurtleName.pos() == PotentialLocation.pos():
#                                     issomeonealreadythere = True
#                             optimalpath = False
#                             if len(enemy.Supports) == 0 or enemy.CurrentHP > (enemy.MaxHP/4):
#                                 for unit in units.UnitsAlive:
#                                     if movedir == "right" and unit.TurtleName.xcor() >= enemy.TurtleName.xcor():
#                                         optimalpath = True
#                                     elif movedir == "left" and unit.TurtleName.xcor() <= enemy.TurtleName.xcor():
#                                         optimalpath = True
#                                     elif movedir == "up" and unit.TurtleName.ycor() >= enemy.TurtleName.ycor():
#                                         optimalpath = True
#                                     elif movedir == "down" and unit.TurtleName.ycor() <= enemy.TurtleName.ycor():
#                                         optimalpath = True
#                             else:
#                                  optimalpath = True
#                             if PotentialLocation.xcor() >= -650 and PotentialLocation.xcor() <= 250 and PotentialLocation.ycor() >= -300 and PotentialLocation.ycor() <= 350 and issomeonealreadythere == False and optimalpath == True:
#                                 print("Moved", movedir)
#                                 movedtile = True
#                                 enemy.TurtleName.goto(PotentialLocation.pos())
#                                 if whichdirection == 1:
#                                     cantmoveto = 2
#                                 elif whichdirection == 2:
#                                     cantmoveto = 1
#                                 elif whichdirection == 3:
#                                     cantmoveto = 4
#                                 elif whichdirection == 4:
#                                     cantmoveto = 3
#                                 time.sleep(waitspeed/4)
#                                 if hassupports == True:
#                                     for support in enemy.Supports:
#                                         if enemy.CurrentHP > support.HPCost and hasdoneaction == False:
#                                             rangedist = support.MoveRange
#                                             supis1 = False
#                                             supisinfin = False
#                                             if rangedist == 1:
#                                                 supis1 = True
#                                                 print(enemy.DisplayName,support.CombatName,"Range 1 True")
#                                             elif rangedist == "Infinite":
#                                                 supisinfin = True
#                                                 print(enemy.DisplayName,support.CombatName,"Range infinite True")
#                                             else:
#                                                 print(enemy.DisplayName,support.CombatName,"is not 1 Range or Infinite Range")
#                                             listofpossiblehealingtargets = []
#                                             for otherenemy in units.EnemyUnitsAlive:
#                                                 if otherenemy != enemy:
#                                                     if rangedist == "Infinite" and otherenemy.CurrentHP < otherenemy.MaxHP:
#                                                         listofpossiblehealingtargets.append(otherenemy)
#                                                         print(otherenemy.DisplayName,"is a possible support target (infinite range) for", enemy.DisplayName)
#                                                     elif rangedist != "Infinite" and enemy.TurtleName.distance(otherenemy.TurtleName) <= (rangedist*50) and enemy.TurtleName.distance(otherenemy.TurtleName) != 50:
#                                                         if otherenemy.CurrentHP < otherenemy.MaxHP:
#                                                             listofpossiblehealingtargets.append(otherenemy)
#                                                             print(otherenemy.DisplayName,"is a possible support target (>1 range) for", enemy.DisplayName)
#                                                     elif rangedist != "Infinite" and enemy.TurtleName.distance(otherenemy.TurtleName) == 50 and otherenemy.CurrentHP < otherenemy.MaxHP:
#                                                         listofpossiblehealingtargets.append(otherenemy)
#                                                         print(otherenemy.DisplayName,"is a possible support target (1 range) for", enemy.DisplayName)
#                                             prioritysuptarget = None
#                                             prioritysuptargethpdifference = 0
#                                             if len(listofpossiblehealingtargets) > 0:
#                                                 for target in listofpossiblehealingtargets:
#                                                     if (target.MaxHP - target.CurrentHP) > prioritysuptargethpdifference:
#                                                         prioritysuptarget = target
#                                                         prioritysuptargethpdifference = (target.MaxHP - target.CurrentHP)
#                                                         print(prioritysuptarget.DisplayName,"is now the target for support")
#                                                     elif (target.MaxHP - target.CurrentHP) == prioritysuptargethpdifference:
#                                                         if target.MaxHP > prioritysuptarget.MaxHP:
#                                                             prioritysuptarget = target
#                                                             prioritysuptargethpdifference = (target.MaxHP - target.CurrentHP)
#                                                             print(prioritysuptarget.DisplayName,"is now the target for support")
#                                             if prioritysuptarget != None and hasdoneaction == False:
#                                                 while currentlydoingsomething == True:
#                                                     print("Another action is happening right now, delaying action")
#                                                     time.sleep(1)
#                                                 currentlydoingsomething = True
#                                                 print("Now supporting", prioritysuptarget.DisplayName)
#                                                 hasdoneaction = True
#                                                 SelectedUnit = enemy
#                                                 TargetUnit = prioritysuptarget
#                                                 MoveToPerfrom = support
#                                                 print(MoveToPerfrom.CombatName)
#                                                 MakeTextSquare()
#                                                 TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                                                 AmountToHeal = round(SelectedUnit.ATK*MoveToPerfrom.PWR)
#                                                 TargetUnit.CurrentHP += AmountToHeal
#                                                 if TargetUnit.CurrentHP > TargetUnit.MaxHP:
#                                                     TargetUnit.CurrentHP = TargetUnit.MaxHP
#                                                 SelectedUnit.CurrentHP -= MoveToPerfrom.HPCost
#                                                 TextboxMaker.goto(-475,75)
#                                                 thingtoprint = "HP: " + str(SelectedUnit.CurrentHP)
#                                                 TextboxMaker.write(thingtoprint,False, align="left",font=(GameFont, round(20*FontMul), "bold"))
#                                                 TextboxMaker.goto(75,75)
#                                                 thingtoprint = "HP: " + str(TargetUnit.CurrentHP)
#                                                 TextboxMaker.write(thingtoprint,False, align="right",font=(GameFont, round(20*FontMul), "bold"))
#                                                 TextboxMaker.goto(-200,-25)
#                                                 printthisthing = str((SelectedUnit.DisplayName, "uses", MoveToPerfrom.CombatName, "and", TargetUnit.DisplayName,"recovers",AmountToHeal,"HP"))
#                                                 TextboxMaker.write((((((printthisthing).replace("'","").replace("(","")).replace(")","")).replace(",",""))),False, align="center",font=(GameFont, round(20*FontMul), "bold"))
#                                                 time.sleep(waitspeed)
#                                                 TextboxMaker.clear()
#                                                 TargetUnit = None
#                                                 SelectedUnit = None
#                                                 currentlydoingsomething = False
                                                
#                                             else:
#                                                 print("No support targets within range")
#                                 if hasattacks == True and hasdoneaction == False:
#                                     print("Checking for attack target")
#                                     for attack in enemy.Attacks:
#                                         if enemy.CurrentHP > attack.HPCost and hasdoneaction == False:
#                                             rangedist = attack.MoveRange
#                                             attackis1 = False
#                                             attackisinfin = False
#                                             if rangedist == 1:
#                                                 attackis1 = True
#                                                 print(enemy.DisplayName,attack.CombatName,"Range 1 True")
#                                             elif rangedist == "Infinite":
#                                                 attackisinfin = True
#                                                 print(enemy.DisplayName,attack.CombatName,"Range infinite True")
#                                             else:
#                                                 print(enemy.DisplayName,attack.CombatName,"is not 1 Range or Infinite Range")
#                                             listofpossibleattacktargets = []
#                                             for attacktarget in units.UnitsAlive:
#                                                 if rangedist == "Infinite":
#                                                     listofpossibleattacktargets.append(attacktarget)
#                                                     print(attacktarget.DisplayName,"is a possible attack (inf range) target for", enemy.DisplayName)
#                                                 elif rangedist == 1 and enemy.TurtleName.distance(attacktarget.TurtleName) == 50:
#                                                     listofpossibleattacktargets.append(attacktarget)
#                                                     print(attacktarget.DisplayName,"is a possible attack (range 1) target for", enemy.DisplayName)
#                                                 elif rangedist != "Infinite" and enemy.TurtleName.distance(attacktarget.TurtleName) <= (rangedist*50) and enemy.TurtleName.distance(attacktarget.TurtleName) != 50:
#                                                     listofpossibleattacktargets.append(attacktarget)
#                                                     print(attacktarget.DisplayName,"is a possible attack (range > 1) target for", enemy.DisplayName)
#                                             priorityattacktarget = None
#                                             priorityattacktargethpdifference = 0
#                                             highestdamage = -1
#                                             targettoattack = None
#                                             if len(listofpossibleattacktargets) > 0:
#                                                 for target in listofpossibleattacktargets:
#                                                     damage = 0
#                                                     if attack.HasExtra == True and attack.Extra in target.Traits:
#                                                         if attack.MoveType == "Physical":
#                                                             damage = round(((enemy.ATK * attack.PWR) - (target.DEF / 2)) * attack.ExtraMul)
#                                                         else:
#                                                             damage = round(((enemy.ATK * attack.PWR) - (target.RES / 2)) * attack.ExtraMul)
#                                                     else:
#                                                         if attack.MoveType == "Physical":
#                                                             damage = round((enemy.ATK * attack.PWR) - (target.DEF / 2))
#                                                         else:
#                                                             damage = round((enemy.ATK * attack.PWR) - (target.RES / 2))
#                                                     if damage < 0:
#                                                         damage = 0
#                                                     print("Potential Damage:", damage)
#                                                     if damage > highestdamage:
#                                                         print(target.DisplayName, "is now the target")    
#                                                         highestdamage = damage
#                                                         targettoattack = target
#                                                 print("currentlydoingsomething =", currentlydoingsomething)
#                                                 while currentlydoingsomething == True:
#                                                     print("Another action is happening right now, delaying action")
#                                                     time.sleep(2)
#                                                     pass
#                                                 currentlydoingsomething = True
#                                                 hasdoneaction = True
#                                                 print(targettoattack.DisplayName,"will now be attacked")
#                                                 SelectedUnit = enemy
#                                                 TargetUnit = targettoattack
#                                                 MoveToPerfrom = attack
#                                                 MakeTextSquare()
#                                                 TwoPortrait(SelectedUnit.Portrait, TargetUnit.Portrait)
#                                                 AttackPrint1()

#                             else:
#                                 cantgoto.append(str(whichdirection))
#                                 PotentialLocation.goto(enemy.TurtleName.pos())
#                                 print("Cannot move", movedir)
#                                 if "1" in cantgoto and "2" in cantgoto and "3" in cantgoto and "4" in cantgoto:
#                                     hasdoneaction = True
#                                     print("Cannot move in any direction")
#                         else:
#                             cantgoto.append(str(whichdirection))
#                             PotentialLocation.goto(enemy.TurtleName.pos())
#                             print("Cannot move", movedir)
#                             if "1" in cantgoto and "2" in cantgoto and "3" in cantgoto and "4" in cantgoto:
#                                 hasdoneaction = True
#                                 print("Cannot move in any direction")




                            



#         print("Preparing Player Phase...")
#         Status == 0
#         for ally in units.UnitsAlive:
#             ally.HasMoved = False
#             ally.HasActioned = False
#         SelectedUnit = None
#         ViewingUnit = None
#         PotentialLocation.hideturtle()
#         if units.Proton in units.UnitsAlive or units.XuirMan in units.UnitsAlive:
#             print("Enemy units alive:", len(units.EnemyUnitsAlive))
#             if len(units.EnemyUnitsAlive) != 0:
#                 print("Player Phase has started")
#                 CancelAction()
#             else:
#                 DisableKeys()
#                 Status = 6
#                 print("All enemies have been defeated")
#                 for ally in units.ListOfPlayableUnits:
#                     ally.CurrentHP = ally.MaxHP
#                     ally.TurtleName.hideturtle()
#                 cutscenes.Text3("[Battle Complete]")
#                 TimeWasterSelectionVer.goto(TimeWasterSelectionVer.xcor()+100,TimeWasterSelectionVer.ycor()+100)
#                 cutscenes.Cutscene()
#         else:
#             print("Proton has been defeated")
#             MakeTextSquare()
#             TextboxMaker.goto(-200,-25)
#             TextboxMaker.write("Game Over\nProton has been defeated",False, align="center",font=(GameFont, round(20*FontMul), "bold"))

    
        
        
#     else:
#         print("Error: Status != 0 and/or Selected Unit != None")
#         print("Status:", Status)
#         if SelectedUnit != None:
#             print("Selected Unit:", SelectedUnit.DisplayName)
#         else:
#             print("There is no selected unit")




# DefaultInputs()

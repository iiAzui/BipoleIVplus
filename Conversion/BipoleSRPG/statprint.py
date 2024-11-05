import turtle
import units
import time
import screensetup
import select
import os
current_directory = os.getcwd()

StatPrinter = turtle.Turtle()
StatPrinter.hideturtle()
StatPrinter.speed(0)

CanPrint = True

gamefont = "Gamepixies"

import oscheck
FontMul = oscheck.TextMul

def setselected(unit,chapterlevel):
    global CanPrint
    if CanPrint == True:
        unit.TurtleName.onclick(None)
        Selected = unit
        StatPrint(unit,chapterlevel)
        unit.TurtleName.onclick(setselected(unit,chapterlevel))
        CanPrint = False
    else:
        return

def SideSquare():
    global CanPrint
    if CanPrint == True:
        StatPrinter.fillcolor("white")
        StatPrinter.speed(0)
        StatPrinter.penup()
        StatPrinter.goto(300,500)
        StatPrinter.pendown()
        StatPrinter.begin_fill()
        StatPrinter.goto(300,-750)
        StatPrinter.goto(1000,-750)
        StatPrinter.goto(1000,750)
        StatPrinter.goto(300,750)
        StatPrinter.end_fill()
        StatPrinter.penup()
        CanPrint = False
    else:
        return

def StatPrint(unit,chapterlevel):
    global CanPrint
    if CanPrint == True:
        screensetup.BattleScreen.tracer(0)
        StatPrinter.clear()
        select.DisableKeys()
        SideSquare()
        StatPrinter.goto(510,325)
        StatPrinter.write(unit.DisplayName,False, align="center",font=(gamefont, round(35*FontMul), "bold"))
        StatPrinter.goto(625,275)
        #StatPrinter.showturtle()
        StatPrinter.shape(unit.Portrait)
        StatPrinter.stamp()
        StatPrinter.shape("arrow")
        #StatPrinter.hideturtle()
        StatPrinter.goto(440,285)
        Text_To_Write = (((str(("Level:",unit.Level,"EXP:", unit.EXP)).replace("'","")).replace(",","")).replace("(","")).replace(")","")
        StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(20*FontMul), "bold"))
        StatPrinter.goto(440,255)
        Text_To_Write = (((str(("ATK:",unit.ATK,"DEF:",unit.DEF,"RES:",unit.RES)).replace("'","")).replace(",","")).replace("(","")).replace(")","")
        StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(20*FontMul), "bold"))
        StatPrinter.goto(440,225)
        Text_To_Write = (((str(("SPD:",unit.SPD,"AGL:",unit.AGL,"ACR:",unit.ACR)).replace("'","")).replace(",","")).replace("(","")).replace(")","")
        StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(20*FontMul), "bold"))
        StatPrinter.goto(380,195)
        StatPrinter.write("Attacks:",False, align="center",font=(gamefont, round(15*FontMul), "bold"))
        if len(unit.Attacks) != 0:
            yindex = 170
            listnoindex = 0
            for attack in unit.Attacks:
                StatPrinter.goto(380,yindex)
                #Text_To_Write = ((str((unit.Attacks[listnoindex]).replace("'","")).replace(",","")).replace("(","")).replace(")","")
                Text_To_Write = str((unit.Attacks[listnoindex]).DisplayName)
                StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(15*FontMul), "bold"))
                yindex -= 25
                listnoindex += 1
        else:
            StatPrinter.goto(380,170)
            StatPrinter.write("N/A",False, align="center",font=(gamefont, round(15*FontMul), "bold"))
        StatPrinter.goto(475,195)
        StatPrinter.write("Supports:",False, align="center",font=(gamefont, round(15*FontMul), "bold"))
        if len(unit.Supports) != 0:
            yindex = 170
            listnoindex = 0
            for attack in unit.Supports:
                StatPrinter.goto(475,yindex)
                #Text_To_Write = ((str((unit.Supports[listnoindex]).replace("'","")).replace(",","")).replace("(","")).replace(")","")
                Text_To_Write = str((unit.Supports[listnoindex]).DisplayName)
                StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(15*FontMul), "bold"))
                yindex -= 25
                listnoindex += 1
        else:
            StatPrinter.goto(475,170)
            StatPrinter.write("N/A",False, align="center",font=(gamefont, round(15*FontMul), "bold"))
        StatPrinter.goto(600,195)
        StatPrinter.write("Traits:",False, align="center",font=(gamefont, round(15*FontMul), "bold"))
        if len(unit.Traits) != 0:
            yindex = 170
            listnoindex = 0
            for attack in unit.Traits:
                StatPrinter.goto(600,yindex)
                Text_To_Write = ((str((unit.Traits[listnoindex]).replace("'","")).replace(",","")).replace("(","")).replace(")","")
                StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(15*FontMul), "bold"))
                yindex -= 25
                listnoindex += 1
        else:
            #StatPrinter.goto(600,170)
            StatPrinter.goto(630,170)
            StatPrinter.write("N/A",False, align="center",font=(gamefont, round(15*FontMul), "bold"))
        StatPrinter.goto(505,-25)
        Text_To_Write = str("Class: " + str(unit.UnitClass))
        StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(20*FontMul), "bold"))
        StatPrinter.goto(505,-70)
        Text_To_Write = str("HP: " + str(unit.CurrentHP) + "/" + str(unit.MaxHP))
        StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(40*FontMul), "bold"))
        StatPrinter.goto(505,-110)
        StatPrinter.write("Growths",False, align="center",font=(gamefont, round(20*FontMul), "bold"))
        StatPrinter.goto(505,-135)
        Text_To_Write = str("ATK: " +str(unit.ATKGrowth) + "   HP: " + str(unit.HPGrowth) + "   DEF: " + str(unit.DEFGrowth))
        StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(20*FontMul), "bold"))
        StatPrinter.goto(505,-160)
        Text_To_Write = str("RES: " + str(unit.RESGrowth) + "   AGL: " + str(unit.AGLGrowth) + "   ACR: " + str(unit.ACRGrowth))
        StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(20*FontMul), "bold"))
        StatPrinter.goto(505,-210)
        StatPrinter.write("Bio:",False, align="center",font=(gamefont, round(25*FontMul), "bold"))
        StatPrinter.goto(505,-285)
        Text_To_Write = unit.Bio
        StatPrinter.write(Text_To_Write,False, align="center",font=(gamefont, round(10*FontMul), "bold"))

        StatPrinter.goto(505,-350)
        StatPrinter.write(("Chapter EXP Level Determinant: " + str(chapterlevel)),False, align="center",font=(gamefont, round(20*FontMul), "bold"))


        StatPrinter.hideturtle()
        screensetup.BattleScreen.tracer(1)
        CanPrint = False
        select.DefaultInputs()
    else:
        return
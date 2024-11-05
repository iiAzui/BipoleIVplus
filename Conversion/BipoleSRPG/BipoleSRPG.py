import username
import difficulty
import time
import os

current_directory = os.getcwd()
print("")
print("=======================================================")
print("============ Bipole IV: Liberation of Xuir ============")
print("============          Release 2.2          ============")
print("=======================================================")
print("")
print(" ~~~~~ Made by infinityJKA (infinityjka.itch.io) ~~~~~")
#print("!Make sure to read the manual (guide.pdf) before playing!")
saveloop = True
loadsaveornewgame = None

if __name__ == "__main__":
    while saveloop == True:
        print("")
        print("[1] Load Game [5] New Game")
        loadsaveornewgame = input("")
        if loadsaveornewgame == "1" or loadsaveornewgame == "5":
            saveloop = False
        if loadsaveornewgame == "5":

            entercodeloop = True
            nameentered = ""
            while entercodeloop == True:
                print()
                nameentered = input("Enter your full name: ")
                if nameentered == "":
                    nameentered = "The User"
                print("\""+nameentered+"\" is your full name, correct?")
                print("[1] Yes [2] No")
                nameresponse = input("")
                if nameresponse == "1":
                    username.SetUserName(nameentered)
                    entercodeloop = False
                else:
                    pass

            saveloop = True
            difselected = None
            while saveloop == True:
                print("")
                print("====== Choose Game Difficulty ======")
                print("[1] Easy (150% EXP)")
                print("[2] Standard (Recommended for a first playthrough)")
                print("[3] Hard (75% EXP)")
                print("[4] Insane (75% EXP, enemies always attack first)")
                print("[5] Ultimate (50% EXP, enemies always attack first, determinant reduces support EXP, start in the Tnemecalper route, no codes)")
                print("")
                difinput = input("Difficulty: ")
                if difinput == "1":
                    difficulty.SetDif("Easy")
                    saveloop = False
                elif difinput == "2":
                    difficulty.SetDif("Standard")
                    saveloop = False
                elif difinput == "3":
                    difficulty.SetDif("Hard")
                    saveloop = False
                elif difinput == "4":
                    difficulty.SetDif("Insane")
                    saveloop = False
                elif difinput == "5":
                    difficulty.SetDif("Ultimate")
                    saveloop = False
                    import moves
                    import turtle
                    import select
                    import screensetup
                    import units
                    import statprint
                    import placeunits
                    import cutscenes
                    units.UnitsAlive = [units.Proton,units.TnemecalperI,units.TnemecalperII,units.TnemecalperIII,units.TnemecalperIV]
                    cutscenes.Chapter = "Chapter 02"
                else:
                    pass

            if difficulty.Difficulty != "Ultimate":
                print()
                entercodeloop = True
                codeenterchoice = 1
                codeentered = ""
                while codeenterchoice != "2":
                    print("Do you have a code to enter?")
                    print("[1] Yes [2] No")
                    codeenterchoice = input("")
                    if codeenterchoice != "2":
                        codeentered = input("Code: ")
                        if codeentered == "947187":
                            
                            units.Proton.Supports.append(moves.Purify)
                            codeenterchoice = "2"
                        elif codeentered == "315920":
                            import moves
                            import turtle
                            import select
                            import screensetup
                            import units
                            import statprint
                            import placeunits
                            import cutscenes
                            units.Proton.Supports.append(moves.Purify)
                            units.UnitsAlive = [units.Proton,units.TnemecalperI,units.TnemecalperII,units.TnemecalperIII,units.TnemecalperIV]
                            units.UnitsRecruited.append(units.TnemecalperI)
                            units.UnitsRecruited.append(units.TnemecalperII)
                            units.UnitsRecruited.append(units.TnemecalperIII)
                            units.UnitsRecruited.append(units.TnemecalperIV)
                            select.InstantLevelUp(units.Proton,2)
                            cutscenes.Chapter = "Chapter 02"
                            codeenterchoice = "2"
                        elif codeentered == "23567984127":
                            import moves
                            import turtle
                            import select
                            import screensetup
                            import units
                            import statprint
                            import placeunits
                            import cutscenes
                            import pickle
                            DataLoaded = pickle.load(open("savedata.p", "rb"))
                            username.SetOldUserName(DataLoaded[56])
                            cutscenes.Chapter = "Actual Genocide Ending"
                            codeenterchoice = "2"

                        else:
                            print("=INVALID CODE=")

    import moves
    import turtle
    import select
    import screensetup
    import units
    import statprint
    import placeunits
    #import select
    import cutscenes

    Screen = screensetup.BattleScreen
    Screen.listen()

    TimeWaster = turtle.Turtle()
    TimeWaster.penup()
    TimeWaster.speed(1)
    TimeWaster.hideturtle()


if loadsaveornewgame == "5":

    TimeWaster.goto(TimeWaster.xcor()+100,TimeWaster.ycor()+100)

    #====Testing Stuffs=====

    # for unit in units.ListOfPlayableUnits:
    #     units.UnitsAlive.append(unit)
    # screensetup.BattleScreen.bgcolor("dim grey")
    # units.UnitsAlive.append(units.Erif)
    # units.Repins.Attacks.append(moves.WobWasThere)
    #units.Repins.Attacks.append(moves.ErifWasThere)
    # units.UnitsAlive.append(units.Wodahs)
    # units.UnitsAlive.append(units.Quest)
    # units.UnitsAlive.append(units.Scien)
    # units.UnitsAlive.append(units.Romra)
    # units.UnitsAlive.append(units.Healia)
    # units.UnitsAlive.append(units.Damagein)
    # units.UnitsAlive.append(units.Bladen)
    # units.UnitsAlive.append(units.PlayableBladeous)
    # units.UnitsAlive.append(units.Eulb)
    # units.UnitsAlive.append(units.Proton)
    # units.UnitsAlive.append(units.Wodahs)
    # units.UnitsAlive.append(units.Fael)
    # units.UnitsAlive.append(units.Repins2)
    # units.UnitsAlive.append(units.Eg)
    # units.UnitsAlive.append(units.Rethgif)
    # units.UnitsAlive.append(units.Relaeh)
    # units.UnitsAlive.append(units.Wodahs)
    # units.UnitsAlive.append(units.Eulb)
    # units.UnitsAlive.append(units.Fieht)
    # units.UnitsAlive.append(units.Lias)
    # #units.UnitsAlive.append(units.Wob)
    # units.UnitsAlive.append(units.Yranecrem)
    #  units.UnitsAlive.append(units.Omega)
    # # units.UnitsAlive.append(units.Xuirer)
    # # units.UnitsAlive.append(units.B)
    # select.InstantLevelUp(units.Proton,234)
    # select.InstantLevelUp(units.Eulb,15000)

    # # units.Proton.Portrait = current_directory+"/Portraits/proton_big3.gif"
    # # units.Proton.Sprite = current_directory+"/Sprites/proton_small3.gif"
    # # units.Proton.TurtleName.shape(current_directory+"/Sprites/proton_small3.gif")




    for unit in units.UnitsAlive:
        unit.CurrentHP = unit.MaxHP

    cutscenes.Cutscene()


elif loadsaveornewgame == "1":
    cutscenes.LoadData()


























#Screen.listen()
Screen.mainloop()




import units
import os
current_directory = os.getcwd()

def PlacePlayerUnits():
    SetPosX = -650
    SetPosY = -250
    for character in units.UnitsAlive:
        print(character.DisplayName)
        character.TurtleName.showturtle()
        character.TurtleName.speed(0)
        character.TurtleName.penup()
        character.TurtleName.setpos(SetPosX,SetPosY)
        if SetPosX == 250:
            SetPosY -= 50
            SetPosX = -650
        else:
            SetPosX += 50

def PlaceEnemies(placements):
    # EnemyPosX = -500
    # for character in units.EnemyUnitsAlive:
    #     print(character.DisplayName)
    #     character.TurtleName.showturtle()
    #     character.TurtleName.speed(0)
    #     character.TurtleName.penup()
    #     character.TurtleName.setpos(EnemyPosX,100)
    #     EnemyPosX += 50
    PlaceX = -650
    PlaceY = 350
    print("Placing Enemies:")
    for character in placements:
        if character == None:
            print("=Empty=")
        else:
            print(character.DisplayName)
            character.TurtleName.penup()
            character.TurtleName.speed(0)
            character.TurtleName.goto(PlaceX, PlaceY)
            character.TurtleName.showturtle()
        if PlaceX == 250:
            PlaceX = -650
            PlaceY -= 50
        else:
            PlaceX += 50

# None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None, is one full row

#Chapter 01 ==================================================================================================================================================================================================================
Chapter1Enemies = [units.Chapter1RedSlime1,units.Chapter1RedSlime2,units.Chapter1RedSlime3, units.Chapter1RedSlime4, units.Chapter1BlueSlime1]
Chapter1Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter1RedSlime4,None,None,None,
None,None,None,None,None,None,None,units.Chapter1RedSlime2,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter1RedSlime1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter1RedSlime3,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter1BlueSlime1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 02 ==================================================================================================================================================================================================================
Chapter2Enemies = [units.Chapter2RedSlime1,units.Chapter2RedSlime2,units.Chapter2RedSlime3,units.Chapter2YellowSlime1,units.Chapter2YellowSlime2,units.Chapter2YellowSlime3,units.Chapter2BlueSlime1,units.Chapter2BlueSlime2]
Chapter2Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,units.Chapter2RedSlime2,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,units.Chapter2YellowSlime3,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.Chapter2YellowSlime1,None,None,units.Chapter2YellowSlime2,None,None,None,None,None,None,None,
None,units.Chapter2RedSlime1,None,units.Chapter2RedSlime3,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter2BlueSlime2,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,units.Chapter2BlueSlime1,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 03 ==================================================================================================================================================================================================================
Chapter3Enemies = [units.Chapter3YellowSlime1,units.Chapter3YellowSlime2,units.Chapter3YellowSlime3,units.Chapter3YellowSlime4,units.Chapter3YellowSlime5,units.Chapter3BlueSlime1,units.Chapter3BlueSlime2,units.Chapter3BlueSlime3,units.Chapter3RedSlime1]
Chapter3Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter3RedSlime1,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,units.Chapter3YellowSlime5,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter3YellowSlime3,None,units.Chapter3YellowSlime4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter3YellowSlime1,None,units.Chapter3YellowSlime2,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter3BlueSlime3,
None,None,None,None,None,None,None,None,None,None,units.Chapter3BlueSlime2,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,units.Chapter3BlueSlime1,None,None,None,None,None,None,None,None,None
]

#Chapter 04 ==================================================================================================================================================================================================================
Chapter4Enemies = [units.Chapter4Armored1,units.Chapter4Armored2,units.Chapter4Fighter1,units.Chapter4Fighter2,units.Chapter4Fighter3,units.Chapter4Archer1,units.Chapter4Archer2,units.Chapter4Archer3,units.Chapter4Archer4,units.Chapter4Archer5,units.Retool]
Chapter4Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.Chapter4Armored1,None,None,units.Retool,None,None,units.Chapter4Armored2,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,units.Chapter4Archer3,None,None,None,None,None,units.Chapter4Archer4,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,units.Chapter4Archer5,None,None,None,None,None,None,None,None,None,
None,units.Chapter4Archer1,None,None,None,None,None,None,None,units.Chapter4Archer2,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter4Fighter1,None,None,None,units.Chapter4Fighter2,None,None,None,units.Chapter4Fighter3,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 05 ==================================================================================================================================================================================================================
Chapter5Enemies = [units.Chapter5Archer1,units.Chapter5Archer2,units.Chapter5Archer3,units.Chapter5Armored1,units.Chapter5Armored2,units.Chapter5Armored3,units.Chapter5Armored4,units.Chapter5Armored5,units.Chapter5Fighter1]
Chapter5Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,units.Chapter5Archer1,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,units.Chapter5Armored3,None,units.Chapter5Armored5,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter5Armored2,None,units.Chapter5Fighter1,None,units.Chapter5Armored4,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.Chapter5Armored1,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter5Archer2,None,units.Chapter5Archer3,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 06 ==================================================================================================================================================================================================================
Chapter6Enemies = [units.Chapter6Fighter1,units.Chapter6Fighter2,units.Chapter6Fighter3,units.Chapter6Fighter4,units.Chapter6Fighter5,units.Chapter6Fighter6,units.Chapter6Archer1]
Chapter6Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter6Fighter5,None,units.Chapter6Fighter4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter6Fighter6,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
units.Chapter6Fighter2,None,None,None,units.Chapter6Fighter3,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter6Archer1,None,None,
None,None,units.Chapter6Fighter1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 07 ==================================================================================================================================================================================================================
Chapter7Enemies = [units.Chapter7Armored1,units.Chapter7Armored2,units.Chapter7Armored3,units.Chapter7Armored4,units.Chapter7Armored5,units.Chapter7Armored6,units.Chapter7Armored7,units.Chapter7Armored8,units.Chapter7Archer1,units.Chapter7Archer2,units.Chapter7Archer3]
Chapter7Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,units.Chapter7Armored4,units.Chapter7Armored5,units.Chapter7Armored6,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter7Armored7,units.Chapter7Archer1,units.Chapter7Archer3,units.Chapter7Archer2,units.Chapter7Armored8,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,units.Chapter7Armored1,units.Chapter7Armored2,units.Chapter7Armored3,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 08 ==================================================================================================================================================================================================================
Chapter8Enemies = [units.BladeousBoss,units.Chapter8YellowSlime1,units.Chapter8YellowSlime2,units.Chapter8YellowSlime3,units.Chapter8YellowSlime4]
Chapter8Placement = [
units.Chapter8YellowSlime1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter8YellowSlime2,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,units.BladeousBoss,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
units.Chapter8YellowSlime3,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter8YellowSlime4,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 09a ==================================================================================================================================================================================================================
Chapter9aEnemies = [units.Chapter9aFighter1,units.Chapter9aFighter2,units.Chapter9aFighter3,units.Chapter9aFighter4,units.Chapter9aFighter5,units.Chapter9aFighter6,units.Chapter9aFighter7]
Chapter9aPlacement = [
None,None,None,None,None,None,None,None,units.Chapter9aFighter7,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
units.Chapter9aFighter1,None,None,None,units.Chapter9aFighter2,None,None,None,units.Chapter9aFighter3,None,None,None,units.Chapter9aFighter4,None,None,None,units.Chapter9aFighter5,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter9aFighter6,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 09b ==================================================================================================================================================================================================================
Chapter9bEnemies = [units.Chapter9bArmored1,units.Chapter9bArmored2,units.Chapter9bArmored3]
Chapter9bPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter9bArmored3,None,None,units.Chapter9bArmored2,None,None,units.Chapter9bArmored1,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 10a ==================================================================================================================================================================================================================
Chapter10aEnemies = [units.Chapter10aFighter1,units.Chapter10aFighter2,units.Chapter10aFighter3,units.Chapter10aFighter4]
Chapter10aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter10aFighter2,None,None,units.Chapter10aFighter4,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter10aFighter1,None,None,units.Chapter10aFighter3,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 10b ==================================================================================================================================================================================================================
Chapter10bEnemies = [units.Chapter10bArmored1,units.Chapter10bArmored2,units.Wallimos]
Chapter10bPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,units.Wallimos,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter10bArmored1,None,None,None,None,units.Chapter10bArmored2,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 10c ==================================================================================================================================================================================================================
Chapter10cEnemies = [units.FaelBoss,units.ErifBoss]
Chapter10cPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,units.ErifBoss,None,None,None,units.FaelBoss,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 11a ==================================================================================================================================================================================================================
Chapter11aEnemies = [units.Chapter11aWaterSpirit1,units.Chapter11aWaterSpirit2,units.Chapter11aWaterSpirit3,units.Chapter11aWaterSpirit4,units.Chapter11aWaterSpirit5]
Chapter11aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter11aWaterSpirit5,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,units.Chapter11aWaterSpirit3,None,units.Chapter11aWaterSpirit4,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter11aWaterSpirit1,None,units.Chapter11aWaterSpirit2,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 11b ==================================================================================================================================================================================================================
Chapter11bEnemies = [units.Chapter11aWaterSpirit1,units.Chapter11aWaterSpirit2,units.Chapter11aWaterSpirit3,units.Chapter11aWaterSpirit4,units.Chapter11aWaterSpirit5]
Chapter11bPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter11aWaterSpirit5,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,units.Chapter11aWaterSpirit3,None,units.Chapter11aWaterSpirit4,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter11aWaterSpirit1,None,units.Chapter11aWaterSpirit2,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 12a ==================================================================================================================================================================================================================
Chapter12aEnemies = [units.Chapter12aWaterSpirit1,units.Chapter12aWaterSpirit2,units.Chapter12aWaterSpirit3,units.Chapter12aWaterSpirit4,units.Chapter12aWaterSpirit5,units.Chapter12aWaterSpirit6]
Chapter12aPlacement = [
None,None,None,None,None,units.Chapter12aWaterSpirit4,None,None,None,units.Chapter12aWaterSpirit5,None,None,None,units.Chapter12aWaterSpirit6,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter12aWaterSpirit3,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter12aWaterSpirit2,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter12aWaterSpirit1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 12b ==================================================================================================================================================================================================================
Chapter12bEnemies = [units.Chapter12aWaterSpirit1,units.Chapter12aWaterSpirit2,units.Chapter12aWaterSpirit3,units.Chapter12aWaterSpirit4,units.Chapter12aWaterSpirit5,units.Chapter12aWaterSpirit6]
Chapter12bPlacement = [
None,None,None,None,None,units.Chapter12aWaterSpirit4,None,None,None,units.Chapter12aWaterSpirit5,None,None,None,units.Chapter12aWaterSpirit6,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter12aWaterSpirit3,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter12aWaterSpirit2,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter12aWaterSpirit1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 13a ==================================================================================================================================================================================================================
Chapter13aEnemies = [units.DiverNeville,units.Chapter13aFighter1,units.Chapter13aFighter2,units.Chapter13aFighter3,units.Chapter13aFighter4,units.Chapter13aFighter5,units.Chapter13aFighter6]
Chapter13aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter13aFighter5,None,None,None,units.Chapter13aFighter6,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter13aFighter1,None,units.Chapter13aFighter2,None,None,None,units.Chapter13aFighter3,None,units.Chapter13aFighter4,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.DiverNeville,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 13b ==================================================================================================================================================================================================================
Chapter13bEnemies = [units.DiverNeville,units.Chapter13aFighter1,units.Chapter13aFighter2,units.Chapter13aFighter3,units.Chapter13aFighter4,units.Chapter13aFighter5,units.Chapter13aFighter6]
Chapter13bPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter13aFighter5,None,None,None,units.Chapter13aFighter6,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter13aFighter1,None,units.Chapter13aFighter2,None,None,None,units.Chapter13aFighter3,None,units.Chapter13aFighter4,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.DiverNeville,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 14a ==================================================================================================================================================================================================================
Chapter14aEnemies = [units.BigBrainNeville,units.Chapter14aArcher1,units.Chapter14aArcher2,units.Chapter14aArcher3,units.Chapter14aArcher4,units.Chapter14aArcher5,units.Chapter14aArcher6,units.Chapter14aArcher7,units.Chapter14aArcher8,units.Chapter14aArcher9,units.Chapter14aArcher10,units.Chapter14aArmored1,units.Chapter14aArmored2,units.Chapter14aArmored3]
Chapter14aPlacement = [
None,None,None,None,None,None,None,None,units.Chapter14aArcher7,None,units.BigBrainNeville,None,units.Chapter14aArcher9,None,None,None,None,None,None,
None,units.Chapter14aArmored1,None,None,units.Chapter14aArcher4,None,units.Chapter14aArcher5,None,None,None,units.Chapter14aArcher8,None,units.Chapter14aArcher10,None,None,None,units.Chapter14aArmored2,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter14aArcher1,None,None,None,None,None,None,units.Chapter14aArcher3,None,None,None,None,None,None,None,None,units.Chapter14aArcher6,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,units.Chapter14aArcher2,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter14aArmored3,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 14b ==================================================================================================================================================================================================================
Chapter14bEnemies = [units.BigBrainNeville,units.Chapter14aArcher1,units.Chapter14aArcher2,units.Chapter14aArcher3,units.Chapter14aArcher4,units.Chapter14aArcher5,units.Chapter14aArcher6,units.Chapter14aArcher7,units.Chapter14aArcher8,units.Chapter14aArcher9,units.Chapter14aArcher10,units.Chapter14aArmored1,units.Chapter14aArmored2,units.Chapter14aArmored3]
Chapter14bPlacement = [
None,None,None,None,None,None,None,None,units.Chapter14aArcher7,None,units.BigBrainNeville,None,units.Chapter14aArcher9,None,None,None,None,None,None,
None,units.Chapter14aArmored1,None,None,units.Chapter14aArcher4,None,units.Chapter14aArcher5,None,None,None,units.Chapter14aArcher8,None,units.Chapter14aArcher10,None,None,None,units.Chapter14aArmored2,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter14aArcher1,None,None,None,None,None,None,units.Chapter14aArcher3,None,None,None,None,None,None,None,None,units.Chapter14aArcher6,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,units.Chapter14aArcher2,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter14aArmored3,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 15a ==================================================================================================================================================================================================================
Chapter15aEnemies = [units.Chapter15aFighter1,units.Chapter15aFighter2,units.Chapter15aFighter3,units.Chapter15aFighter4,units.Chapter15aFighter5,units.Chapter15aArmored1,units.Chapter15aArmored2,units.Chapter15aArmored3,units.Chapter15aArmored4,units.Chapter15aArmored5,units.Chapter15aArmored6,units.Chapter15aArmored7,units.Chapter15aArmored8,units.Chapter15aArcher1,units.Chapter15aArcher2,units.KaptainKNeville,units.Chapter15aArcher3,units.Chapter15aArcher4]
Chapter15aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter15aFighter4,None,None,None,None,units.Chapter15aArmored8,None,None,None,None,units.Chapter15aFighter5,None,None,None,None,None,None,None,
None,None,None,None,None,units.Chapter15aArmored6,units.Chapter15aArcher4,units.Chapter15aArmored7,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter15aArmored4,units.Chapter15aArcher2,units.KaptainKNeville,units.Chapter15aArcher3,units.Chapter15aArmored5,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter15aFighter2,None,None,None,units.Chapter15aArmored2,units.Chapter15aArcher1,units.Chapter15aArmored3,None,None,None,units.Chapter15aFighter3,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter15aArmored1,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter15aFighter1,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 16a (Xuirists) ==================================================================================================================================================================================================================
Chapter16aEnemies = [units.Chapter16Xuirist1,units.Chapter16Xuirist2,units.Chapter16Xuirist3,units.Chapter16Xuirist4,units.Chapter16Xuirist5,units.Chapter16Xuirist6,units.Chapter16Xuirist7,units.Tluc]
Chapter16aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter16Xuirist5,None,None,None,units.Tluc,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter16Xuirist7,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter16Xuirist3,None,None,units.Chapter16Xuirist6,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter16Xuirist1,None,units.Chapter16Xuirist2,None,units.Chapter16Xuirist4,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 16a (Rethgif and Eg) (Enemy) ==================================================================================================================================================================================================================
RethgifandEgEnemies = [units.RethgifEnemy,units.EgEnemy]
RethgifandEgEnemiesPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
units.EgEnemy,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
units.RethgifEnemy,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 16a (Rethgif and Eg) (Ally) ==================================================================================================================================================================================================================
RethgifandEgAllies = [units.Rethgif,units.Eg]
RethgifandEgAlliesPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
units.Eg,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
units.Rethgif,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 17a ==================================================================================================================================================================================================================
Chapter17aEnemies = [units.Chapter17Xuirist1,units.Chapter17Xuirist2,units.Chapter17Xuirist3,units.Chapter17Xuirist4,units.Chapter17Xuirist5,units.Chapter17Xuirist6,units.Chapter17Xuirist7,units.Chapter17Xuirist8,units.Chapter17Xuirist9,units.Chapter17Xuirist10,units.Chapter17Xuirist11,units.Chapter17Xuirist12,units.Chapter17Xuirist13,units.Chapter17Xuirist14]
Chapter17aPlacement = [
None,None,None,units.Chapter17Xuirist10,None,units.Chapter17Xuirist11,None,units.Chapter17Xuirist12,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,units.Chapter17Xuirist9,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter17Xuirist5,None,units.Chapter17Xuirist6,None,units.Chapter17Xuirist7,None,units.Chapter17Xuirist8,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,units.Chapter17Xuirist13,None,units.Chapter17Xuirist14,None,None,None,None,None,None,None,None,None,
None,None,units.Chapter17Xuirist1,None,units.Chapter17Xuirist2,None,units.Chapter17Xuirist3,None,units.Chapter17Xuirist4,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 17d ==================================================================================================================================================================================================================
Chapter17dEnemies = [units.BBoss]
Chapter17dPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,units.BBoss,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 18a ==================================================================================================================================================================================================================
Chapter18aEnemies = [units.Chapter18Xuirist1,units.Chapter18Xuirist2,units.Chapter18Xuirist3,units.Chapter18Xuirist4,units.Chapter18Xuirist5,units.Chapter18Xuirist6,units.Chapter18Xuirist7,units.Chapter18Xuirist8,units.Chapter18Xuirist9,units.Chapter18Xuirist10,units.Chapter18Xuirist11,units.Chapter18Xuirist12,units.Chapter18Xuirist13,units.Chapter18Xuirist14]
Chapter18aPlacement = [
units.Chapter18Xuirist13,None,None,None,None,None,None,units.Chapter18Xuirist3,units.Chapter18Xuirist4,units.Chapter18Xuirist5,units.Chapter18Xuirist6,units.Chapter18Xuirist7,None,None,None,None,None,None,units.Chapter18Xuirist14,
None,None,None,None,None,None,None,units.Chapter18Xuirist1,None,None,None,units.Chapter18Xuirist2,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,units.Chapter18Xuirist8,None,units.Chapter18Xuirist9,None,units.Chapter18Xuirist10,None,None,None,units.Chapter18Xuirist11,None,units.Chapter18Xuirist12,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 19a ==================================================================================================================================================================================================================
Chapter19aEnemies = [units.Chapter19Xuirist1,units.Chapter19Xuirist2,units.Chapter19Xuirist3,units.Chapter19Xuirist4,units.Chapter19Xuirist5,units.Chapter19Armored1,units.Chapter19Armored2,units.Chapter19Armored3,units.Chapter19Armored4,units.Chapter19Armored5,units.Chapter19Armored6,units.Chapter19Archer1,units.Chapter19Archer2,units.Chapter19Archer3,units.Chapter19Archer4,units.Chapter19Archer5,units.Chapter19Archer6]
Chapter19aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter19Xuirist1,None,units.Chapter19Xuirist2,None,units.Chapter19Xuirist3,None,units.Chapter19Xuirist4,None,units.Chapter19Xuirist5,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter19Armored1,None,units.Chapter19Armored2,None,units.Chapter19Armored3,None,units.Chapter19Armored4,None,units.Chapter19Armored5,None,units.Chapter19Armored6,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,units.Chapter19Archer1,None,units.Chapter19Archer2,None,units.Chapter19Archer3,None,units.Chapter19Archer4,None,units.Chapter19Archer5,None,units.Chapter19Archer6,None,None,None,None,None,None,None
]

#Chapter 20a ==================================================================================================================================================================================================================
Chapter20aEnemies = [units.Chapter20aFighter1,units.Chapter20aFighter2,units.Chapter20aFighter3,units.Chapter20aFighter4,units.Chapter20aArmored1]
Chapter20aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,units.Chapter20aArmored1,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,units.Chapter20aFighter1,None,units.Chapter20aFighter2,None,None,None,units.Chapter20aFighter3,None,units.Chapter20aFighter4,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 20b ==================================================================================================================================================================================================================
Chapter20bEnemies = [units.Dael,units.DnefedEnemy,units.ThgifEnemy,units.GnirifEnemy,units.CigamEnemy]
Chapter20bPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.GnirifEnemy,None,units.CigamEnemy,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Dael,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,units.DnefedEnemy,None,units.ThgifEnemy,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 21a ==================================================================================================================================================================================================================
Chapter21aEnemies = [units.Chapter21aXuirist1,units.Chapter21aXuirist2,units.Chapter21aXuirist3,units.Chapter21aXuirist4,units.Chapter21aXuirist5,units.Chapter21aXuirist6,units.Undead1,units.Undead2,units.Undead3,units.Undead4,units.Undead5,units.OmegaBoss,units.Chapter21aBreak]
Chapter21aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,units.Undead4,None,units.Chapter21aBreak,None,units.Undead5,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,units.OmegaBoss,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,units.Undead2,None,None,None,units.Undead3,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,units.Undead1,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter21aXuirist6,None,None,None,
None,None,None,None,None,None,None,None,units.Chapter21aXuirist1,None,None,None,units.Chapter21aXuirist4,None,None,None,units.Chapter21aXuirist5,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,units.Chapter21aXuirist2,None,None,None,units.Chapter21aXuirist3,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 22a ==================================================================================================================================================================================================================
Chapter22aEnemies = [units.IfBoss,units.Chapter22aScientist1,units.Chapter22aScientist2,units.Chapter22aScientist3,units.Chapter22aScientist4,units.Chapter22aScientist5,units.Chapter22aScientist6,units.Chapter22aScientist7,units.Chapter22aScientist8,units.Chapter22aScientist9,units.Chapter22aScientist10,units.Chapter22aScientist11]
Chapter22aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.IfBoss,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter22aScientist1,None,units.Chapter22aScientist7,None,units.Chapter22aScientist8,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter22aScientist2,None,units.Chapter22aScientist6,None,units.Chapter22aScientist5,None,units.Chapter22aScientist10,None,units.Chapter22aScientist11,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter22aScientist3,None,units.Chapter22aScientist4,None,units.Chapter22aScientist9,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 23a ==================================================================================================================================================================================================================
Chapter23aEnemies = [units.ElifBoss,units.Chapter23aScientist1,units.Chapter23aScientist2,units.Chapter23aScientist3,units.Chapter23aScientist4,units.Chapter23aScientist5,units.Chapter23aScientist6,units.Chapter23aScientist7,units.Chapter23aScientist8,units.Chapter23aScientist9,units.Chapter23aScientist10,units.Chapter23aArcher1,units.Chapter23aArcher2]
Chapter23aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter23aArcher1,None,units.ElifBoss,None,units.Chapter23aArcher2,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter23aScientist6,None,units.Chapter23aScientist7,None,units.Chapter23aScientist8,None,units.Chapter23aScientist9,None,units.Chapter23aScientist10,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,units.Chapter23aScientist1,None,units.Chapter23aScientist2,None,units.Chapter23aScientist3,None,units.Chapter23aScientist4,None,units.Chapter23aScientist5,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 24a ==================================================================================================================================================================================================================
Chapter24aEnemies = [units.ElseBoss,units.Chapter24aScientist1,units.Chapter24aScientist2,units.Chapter24aScientist3,units.Chapter24aScientist4,units.Chapter24aScientist5,units.Chapter24aScientist6,units.Chapter24aScientist7,units.Chapter24aScientist8,units.Chapter24aScientist9]
Chapter24aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.ElseBoss,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter24aScientist7,None,units.Chapter24aScientist9,None,units.Chapter24aScientist8,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter24aScientist3,None,units.Chapter24aScientist4,None,units.Chapter24aScientist5,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter24aScientist1,None,units.Chapter24aScientist6,None,units.Chapter24aScientist2,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 25a ==================================================================================================================================================================================================================
Chapter25aEnemies = [units.BreakItucher,units.Chapter25aScientist1,units.Chapter25aScientist2,units.Chapter25aScientist3,units.Chapter25aScientist4,units.Chapter25aScientist5,units.Chapter25aScientist6]
Chapter25aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.BreakItucher,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter25aScientist5,None,None,None,units.Chapter25aScientist6,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter25aScientist3,None,None,None,units.Chapter25aScientist4,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter25aScientist1,None,None,None,units.Chapter25aScientist2,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 25b ==================================================================================================================================================================================================================
Chapter25bEnemies = [units.Breakc25b,units.Chapter25aScientist1,units.Chapter25aScientist2,units.Chapter25aScientist3,units.Chapter25aScientist4,units.Chapter25aScientist5,units.Chapter25aScientist6]
Chapter25bPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.Breakc25b,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter25aScientist5,None,None,None,units.Chapter25aScientist6,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter25aScientist3,None,None,None,units.Chapter25aScientist4,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter25aScientist1,None,None,None,units.Chapter25aScientist2,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 26a ==================================================================================================================================================================================================================
Chapter26aEnemies = [units.Chapter26aScientist12,units.Chapter26aScientist11,units.Chapter26aScientist10,units.Chapter26aScientist9,units.Chapter26aScientist8,units.Chapter26aScientist7,units.Chapter26aScientist6,units.Chapter26aScientist5,units.Chapter26aScientist4,units.Chapter26aScientist3,units.Chapter26aScientist2,units.Chapter26aScientist1,units.Chapter26aArmored1,units.Chapter26aArmored2,units.DeathPepperBoss]
Chapter26aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter26aArmored1,None,units.DeathPepperBoss,None,units.Chapter26aArmored2,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter26aScientist1,None,units.Chapter26aScientist2,None,units.Chapter26aScientist3,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter26aScientist4,None,units.Chapter26aScientist5,None,units.Chapter26aScientist6,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter26aScientist7,None,units.Chapter26aScientist8,None,units.Chapter26aScientist9,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,units.Chapter26aScientist10,None,units.Chapter26aScientist11,None,units.Chapter26aScientist12,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 27a ==================================================================================================================================================================================================================
Chapter27aEnemies = [units.QuestBoss]
Chapter27aPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.QuestBoss,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 27b ==================================================================================================================================================================================================================
Chapter27bEnemies = [units.RepinsBoss1]
Chapter27bPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.RepinsBoss1,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 27c1 ==================================================================================================================================================================================================================
Chapter27c1Enemies = [units.RepinsBoss2]
Chapter27c1Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.RepinsBoss2,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 27c2 ==================================================================================================================================================================================================================
Chapter27c2Enemies = [units.RepinsBoss3]
Chapter27c2Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.RepinsBoss3,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 27c3 ==================================================================================================================================================================================================================
Chapter27c3Enemies = [units.RepinsBoss3]
Chapter27c3Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,units.RepinsBoss3,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 27c4 ==================================================================================================================================================================================================================
Chapter27c4Enemies = [units.RepinsBoss5]
Chapter27c4Placement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.RepinsBoss5,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 27d ==================================================================================================================================================================================================================
Chapter27dEnemies = [units.VruhBoss]
Chapter27dPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.VruhBoss,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

#Chapter 27e ==================================================================================================================================================================================================================
Chapter27eEnemies = [units.Etamitlu,units.AhcemBoss]
Chapter27ePlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.AhcemBoss,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,units.Etamitlu,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]


#Chapter 27f ==================================================================================================================================================================================================================
Chapter27fEnemies = [units.XuirWrath1,units.XuirWrath2,units.XuirWrath3,units.XuirWrath4]
Chapter27fPlacement = [
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,units.XuirWrath1,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,units.XuirWrath2,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,units.XuirWrath3,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,units.XuirWrath4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
]

all_chapter_placements = [
    Chapter1Placement,
    Chapter2Placement,
    Chapter3Placement,
    Chapter4Placement,
    Chapter5Placement,
    Chapter6Placement,
    Chapter7Placement,
    Chapter8Placement,
    Chapter9aPlacement,
    Chapter9bPlacement,
    Chapter10aPlacement,
    Chapter10bPlacement,
    Chapter10cPlacement,
    Chapter11aPlacement,
    Chapter11bPlacement,
    Chapter12aPlacement,
    Chapter12bPlacement,
    Chapter13aPlacement,
    Chapter13bPlacement,
    Chapter14aPlacement,
    Chapter14bPlacement,
    Chapter15aPlacement,
    Chapter16aPlacement,
    Chapter17aPlacement,
    Chapter17dPlacement,
    Chapter18aPlacement,
    Chapter19aPlacement,
    Chapter20aPlacement,
    Chapter20bPlacement,
    Chapter21aPlacement,
    Chapter22aPlacement,
    Chapter23aPlacement,
    Chapter24aPlacement,
    Chapter25aPlacement,
    Chapter25bPlacement,
    Chapter26aPlacement,
    Chapter27aPlacement,
    Chapter27bPlacement,
    Chapter27c1Placement,
    Chapter27c2Placement,
    Chapter27c3Placement,
    Chapter27c4Placement,
    Chapter27dPlacement,
    Chapter27ePlacement,
    Chapter27fPlacement,
]

all_chapter_names = [
    "Chapter1",
    "Chapter2",
    "Chapter3",
    "Chapter4",
    "Chapter5",
    "Chapter6",
    "Chapter7",
    "Chapter8",
    "Chapter9a",
    "Chapter9b",
    "Chapter10a",
    "Chapter10b",
    "Chapter10c",
    "Chapter11a",
    "Chapter11b",
    "Chapter12a",
    "Chapter12b",
    "Chapter13a",
    "Chapter13b",
    "Chapter14a",
    "Chapter14b",
    "Chapter15a",
    "Chapter16a",
    "Chapter17a",
    "Chapter17d",
    "Chapter18a",
    "Chapter19a",
    "Chapter20a",
    "Chapter20b",
    "Chapter21a",
    "Chapter22a",
    "Chapter23a",
    "Chapter24a",
    "Chapter25a",
    "Chapter25b",
    "Chapter26a",
    "Chapter27a",
    'Chapter27b',
    "Chapter27c1",
    "Chapter27c2",
    "Chapter27c3",
    "Chapter27c4",
    "Chapter27d",
    "Chapter27e",
    "Chapter27f",
]
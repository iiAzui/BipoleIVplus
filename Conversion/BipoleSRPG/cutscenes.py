import username
import difficulty
import screensetup
import units
import select
import moves
import screensetup
import turtle
import statprint
import placeunits
import time
import pickle
import os
current_directory = os.getcwd()

SaveHasBeenLoaded = False

SaveDataList = []

ChapterLevel = 0

Chapter = None #"Chapter 27b" #"Chapter 22a" #"Chapter 20a" #None #"Chapter 20a" #"Chapter 18a" #None #"Chapter 07" #"Prologue1"
CutsceneIndex = 0 #0 #27 #34 #12 #0
UnitsToPlace = []
UnitFormation = []
CanSkipCutscene = False
BattleStarted = False
gamefont = "Gamepixies"
import oscheck
FontMul = oscheck.TextMul

RecruitRomra = None
TnemecalpersJoined = False
RecruitLacirtcele = None
RecruitDamagein = None
RecruitHealia = None
RecruitWob = None
RecruitBladen = None
RecruitWodahs = None
RecruitFael = False
RecruitErif = False
RecruitVruh = False
RecruitRepins = False
RecruitRelaeh = False
RecruitLias = False
Qinput = False
Winput = False
Einput = False

# Used for conversion
current_string = ""
current_left = ""
current_right = ""
cutscene_ended = False
battle_started = False

def register_shape(spritename):
    pass

def Text1(text,portrait):
    global current_string
    global current_left
    global current_right
    current_string = text
    current_left = portrait
    current_right = ""

def Text2(text,portrait1,portrait2):
    global current_string
    global current_left
    global current_right
    current_string = text
    current_left = portrait1
    current_right = portrait2

def Text3(text):
    global current_string
    global current_left
    global current_right
    current_string = text
    current_left = ""
    current_right = ""

def line2(text):
    global current_string
    current_string += text

def line3(text):
    global current_string
    current_string += text

def ClearInputs():
    global Qinput
    global Winput
    global Einput
    Qinput = False
    Winput = False
    Einput = False



def EndingCharacter(unit,how1,how2,how3):
    global CutsceneIndex
    CutsceneIndex += 1
    unit = unit
    if unit in units.UnitsAlive:
        if how1 == True:
            Text1("how",unit.Portrait)
        else:
            Text1(unit.DisplayName + ": Survived",unit.Portrait)
    elif unit in units.UnitsRecruited:
        if how2 == True:
            Text1("how",unit.Portrait)
        else:
            Text1(unit.DisplayName + ": Defeated ",unit.Portrait)
    else:
        if how3 == True:
            Text1("how",unit.Portrait)
        else:
            Text1(unit.DisplayName + ": Not Recruited ",unit.Portrait)
    

pernicious = "pernicious_big"

def Cutscene():
    global pernicious
    global Chapter
    global CutsceneIndex
    global UnitsToPlace
    global UnitFormation
    global RecruitRomra
    global CanSkipCutscene
    global TnemecalpersJoined
    global RecruitLacirtcele
    global RecruitDamagein
    global RecruitHealia
    global BattleStarted
    global RecruitWob
    global RecruitBladen
    global RecruitWodahs
    global RecruitFael
    global RecruitErif
    global RecruitVruh
    global RecruitRepins
    global RecruitRelaeh
    global Qinput
    global Winput
    global Einput
    global ChapterLevel

    global battle_started
    global cutscene_ended
    # ()
    # screensetup.BattleScreen.tracer(1)
    if Chapter == None:
        screensetup.BattleScreen.bgcolor("black")
        Text3("[Act 1]")
        Chapter = "Prologue1"

    # current_directory\+"/Portraits/([a-zA-Z0-9_]+).gif
    # "$1"
        
    elif Chapter == "Prologue1": #=====================Prologue1===============================================================
        if CutsceneIndex == 0:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Year 1279 AN]")
            line2("[Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            Text1("Death Pepper: Scien!",units.DeathPepper.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            register_shape("scien_big2")
            Text2("Scien: Yes?",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text2("Death Pepper: Has the second protype awakened it's Xuir Arts yet?",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("Scien: Not yet, sir.",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text2("Death Pepper: Then it's likely another failure.",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("Death Pepper: Prepare the new extraction room, I might as well get some",units.DeathPepper.Portrait,"scien_big2")
            line2("life energy from this.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("Death Pepper: And who knows, the torture might awaken one of it's arts.",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("Scien: Sir...",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("Scien: Sir... I will not.",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("Death Pepper: You dare defy my orders?",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("Scien: I've worked at this research center for the past seven years,",units.DeathPepper.Portrait,"scien_big2")
            line2("but I can no longer handle this suffering.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text2("Scien: I will likely die, but atleast this will reduce the suffering",units.DeathPepper.Portrait,"scien_big2")
            line2("of others.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("Death Pepper: ...",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Death Pepper: I've suspected that you'd betray me.",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("Death Pepper: Don't think that I haven't noticed that the Forbidden",units.DeathPepper.Portrait,"scien_big2")
            line2("Ritual you had given was fake.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Scien: You attempted the Forbidden Ritual of Nation!?",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("Death Pepper: The only reason you're still alive is because of your",units.DeathPepper.Portrait,"scien_big2")
            line2("of your efficiency, though it seems that you'll no longer")
            line3("cooperate with us.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("Death Pepper: It's a shame that I'll have to kill you now, the only",units.DeathPepper.Portrait,"scien_big2")
            line2("other person that could replace you is Break, and let's say that I'm")
            line3("not his biggest fan.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("Scien: ...",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("Scien: It's been eight painful years since you destroyed my town for",units.DeathPepper.Portrait,"scien_big2")
            line2("the Forbidden Ritual...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Scien: For these eight years, I've lacked the courage to stop the",units.DeathPepper.Portrait,"scien_big2")
            line2("pain, to not continue to work with you...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Scien: I should have done this earlier, but it is something I can",units.DeathPepper.Portrait,"scien_big2")
            line2("no longer live with.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("Scien: Though it will not make up for my past actions, I will do",units.DeathPepper.Portrait,"scien_big2")
            line2("everything I can to save even one soul from this place.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("(Scien grabs a young child)",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("Death Pepper: What do you think you're doing!?",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("Scien: If he stays here, he will die in three days when the",units.DeathPepper.Portrait,"scien_big2")
            line2("extraction finishes. With this, he will have a chance of")
            line3("surival.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("(Scien activates a device)",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Death Pepper: BREAK! DEACTIVATE THE DEVICE!", units.DeathPepper.Portrait, "scien_big2")#units.DeathPepper.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Break: The device seems to be malfunctioning...", units.DeathPepper.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("Death Pepper: Wait, does that mean...", units.DeathPepper.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("Death Pepper: You fool! There's no way you'll survive with", units.DeathPepper.Portrait, units.Break.Portrait)
            line2("a broken teleporter! Who knows where it'll take you.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text2("Death Pepper: You'll probably starve in the middle of the ocean.", units.DeathPepper.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
            Text2("Scien: If so, I will accept that fate as punishment.",units.DeathPepper.Portrait,"scien_big2")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 34:
            Text1("(The teleporter activates and Scien disappears with the child)",units.DeathPepper.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 35:
            Text1("Death Pepper: They got away, what a waste of resources...",units.DeathPepper.Portrait)
            CutsceneIndex = 0
            Chapter = "Prologue2"
            
    elif Chapter == "Prologue2": #=====================Prologue2===============================================================
        if CutsceneIndex == 0:
            Text3("...")
            units.UnitsAlive.append(units.Proton)
            units.UnitsAlive.append(units.Quest)
            units.UnitsRecruited.append(units.Quest)
            units.UnitsAlive.append(units.Scien)
            units.UnitsRecruited.append(units.Scien)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            Text3("[1298 AN, 19 years later]")
            line2("[Static Castle, The Territories of Bipole]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            screensetup.BattleScreen.bgcolor("gray")
            Text3("???: *knock* *knock* *knock*")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text3("???: Who is it?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("???: Greeetings, Quest.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text1("Proton: I am Proton Xurr of the Knights of Static.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("Quest: Ah, the Nolavillian Knight.",units.Proton.Portrait, units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("Proton: Xuir, actually.",units.Proton.Portrait, units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("Quest: My apologies.",units.Proton.Portrait, units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("Quest: Anyway, why are you here?",units.Proton.Portrait, units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("Proton: There is a large band of bandits, known as the", units.Proton.Portrait, units.Quest.Portrait)
            line2("Guild of Retool, who have threatened the allied territory")
            line3("of Sine with an attack.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("Proton: The King has request us, as well as the head of the",units.Proton.Portrait, units.Quest.Portrait)
            line2("knights, Sir Scien, to assist Sine against the forces.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text2("Quest: I would decline, but I suppose this is an order",units.Proton.Portrait, units.Quest.Portrait)
            line2("from the King.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("Quest: *sigh*",units.Proton.Portrait, units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Quest: I'll meet you at the front gates in an hour,",units.Proton.Portrait, units.Quest.Portrait)
            line2("is that alright?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("Proton: Yes, we will await you there.",units.Proton.Portrait, units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[1 hour later...]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            screensetup.BattleScreen.bgcolor("green")
            Text2("Proton: So you finally arrive...",units.Proton.Portrait, units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("Proton: Shall we get going?",units.Proton.Portrait, units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("Quest: Actually, there's this knight who has",units.Proton.Portrait, units.Quest.Portrait)
            line2("offered to aid us...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("???: Hello, I'm Romra!",units.Romra.Portrait, units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Romra: I'm a newly certified knight, and I wish",units.Romra.Portrait, units.Proton.Portrait)
            line2("to one day join the Static Elemental Offense")
            line3("Squad.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Romra: Of course, I'll need all of the training",units.Romra.Portrait, units.Proton.Portrait)
            line2("I can get to do so.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("Romra: If you would allow it, I would like to",units.Romra.Portrait, units.Proton.Portrait)
            line2("partake in this mission along side you.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text3("[Recruit Romra?]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(RomraRecruitYes, "q")
            (screensetup.BattleScreen).onkey(RomraRecruitNo, "w")
        elif CutsceneIndex == 25:
            if RecruitRomra == True:
                Text2("Romra: Yes! Thank you!",units.Romra.Portrait, units.Proton.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Romra: Oh, sorry for bothering you.",units.Romra.Portrait, units.Proton.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 26:
            if RecruitRomra == True:
                Text3("[Romra has joined your party]")
                units.UnitsAlive.append(units.Romra)
                units.UnitsRecruited.append(units.Romra)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 27:
            Text2("Scien: Let's get going.",units.Scien.Portrait, units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 01"
            
    elif Chapter == "Chapter 01": #=====================Chapter01===============================================================
        ChapterLevel = 2
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 01]")
            line2("[Static Path, Territory of Static]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text2("Scien: There are some Slimes blocking out way.",units.Scien.Portrait, units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text2("Scien: We'll need to defeat them to continue",units.Scien.Portrait, units.Proton.Portrait)
            line2("onwards.")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter1Enemies
            UnitFormation = placeunits.Chapter1Placement
            BattleStarted = False
            battle_started = True
        elif units.Scien in units.UnitsAlive and CutsceneIndex > 2:
            if CutsceneIndex == 3:
                Text1("Scien: We've defeated the enemy slimes.",units.Scien.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 4:
                Text1("Scien: We'll need to be careful, there will likely be",units.Scien.Portrait)
                line2("more ahead.")
                CutsceneIndex = 0
                Chapter = "Chapter 02"
                
                SaveData()
        elif len(units.UnitsAlive) > 1 and CutsceneIndex == 3:
            CutsceneIndex = 0
            Chapter = "Chapter 02"
            Cutscene()
        elif len(units.UnitsAlive) == 1 and CutsceneIndex > 2:
            if CutsceneIndex == 3:
                Text1("Proton: It seems that all of the others have",units.Proton.Portrait)
                line2("somehow died.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 4:
                register_shape("azurehooded_big")
                Text2("???: ...",units.Proton.Portrait,"azurehooded_big")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 5:
                Text2("Proton: Who's there!?",units.Proton.Portrait,"azurehooded_big")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 6:
                Text2("???: I am The Link...",units.Proton.Portrait,"azurehooded_big")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 7:
                Text2("The Link: All of your allies have fallen, this is obviously",units.Proton.Portrait,"azurehooded_big")
                line2("not good.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("The Link: If you have done this by accident, please be",units.Proton.Portrait,"azurehooded_big")
                line2("more careful.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("The Link: To make up for your lost allies, the",units.Proton.Portrait,"azurehooded_big")
                line2("Tnemecalpers will be assisting you.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text3("[The Tnemecalpers joined your party]")
                units.UnitsAlive.append(units.TnemecalperI)
                units.UnitsRecruited.append(units.TnemecalperI)
                units.UnitsAlive.append(units.TnemecalperII)
                units.UnitsRecruited.append(units.TnemecalperII)
                units.UnitsAlive.append(units.TnemecalperIII)
                units.UnitsRecruited.append(units.TnemecalperIII)
                units.UnitsAlive.append(units.TnemecalperIV)
                units.UnitsRecruited.append(units.TnemecalperIV)
                CutsceneIndex += 1
                
        elif units.TnemecalperI in units.UnitsAlive:
            if CutsceneIndex == 11:
                Text1("Proton: Hey, wait a second...",units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 12:
                Text1("Proton: ...he's gone.",units.Proton.Portrait)
                CutsceneIndex = 0
                Chapter = "Chapter 02"
                
    elif Chapter == "Chapter 02": #=====================Chapter02===============================================================
        ChapterLevel = 3
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 02]")
            line2("[Outer Static, Territory of Static]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text1("Proton: There's some slimes up ahead, prepare", units.Proton.Portrait)
            line2("for battle!")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter2Enemies
            UnitFormation = placeunits.Chapter2Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 2:
            Text1("Proton: We'll be reaching the Territory of Cos soon.", units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Proton: If we need reinforcements, there will be a", units.Proton.Portrait)
            line2("member of the Elemental Offense Squad at a nearby")
            line3("town.")
            CutsceneIndex = 0
            Chapter = "Chapter 03"
            
    elif Chapter == "Chapter 03": #=====================Chapter03===============================================================
        ChapterLevel = 4
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 03]")
            line2("[Cos Castle Town, Territory of Cos]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("grey")
            Text1("Proton: We've arrived at the town...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text2("???: Wha' suuup?",units.Proton.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text2("???: It's me, Lacirtcele Sus of the Elemental",units.Proton.Portrait,units.Lacirtcele.Portrait)
            line2("Offense Squad.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("Lacirtcele: I heard y'all might need some help.",units.Proton.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text3("[Recruit Lacirtcele?]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(LacirtceleRecruitYes, "q")
            (screensetup.BattleScreen).onkey(LacirtceleRecruitNo, "w")
        elif CutsceneIndex == 6:
            if RecruitLacirtcele == True:
                Text2("Lacirtcele: Like... poggers, bruh.",units.Proton.Portrait, units.Lacirtcele.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Lacirtcele: No problem man, see y'all later.",units.Proton.Portrait, units.Lacirtcele.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 7:
            if RecruitLacirtcele == True:
                Text3("[Lacirtcele has joined your party]")
                units.UnitsAlive.append(units.Lacirtcele)
                units.UnitsRecruited.append(units.Lacirtcele)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 8:
            Text1("Proton: We should get going.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            screensetup.BattleScreen.bgcolor("green")
            Text3("[The group continues onwards]")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter3Enemies
            UnitFormation = placeunits.Chapter3Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 10:
            Text1("Proton: Everyone get prepared, we should",units.Proton.Portrait)
            line2("be reaching Sine soon.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            if units.Quest in units.UnitsAlive and units.Romra in units.UnitsAlive:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex = 0
                Chapter = "Chapter 04"
                Cutscene()
        elif CutsceneIndex == 12:
            Text2("Romra: Hey.",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text2("Quest: Hello.",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text2("Romra: Can I ask you a question?",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 15:
            Text2("Quest: Already have, but go ahead.",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 16:
            Text2("Romra: What are you?",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 17:
            Text2("Quest: What do you mean?",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 18:
            Text2("Romra: I know that Scien is the head of the",units.Romra.Portrait,units.Quest.Portrait)
            line2("Knights of Static and that Lacirtcele is a")
            line3("member of the Elemental Offense Sqaud...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 19:
            Text2("Romra: ...and I was wondering if you had",units.Romra.Portrait,units.Quest.Portrait)
            line2("a special rank, since you were requested")
            line3("by the king himself.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 20:
            Text2("Quest: Of course I do!",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 21:
            Text2("Quest: I am the High Mage of the Castle Static!",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 22:
            Text2("Quest: And I am also the Head of Artifact Research",units.Romra.Portrait,units.Quest.Portrait)
            line2("in the Territory of Static!")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 23:
            Text2("Quest: I doubt anyone in the land of Bipole knows",units.Romra.Portrait,units.Quest.Portrait)
            line2("more about the Artifacts than I do!")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 24:
            Text2("Romra: Artifacts?",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 25:
            Text2("Quest: Yes, most of the general population",units.Romra.Portrait,units.Quest.Portrait)
            line2("knows not of their existence.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 26:
            Text2("Quest: They are powerful relics created by the",units.Romra.Portrait,units.Quest.Portrait)
            line2("Gods to guide us mortals.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 27:
            Text2("Quest: Though we do not know where any of them",units.Romra.Portrait,units.Quest.Portrait)
            line2("are now, they are hiding somewhere, waiting for")
            line3("someone to rediscover them!")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 28:
            Text2("Quest: Surely you've heard of the legends about",units.Romra.Portrait,units.Quest.Portrait)
            line2("the Holy Itucher?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Romra: I have.",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("Quest: According to my research, the Holy Itucher",units.Romra.Portrait,units.Quest.Portrait)
            line2("exists, and it is located somewhere on this")
            line3("continent!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("Romra: What would you do if you ever found it?",units.Romra.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text2("Quest: Of course, I would analyze it to it's fullest",units.Romra.Portrait,units.Quest.Portrait)
            line2("extent.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
            Text2("Quest: Though I believe that it would be inevidable",units.Romra.Portrait,units.Quest.Portrait)
            line2("that I would fall to the temptation of trying out")
            line3("it's powers.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 34:
            Text3("[Quest and Romra leveled up!]")
            select.InstantLevelUp(units.Quest,1)
            select.InstantLevelUp(units.Romra,1)
            CutsceneIndex = 0
            Chapter = "Chapter 04"
            
    elif Chapter == "Chapter 04": #=====================Chapter04===============================================================
        ChapterLevel = 5
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 04]")
            line2("[Sine Castle Town, Territory of Sine]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text1("Proton: The Guild of Retool will be here any minute,",units.Proton.Portrait)
            line2("stay on guard.")
            placeunits.PlacePlayerUnits()
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            
            
            UnitsToPlace = placeunits.Chapter4Enemies
            UnitFormation = placeunits.Chapter4Placement
            placeunits.PlacePlayerUnits()
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("Retool: Hah hah hah!,",units.Retool.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Retool: I heard they were getting reinforcements",units.Retool.Portrait)
            line2("but this is nothing!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Retool: Nothing to be afraid of, let's get 'em!",units.Retool.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            CutsceneIndex += 1
            
            
            
            
        elif CutsceneIndex == 6:
            Text1("Retool: Ah... I'm not going to die here...",units.Retool.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text1("Retool: It's time to retreat...",units.Retool.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text3("[The Guild of Retool retreats].")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text1("Proton: We did it...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text3("???: Hmm... that was a high amount of damage...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text1("Proton: Who's there!?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text2("???: It is I, the great Damagein Elite!",units.Proton.Portrait,units.Damagein.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("Proton: ...",units.Proton.Portrait,units.Damagein.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Proton: ...who?",units.Proton.Portrait,units.Damagein.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("Damagein: I, the great Damagein, have dedicated my life",units.Proton.Portrait,units.Damagein.Portrait)
            line2("towards seeking one thing... DAMAGE!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Damagein: And I have just witnessed YOU deal DAMAGE",units.Proton.Portrait,units.Damagein.Portrait)
            line2("to those bandits!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("Damagein: So I will ask, might I join your army in order",units.Proton.Portrait,units.Damagein.Portrait)
            line2("to witness more damage?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text3("[Recruit Damagein?]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(DamageinRecruitYes, "q")
            (screensetup.BattleScreen).onkey(DamageinRecruitNo, "w")
        elif CutsceneIndex == 19:
            if RecruitDamagein == True:
                Text2("Damagein: It's time for some damage!",units.Proton.Portrait, units.Damagein.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Damagein: Very well then, I will seek damage elsewhere.",units.Proton.Portrait, units.Damagein.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 20:
            if RecruitDamagein == True:
                units.UnitsRecruited.append(units.Damagein)
                units.UnitsAlive.append(units.Damagein)
                Text3("[Damagein joined your party]")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 21:
            Text3("???: Are you the people who protected this town?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("???: I am Healia Aid, and I wish to join your army",units.Proton.Portrait,units.Healia.Portrait)
            line2("for saving my hometown.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text3("[Recruit Healia?]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(HealiaRecruitYes, "q")
            (screensetup.BattleScreen).onkey(HealiaRecruitNo, "w")
        elif CutsceneIndex == 24:
            if RecruitHealia == True:
                Text2("Healia: Thank you, I will make sure to do",units.Proton.Portrait, units.Healia.Portrait)
                line2("my part.")
                CutsceneIndex += 1
                
            else:
                Text2("Healia: Understood, I wish you all a safe",units.Proton.Portrait, units.Healia.Portrait)
                line2("journey.")
                CutsceneIndex += 1
                
        elif CutsceneIndex == 25:
            if RecruitHealia == True:
                units.UnitsAlive.append(units.Healia)
                units.UnitsRecruited.append(units.Healia)
                Text3("[Healia joined your party]")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 26: 
            if units.Scien in units.UnitsAlive and units.Lacirtcele in units.UnitsAlive:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            else:
                Chapter = "Chapter 05"
                CutsceneIndex = 0
                Cutscene()
        elif CutsceneIndex == 27:
            Text2("Scien: Hello, Lacirtcele.",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Lacirtcele: Sup.",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Scien: Have you prepared our letter to send",units.Scien.Portrait,units.Lacirtcele.Portrait)
            line2("back to Static?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("Lacirtcele: Nah.",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("Lacirtcele: I'll get to it later though trust",units.Scien.Portrait,units.Lacirtcele.Portrait)
            line2("me fam.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text2("Scien: I would rather not trust you.",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
            Text2("Scien: This is a very important letter, you know?",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 34:
            Text2("Lacirtcele: I do not \"know\".",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 35:
            Text2("Lacirtcele: I may purposely choose not to \"know\".",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 36:
            Text2("Scien: I may \"purposely\" remove you from the",units.Scien.Portrait,units.Lacirtcele.Portrait)
            line2("Elemental Offense Sqaud.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 37:
            Text2("Lacirtcele: That might be bad.",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 38:
            Text2("Scien: Yes, it would be \"bad\".",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 39:
            Text2("Scien: Now prepare that letter.",units.Scien.Portrait,units.Lacirtcele.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 40:
            Text3("[Scien and Lacirtcele leveled up!]")
            select.InstantLevelUp(units.Scien,1)
            select.InstantLevelUp(units.Lacirtcele,1)
            CutsceneIndex = 0
            Chapter = "Chapter 05"
            
    elif Chapter == "Chapter 05": #=====================Chapter05===============================================================
        ChapterLevel = 7
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 05]")
            line2("[Cos Path, Territory of Cos]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text1("Proton: Looks like some bandits are in our way.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Proton: We'll need to defeat them to go back to",units.Proton.Portrait)
            line2("Static.")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter5Enemies
            UnitFormation = placeunits.Chapter5Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 3:
            if units.TnemecalperIII in units.UnitsAlive:
                Text2("Tnemecalper III: ALLY DETECTED!",units.TnemecalperIII.Portrait,units.Proton.Portrait)
                line2("ALLY DETECTED!")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex = 34
                Cutscene()
        elif CutsceneIndex == 4:
            Text2("Proton: Huh?",units.TnemecalperIII.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text2("Tnemecalper III: ALLY DETECTED!",units.TnemecalperIII.Portrait,units.Proton.Portrait)
            line2("ALLY DETECTED!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("Proton: Am I supposed to find a new ally?",units.TnemecalperIII.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("(Tnemecalper III points towards a village)",units.TnemecalperIII.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("Proton: I'm supposed to go there?",units.TnemecalperIII.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("Tnemecalper III: ALLY DETECTED!",units.TnemecalperIII.Portrait,units.Proton.Portrait)
            line2("ALLY DETECTED!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("Proton: Sure.",units.TnemecalperIII.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            screensetup.BattleScreen.bgcolor("grey")
            Text3("[Obscure Village, Territory of Cos]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text1("???: I'm bored...",units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text1("???: Maybe I should walk to another random",units.Wob.Portrait)
            line2("village...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text1("???: ...",units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text1("???: Oh, it looks like there's a group of people",units.Wob.Portrait)
            line2("entering the village.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Proton: So... what do I do now that",units.Proton.Portrait,units.TnemecalperIII.Portrait)
            line2("I'm here at the village?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("???: Hey! You there!",units.Proton.Portrait,units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("???: You guys are from the army, right?",units.Proton.Portrait,units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("Proton: Yeah.",units.Proton.Portrait,units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("???: Can I join you guys on your mission?",units.Proton.Portrait,units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Proton: Aren't you just a kid?",units.Proton.Portrait,units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("???: I'm not a kid, I'm like... 12.",units.Proton.Portrait,units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("???: I'm Wob, and I'm going to be part of the Static",units.Proton.Portrait,units.Wob.Portrait)
            line2("army next year! But the wait is so boring that I started")
            line3("walking to random villages! So let me join you guys!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("Wob: I feel like an NPC...",units.Proton.Portrait,units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("Proton: Wait, you're joining the Static army",units.Proton.Portrait,units.Wob.Portrait)
            line2("next year? Doesn't that mean you live in Static?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("Wob: Yeah, but I got bored and walked to this",units.Proton.Portrait,units.Wob.Portrait)
            line2("random village.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("Proton: These roads are dangerous, how are you",units.Proton.Portrait,units.Wob.Portrait)
            line2("unharmed?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Wob: I know how to defend myself, my sister",units.Proton.Portrait,units.Wob.Portrait)
            line2("taught me how to use a bow.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Proton: You seem more competent than I originally",units.Proton.Portrait,units.Wob.Portrait)
            line2("thought.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("Wob: Yeah! Let me join your mission!",units.Proton.Portrait,units.Wob.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text3("[Recruit Wob?]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(WobRecruitYes, "q")
            (screensetup.BattleScreen).onkey(WobRecruitNo, "w")
        elif CutsceneIndex == 32:
            if RecruitWob == True:
                Text2("Wob: Yes! Let's go!",units.Proton.Portrait, units.Wob.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Wob: C'mon...",units.Proton.Portrait, units.Wob.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 33:
            if RecruitWob == True:
                Text3("[Wob has joined your party]")
                units.UnitsAlive.append(units.Wob)
                units.UnitsRecruited.append(units.Wob)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 34:
            if units.Proton in units.UnitsAlive and units.TnemecalperII in units.UnitsAlive:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            else:
                Chapter = "Chapter 06"
                CutsceneIndex = 0
                Cutscene()
        elif CutsceneIndex == 35:
            screensetup.BattleScreen.bgcolor("green")
            Text2("Proton: ...",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 36:
            Text2("Proton: Hello?",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 37:
            Text2("Tnemecalper II: This is a greeting.",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 38:
            Text2("Tnemecalper II: This is a message.",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 39:
            Text2("Proton: Do you know how to... converse?",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 40:
            Text2("Tnemecalper II: This is a message:",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 41:
            Text2("Tnemecalper II: This is a message:",units.Proton.Portrait,units.TnemecalperII.Portrait)
            line2("Congratulations! Keep keeping your allies alive!")
            line3("                                   -The Link")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 42:
            Text2("Proton: ...",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 43:
            Text2("Proton: Are you even alive?", units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 44:
            Text2("Tnemecalper II: This is a explanation:",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 45:
            Text2("Tnemecalper II: This is a explanation:",units.Proton.Portrait,units.TnemecalperII.Portrait)
            line2("   explanation")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 46:
            Text2("Proton: ...",units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 47:
            Text2("Proton: This is:", units.Proton.Portrait,units.TnemecalperII.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 48:
            Text2("Proton: This is:", units.Proton.Portrait,units.TnemecalperII.Portrait)
            line2("                 depressing.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 49:
            Text3("[Proton and Tnemecalper II leveled up!]")
            select.InstantLevelUp(units.Proton,1)
            select.InstantLevelUp(units.TnemecalperII,1)
            CutsceneIndex = 0
            Chapter = "Chapter 06"
            
    elif Chapter == "Chapter 06": #=====================Chapter06===============================================================
        ChapterLevel = 8
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 06]")
            line2("[Outer Static, Territory of Static]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: It's getting dark, we'll stop by at",units.Proton.Portrait)
            line2("nearby town soon.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text3("[Outer Town, Territory of Static]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text3("(The streets are full of people, shouting and")
            line2("moving chaotically)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Proton: I did not expect the town to be so busy",units.Proton.Portrait)
            line2("this late at night...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text2("???: Hey, you just get here?",units.Proton.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("Proton: Yes, we have just arrived.",units.Proton.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("???: Then you probably haven't heard the news",units.Proton.Portrait,units.Bladen.Portrait)
            line2("yet, have you?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("Proton: News?",units.Proton.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("???: The Holy Itucher has been discovered at",units.Proton.Portrait,units.Bladen.Portrait)
            line2("the Nation of Altar.")
            CutsceneIndex += 1
            
        elif CutsceneIndex >= 10 and CutsceneIndex <= 11 and units.Quest in units.UnitsAlive:
            if CutsceneIndex == 10:
                Text2("Quest: The Holy Itucher!?",units.Quest.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Quest: You mean to tell me that an artifact",units.Quest.Portrait,units.Bladen.Portrait)
                line2("was discovered while I was away on this mission!?")
                CutsceneIndex += 1
                
        elif CutsceneIndex >= 10 and CutsceneIndex <= 11:
            if CutsceneIndex == 10:
                Text2("Proton: The artifact of power?",units.Proton.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("???: Yep, the artifact of power.",units.Proton.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 12:
            Text2("???: You all know the legends, right?",units.Proton.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("???: 'bout how the \"worthy one to wield the",units.Proton.Portrait,units.Bladen.Portrait)
            line2("Holy Itucher will be granted the power of the")
            line3("Dimensionals\"?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14 and units.Quest in units.UnitsAlive:
            Text2("Quest: Of course I do, I'm the Head of Artifact",units.Quest.Portrait,units.Bladen.Portrait)
            line2("Research in the Territory of Static!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Proton: I have heard of such legends.",units.Proton.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("???: As you can tell, everyone in town is rushing",units.Proton.Portrait,units.Bladen.Portrait)
            line2("to head to the Nation of Altar.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Proton: What about you?",units.Proton.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("???: I'm on my way to the Nation of Altar",units.Proton.Portrait,units.Bladen.Portrait)
            line2("myself.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("???: My cousin works there at the temple, so",units.Proton.Portrait,units.Bladen.Portrait)
            line2("I'll know the way there better than the others.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("???: I can help you guys get there if you",units.Proton.Portrait,units.Bladen.Portrait)
            line2("have the gold, you know?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("Proton: You'll do that and miss out on getting",units.Proton.Portrait,units.Bladen.Portrait)
            line2("it for yourself?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("???: Me? The chosen one? Don't make me laugh.",units.Proton.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("???: If I'm not getting the power I might as",units.Proton.Portrait,units.Bladen.Portrait)
            line2("well get some money.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23 and units.Quest in units.UnitsAlive:
            Text2("Quest: Hiring him or not, we should head there",units.Proton.Portrait,units.Quest.Portrait)
            line2("immediately. Who knows what could happen if the")
            line3("Itucher got into the wrong hands.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text1("Proton: (Hiring him or not, we should head there",units.Proton.Portrait)
            line2("immediately. Who knows what could happen if the")
            line3("Itucher got into the wrong hands...)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text3("[Recruit ????]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(BladenRecruitYes, "q")
            (screensetup.BattleScreen).onkey(BladenRecruitNo, "w")
        elif CutsceneIndex == 25:
            if RecruitBladen == True:
                Text2("???: You've made the right choice. My name's",units.Proton.Portrait, units.Bladen.Portrait)
                line2("Bladen, by the way.")
                CutsceneIndex += 1
                
            else:
                Text2("???: Alright then, good luck getting to",units.Proton.Portrait, units.Bladen.Portrait)
                line2("Altar.")
                CutsceneIndex += 1
                
        elif CutsceneIndex == 26:
            if RecruitBladen == True:
                Text3("[Bladen has joined your party]")
                units.UnitsAlive.append(units.Bladen)
                units.UnitsRecruited.append(units.Bladen)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 27:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: Even though it's nightime, will need to head",units.Proton.Portrait)
            line2("to Altar immediately.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text1("Proton: The world will be in danger if the Holy Itucher",units.Proton.Portrait)
            line2("is used for evil.")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter6Enemies
            UnitFormation = placeunits.Chapter6Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 29:
            if units.TnemecalperIV in units.UnitsAlive:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex = 0
                Chapter = "Chapter 07"
                Cutscene()
        elif CutsceneIndex == 30:
            Text2("Proton: Greetings.",units.Proton.Portrait,units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("Tnemecalper IV: ...",units.Proton.Portrait,units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text2("Proton: ...",units.Proton.Portrait,units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
            Text2("Tnemecalper IV: ...",units.Proton.Portrait,units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 34:
            Text2("Tnemecalper IV: 360[N/A]SCOPE",units.Proton.Portrait,units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 35:
            Text2("Tnemecalper IV: :pogchamp:",units.Proton.Portrait,units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 36:
            Text2("Proton: Okay I'm not doing this.",units.Proton.Portrait,units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 37:
            Text1("(Proton walks away)", units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 38:
            Text1("Tnemecalper IV: ...",units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 39:
            Text1("Tnemecalper IV: gg no re",units.TnemecalperIV.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 40:
            Text3("[Proton and Tnemecalper IV leveled up!]")
            select.InstantLevelUp(units.Proton,1)
            select.InstantLevelUp(units.TnemecalperIV,1)
            CutsceneIndex = 0
            Chapter = "Chapter 07"
            
    elif Chapter == "Chapter 07": #=====================Chapter07===============================================================
        ChapterLevel = 9
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 07]")
            line2("[Cos Path, Territory of Cos]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: There's a member of the Elemental",units.Proton.Portrait)
            line2("Offense Squad at a village we'll be passing")
            line3("by.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: It will be important that we have",units.Proton.Portrait)
            line2("enough power to stop any evil which may be")
            line3("at The Nation of Altar.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Obscure Village, Territory of Cos]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text2("???: So, you guys are heading to Altar?",units.Proton.Portrait,units.Wodahs.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text2("???: I just finished a mission in Quad so",units.Proton.Portrait,units.Wodahs.Portrait)
            line2("I'll be able to help you if you need it.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text3("[Recruit ????]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(WodahsRecruitYes, "q")
            (screensetup.BattleScreen).onkey(WodahsRecruitNo, "w")
        elif CutsceneIndex == 7:
            if RecruitWodahs == True:
                Text2("???: Got it.",units.Proton.Portrait, units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("???: Alright then, I'll be heading",units.Proton.Portrait, units.Wodahs.Portrait)
                line2("back to Static.")
                CutsceneIndex += 1
                
        elif CutsceneIndex == 8:
            if RecruitWodahs == True:
                Text3("[Wodahs has joined your party]")
                units.UnitsAlive.append(units.Wodahs)
                units.UnitsRecruited.append(units.Wodahs)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 9:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: We're almost at Altar, but there's some",units.Proton.Portrait)
            line2("bandits up ahead.")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter7Enemies
            UnitFormation = placeunits.Chapter7Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 10:
            if units.Bladen in units.UnitsAlive and units.Healia in units.UnitsAlive:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex = 0
                Chapter = "Chapter 08"
                Cutscene()
        elif CutsceneIndex == 11:
            Text2("Healia: Hello, Bladen.",units.Healia.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text2("Bladen: Hey.",units.Healia.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("Healia: Bladen, you said your cousin lives",units.Healia.Portrait,units.Bladen.Portrait)
            line2("in the Nation of Altar, yes?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Bladen: Yeah, he lives at the Altar Temple.",units.Healia.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("Healia: The Altar Temple, huh. He must be pretty",units.Healia.Portrait,units.Bladen.Portrait)
            line2("important to be living there.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Bladen: He's the head of defense at the temple, he",units.Healia.Portrait,units.Bladen.Portrait)
            line2("guards the valuables and such.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("Healia: I wonder how he deals with all of the",units.Healia.Portrait,units.Bladen.Portrait)
            line2("pressure of such an important job...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("Healia: I come from a noble Sine family, and my",units.Healia.Portrait,units.Bladen.Portrait)
            line2("parents expect me to do something grand.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("Healia: But how am I suppposed to fix our current",units.Healia.Portrait,units.Bladen.Portrait)
            line2("political situation?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("Healia: Ever since my parent's involvement in",units.Healia.Portrait,units.Bladen.Portrait)
            line2("the Quad Genocide became known, they've kept")
            line3("expecting more and more of me...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Healia: It's not my fault that they wanted to",units.Healia.Portrait,units.Bladen.Portrait)
            line2("make some money by investing in the genocide")
            line3("following the economic recession from the...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Healia: ...western territories' involvement with",units.Healia.Portrait,units.Bladen.Portrait)
            line2("the unauthorized voyages to the Forbidden Sea,")
            line3("which led to the Minor Civil War of 1282 AN.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("Healia: Why don't they just not get involved",units.Healia.Portrait,units.Bladen.Portrait)
            line2("in the genocide and just do some stocks or")
            line3("something?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("Healia: Don't you think that would be safer",units.Healia.Portrait,units.Bladen.Portrait)
            line2("both financially and socially?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("Bladen: I...",units.Healia.Portrait,units.Bladen.Portrait)
            
            Text2("Bladen: I don't...",units.Healia.Portrait,units.Bladen.Portrait)
            
            Text2("Bladen: I don't care.",units.Healia.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("Bladen: I was paid to take you paying fools to",units.Healia.Portrait,units.Bladen.Portrait)
            line2("Altar, where you will probably die to the defenses.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("Bladen: I could not care less about the economic",units.Healia.Portrait,units.Bladen.Portrait)
            line2("affairs of the Sine nobility.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Bladen: If you have nothing relevant to say, then",units.Healia.Portrait,units.Bladen.Portrait)
            line2("leave me alone.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Healia: ...",units.Healia.Portrait,units.Bladen.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text3("[Healia and Bladen leveled up!]")
            select.InstantLevelUp(units.Healia,1)
            select.InstantLevelUp(units.Bladen,1)
            CutsceneIndex = 0
            Chapter = "Chapter 08"
            
    elif Chapter == "Chapter 08": #=====================Chapter08===============================================================
        ChapterLevel = 10
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 08]")
            line2("[Altar Town, Nation of Altar]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            Text3("(The town is ravaged, with the ground is")
            line2("covered in destroyed buildings and flames...)")
            CutsceneIndex += 1
             
        elif units.Bladen in units.UnitsAlive and CutsceneIndex >= 2 and CutsceneIndex < 11:
            if CutsceneIndex == 2:
                screensetup.BattleScreen.bgcolor("dark red")
                Text1("Bladen: ...",units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 3:
                Text1("Bladen: What happened here?",units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 4:
                Text2("???: ...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 5:
                Text2("Bladen: (Is that Bladeous?)",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 6:
                Text2("Bladen: Hey! What happened here?",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 7:
                Text2("Bladeous: ...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("(Bladeous attacks Bladen)",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("Bladen: Hey! What's happened to you?",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Bladen: You aren't the one who did this,",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                line2("are you?")
                CutsceneIndex += 1
                
        elif CutsceneIndex >=2 and CutsceneIndex < 11:
            if CutsceneIndex == 2:
                screensetup.BattleScreen.bgcolor("dark red")
                Text1("Proton: What happened here...",units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 3:
                Text2("???: ...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 4:
                Text2("(??? attacks Proton)",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 5:
                Text2("Proton: Hey, don't attack us!",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 6:
                Text2("???: ...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex = 11
                
        elif CutsceneIndex == 11:
            Text2("Proton: Everyone, prepare for battle!",units.Proton.Portrait,units.BladeousBoss.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter8Enemies
            UnitFormation = placeunits.Chapter8Placement
            BattleStarted = False
            battle_started = True
        elif moves.Purify in units.Proton.Supports and CutsceneIndex <= 39 and len(units.UnitsAlive) != 1:
            if CutsceneIndex == 12:
                Text2("Bladeous: You there...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Bladeous: Seal me in the Temple of",units.Proton.Portrait,units.BladeousBoss.Portrait)
                line2("Altar while I'm weakened...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Bladeous: The power of the Itucher will",units.Proton.Portrait,units.BladeousBoss.Portrait)
                line2("regain control of me soon...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("(Proton used Purify!)",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Bladeous: ..!?",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text2("Bladeous: The power of the Itucher is fading...",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 18:
                Text2("Bladeous: ...",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 19:
                Text2("Bladeous: I don't know how, but you've freed me",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                line2("from the control of the Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 20:
                Text3("(The ground suddenly starts shaking)")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 21:
                Text2("Proton: Is this an earthquake?",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Bladeous: No, I believe this is the reawakening",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                line2("of the dimensional \"Dark God\" Wallimos Alexander.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("Bladeous: I must have been destined to be sealed in the",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                line2("temple, but you've somehow defied fate.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Bladeous: Hopefully, this does not cause the Xuir",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                line2("Wrath...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 25:
                Text2("Proton: So, what do we do to stop the reawakening of",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                line2("the Dark God?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 26:
                Text2("Bladeous: We must travel to the Forbidden Dephs of the",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                line2("Temple of Altar.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 27:
                Text2("Bladeous: Though it is an government secret, the temple's",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                line2("original purpose was to keep the two dimensionals,")
                line3("Bobbish Razz and Wallimos Alexander, sealed underground.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 28:
                Text2("Bladeous: If we travel to the dephs, we will be able to find",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                line2("the location of the binding.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 29:
                Text2("Proton: Understood.",units.Proton.Portrait,units.PlayableBladeous.Portrait)
                units.UnitsAlive.append(units.PlayableBladeous)
                units.UnitsRecruited.append(units.PlayableBladeous)
                CutsceneIndex = 0
                Chapter = "Chapter 09b"
                
        elif units.Bladen in units.UnitsAlive and CutsceneIndex <= 39:
            if CutsceneIndex == 12:
                Text2("Bladeous: Bladen...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Bladen: ...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Bladeous: The Itucher isn't... here anymore...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Bladeous: They took it... the Nolavillians...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Bladen: Nolavillians?",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text2("Bladeous: I tried to stop them... and I activated",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                line2("the Itucher...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 18:
                Text2("Bladeous: But I wasn't... worthy...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 19:
                Text2("Bladeous: I... couldn't control it's power...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 20:
                Text2("Bladeous: My allies... the townspeople... I...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 21:
                Text2("Bladeous: I... killed them all...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Bladeous: But I couldn't even... defeat the",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                line2("Nolavillians...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("Bladeous: It was pointless... I failed...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Bladeous: And who knows... what will happen now...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 25:
                Text2("Bladeous: The Shadow Realm... that's where they're",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                line2("taking it...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 26:
                Text2("Bladeous: They said it would be... the key to creating",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                line2("an artificial dimensional...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 27:
                Text2("Bladeous: The fourth generation... Xuir...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 28:
                Text2("Proton: Xuir!?",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 29:
                Text2("Bladeous: It's... starting to take over...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                line2("again...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 30:
                Text2("Bladeous: Seal me in the temple... while I'm",units.Proton.Portrait,units.BladeousBoss.Portrait)
                line2("still weakened...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 31:
                Text2("Bladen: ...",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 32:
                Text2("Bladen: ...understood.",units.Bladen.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 33:
                Text3("(Bladen puts Bladeous in the Altar Temple and")
                line2("performs a sealing spell on it.)")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text2("Bladen: ...",units.Bladen.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 35:
                Text2("Bladen: ...I know what I need to do.",units.Bladen.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 36:
                Text2("Bladen: I've been avoiding this for too long,",units.Bladen.Portrait,units.Proton.Portrait)
                line2("but it was inevidable.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 37:
                Text2("Bladen: I'm going to go to Nolavillia and",units.Bladen.Portrait,units.Proton.Portrait)
                line2("take back the Holy Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("Bladen: My family's been the guardians of",units.Bladen.Portrait,units.Proton.Portrait)
                line2("the Altar Temple, but I've never wanted to")
                line3("do it...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text2("Bladen: ...but the whole world is at stake",units.Bladen.Portrait,units.Proton.Portrait)
                line2("here.")
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 39:
            if CutsceneIndex == 12:
                Text2("Bladeous: The Itucher...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Bladeous: I couldn't control it...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Bladeous: And now... they have it...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Bladeous: The Nolavillians...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Bladeous: At the... Shadow Realm...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text2("Bladeous: Please... stop them...",units.Proton.Portrait,units.BladeousBoss.Portrait)
                CutsceneIndex = 40
                
        elif CutsceneIndex == 40:
                Text1("Proton: ...",units.Proton.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 41:
                Text1("Proton: We'll be heading to Nolavillia",units.Proton.Portrait)
                line2("as soon as we can.")
                CutsceneIndex += 1
                
        elif CutsceneIndex == 42:
            if units.Scien in units.UnitsAlive:
                Text1("Scien: Nolavillia... I haven't been there",units.Scien.Portrait)
                line2("since the incident...")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 43:
            if units.Quest in units.UnitsAlive:
                Text1("Quest: Nolavillia, huh. I'll go wherever",units.Quest.Portrait)
                line2("the artifacts are.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 44:
            if units.Romra in units.UnitsAlive:
                Text1("Romra: Going to Nolavillia? I wonder if it'll",units.Romra.Portrait)
                line2("help me get stronger...")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 45:
            if units.Lacirtcele in units.UnitsAlive:
                Text1("Lacirtcele: Nolavillia... rad name bruh.",units.Lacirtcele.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 46:
            if units.Damagein in units.UnitsAlive:
                Text1("Damagein: Nolavillia? I hope they have lots",units.Damagein.Portrait)
                line2("of damage!")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 47:
            if units.Healia in units.UnitsAlive:
                Text1("Healia: Nolavillia, I wonder what it's like...",units.Healia.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 48:
            if units.Wob in units.UnitsAlive:
                Text1("Wob: Nolavillia? Sounds fun, I'm going.",units.Wob.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 49:
            if units.Wodahs in units.UnitsAlive:
                Text1("Wodahs: Guess I'm going to Nolavillia now.",units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 50:
            if len(units.UnitsAlive) == 1:
                Text1("The Link: All of your allies have died...",units.Azure.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 51:
            if len(units.UnitsAlive) == 1:
                Text1("The Link: If it weren't for your destiny in",units.Azure.Portrait)
                line2("the Neville Prophecy, I would've stopped you")
                line3("by now.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 52:
            if len(units.UnitsAlive) == 1:
                Text1("The Link: You will fufill your purpose and reclaim",units.Azure.Portrait)
                line2("the Holy Itucher.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 53:
            if len(units.UnitsAlive) == 1:
                Text1("The Link: Then, I will execute you.",units.Azure.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 54:
            if len(units.UnitsAlive) == 1:
                Text1("Azure: As the Link of this realm, I swear upon",units.Azure.Portrait)
                line2("this mission.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 55:
            if len(units.UnitsAlive) == 1:
                Text3("[Azure joined your party]")
                units.UnitsAlive.append(units.Azure)
                units.UnitsRecruited.append(units.Azure)
                units.Proton.Portrait = "proton_big3"
                units.Proton.Sprite = current_directory+"/Sprites/proton_small3.gif"
                units.Proton.TurtleName.shape(current_directory+"/Sprites/proton_small3.gif")
                units.Proton.Supports.append(moves.Medkit)
                select.InstantLevelUp(units.Proton,(units.Proton.Level*2))
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 56:
            if units.Azure in units.UnitsRecruited:
                Text3("[The Genocide Route has been activated]")
                line2("[You can no longer recruit new units]")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 57:
            Text1("Proton: We'll need to go back to Static to",units.Proton.Portrait)
            line2("get resources and a means of transportation.")
            CutsceneIndex = 0
            Chapter = "Chapter 09a"
            
    elif Chapter == "Chapter 09a": #=====================Chapter09a===============================================================
        ChapterLevel = 11
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 09a]")
            line2("[Cos Path, Territory of Cos]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: We need to return quickly.",units.Proton.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter9aEnemies
            UnitFormation = placeunits.Chapter9aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 2:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Proton: We're almost there.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex >= 4 and units.TnemecalperI in units.UnitsAlive:
            if CutsceneIndex == 4:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 5:
                Text2("Tnemecalper I: ...",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 6:
                Text2("Proton: ...",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 7:
                Text2("(Tnemecalper I starts clapping)",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("Tnemecalper I: CLAP CLAP CLAP CLAP CLAP",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("Proton: Huh?",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Tnemecalper I: CLAP CLAP CLAP CLAP CLAP",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Tnemecalper I: MESSAGE RECIEVED! MESSAGE RECIEVED!",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 12:
                Text2("Tnemecalper I: MESSAGE:",units.Proton.Portrait,units.TnemecalperI.Portrait)
                line2(" Great job! You've failed the genocide route! I")
                line3(  "hope you learned the \"power of friendship\"!")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Tnemecalper I: MESSAGE:",units.Proton.Portrait,units.TnemecalperI.Portrait)
                line2("  Now go save the world!")
                line3("                               -The Link")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Tnemecalper I: CLAP CLAP CLAP CLAP CLAP",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Proton: ...",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Proton: ...okay?",units.Proton.Portrait,units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text3("[Proton and Tnemecalper I leveled up!]")
                select.InstantLevelUp(units.Proton,1)
                select.InstantLevelUp(units.TnemecalperI,1)
                CutsceneIndex = 0
                Chapter = "Chapter 10a"
                
        elif CutsceneIndex >= 4:
            CutsceneIndex = 0
            if units.Azure in units.UnitsRecruited:
                Chapter = "Chapter 10c"
            else:
                Chapter = "Chapter 10a"
            Cutscene()
    elif Chapter == "Chapter 09b": #=====================Chapter09b===============================================================
        ChapterLevel = 11
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 09b]")
            line2("[Forbidden Dephs, Nation of Altar]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark goldenrod")
            Text1("Bladeous: It seems that Wallimos has conjured",units.PlayableBladeous.Portrait)
            line2("some guards.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Bladeous: We'll need to defeat them to proceed.",units.PlayableBladeous.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter9bEnemies
            UnitFormation = placeunits.Chapter9bPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 3:
            Text1("Proton: Let's keep going.",units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 10b"
            
    elif Chapter == "Chapter 10a": #=====================Chapter10a===============================================================
        ChapterLevel = 13
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 10a]")
            line2("[Outer Static, Territory of Static]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            UnitsToPlace = placeunits.Chapter10aEnemies
            UnitFormation = placeunits.Chapter10aPlacement
            BattleStarted = False
            CutsceneIndex += 1
            battle_started = True
        elif CutsceneIndex == 2 and units.Azure not in units.UnitsRecruited:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Static Town, Territory of Static]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3 and units.Azure not in units.UnitsRecruited:
            screensetup.BattleScreen.bgcolor("grey")
            Text1("Proton: Everyone, I have talked with the king",units.Proton.Portrait)
            line2("and he has provided us a ship.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4 and units.Azure not in units.UnitsRecruited:
            Text1("Proton: We will set sail as soon as everyone is ready.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5 and units.Azure not in units.UnitsRecruited:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Static Town Port, Territory of Static]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6 and units.Azure not in units.UnitsRecruited:
            screensetup.BattleScreen.bgcolor("navy")
            Text2("???: Hello, are you Proton Xurr?",units.Proton.Portrait,units.Fael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7 and units.Azure not in units.UnitsRecruited:
            Text2("Proton: I am.",units.Proton.Portrait,units.Fael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8 and units.Azure not in units.UnitsRecruited:
            Text2("???: I am Fael Illyure of the Elemental",units.Proton.Portrait,units.Fael.Portrait)
            line2("Offense Squad.")
            CutsceneIndex += 1
            
        elif CutsceneIndex >= 9 and CutsceneIndex <= 13 and units.Wob in units.UnitsAlive and units.Azure not in units.UnitsRecruited:
            if CutsceneIndex == 9:
                Text2("???: And I am Eri...",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Wob: Hey Erif.",units.Wob.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Erif: Wob? Why are you here?",units.Wob.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Wob: Why are YOU here?",units.Wob.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Erif: We've been assigned to help Proton on",units.Wob.Portrait,units.Erif.Portrait)
                line2("his voyage to the Nolavillian Continent.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Erif: But there's another mission going on and",units.Wob.Portrait,units.Erif.Portrait)
                line2("only one of us can help him.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 12:
                Text2("Erif: Proton, I do not trust my brother to",units.Proton.Portrait,units.Erif.Portrait)
                line2("be safe on his own, please allow me to go")
                line3("with him.")
                CutsceneIndex = 14
                
        elif CutsceneIndex >= 9 and CutsceneIndex <= 13 and units.Azure not in units.UnitsRecruited:
            if CutsceneIndex == 9:
                Text2("???: And I am Erif Blaze of the Elemental",units.Proton.Portrait,units.Erif.Portrait)
                line2("Offense Squad.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Erif: We have been assigned to assist you on",units.Proton.Portrait,units.Erif.Portrait)
                line2("your voyage to the Nolavillian Continent.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Erif: However, due to another assignment going on,",units.Proton.Portrait,units.Erif.Portrait)
                line2("only one of us can help you.")
                CutsceneIndex = 14
                
        elif CutsceneIndex == 14 and units.Azure not in units.UnitsRecruited:
                Text2("[Q] Recruit Fael",units.Fael.Portrait,units.Erif.Portrait)
                line2("[W] Recruit Erif")
                line3("[E] Don't recruit either")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(FaelRecruitYes, "q")
                (screensetup.BattleScreen).onkey(ErifRecruitYes, "w")
                (screensetup.BattleScreen).onkey(RecruitNeither, "e")
        elif RecruitFael != True and RecruitErif != True and units.Azure not in units.UnitsRecruited:
            if CutsceneIndex == 15:
                Text2("Fael: Bruh.",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("(...)",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text3("???: DID SOMEBODY SAY \"BRUH\"!?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 18:
                Text2("???: Bruh-huh!",units.Proton.Portrait,units.Vruh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 19:
                Text2("???: I am the great Vruh E. Momen LXIX!",units.Proton.Portrait,units.Vruh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 20:
                Text2("Vruh: I search the world for epic \"Bruh",units.Proton.Portrait,units.Vruh.Portrait)
                line2("Moments\", and your sir... have just said")
                line3("\"Bruh\"!")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 21:
                Text2("Vruh: Such wholesomeness! Such gaming!",units.Proton.Portrait,units.Vruh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Vruh: Such",units.Proton.Portrait,units.Vruh.Portrait)
                
                Text2("Vruh: Such.",units.Proton.Portrait,units.Vruh.Portrait)
                
                Text2("Vruh: Such..",units.Proton.Portrait,units.Vruh.Portrait)
                
                Text2("Vruh: Such...",units.Proton.Portrait,units.Vruh.Portrait)
                
                Text2("Vruh: Such... D",units.Proton.Portrait,units.Vruh.Portrait)
                
                Text2("Vruh: Such... D R",units.Proton.Portrait,units.Vruh.Portrait)
                
                Text2("Vruh: Such... D R I",units.Proton.Portrait,units.Vruh.Portrait)
                
                Text2("Vruh: Such... D R I P",units.Proton.Portrait,units.Vruh.Portrait)
                
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("Vruh: This is truly poggers!",units.Proton.Portrait,units.Vruh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Vruh: Oh what an adventure this will be!",units.Proton.Portrait,units.Vruh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 25:
                Text3("[Q] You're hired")
                line2("[W] We never recruited you")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(VruhRecruitYes, "q")
                (screensetup.BattleScreen).onkey(Cutscene, "w")
            elif RecruitVruh == True and units.Azure not in units.UnitsRecruited:
                if CutsceneIndex == 26:
                    Text2("Vruh: Poggers.",units.Proton.Portrait,units.Vruh.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 27:
                    Text3("[Vruh joined your party]")
                    units.UnitsAlive.append(units.Vruh)
                    units.UnitsRecruited.append(units.Vruh)
                    CutsceneIndex = 0
                    Chapter = "Chapter 11a"
                    
            elif units.Azure not in units.UnitsRecruited:
                if CutsceneIndex == 26:
                    Text2("Vruh: Oh, so that's how it is...",units.Proton.Portrait,units.Vruh.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 27:
                    Text2("Vruh: You shall repent in the fires of the Xuir Wrath",units.Proton.Portrait,units.Vruh.Portrait)
                    line2("for all of eternity, with no hope of ever escaping")
                    line3("to freedom, for you have disturbed the way of the Bruh.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 28:
                    Text2("Vruh: I wait for the day in which I may witness your",units.Proton.Portrait,units.Vruh.Portrait)
                    line2("untimely gameend so in which I could perform the dance")
                    line3("of the defaults upon your soulless husk of a body.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 29:
                    Text2("Vruh: /s",units.Proton.Portrait,units.Vruh.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 29:
                    Text2("Vruh: See y'all homies later.",units.Proton.Portrait,units.Vruh.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 30:
                    Text1("Proton: ...",units.Proton.Portrait)
                    CutsceneIndex = 0
                    Chapter = "Chapter 11a"
                    
        elif RecruitFael == True:
            if CutsceneIndex == 15:
                Text2("Fael: I will not fail.",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text3("[Fael joined your party]")
                units.UnitsAlive.append(units.Fael)
                units.UnitsRecruited.append(units.Fael)
                CutsceneIndex = 0
                Chapter = "Chapter 11a"
                
        elif RecruitErif == True:
            if CutsceneIndex == 15:
                Text2("Erif: I will not disappoint.",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text3("[Erif joined your party]")
                units.UnitsAlive.append(units.Erif)
                units.UnitsRecruited.append(units.Erif)
                CutsceneIndex = 0
                Chapter = "Chapter 11a"
                
    elif Chapter == "Chapter 10b": #=====================Chapter10b===============================================================
        ChapterLevel = 13
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 10b]")
            line2("[Forbidden Dephs, Nation of Altar]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark goldenrod")
            Text1("Proton: We've reached the location of binding.",units.Proton.Portrait)
            placeunits.PlacePlayerUnits()
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            
            
            UnitsToPlace = placeunits.Chapter10bEnemies
            UnitFormation = placeunits.Chapter10bPlacement
            placeunits.PlacePlayerUnits()
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("Wallimos: So the mortals arrive...",units.Wallimos.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Wallimos: I am the Dark God, Wallimos Alexander!",units.Wallimos.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Wallimos: And you will be the newest sacrifice!",units.Wallimos.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            CutsceneIndex += 1
            
            
            
            
        elif CutsceneIndex == 6:
            Text1("Proton: We somehow did it...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text1("Proton: Wallimos has been sealed once again.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text1("Proton: Now, back to what we were doing...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text1("Proton: We need to return back to Static and",units.Proton.Portrait)
            line2("head to the Nolavillian continent.")
            CutsceneIndex = 0
            Chapter = "Chapter 09a"
            
    elif Chapter == "Chapter 10c": #=====================Chapter10c===============================================================
        ChapterLevel = 12
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 10c]")
            line2("[Outer Static, Territory of Static]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: ...",units.Proton.Portrait)
            placeunits.PlacePlayerUnits()
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            
            
            UnitsToPlace = placeunits.Chapter10cEnemies
            UnitFormation = placeunits.Chapter10cPlacement
            placeunits.PlacePlayerUnits()
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("Fael: Proton Xurr, you are currently under",units.Fael.Portrait)
            line2("investigation due to the deaths of all of your")
            line3("allies.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Fael: You shall return to the castle immediately,",units.Fael.Portrait)
            line2("where you will temporarily be held.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text3("(Proton attacks Fael)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text1("Fael: So you choose to be guilty, we have",units.Fael.Portrait)
            line2("been authroized to fight back.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text1("Fael: We will defeat you!",units.Fael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            CutsceneIndex += 1
            
            
            
            
        elif CutsceneIndex == 9:
            Text1("Fael: So in the end... I still failed...",units.Fael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text1("Erif: I can't... die here...",units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 11b"
             
    elif Chapter == "Chapter 11a": #=====================Chapter11a===============================================================
        ChapterLevel = 15
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[End of Act I]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            Text2("Proton: Survived",units.Proton.Portrait,units.Scien.Portrait)
            if units.Quest in units.UnitsAlive:
                line2("Quest: Survived")
            elif units.Quest in units.UnitsRecruited:
                line2("Quest: Defeated")
            else:
                line2("Quest: Not Recruited")
            if units.Scien in units.UnitsAlive:
                line3("Scien: Survived")
            elif units.Scien in units.UnitsRecruited:
                line3("Scien: Defeated")
            else:
                line3("Scien: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            if units.Romra in units.UnitsAlive:
                Text2("Romra: Survived",units.Romra.Portrait,units.TnemecalperII.Portrait)
            elif units.Romra in units.UnitsRecruited:
                Text2("Romra: Defeated",units.Romra.Portrait,units.TnemecalperII.Portrait)
            else:
                Text2("Romra: Not Recruited",units.Romra.Portrait,units.TnemecalperII.Portrait)
            if units.TnemecalperI in units.UnitsAlive:
                line2("Tnemecalper I: Survived")
            elif units.TnemecalperI in units.UnitsRecruited:
                line2("Tnemecalper I: Defeated")
            else:
                line2("Tnemecalper I: Not Recruited")
            if units.TnemecalperII in units.UnitsAlive:
                line3("Tnemecalper II: Survived")
            elif units.TnemecalperII in units.UnitsRecruited:
                line3("Tnemecalper II: Defeated")
            else:
                line3("Tnemecalper II: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            if units.TnemecalperIII in units.UnitsAlive:
                Text2("Tnemecalper III: Survived",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            elif units.TnemecalperIII in units.UnitsRecruited:
                Text2("Tnemecalper III: Defeated",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            else:
                Text2("Tnemecalper III: Not Recruited",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            if units.TnemecalperIV in units.UnitsAlive:
                line2("Tnemecalper IV: Survived")
            elif units.TnemecalperIV in units.UnitsRecruited:
                line2("Tnemecalper IV: Defeated")
            else:
                line2("Tnemecalper IV: Not Recruited")
            if units.Lacirtcele in units.UnitsAlive:
                line3("Lacirtcele: Survived")
            elif units.Lacirtcele in units.UnitsRecruited:
                line3("Lacirtcele: Defeated")
            else:
                line3("Lacirtcele: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            if units.Damagein in units.UnitsAlive:
                Text2("Damagein: Survived",units.Damagein.Portrait,units.Wob.Portrait)
            elif units.Damagein in units.UnitsRecruited:
                Text2("Damagein: Defeated",units.Damagein.Portrait,units.Wob.Portrait)
            else:
                Text2("Damagein: Not Recruited",units.Damagein.Portrait,units.Wob.Portrait)
            if units.Healia in units.UnitsAlive:
                line2("Healia: Survived")
            elif units.Healia in units.UnitsRecruited:
                line2("Healia: Defeated")
            else:
                line2("Healia: Not Recruited")
            if units.Wob in units.UnitsAlive:
                line3("Wob: Survived")
            elif units.Wob in units.UnitsRecruited:
                line3("Wob: Defeated")
            else:
                line3("Wob: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            if units.Bladen in units.UnitsAlive:
                Text2("Bladen: Survived",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            elif units.Bladen in units.UnitsRecruited:
                Text2("Bladen: Defeated",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            else:
                Text2("Bladen: Not Recruited",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            if units.Wodahs in units.UnitsAlive:
                line2("Wodahs: Survived")
            elif units.Wodahs in units.UnitsRecruited:
                line2("Wodahs: Defeated")
            else:
                line2("Wodahs: Not Recruited")
            if units.PlayableBladeous in units.UnitsAlive:
                line3("Bladeous: Survived")
            elif units.PlayableBladeous in units.UnitsRecruited:
                line3("Bladeous: Defeated")
            else:
                line3("Bladeous: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            if units.Azure in units.UnitsAlive:
                Text2("Azure: Survived",units.Azure.Portrait,units.Erif.Portrait)
            elif units.Azure in units.UnitsRecruited:
                Text2("Azure: Defeated",units.Azure.Portrait,units.Erif.Portrait)
            else:
                Text2("Azure: Not Recruited",units.Azure.Portrait,units.Erif.Portrait)
            if units.Fael in units.UnitsAlive:
                line2("Fael: Survived")
            elif units.Fael in units.UnitsRecruited:
                line2("Fael: Defeated")
            else:
                line2("Fael: Not Recruited")
            if units.Erif in units.UnitsAlive:
                line3("Erif: Survived")
            elif units.Erif in units.UnitsRecruited:
                line3("Erif: Defeated")
            else:
                line3("Erif: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            if units.Vruh in units.UnitsAlive:
                Text1("Vruh: Survived",units.Vruh.Portrait)
            elif units.Vruh in units.UnitsRecruited:
                Text1("Vruh: Defeated",units.Vruh.Portrait)
            else:
                Text1("Vruh: Not Recruited",units.Vruh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text3("[Act II]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text3("[Chapter 11a]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            screensetup.BattleScreen.bgcolor("navy")
            Text1("Proton: We'll be sailing around the Territory",units.Proton.Portrait)
            line2("of Castle and will head northeast to Nolavillia")
            line3("from there.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text1("Proton: But we'll need to be careful, the",units.Proton.Portrait)
            line2("Bipole Sea is a dangerous place.")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter11aEnemies
            UnitFormation = placeunits.Chapter11aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 13:
            screensetup.BattleScreen.bgcolor("navy")
            Text1("Proton: We should be safe for now...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif units.Fael in units.UnitsAlive and CutsceneIndex <= 31:
            if CutsceneIndex == 14:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Fael: Hey Proton.",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Proton: Hey.",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text2("Fael: It feels strange, leaving Bipole.",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 18:
                Text2("Fael: I've never left the continent before.",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 19:
                Text2("Proton: This will be my first time going back",units.Proton.Portrait,units.Fael.Portrait)
                line2("to Nolavilla.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 20:
                Text2("Proton: I don't remember anything from when I",units.Proton.Portrait,units.Fael.Portrait)
                line2("was there, so it feels strange for me too.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 21:
                Text2("Fael: ...",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Fael: I never expected to be leaving the continent,",units.Proton.Portrait,units.Fael.Portrait)
                line2("always thought I'd die before it would have the")
                line3("chance.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("Proton: Why's that?",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Fael: Well, I don't actually like archery, but I'm",units.Proton.Portrait,units.Fael.Portrait)
                line2("good at it.")
                CutsceneIndex = 26
                
            elif CutsceneIndex == 26:
                Text2("Fael: So after my parents made me join the army and the",units.Proton.Portrait,units.Fael.Portrait)
                line2("EOS, I thought I would live my life fighting until I died")
                line3("on the battlefield.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 27:
                Text2("Fael: But I'm glad that I'll be able to go to Nolavillia,",units.Proton.Portrait,units.Fael.Portrait)
                line2("I've always wanted to explore the world.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 28:
                Text3("[Proton and Fael leveled up!]")
                select.InstantLevelUp(units.Proton,2)
                select.InstantLevelUp(units.Fael,2)
                CutsceneIndex = 32
                
        elif units.Erif in units.UnitsAlive and CutsceneIndex <= 31:
            if CutsceneIndex == 14:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Erif: Hello.",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Proton: Hello.",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text2("Erif: ...",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 18:
                Text2("Erif: So the Holy Itucher, it truly",units.Proton.Portrait,units.Erif.Portrait)
                line2("exists?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 19:
                Text2("Proton: It seems.",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 20:
                Text2("Erif: My older brother was always obsessed with",units.Proton.Portrait,units.Erif.Portrait)
                line2("with relics.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 21:
                Text2("Erif: I remeber him saying that he'd find the Holy",units.Proton.Portrait,units.Erif.Portrait)
                line2("Itucher one day.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Erif: \"Hey, I'm going to find the Itucher one day!\"",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("Erif: I'd do anything to go back to those days...",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Erif: ...",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 25:
                Text2("Erif: If he were still here, I wonder if he'd be able",units.Proton.Portrait,units.Erif.Portrait)
                line2("to actually find it...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 26:
                Text2("Erif: ...",units.Proton.Portrait,units.Erif.Portrait)
                CutsceneIndex = 31
                
            elif CutsceneIndex == 31:
                Text3("[Proton and Erif leveled up!]")
                select.InstantLevelUp(units.Proton,2)
                select.InstantLevelUp(units.Erif,2)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 31:
            CutsceneIndex = 32
            Cutscene()
        elif len(units.UnitsAlive) <= 5:
            if CutsceneIndex == 32:
                Text3("[A small boat passes by Proton's ship]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 33:
                Text2("???: What are you guys doing?",units.Proton.Portrait,units.Recils.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text2("Proton: Going to Nolavillia to reclaim the Holy",units.Proton.Portrait,units.Recils.Portrait)
                line2("Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 35:
                Text2("???: Someone's taken it already?",units.Proton.Portrait,units.Recils.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 36:
                Text2("Proton: Yeah, some evil scientists.",units.Proton.Portrait,units.Recils.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 37:
                Text2("???: ...",units.Proton.Portrait,units.Recils.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("???: You guys mind if I join you? This would look",units.Proton.Portrait,units.Recils.Portrait)
                line2("pretty good on my rėsumé.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text3("[Recruit ???]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
            elif CutsceneIndex == 40:
                if Qinput == True:
                    Text2("???: Thanks, this should be interesting.",units.Proton.Portrait, units.Recils.Portrait)
                    line2("this..")
                    CutsceneIndex += 1
                    
                else:
                    Text2("???: Okay then.",units.Proton.Portrait, units.Recils.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 41:
                if Qinput == True:
                    Text3("[Recils has joined your party]")
                    units.UnitsAlive.append(units.Recils)
                    units.UnitsRecruited.append(units.Recils)
                    CutsceneIndex = 0
                    Chapter = "Chapter 12a"
                    ClearInputs()
                    
                else:
                    CutsceneIndex = 0
                    Chapter = "Chapter 12a"
                    ClearInputs()
                    Cutscene()
        else:
            CutsceneIndex = 0
            Chapter = "Chapter 12a"
            Cutscene()
    elif Chapter == "Chapter 11b": #=====================Chapter11b===============================================================
        ChapterLevel = 15
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[End of Act I]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text3("[Act II]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text3("[Chapter 11b]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            screensetup.BattleScreen.bgcolor("navy")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter11bEnemies
            UnitFormation = placeunits.Chapter11bPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 5:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 12b"
            
    elif Chapter == "Chapter 12a": #=====================Chapter12a===============================================================
        ChapterLevel = 17
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 12a]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("navy")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Proton: I think I see someone.",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text3("(A small boat passes by Proton's ship)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("???: ...",units.Proton.Portrait,units.Repins.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text2("Proton: Hello.",units.Proton.Portrait,units.Repins.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text2("???: Hello.",units.Proton.Portrait,units.Repins.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex > 6 and CutsceneIndex <= 22 and units.Erif in units.UnitsAlive or CutsceneIndex > 6 and CutsceneIndex <= 10 and units.Wob in units.UnitsAlive:
            if CutsceneIndex == 7:
                if units.Erif in units.UnitsAlive:
                    units.Repins.Attacks.append(moves.ErifWasThere)
                if units.Wob in units.UnitsAlive:
                    units.Repins.Attacks.append(moves.WobWasThere)
                Text2("???: Wait, is that...",units.Proton.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("???: Sorry, but I must be on my way.",units.Proton.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text1("(??? leaves the area)",units.Proton.Portrait)
                CutsceneIndex = 23
                
        elif CutsceneIndex > 6 and CutsceneIndex <= 22 and units.Wodahs in units.UnitsAlive:
            if CutsceneIndex == 7:
                Text2("Wodahs: Repins, is that you?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("Repins: Wodahs? What are you doing here?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("Wodahs: Hunting after the Itucher.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Repins: I'm coming back from Altar, someone's",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("already taken the Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Wodahs: I've went to Altar as well, but we know",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("where the Itucher's been moved to.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 12:
                Text2("Repins: You do!?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Wodahs: You could come with us if you'd like, since",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("you've always been obsessed with finding the Itucher")
                line3("and all.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Wodahs: Also, the King of Static will pay all of us who help",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("retrieve it.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Repins: Are you serious!?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Repins: ...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text2("Repins: PLEASE ALLOW ME TO HELP YOU RETRIEVE THE HOLY",units.Proton.Portrait,units.Repins.Portrait)
                line2("ITUCHER!!!")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 18:
                Text3("[Recruit Repins]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(RepinsRecruitYes, "q")
                (screensetup.BattleScreen).onkey(Cutscene, "w")
            elif CutsceneIndex == 19:
                if RecruitRepins == True:
                    Text2("Repins: I've... I've waited so long for",units.Proton.Portrait, units.Repins.Portrait)
                    line2("this..")
                    CutsceneIndex += 1
                    
                else:
                    Text2("Repins: ...",units.Proton.Portrait, units.Repins.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 20:
                if RecruitRepins == True:
                    Text2("Repins: THANK YOU! THANK YOU SO MUCH!!!",units.Proton.Portrait, units.Repins.Portrait)
                    CutsceneIndex += 1
                    
                else:
                    units.Repins.Attacks.append(moves.DeclinedRepins)
                    Text1("(Repins leaves in silence)",units.Proton.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 21:
                if RecruitRepins == True:
                    Text3("[Repins has joined your party]")
                    units.UnitsAlive.append(units.Repins)
                    units.UnitsRecruited.append(units.Repins)
                    CutsceneIndex += 1
                    
                else:
                    CutsceneIndex += 1
                    Cutscene()
            elif CutsceneIndex == 22:
                Text1("Proton: ...",units.Proton.Portrait)
                CutsceneIndex = 23
                 
        elif CutsceneIndex > 6 and CutsceneIndex <= 22:
            if CutsceneIndex == 7:
                Text2("???: Sorry, but I must be on my way.",units.Proton.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text1("(??? leaves the area)",units.Proton.Portrait)
                CutsceneIndex = 23
                
        elif CutsceneIndex == 23:
            Text1("Proton: There are some enemies approaching, prepare",units.Proton.Portrait)
            line2("for battle!")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter12aEnemies
            UnitFormation = placeunits.Chapter12aPlacement
            BattleStarted = False
            battle_started = True
        elif units.Wodahs in units.UnitsAlive and units.Repins in units.UnitsAlive:
            if CutsceneIndex == 24:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 25:
                Text2("Wodahs: Hey Repins.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 26:
                Text2("Repins: Hey.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 27:
                Text2("Wodahs: How long's it been since the academy?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 28:
                Text2("Repins: About 2 years.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 29:
                Text2("Wodahs: Dang, time really flies.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 30:
                Text2("Repins: Anything happend back at Static?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 31:
                Text2("Wodahs: I was actually able to become a member",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("of the Elemental Offense Squad.")
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 32:
                Text2("Wodahs: Suprisingly, they're pretty chill.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 33:
                Text2("Wodahs: I mostly do solo missions though, so",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("I don't really get to hang out much.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text2("Repins: Anything I should know about them?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 35:
                Text2("Wodahs: Hmm...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 36:
                Text2("Wodahs: Lacirtcele thinks he's cool, he's not.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 37:
                Text2("Wodahs: Fael is boring, all he ever talks about",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("is archery and work.")
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 38:
                Text2("Wodahs: Erif is also boring, all she every talks",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("about is the Quad Genocide and her dead family.")
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 39:
                Text2("Wodahs: And there's some generic-looking guy",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("who I haven't even bothered talking to.")
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 40:
                Text2("Wodahs: There's probably a few more that I've forgotten",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("but haven't actually met all of them yet.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 41:
                Text2("Wodahs: As for other people here, Proton",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("is pretty chill.")
                CutsceneIndex += 1
                  
            elif CutsceneIndex == 42 and units.Quest in units.UnitsAlive:
                Text2("Wodahs: Quest is boring and only ever talks about finding",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("the Holy Itucher, kind of like you used to.")
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 42:
                CutsceneIndex +=1
                Cutscene()
            elif CutsceneIndex == 43 and units.Scien in units.UnitsAlive:
                Text2("Wodahs: I am genuienly terrified by Scien.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 43:
                CutsceneIndex +=1
                Cutscene()
            elif CutsceneIndex == 44 and units.Romra in units.UnitsAlive:
                Text2("Wodahs: Romra exists.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 44:
                CutsceneIndex +=1
                Cutscene()
            elif CutsceneIndex == 45 and units.Damagein in units.UnitsAlive:
                Text2("Wodahs: Damagein is crazy, stay away from him.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 45:
                CutsceneIndex +=1
                Cutscene()
            elif CutsceneIndex == 46 and units.Healia in units.UnitsAlive:
                Text2("Wodahs: Healia is Sine noble, or something. I'd like to",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("see her say that to Erif.")
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 46:
                CutsceneIndex +=1
                Cutscene()
            elif CutsceneIndex == 47 and units.Bladen in units.UnitsAlive:
                Text2("Wodahs: Bladen is sus, I don't trust him.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 47:
                CutsceneIndex +=1
                Cutscene()
            elif CutsceneIndex == 48:
                Text2("Wodahs: And of course, there's me.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 49:
                Text2("Wodahs: I'm epic.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 50:
                Text3("[Wodahs and Repins leveled up!]")
                select.InstantLevelUp(units.Wodahs,2)
                select.InstantLevelUp(units.Repins,2)
                CutsceneIndex = 0
                Chapter = "Chapter 13a"
                 
        else:
            CutsceneIndex = 0
            Chapter = "Chapter 13a"
            Cutscene()
    elif Chapter == "Chapter 12b": #=====================Chapter12b===============================================================
        ChapterLevel = 17
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 12b]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("navy")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter12bEnemies
            UnitFormation = placeunits.Chapter12bPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 2:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 13b"
            Cutscene()
    elif Chapter == "Chapter 13a": #=====================Chapter13a===============================================================
        ChapterLevel = 19
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 13a]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("navy")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Proton: I think I see someone.",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text3("(A small boat passes by Proton's ship)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("???: ...",units.Proton.Portrait,units.Relaeh.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text2("???: Are you going to Altar?",units.Proton.Portrait,units.Relaeh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("???: If so, I don't recommend going there.",units.Proton.Portrait,units.Relaeh.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 7:
            Text2("Proton: No, we are going to Nolavillia.",units.Proton.Portrait,units.Relaeh.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text2("???: Nolavillia?",units.Proton.Portrait,units.Relaeh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("???: I suppose I could live there...",units.Proton.Portrait,units.Relaeh.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 10:
            Text2("???: I used to live at Altar, but my town",units.Proton.Portrait,units.Relaeh.Portrait)
            line2("was destroyed by the Holy Itucher.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            Text2("???: Would you mind if I joined you guys on your",units.Proton.Portrait,units.Relaeh.Portrait)
            line2("journey to Nolavillia?")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            Text3("[Recruit ???]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(RelaehRecruitYes, "q")
            (screensetup.BattleScreen).onkey(Cutscene, "w")
        elif CutsceneIndex == 13:
            if RecruitRelaeh == True:
                Text2("Proton: You can come along if you'd like.",units.Proton.Portrait, units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("???: Oh.",units.Proton.Portrait, units.Relaeh.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 14:
            if RecruitRelaeh == True:
                Text2("Proton: We're also on our way to stop the Holy Itucher",units.Proton.Portrait, units.Relaeh.Portrait)
                line2("from evil.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 15:
            if RecruitRelaeh == True:
                Text2("???: You're going to stop the Holy Itucher? It must be",units.Proton.Portrait, units.Relaeh.Portrait)
                line2("stopped, allow me to help you stop it.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 16:
            if RecruitRelaeh == True:
                Text3("[Relaeh has joined your party]")
                units.UnitsAlive.append(units.Relaeh)
                units.UnitsRecruited.append(units.Relaeh)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 17:
            Text2("???: Oh yeah, did I tell you I was being chased",units.Proton.Portrait,units.Relaeh.Portrait)
            line2("by pirates?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("Proton: What!?",units.Proton.Portrait,units.Relaeh.Portrait)
            CutsceneIndex += 1
            placeunits.PlacePlayerUnits()
            
        elif CutsceneIndex == 19:
            Text2("???: HAR! HAR! HAR! HAR! HARRRRR!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("???: I AM THE GREAT KAPTAIN K'NEVILLE!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("K'Neville: THE GREATEST WARRIOR IN THE REALM!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("K'Neville: THE MASTER OF THE ECONOMY!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("K'Neville: THE KING OF THE UNKNOWN AMOUNT OF SEAS!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("K'Neville: FEAR ME!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("K'Neville: ...AND MY UNTHREATENING CREW!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("???: What poppin' gang.",units.Proton.Portrait,units.DiverNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("K'Neville: HAR! HAR! HAR! HAR! HARRRRR!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("K'Neville: LEEEEEEETS LOOT 'EM!!!!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("???: Where we droppin' bois?",units.Proton.Portrait,units.DiverNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            
            
            UnitsToPlace = placeunits.Chapter13aEnemies
            UnitFormation = placeunits.Chapter13aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text2("???: SKREEEEEEEEEEEEEEEEE!!!!!!!!!!!",units.Proton.Portrait,units.DiverNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("Proton: Everyone! Prepare for battle!",units.Proton.Portrait,units.DiverNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            CutsceneIndex += 1
            
            
            
            
        elif CutsceneIndex > 32 and units.Healia in units.UnitsAlive and units.Erif in units.UnitsAlive:
            if CutsceneIndex == 33:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text2("Healia: Hello, Erif.",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 35:
                Text2("Erif: Hey.",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 36:
                Text2("Healia: Could you tell me why you joined",units.Healia.Portrait,units.Erif.Portrait)
                line2("the Elemental Offense Squad.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 37:
                Text2("Erif: Why I joined?",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("Healia: Yes.",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text2("Erif: ...",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 40:
                Text2("Erif: About 9 years ago, my parents died in the Quad",units.Healia.Portrait,units.Erif.Portrait)
                line2("Genocide.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 41:
                Text2("Erif: Afterwards, my siblings and I were barely able to survive.",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 42:
                Text2("Erif: A year later, my older brother comitted suicide.",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 43:
                Text2("Erif: Once I turned 13, we moved to Static and I joined the army.",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 44:
                Text2("Erif: Joining the army made it so we were able to go without starving.",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 45:
                Text2("Erif: 5 years later, I was promoted to the Elemental Offense Squad and",units.Healia.Portrait,units.Erif.Portrait)
                line2("here I am now.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 46:
                Text2("Erif: ...",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 47:
                Text2("Healia: ...",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 48:
                Text2("Healia: ...that's horrible.",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 49:
                Text2("Erif: So... why did you decide to join Proton's group?",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 50:
                Text2("Healia: ...",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 51:
                Text2("Healia: (Mabye I shouldn't tell her that I'm from Sine...)",units.Healia.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 52:
                Text3("[Healia and Erif leveled up!]")
                select.InstantLevelUp(units.Healia,2)
                select.InstantLevelUp(units.Erif,2)
                CutsceneIndex = 0
                Chapter = "Chapter 14a"
                
        else:
            CutsceneIndex = 0
            Chapter = "Chapter 14a"
            Cutscene()
    elif Chapter == "Chapter 13b": #=====================Chapter13b===============================================================
        ChapterLevel = 19
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 13b]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            Text2("???: Wacky fellow over 'ere!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text2("???: We're gonna loot yer' ship!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text2("???: ...",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("???: What's with that expression?",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            screensetup.BattleScreen.bgcolor("navy")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter13bEnemies
            UnitFormation = placeunits.Chapter13bPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 6:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 14b"
            Cutscene()
    elif Chapter == "Chapter 14a": #=====================Chapter14a===============================================================
        ChapterLevel = 21
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 14a]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("navy")
            Text2("???: Hmmm.....",units.Proton.Portrait,units.BigBrainNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text2("???: It seems like Diver Neville has lost...",units.Proton.Portrait,units.BigBrainNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text2("???: Well then, I guess it's my turn!",units.Proton.Portrait,units.BigBrainNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("???: Everyone, CHARGE!!!",units.Proton.Portrait,units.BigBrainNeville.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter14aEnemies
            UnitFormation = placeunits.Chapter14aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex > 4 and CutsceneIndex <= 24 and units.Repins in units.UnitsAlive and units.Wodahs in units.UnitsAlive:
            if CutsceneIndex == 5:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 6:
                Text2("Wodahs: Hey.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 7:
                Text2("Repins: Hey.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("Wodahs: Remember that time I shot my eye?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("Repins: Yes, very clearly.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Repins: It was the first day of combat academy when",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("we were being tested on how well we could use the")
                line3("weapons.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Repins: And you somehow shot your own eye when trying",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("to use the bow.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 12:
                Text2("Repins: Afterwards, you drew that hitmarker on",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("on your eyepatch.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Wodahs: Correct corrrect correct!",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Wodahs: And I was just thinking, what would my life",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("have been like if I was able to use the bow but")
                line3("was unable to use my fists?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Wodahs: Would I have punched my own eye out?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Repins: Don't ask me, I still have no idea how you would",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("even shoot your own eye.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text2("Wodahs: Well, it's one of the only things I've ever",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("succesfully hit in the center.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 18:
                Text2("Wodahs: Anyways, I'm glad I was sent to the hospital",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("before I had to do the dagger testing.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 19:
                Text2("Wodahs: That could have gone very bad.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 20:
                Text2("Repins: Honestly, I have no idea how you've made it",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("into the Elemental Offense Squad not knowing how to")
                line3("use any weapons.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 21:
                Text2("Wodahs: Some may call it luck, I call it fate.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Repins: It was fate that you have no combat ability",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("outside of punching?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("Wodahs: It's fate that I'm this gamer (insert explosion)",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("transition).")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text3("[Wodahs and Repins leveled up!]")
                select.InstantLevelUp(units.Wodahs,2)
                select.InstantLevelUp(units.Repins,2)
                CutsceneIndex += 1
                
        elif CutsceneIndex > 4 and CutsceneIndex <= 24:
            CutsceneIndex = 25
            Cutscene()
        elif CutsceneIndex > 24 and CutsceneIndex < 72 and units.Wodahs in units.UnitsAlive and units.Fael in units.UnitsAlive and units.Repins in units.UnitsAlive:
            if CutsceneIndex == 25:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 26:
                Text2("Wodahs: FAEL!",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 27:
                Text2("Fael: Huh?",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 28:
                Text2("Wodahs: How does one use a bow?",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 29:
                Text2("Fael: You don't know how to use a bow?",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 30:
                Text2("Wodahs: Let me be more precise...",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 31:
                Text2("Wodahs: How does one not shoot themself when",units.Wodahs.Portrait,units.Fael.Portrait)
                line2("firing a bow?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 32:
                Text2("Fael: How DOES one shoot themself when",units.Wodahs.Portrait,units.Fael.Portrait)
                line2("firing a bow?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 33:
                Text2("Wodahs: ...",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text2("Wodahs: ...very epically.",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 35:
                Text2("Fael: Wait, don't tell me you've...",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 36:
                Text2("Wodahs: FAKE NEWS!!!",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 37:
                Text2("Wodahs: I would NEVER shoot myself with a bow!",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("Wodahs: ...or atleast un-epically.",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text2("Repins: Wodahs, it was not very \"epic\".",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 40:
                Text2("Wodahs: !?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 41:
                Text2("Wodahs: Na... nani!?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 42:
                Text2("Wodahs: How could that not be epic??????",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 43:
                Text2("Repins: You shot yourself with your own bow,",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("how is that even remotely \"epic\"?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 44:
                Text2("Wodahs: !?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 45:
                Text2("Wodahs: M... my... social status.....",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 46:
                Text2("Wodahs: It just dropped... by 10%...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 47:
                Text2("Wodahs: ...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 48:
                Text2("Wodahs: Atleast it wasn't a failure.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 49:
                Text2("Fael: That's the definition of a fail.",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 50:
                Text2("Wodahs: Not as much as your name.",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 51:
                Text2("Fael: !?",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 52:
                Text2("Wodahs: Critical hit, get destroyed.",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 53:
                Text2("Repins: What was this conversation even originally",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("about?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 54:
                Text2("Wodahs: Me, epically, asking how to use a bow without",units.Wodahs.Portrait,units.Fael.Portrait)
                line2("without epically shooting myself.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 55:
                Text2("Fael: Well, I'm not actually sure what advice to give,",units.Wodahs.Portrait,units.Fael.Portrait)
                line2("you for that.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 56:
                Text2("Fael: Don't aim the bow at yourself?",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 57:
                Text2("Fael: Not sure why you'd do that but...",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 58:
                Text2("Wodahs: No no no no no...",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 59:
                Text2("Wodahs: I wouldn't do something so simple like that.",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 60:
                Text2("Wodahs: I use the bow normally, but then have the arrows",units.Wodahs.Portrait,units.Fael.Portrait)
                line2("somehow end up hitting me.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 61:
                Text2("Fael: ...",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 62:
                Text2("Fael: ...how?",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 63:
                Text2("Wodahs: Here, let me show y...",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 64:
                Text2("Repins: N O .",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 65:
                Text2("Repins: Do not ever let him even near a bow.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 66:
                Text2("Repins: ...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 67:
                Text2("Fael: Okay?",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 68:
                Text2("Fael: ...",units.Wodahs.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 69:
                Text1("Fael: (This is why I don't talk to Wodahs...)",units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 70:
                Text1("Wodahs: (Fael is such a bad archer, he doesn't",units.Wodahs.Portrait)
                line2("even know how to shoot himself smh...)")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 71:
                Text3("[Wodahs, Fael, and Repins leveled up!]")
                select.InstantLevelUp(units.Wodahs,2)
                select.InstantLevelUp(units.Fael,2)
                select.InstantLevelUp(units.Repins,2)
                CutsceneIndex += 1
                
        elif CutsceneIndex > 24 and CutsceneIndex < 72:
            CutsceneIndex = 72
            Cutscene()
        elif CutsceneIndex >= 72 and len(units.UnitsAlive) <= 7:
            if CutsceneIndex == 72:
                Text1("Proton: I think I see a boat coming towards us...",units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 73:
                Text1("Proton: ...",units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 74:
                Text2("???: Hey, you know where this is?",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 75:
                Text2("Proton: The Bipole Sea, nearing Nolavillia.",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 76:
                Text2("???: Oh god, what do I do now...",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 77:
                Text2("Proton: ?",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 78:
                Text2("???: This is pretty far away from Altar, right?",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 79:
                Text2("???: I was escaping from there but then a storm",units.Proton.Portrait,units.Eulb.Portrait)
                line2("hit me and I ended up here.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 80:
                Text2("???: Is is okay if you could take me to whereever",units.Proton.Portrait,units.Eulb.Portrait)
                line2("you're going?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 81:
                Text2("Proton: We're going to Nolavillia to retrieve the Holy",units.Proton.Portrait,units.Eulb.Portrait)
                line2("Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 82:
                Text2("Proton: I'm warning you, it could get dangerous.",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 83:
                Text2("???: Wait, why would you want the Itucher?",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 84:
                Text2("???: It like destroyed Altar Town and stuff.",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 85:
                Text2("Proton: Well, some evil scientists have gotten",units.Proton.Portrait,units.Eulb.Portrait)
                line2("it and the world is in danger.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 86:
                Text2("???: The world is in danger?",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 87:
                Text2("???: I guess I should probably help you stop that.",units.Proton.Portrait,units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 88:
                Text3("[Recruit ???]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
            elif CutsceneIndex == 89:
                if Qinput == True:
                    Text2("???: Got it.",units.Proton.Portrait, units.Eulb.Portrait)
                    line2("this..")
                    CutsceneIndex += 1
                    
                else:
                    Text2("???: Okay...",units.Proton.Portrait, units.Eulb.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 90:
                if Qinput == True:
                    Text3("[Eulb has joined your party]")
                    units.UnitsAlive.append(units.Eulb)
                    units.UnitsRecruited.append(units.Eulb)
                    CutsceneIndex = 0
                    Chapter = "Chapter 15a"
                    ClearInputs()
                    
                else:
                    CutsceneIndex = 0
                    Chapter = "Chapter 15a"
                    ClearInputs()
                    Cutscene()
        elif CutsceneIndex >= 72:
            CutsceneIndex = 0
            Chapter = "Chapter 15a"
            Cutscene()
    elif Chapter == "Chapter 14b": #=====================Chapter14b===============================================================
        ChapterLevel = 21
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 14b]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("navy")
            Text2("???: He seems strong...",units.Proton.Portrait,units.BigBrainNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text2("???: Prepare for battle!",units.Proton.Portrait,units.BigBrainNeville.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter14bEnemies
            UnitFormation = placeunits.Chapter14bPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 3:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 15b"
            
    elif Chapter == "Chapter 15a": #=====================Chapter15a===============================================================
        ChapterLevel = 23
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 15a]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("navy")
            Text2("K'Neville: Yerrrrr....",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            screensetup.BattleScreen.bgcolor("navy")
            Text2("K'Neville: Do I have to do everything myself?",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter15aEnemies
            UnitFormation = placeunits.Chapter15aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 3:
            Text2("K'Neville: ARGHHHHH!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("K'Neville: WE BE RETREAT'N!!!",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text3("(The K'Neville Pirates retreat)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text1("Proton: It looks like they've retreated.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text1("Proton: Huh, what's that?.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text3("(Proton sees a boat in the distance)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text1("Proton: Is that a house?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text3("(A small house is ontop of the boat)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text3("(Proton knocks on the door of the house)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("???: Hello?",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Proton: Hello, I was wondering, what is this?",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("???: My house?",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Proton: Your house is in the middle of a dangerous",units.Proton.Portrait,units.Lias.Portrait)
            line2("sea?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("???: Why are you so suprised?",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("Proton: How do you even get water?",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("???: Do you not see water around you?",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20 and units.Quest in units.UnitsAlive:
            Text2("Quest: You should not be alive right now.",units.Quest.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
                    
        elif CutsceneIndex == 20:
            Text2("Proton: ...",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
                   
        elif CutsceneIndex == 21:
            Text2("Proton: Sure.",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
                   
        elif CutsceneIndex == 22:
            Text3("(Proton starts to leave)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 23:
            Text2("Lias: Wait, what are you guys even doing in the",units.Proton.Portrait,units.Lias.Portrait)
            line2("middle of the sea?")
            CutsceneIndex += 1
                   
        elif CutsceneIndex == 24:
            Text2("Proton: We're traveling to Nolavillia to retrieve the Holy",units.Proton.Portrait,units.Lias.Portrait)
            line2("Itucher.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 25:
            Text2("Lias: Sounds fun, can I go?",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
                   
        elif CutsceneIndex == 26:
            Text2("Proton: ?",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
                
        elif CutsceneIndex == 27:
            Text2("Lias: What? It sounds like fun.",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
                 
        elif CutsceneIndex == 28:
            Text2("Proton: ...",units.Proton.Portrait,units.Lias.Portrait)
            CutsceneIndex += 1
                 
        elif CutsceneIndex == 29:
            Text3("[Recruit ???]")
            line2("(Q) Recruit")
            line3("(W) Do not recruit")
            CutsceneIndex += 1
            (screensetup.BattleScreen).onkey(LiasRecruitYes, "q")
            (screensetup.BattleScreen).onkey(Cutscene, "w")
        elif CutsceneIndex == 30:
            if RecruitLias == True:
                Text2("Proton: Sure, you can come with us.",units.Proton.Portrait, units.Lias.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Proton: No.",units.Proton.Portrait, units.Lias.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 31:
            if RecruitLias == True:
                Text2("Lias: Cool.",units.Proton.Portrait, units.Lias.Portrait)
                CutsceneIndex += 1
                
            else:
                Text3("(Proton leaves)")
                CutsceneIndex += 1
                
        elif CutsceneIndex == 32:
            if RecruitLias == True:
                Text3("[Lias has joined your party]")
                units.UnitsAlive.append(units.Lias)
                units.UnitsRecruited.append(units.Lias)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex > 32 and CutsceneIndex <= 51 and len(units.UnitsAlive) <= 8:
            if CutsceneIndex == 33:
                Text1("Proton: ...",units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text1("Proton: Hey, I think I see someone in the", units.Proton.Portrait)
                line2("water.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 35:
                Text1("Proton: ...", units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 36:
                Text2("???: Hey, could you help me?", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 37:
                Text2("Proton: Why are you in the middle of the ocean?", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("???: Because I was stealing from Kaptain K'Neville's", units.Proton.Portrait, units.Fieht.Portrait)
                line2("ships then a battle started so I jumped off.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text2("Proton: You were stealing from Kaptain K'Neville?", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 40:
                Text2("???: Everything he has is already stolen anyways.", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 41:
                Text2("???: ...", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 42:
                Text2("???: Could you help me out?", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 43:
                Text3("(Proton brings ??? onto the ship)")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 44:
                Text2("???: Thanks.", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 44:
                Text2("???: So, where are you guys going?", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 45:
                Text2("Proton: We're going to Nolavillia to retrieve the", units.Proton.Portrait, units.Fieht.Portrait)
                line2("Holy Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 46:
                Text2("???: You getting paid to do it?", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 47:
                Text2("Proton: Yeah.", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 48:
                Text2("???: Cool, can I join you guys?", units.Proton.Portrait, units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 49:
                Text3("[Recruit ???]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
            elif CutsceneIndex == 50:
                if Qinput == True:
                    Text2("???: Nice.",units.Proton.Portrait, units.Fieht.Portrait)
                    CutsceneIndex += 1
                    
                else:
                    Text1("(Proton throws ??? back into the ocean)",units.Proton.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 51:
                if Qinput == True:
                    Text3("[Fieht has joined your party]")
                    units.UnitsAlive.append(units.Fieht)
                    units.UnitsRecruited.append(units.Fieht)
                    CutsceneIndex += 1
                    ClearInputs()
                    
                else:
                    CutsceneIndex += 1
                    ClearInputs()
                    Cutscene()
        elif CutsceneIndex > 32 and CutsceneIndex <= 51 :
            CutsceneIndex = 52
            Cutscene()
        elif CutsceneIndex == 52:
            screensetup.BattleScreen.bgcolor("black")
            Text1("Proton: .",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 53:
            Text1("Proton: ..",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 54:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 55:
            Text1("Proton: ...!",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 56:
            screensetup.BattleScreen.bgcolor("navy")
            Text1("Proton: I see land!",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 57:
            Text1("Proton: I think we've finally make it to",units.Proton.Portrait)
            line2("Nolavillia!")
            CutsceneIndex = 0 
            Chapter = "Chapter 16a"
            
    elif Chapter == "Chapter 15b": #=====================Chapter15b===============================================================
        ChapterLevel = 23
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 15b]")
            line2("[Bipole Sea, Bipole Sea]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("navy")
            Text2("K'Neville: Yerrrrr....",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            screensetup.BattleScreen.bgcolor("navy")
            Text2("K'Neville: What's up with this guy?",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter15aEnemies
            UnitFormation = placeunits.Chapter15aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 3:
            Text2("K'Neville: ARGHHHHH...",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("K'Neville: WE... MUST... RETREAT...",units.Proton.Portrait,units.KaptainKNeville.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text3("[K'Neville has died]")
            CutsceneIndex = 0 
            Chapter = "Chapter 16b"
            
    elif Chapter == "Chapter 16a": #=====================Chapter16a===============================================================
        ChapterLevel = 25
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[End of Act II]")
            CutsceneIndex += 1
    
        elif CutsceneIndex == 1:
            Text2("Proton: Survived",units.Proton.Portrait,units.Scien.Portrait)
            if units.Quest in units.UnitsAlive:
                line2("Quest: Survived")
            elif units.Quest in units.UnitsRecruited:
                line2("Quest: Defeated")
            else:
                line2("Quest: Not Recruited")
            if units.Scien in units.UnitsAlive:
                line3("Scien: Survived")
            elif units.Scien in units.UnitsRecruited:
                line3("Scien: Defeated")
            else:
                line3("Scien: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            if units.Romra in units.UnitsAlive:
                Text2("Romra: Survived",units.Romra.Portrait,units.TnemecalperII.Portrait)
            elif units.Romra in units.UnitsRecruited:
                Text2("Romra: Defeated",units.Romra.Portrait,units.TnemecalperII.Portrait)
            else:
                Text2("Romra: Not Recruited",units.Romra.Portrait,units.TnemecalperII.Portrait)
            if units.TnemecalperI in units.UnitsAlive:
                line2("Tnemecalper I: Survived")
            elif units.TnemecalperI in units.UnitsRecruited:
                line2("Tnemecalper I: Defeated")
            else:
                line2("Tnemecalper I: Not Recruited")
            if units.TnemecalperII in units.UnitsAlive:
                line3("Tnemecalper II: Survived")
            elif units.TnemecalperII in units.UnitsRecruited:
                line3("Tnemecalper II: Defeated")
            else:
                line3("Tnemecalper II: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            if units.TnemecalperIII in units.UnitsAlive:
                Text2("Tnemecalper III: Survived",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            elif units.TnemecalperIII in units.UnitsRecruited:
                Text2("Tnemecalper III: Defeated",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            else:
                Text2("Tnemecalper III: Not Recruited",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            if units.TnemecalperIV in units.UnitsAlive:
                line2("Tnemecalper IV: Survived")
            elif units.TnemecalperIV in units.UnitsRecruited:
                line2("Tnemecalper IV: Defeated")
            else:
                line2("Tnemecalper IV: Not Recruited")
            if units.Lacirtcele in units.UnitsAlive:
                line3("Lacirtcele: Survived")
            elif units.Lacirtcele in units.UnitsRecruited:
                line3("Lacirtcele: Defeated")
            else:
                line3("Lacirtcele: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            if units.Damagein in units.UnitsAlive:
                Text2("Damagein: Survived",units.Damagein.Portrait,units.Wob.Portrait)
            elif units.Damagein in units.UnitsRecruited:
                Text2("Damagein: Defeated",units.Damagein.Portrait,units.Wob.Portrait)
            else:
                Text2("Damagein: Not Recruited",units.Damagein.Portrait,units.Wob.Portrait)
            if units.Healia in units.UnitsAlive:
                line2("Healia: Survived")
            elif units.Healia in units.UnitsRecruited:
                line2("Healia: Defeated")
            else:
                line2("Healia: Not Recruited")
            if units.Wob in units.UnitsAlive:
                line3("Wob: Survived")
            elif units.Wob in units.UnitsRecruited:
                line3("Wob: Defeated")
            else:
                line3("Wob: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            if units.Bladen in units.UnitsAlive:
                Text2("Bladen: Survived",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            elif units.Bladen in units.UnitsRecruited:
                Text2("Bladen: Defeated",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            else:
                Text2("Bladen: Not Recruited",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            if units.Wodahs in units.UnitsAlive:
                line2("Wodahs: Survived")
            elif units.Wodahs in units.UnitsRecruited:
                line2("Wodahs: Defeated")
            else:
                line2("Wodahs: Not Recruited")
            if units.PlayableBladeous in units.UnitsAlive:
                line3("Bladeous: Survived")
            elif units.PlayableBladeous in units.UnitsRecruited:
                line3("Bladeous: Defeated")
            else:
                line3("Bladeous: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            if units.Azure in units.UnitsAlive:
                Text2("Azure: Survived",units.Azure.Portrait,units.Erif.Portrait)
            elif units.Azure in units.UnitsRecruited:
                Text2("Azure: Defeated",units.Azure.Portrait,units.Erif.Portrait)
            else:
                Text2("Azure: Not Recruited",units.Azure.Portrait,units.Erif.Portrait)
            if units.Fael in units.UnitsAlive:
                line2("Fael: Survived")
            elif units.Fael in units.UnitsRecruited:
                line2("Fael: Defeated")
            else:
                line2("Fael: Not Recruited")
            if units.Erif in units.UnitsAlive:
                line3("Erif: Survived")
            elif units.Erif in units.UnitsRecruited:
                line3("Erif: Defeated")
            else:
                line3("Erif: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            if units.Vruh in units.UnitsAlive:
                Text2("Vruh: Survived",units.Vruh.Portrait,units.Repins.Portrait)
            elif units.Vruh in units.UnitsRecruited:
                Text2("Vruh: Defeated",units.Vruh.Portrait,units.Repins.Portrait)
            else:
                Text2("Vruh: Not Recruited",units.Vruh.Portrait,units.Repins.Portrait)
            if units.Recils in units.UnitsAlive:
                line2("Recils: Survived")
            elif units.Recils in units.UnitsRecruited:
                line2("Recils: Defeated")
            else:
                line2("Recils: Not Recruited")
            if units.Repins in units.UnitsAlive:
                line3("Repins: Survived")
            elif units.Repins in units.UnitsRecruited:
                line3("Repins: Defeated")
            else:
                line3("Repins: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            if units.Relaeh in units.UnitsAlive:
                Text2("Relaeh: Survived",units.Relaeh.Portrait,units.Lias.Portrait)
            elif units.Relaeh in units.UnitsRecruited:
                Text2("Relaeh: Defeated",units.Relaeh.Portrait,units.Lias.Portrait)
            else:
                Text2("Relaeh: Not Recruited",units.Relaeh.Portrait,units.Lias.Portrait)
            if units.Eulb in units.UnitsAlive:
                line2("Eulb: Survived")
            elif units.Eulb in units.UnitsRecruited:
                line2("Eulb: Defeated")
            else:
                line2("Eulb: Not Recruited")
            if units.Lias in units.UnitsAlive:
                line3("Lias: Survived")
            elif units.Lias in units.UnitsRecruited:
                line3("Lias: Defeated")
            else:
                line3("Lias: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            if units.Fieht in units.UnitsAlive:
                Text1("Fieht: Survived",units.Fieht.Portrait)
            elif units.Fieht in units.UnitsRecruited:
                Text1("Fieht: Defeated",units.Fieht.Portrait)
            else:
                Text1("Fieht: Not Recruited",units.Fieht.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text3("[Act III]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text3("[Chapter 16a]")
            line2("[Nolavillia, Nolavillian Continent]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            screensetup.BattleScreen.bgcolor("green")
            placeunits.PlacePlayerUnits()
            Text1("Proton: So we're finally here...", units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif units.Scien in units.UnitsAlive and CutsceneIndex <= 16:
            if CutsceneIndex == 14:
                Text2("Scien: It feels strange, being back in Nolavillia.", units.Proton.Portrait,units.Scien.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Scien: I feel like a stranger, like I don't deserve to", units.Proton.Portrait,units.Scien.Portrait)
                line2("return here...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Scien: ...", units.Proton.Portrait,units.Scien.Portrait)
                CutsceneIndex += 1
                
        elif units.Scien not in units.UnitsAlive and CutsceneIndex <= 16:
            if CutsceneIndex == 14:
                Text1("Proton: Nolavillia is technically my native continent,", units.Proton.Portrait)
                line2("but it doesn't feel like it.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text1("Proton: This place... something about it is just...", units.Proton.Portrait)
                line2("unsettling.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text1("Proton: If Scien were here, I wonder what he would've", units.Proton.Portrait)
                line2("felt, coming back to Nolavillia after all of this time...")
                CutsceneIndex += 1
                
        elif CutsceneIndex == 17:
            
            
            UnitsToPlace = placeunits.Chapter16aEnemies
            UnitFormation = placeunits.Chapter16aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("???: Do I see what I think I see!?",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text1("???: F- F- F- FOREIGNERS!?", units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text1("???: F- F- F- FOREIGNERS!?", units.Tluc.Portrait)
            line2("On MY Xuirist territory?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text1("???: *laughs maniacally*", units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text1("???: YOU THERE!", units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Proton: Me?", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("???: Yes, you!", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("???: Why are you on the shores of Xuirist land?", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("Proton: We've come from the Bipole continent, and", units.Tluc.Portrait,units.Proton.Portrait)
            line2("we just need to pass through and get to the Nation")
            line3("of Nation.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("???: Tomfoolery!", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("???: I know your Razzions are trying to invade us!", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("???: The one and only true god of this world is the", units.Tluc.Portrait,units.Proton.Portrait)
            line2("True Xuir!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("???: Those who worship the false god of Bobbish must be", units.Tluc.Portrait,units.Proton.Portrait)
            line2("exterminated!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("Proton: The True Xuir?", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("???: What about him?", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("Proton: Xuir?", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("Proton: I am Xuir.", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text2("???: Hmm?", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
            Text2("???: Wait... your arm...", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 34:
            register_shape("protonarm_big")
            Text2("???: That is the mark of the Proto-Xuirs.", units.Tluc.Portrait,"protonarm_big")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 35:
            Text2("Proton: Now, may we pass?", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 36:
            Text2("???: Heh heh heh...", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 37:
            Text2("???: HAH HAH HAH HAH!!!!", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 38:
            Text2("???: HAAAAAHAHAHAHAHAHAHAHAHA!!!!", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 39:
            Text2("???: YOU FOOL!", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 40:
            Text2("???: YOU COMPLETE IDIOT!!!", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 41:
            Text2("Proton: Huh?", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 42:
            Text2("???: We've been searching for you Proto-Xuirs,", units.Tluc.Portrait,units.Proton.Portrait)
            line2("and now you've come running at us!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 43:
            Text2("???: And funniest thing is, you weren't even on", units.Tluc.Portrait,units.Proton.Portrait)
            line2("the list of escaped Proto-Xuirs to capture!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 44:
            Text2("???: May the false Xuirs perish and my paycheck", units.Tluc.Portrait,units.Proton.Portrait)
            line2("be raised...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 45:
            Text2("???: ATTACK!!!", units.Tluc.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 46:
            
            
            UnitsToPlace = placeunits.RethgifandEgEnemies
            UnitFormation = placeunits.RethgifandEgEnemiesPlacement
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("???: Eg, do I think I see what I see?",units.Rethgif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 47:
            Text2("Eg: Likely.", units.Rethgif.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 48:
            Text2("???: This is amazing!", units.Rethgif.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 49:
            Text2("???: It's been a while since I've been in a battle.", units.Rethgif.Portrait,units.Eg.Portrait)
            line2("this big...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 50:
            Text2("???: We must fight in this battle!", units.Rethgif.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 51:
            Text2("???: If we don't fight, I might end up consuming large", units.Rethgif.Portrait,units.Eg.Portrait)
            line2("amounts of laundry cleaner again; and that would be")
            line3("something that I'd rather not experience.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 52:
            Text2("???: You there!", units.Rethgif.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 53:
            Text2("Proton: What!? More enemies?", units.Rethgif.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 54:
            Text2("???: Will you allow the great Rethgif to fight alongside", units.Rethgif.Portrait,units.Proton.Portrait)
            line2("your forces?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 55:
                Text3("[Recruit Rethgif and Eg]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 56:
            if Qinput == True:
                Text2("Rethgif: Eg, it's time for battle!",units.Rethgif.Portrait, units.Proton.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Rethgif: Okay then, I'll just fight along with the",units.Rethgif.Portrait, units.Proton.Portrait)
                line2("other team.")
                CutsceneIndex += 1
                
        elif CutsceneIndex == 57:
            if Qinput == True:
                Text3("[Rethgif and Eg have joined your party]")
                units.UnitsAlive.append(units.Rethgif)
                units.UnitsRecruited.append(units.Rethgif)
                units.UnitsAlive.append(units.Eg)
                units.UnitsRecruited.append(units.Eg)
                units.RethgifEnemy.TurtleName.hideturtle()
                units.EgEnemy.TurtleName.hideturtle()
                UnitsToPlace = placeunits.RethgifandEgAllies
                UnitFormation = placeunits.RethgifandEgAlliesPlacement
                placeunits.PlaceEnemies(UnitFormation)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                Text3("[Rethgif and Eg have joined the enemy team]")
                units.EnemyUnitsAlive.append(units.RethgifEnemy)
                units.EnemyUnitsAlive.append(units.EgEnemy)
                CutsceneIndex += 1
                ClearInputs()
                
        elif CutsceneIndex == 58:
            CutsceneIndex += 1
            
            
            
            
        elif CutsceneIndex <= 69 and units.Damagein in units.UnitsAlive and units.Relaeh in units.UnitsAlive:
            if CutsceneIndex == 59:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 60:
                Text2("Damagein: Relaeh.",units.Damagein.Portrait,units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 61:
                Text2("Relaeh: Yes?",units.Damagein.Portrait,units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 62:
                Text2("Damagein: Why do you heal?",units.Damagein.Portrait,units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 63:
                Text2("Relaeh: Why do I heal?",units.Damagein.Portrait,units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 64:
                Text2("Damagein: Yeah.",units.Damagein.Portrait,units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 65:
                Text2("Relaeh: There's a lot of people who harm, but",units.Damagein.Portrait,units.Relaeh.Portrait)
                line2("not many who heal.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 66:
                Text2("Relaeh: I think it's important to have a balance between",units.Damagein.Portrait,units.Relaeh.Portrait)
                line2("harming and healing.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 67:
                Text2("Damagein: So you heal so you can allow more damage...",units.Damagein.Portrait,units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 68:
                Text2("Damagein: Interesting...",units.Damagein.Portrait,units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 69:
                Text3("[Damagein and Relaeh leveled up!]")
                select.InstantLevelUp(units.Damagein,3)
                select.InstantLevelUp(units.Relaeh,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 69:
            CutsceneIndex = 70
            Cutscene()
        elif CutsceneIndex <= 79 and units.Wob in units.UnitsAlive and units.Erif in units.UnitsAlive:
            if CutsceneIndex == 70:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 71:
                Text2("Erif: So this is Nolavillia...", units.Erif.Portrait,units.Wob.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 72:
                Text2("Wob: You've never been here?", units.Erif.Portrait,units.Wob.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 73:
                Text2("Erif: No.", units.Erif.Portrait,units.Wob.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 74:
                Text2("Erif: I think you're overestimating how far we", units.Erif.Portrait,units.Wob.Portrait)
                line2("usually go on missions.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 75:
                Text2("Wob: Oh.", units.Erif.Portrait,units.Wob.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 76:
                Text2("Wob: I guess I'm pretty lucky to be in this", units.Erif.Portrait,units.Wob.Portrait)
                line2("mission, then.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 77:
                Text2("Erif: I'm still not sure why you're here.", units.Erif.Portrait,units.Wob.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 78:
                Text2("Wob: Neither am I.", units.Erif.Portrait,units.Wob.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 79:
                Text3("[Erif and Wob leveled up!]")
                select.InstantLevelUp(units.Erif,3)
                select.InstantLevelUp(units.Wob,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 79:
            CutsceneIndex = 80
            Cutscene()
        elif CutsceneIndex == 80:
            screensetup.BattleScreen.bgcolor("black")
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 81:
            Text3("Hahahahahaha!!!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 82:
            Text3("Those fools!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 83:
            Text1("Tluc: I've somehow managed to survive this encounter...",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 84:
            Text1("Tluc: ...",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 85:
            Text1("Tluc: I pledge my life to the True Xuir...",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 86:
            screensetup.BattleScreen.bgcolor("dark red")
            Text1("Tluc: XUIRIST CONNECTION!!!",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 87:
            Text1("Tluc: ...",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 88:
            Text1("Tluc: This is a dire message to all Xuirists...",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 89:
            Text1("Tluc: The Generation 3 Proto-Xuir No 2 has been discovered,",units.Tluc.Portrait)
            line2("alive, on the western land border of the continent.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 90:
            Text1("Tluc: Our squadron has been defeated, and the Proto",units.Tluc.Portrait)
            line2("Xuir is guarded by others.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 91:
            Text1("Tluc: They are currently heading to the Nation of Nation,",units.Tluc.Portrait)
            line2("block off all paths to the Nolavillian Mountain Range")
            line3("immediately. ")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 92:
            Text1("Tluc: We must exterminate these false Xuirs.",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 93:
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 94:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(Tluc has disintegrated)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 95:
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 96:
            Text3("[Xuirist Cavern]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 97:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text2("Break: What is it, Omega?", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 98:
            Text2("Omega: ...", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 99:
            Text2("Omega: The Proto-Xuir is here.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 100:
            Text2("Break: What do you mean?", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 101:
            Text2("Omega: Proto-Xuir G3 N2 has been discovered.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 102:
            Text2("Break: What!?", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 103:
            Text2("Break: How could he have survived for two decades without", units.Break.Portrait,units.OmegaXuirist.Portrait)
            line2("being discovered...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 104:
            Text2("Omega: Tluc has been defeated by him, it seems the Proto-Xuir", units.Break.Portrait,units.OmegaXuirist.Portrait)
            line2("has a team of his own.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 105:
            Text2("Break: You must capture him immediately.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 106:
            Text2("Omega: They're heading to the Nation of Nation, we'll be", units.Break.Portrait,units.OmegaXuirist.Portrait)
            line2("to capture them when they pass by the cavern.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 107:
            Text2("Omega: They'll also be passing by many Xuirist villages, its", units.Break.Portrait,units.OmegaXuirist.Portrait)
            line2("possible they may not even reach us without being captured.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 108:
            Text2("Break: Do not fail.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 109:
            Text2("Break: And do not forget the past.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 110:
            Text2("Omega: ...", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex = 0
            if units.Erif in units.UnitsAlive and units.Healia in units.UnitsAlive:
                Chapter = "Chapter 17a"
            elif units.Healia in units.UnitsAlive:
                Chapter = "Chapter 17b"
            else:
                Chapter = "Chapter 17c"
                     
    elif Chapter == "Chapter 16b": #=====================Chapter16b===============================================================
        ChapterLevel = 25
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 16b]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            
            
            placeunits.PlacePlayerUnits()
            UnitsToPlace = placeunits.Chapter16aEnemies
            UnitFormation = placeunits.Chapter16aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("Tluc: Do I see what I think I see!?",units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Tluc: F- F- F- FOREIGNERS!?", units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Tluc: F- F- F- FOREIGNERS!?", units.Tluc.Portrait)
            line2("On MY Xuirist territory?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Tluc: *laughs maniacally*", units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text1("Tluc: YOU THERE!", units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text1("Tluc: FALL TO THE POWER OF THE XUIRISTS!", units.Tluc.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            
            
            UnitsToPlace = placeunits.RethgifandEgEnemies
            UnitFormation = placeunits.RethgifandEgEnemiesPlacement
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("???: Eg, do I think I see what I see?",units.Rethgif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("Eg: Likely.", units.Rethgif.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("???: This is amazing!", units.Rethgif.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("???: It's been a while since I've been in a battle.", units.Rethgif.Portrait,units.Eg.Portrait)
            line2("this big...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("???: We must fight in this battle!", units.Rethgif.Portrait,units.Eg.Portrait)
            
            units.EnemyUnitsAlive.append(units.RethgifEnemy)
            units.EnemyUnitsAlive.append(units.EgEnemy)
            CutsceneIndex += 1
            
            
            
            
        elif CutsceneIndex == 12:
            Text2("Eg: Pain...", units.Proton.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("Eg: Suffering...", units.Proton.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Eg: Destruction...", units.Proton.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("Eg: Repent...", units.Proton.Portrait,units.Eg.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text1("Proton: ...", units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 17d"
             
    elif Chapter == "Chapter 17a": #=====================Chapter17a===============================================================
        ChapterLevel = 27
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 17a]")
            line2("[Sazuki Field, Western Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: It's getting dark, we'll have to camp out",units.Proton.Portrait)
            line2("here for the night.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Proton: !?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Proton: I see someone coming towards us, prepare for",units.Proton.Portrait)
            line2("potential combat.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text1("Proton: You! Identify youself!",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("???: Well this place is quite putrid, isn't it?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("???: I am the great Elbon Rich of the Nation of",units.Proton.Portrait,units.Elbon.Portrait)
            line2("Shade.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("Proton: Nation of Shade? How did you get here?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("Elbon: I've followed your boat since it left",units.Proton.Portrait,units.Elbon.Portrait)
            line2("Bipole.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("Elbon: You see, I'm here on a mission as well, a",units.Proton.Portrait,units.Elbon.Portrait)
            line2("mission that I would argue is more important than")
            line3("yours.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text2("Elbon: I am here to retrive Healia Aid of the Territory",units.Proton.Portrait,units.Elbon.Portrait)
            line2("of Sine and to bring her back to the Bipole continent.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("Erif: Wait, she's from the Territory of Sine?",units.Erif.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Elbon: You plebians never bother remembering the details,",units.Erif.Portrait,units.Elbon.Portrait)
            line2("do you?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("Elbon: Anyways, she is to return to the Continent of Bipole",units.Proton.Portrait,units.Elbon.Portrait)
            line2("right away.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Healia: ...",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("Erif: Are we just going to ignore what was just said?",units.Proton.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("Proton: That Elbon followed our boat through an entire",units.Proton.Portrait,units.Erif.Portrait)
            line2("sea?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("Erif: No. Why have we recruited a SINE NOBLE into the Army",units.Proton.Portrait,units.Erif.Portrait)
            line2("of the *STATIC* Territory?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("Proton: In order to rebuilt our alliance with the Sine Territory,",units.Proton.Portrait,units.Erif.Portrait)
            line2("we helped fend off bandits from Sine.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Proton: In return, Healia offered to support our forces.",units.Proton.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Proton: Is there a problem with that?",units.Proton.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("Erif: Yes, there is one major problem with that.",units.Proton.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("Erif: Does anyone remember the Quad Genocide from nine years",units.Proton.Portrait,units.Erif.Portrait)
            line2("ago?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("Elbon: Oh, I do!",units.Elbon.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("Elbon: The Quad King was being arrogant and wouldn't give his",units.Elbon.Portrait,units.Erif.Portrait)
            line2("resources to support the construction of the new Shadeian")
            line3("Castle.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("Elbon: So in punishment, we, along with the help of the Sine",units.Elbon.Portrait,units.Erif.Portrait)
            line2("territory, taught the people of Quad their place by burning")
            line3("down their capital.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Elbon: Honestly, it's one of the dumbest genocides in history.",units.Elbon.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Elbon: If Quad would've just paid up, there wouldn't of been",units.Elbon.Portrait,units.Erif.Portrait)
            line2("any reason to waste resources burning down their pathetic")
            line3("capital.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("Erif: This is exactly why we shouldn't be recruiting Sine",units.Proton.Portrait,units.Erif.Portrait)
            line2("Nobles into the army.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("Erif: And that last name... \"Aid\"...",units.Proton.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text2("Erif: The House of Aid was one of the biggest supporters.",units.Proton.Portrait,units.Erif.Portrait)
            line2("of the Quad Genocide.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
            Text2("Elbon: Exactly, she should be more proud.",units.Elbon.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 34:
            Text2("Erif: We're recruiting these genocidists into our army for",units.Proton.Portrait,units.Erif.Portrait)
            line2("what? A peace treaty that will be broken the second Shade")
            line3("tells them that they're bored?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 35:
            Text2("Erif: We should be executing her, not recruiting her.",units.Proton.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 36:
            if units.Quest in units.UnitsAlive:
                Text2("Quest: I agree, we shouldn't be risking the territory's",units.Quest.Portrait,units.Erif.Portrait)
                line2("safety over an unlikely treaty.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 37:
            if units.Scien in units.UnitsAlive:
                Text2("Scien: I think she brings up a good point. If I could be",units.Scien.Portrait,units.Erif.Portrait)
                line2("executed to stop another genocide, I would gladly do it.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 38:
            if units.Romra in units.UnitsAlive:
                Text2("Romra: We're the army. We need keep our people safe,",units.Romra.Portrait,units.Erif.Portrait)
                line2("even if it means some sacrifices.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 39:
            if units.Lacirtcele in units.UnitsAlive:
                Text2("Lacirtcele: I think, we should like... execute her. She's",units.Lacirtcele.Portrait,units.Erif.Portrait)
                line2("kind of sus, bruh.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 40:
            if units.Wob in units.UnitsAlive:
                Text2("Wob: Trust me, you don't want another Quad Genocide.",units.Wob.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 41:
            if units.Bladen in units.UnitsAlive:
                Text2("Bladen: Yeah, we should probably execute her.",units.Bladen.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 42:
            if units.Wodahs in units.UnitsAlive:
                Text2("Wodahs: I'm gonna have to side with Erif on this one.",units.Wodahs.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 43:
            if units.PlayableBladeous in units.UnitsAlive:
                Text2("Bladeous: We can't risk another genocide.",units.PlayableBladeous.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 44:
            if units.Recils in units.UnitsAlive:
                Text2("Recils: Another genocide would be bad for the economy.",units.Recils.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 45:
            if units.Relaeh in units.UnitsAlive:
                Text2("Relaeh: Altar could not handle a potential genocide, we",units.Relaeh.Portrait,units.Erif.Portrait)
                line2("should execute her before she can sabotage us.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 46:
            if units.Eulb in units.UnitsAlive:
                Text2("Eulb: W... wha? Ummm... sure?",units.Eulb.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 47:
            if units.Fieht in units.UnitsAlive:
                Text2("Fieht: Definently execute her. I've seen the Quad",units.Fieht.Portrait,units.Erif.Portrait)
                line2("Ruins, and it hasn't given me a good impression.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 48:
            if units.Rethgif in units.UnitsAlive:
                Text2("Rethgif: Though I don't know anything about Bipole, this",units.Rethgif.Portrait,units.Erif.Portrait)
                line2("sure doesn't look good for Healia.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 49:
            if units.Eg in units.UnitsAlive:
                Text2("Eg: Execute.",units.Eg.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 50:
            Text2("Healia: ...",units.Healia.Portrait,units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 51:
            Text2("Proton: Has anyone considered the fact that killing",units.Healia.Portrait,units.Proton.Portrait)
            line2("a noble could trigger a war?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 52:
            Text2("Erif: We could defeat them in war, but we can't defeat",units.Erif.Portrait,units.Proton.Portrait)
            line2("them if they keep infiltrating our army.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 53:
            Text2("Erif: And she also deserves an execution for her involvement",units.Erif.Portrait,units.Proton.Portrait)
            line2("in the Quad Genocide.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 54:
            Text2("Proton: ...",units.Erif.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 55:
            Text2("Erif: Without any objections, it's time to execute her.",units.Erif.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 56:
            Text3("[Erif stabs Healia]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 57:
            Text3("[Healia has died]")
            print("UnitsAlive:", units.UnitsAlive)
            units.UnitsAlive.remove(units.Healia)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 58:
            Text3("[Erif has leveled up!]")
            select.InstantLevelUp(units.Erif,3)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 59:
            Text1("Elbon: Well that was exciting.",units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 60:
            Text1("Elbon: I shall now leave.",units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 61:
            Text2("Erif: Actually, you won't.",units.Elbon.Portrait, units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 62:
            Text2("Elbon: Hmmm? And why might that be?",units.Elbon.Portrait, units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 63:
            Text2("Erif: Because of this.",units.Elbon.Portrait, units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 64:
            Text3("[Erif stabs Elbon]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 65:
            Text2("Elbon: Y... you...",units.Elbon.Portrait, units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 66:
            Text2("Elbon: Bi... pole... scum...",units.Elbon.Portrait, units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 67:
            Text3("[Elbon has died]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 68:
            Text1("Erif: ...", units.Erif.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 69:
            Text2("Proton: Was that necessary?",units.Erif.Portrait, units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 70:
            Text2("Erif: Yes.",units.Erif.Portrait, units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 71:
            Text2("Erif: They can assume that he died in the sea, I'm suprised",units.Erif.Portrait, units.Proton.Portrait)
            line2("a noble like him even made it here alive.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 69:
            Text2("Proton: ...",units.Erif.Portrait, units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 72:
            Text3("???: ...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 73:
            Text1("Proton: Did somebody else come here with Elbon?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 74:
            Text2("???: No.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 75:
            Text2("Proton: Who's there!?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 76:
            Text2("???: I am B, a traveler of worlds.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 77:
            Text2("Proton: ?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 78:
            Text2("B: This timeline, it's started to diverge very far...",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 79:
            Text2("Proton: What do you mean?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 80:
            Text2("B: The world we live in is made up of alternate and parallel",units.Proton.Portrait, units.B.Portrait)
            line2("universes, also known as timelines.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 81:
            Text2("B: Every decision you've ever made in your life, big or small,",units.Proton.Portrait, units.B.Portrait)
            line2("has led to a divergence in the timelines.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 82:
            Text2("Proton: What are you trying to say?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 83:
            Text2("B: What I'm trying to say is that this timeline has started to",units.Proton.Portrait, units.B.Portrait)
            line2("diverge farther than most.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 84:
            Text2("B: The collective entity of all of our timelines is called a",units.Proton.Portrait, units.B.Portrait)
            line2("time cluster, and you could say our time cluster has a")
            line3("\"desired\" path.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 85:
            Text2("B: You see, we live in a timeline where the Neville Prophecy was",units.Proton.Portrait, units.B.Portrait)
            line2("implemented.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 86:
            Text2("B: A safety mechanism created by the Nexters in order to keep society",units.Proton.Portrait, units.B.Portrait)
            line2("from destroying itself again.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 87:
            Text2("B: If our timeline diverges too far from the prophecy's desired \"canon\",",units.Proton.Portrait, units.B.Portrait)
            line2("we could be in severe danger.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 88:
            Text2("Proton: What kind of danger?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 89:
            Text2("B: The unleashing of the Xuir Wrath and the One Who Consumes All.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 90:
            Text2("Proton: Why would a safety mechanic be made to endanger us?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 91:
            Text2("B: It is to prevent an event such as the Finis Event from every happening again,",units.Proton.Portrait, units.B.Portrait)
            line2("though the prophecy has become a little more strict following the temporary")
            line3("release of the Xuir Wrath due to Nevillion Omega.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 92:
            Text2("Proton: The \"Xuir Wrath\", don' tell me...",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 93:
            Text2("B: Yes, the Shadow Realm has made many attempts to recreate the True Xuir by",units.Proton.Portrait, units.B.Portrait)
            line2("using the Neville Prophecy, which contains an entity known as the Xuir Wrath.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 94:
            Text2("B: Though all attempts have failed.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 95:
            Text2("Proton: How do you know all of this.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 96:
            Text2("B: I've been afflicted by something called the Warp Time by The Link.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 97:
            Text2("B: Every 18 months, I am sent to another timeline in a different year.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 98:
            Text2("B: Through my travels, I have met The Link multiple times and have learned",units.Proton.Portrait, units.B.Portrait)
            line2("the ways in which this world works.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 99:
            Text2("Proton: So you've traveled through timelines and you're talking about the",units.Proton.Portrait, units.B.Portrait)
            line2("danger that we may be in, but how does this directly pertain to us?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 100:
            Text2("Proton: Are we the cause of this timeline's diversion?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 101:
            Text2("B: It seems so, though it may be the workings of an higher entity.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 102:
            Text2("B: I would like to accompany you on your journey to retrieve the Holy Itucher,",units.Proton.Portrait, units.B.Portrait)
            line2("perphaps then I would take note of the effects of the diversion.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 103:
            Text2("Proton: But aren't we in danger?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 104:
            Text2("B: No, not exactly.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 105:
            Text2("B: This timeline has not diverged enough to awaken the Xuir Wrath, but it has",units.Proton.Portrait, units.B.Portrait)
            line2("diverged further than most other timelines that include these events")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 106:
            Text2("Proton: ...",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 107:
            Text2("B: Do not worry, I have seen much worse timelines. Honestly, it was refreshing",units.Proton.Portrait, units.B.Portrait)
            line2("to see that Elbon go away for once.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 108:
            Text2("Proton: Wait, you've already helped us before?",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 109:
            Text2("B: Not exactly \"helped\", more like observed.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 110:
            Text2("B: But I've also fought against you many times.",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 111:
            Text2("Proton: ...",units.Proton.Portrait, units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 112:
                Text3("[Recruit B]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 113:
            if Qinput == True:
                Text2("B: This should be interesting...",units.Proton.Portrait, units.B.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("B: It seems I'll have to observe for this timeline...",units.Proton.Portrait, units.B.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 114:
            if Qinput == True:
                Text3("[B has joined your party]")
                units.UnitsAlive.append(units.B)
                units.UnitsRecruited.append(units.B)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                CutsceneIndex += 1
                ClearInputs()
                Cutscene()
        elif CutsceneIndex == 115:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[The next day...]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 116:
            Text1("Proton: Hmmm? What's that noise?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 117:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 118:
            Text1("Proton: !?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 119:
            Text1("Proton: Everyone! We're surrounded by Xuirists!",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 120:
            Text1("Proton: Prepare for battle!",units.Proton.Portrait)
            CutsceneIndex += 1
            
            UnitsToPlace = placeunits.Chapter17aEnemies
            UnitFormation = placeunits.Chapter17aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 121:
            Text1("Proton: We've managed to survive the attack, but it seems",units.Proton.Portrait)
            line2("like the Xuirists will keep hunting us while we're in")
            line3("Nolavillia.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 122:
            Text1("Proton: We should head to Nation as quickly as possible.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 123:
            Text3("???: Hey, you there!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 124:
            Text1("Proton: ?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 125:
            Text2("???: Could you open the cage I'm stuck in?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 126:
            Text2("Proton: Why are you in that cage?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 127:
            Text2("???: The Xuirists captured me after I escaped from the",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("Shadow Realm.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 128:
            Text2("???: I think they were going to sacrifice me.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 129:
            Text2("Proton: The Shadow Realm?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 130:
            Text2("???: Yeah, I'm something called a \"Proto-Xuir\", a failed",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("clone of some dimensional called the \"True Xuir\".")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 131:
            Text2("Proton: You're a Xuir?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 132:
            Text2("???: Yeah I just said that.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 133:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 134:
            Text3("[Proton opens the cage]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 135:
            Text2("???: Thanks.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 136:
            Text2("???: I'd stick around, but there's something I have",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("to do.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 137:
            Text2("???: There are some other Proto-Xuirs that escaped with me,",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("and one of them was captured by the Xuirists.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 138:
            Text2("Proton: There's other Proto-Xuirs?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 139:
            Text2("???: Yeah, it's not like I'm the only one.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 140:
            Text2("Proton: Nolavillia is truly a strange place, to think",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("that there would be so many other Xuirs...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 141:
            Text2("???: Huh?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 142:
            Text2("Proton: Sorry, this is my first time in Nolavillia since",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("I escaped from the Shadow Realm 20 years ago.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 143:
            Text2("???: Are you also a Proto-Xuir?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 144:
            Text2("Proton: Yes.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 145:
            Text2("???: 20 years ago... are you Xuirond?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 146:
            Text2("Proton: I don't this so.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 147:
            Text2("Proton: My engraving says G3 N2.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 148:
            Text2("???: Ah, so you are Xuirond.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 149:
            Text2("???: We thought you died years ago.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 150:
            Text2("???: Of course, we don't really remember you since",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("we were still young.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 151:
            Text2("???: I'm Xuirventh: Generation 3 Number 7.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 152:
            Text2("Xuirventh: We weren't given names so, Xuirventh is",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("just a name I made up a few years ago.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 153:
            Text2("Xuirventh: So, what do you go by these days, Xuirond?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 154:
            Text2("Proton: Proton.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 155:
            Text2("Xuirventh: Fancy name, doesn't have to do with numbers",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("either.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 156:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 157:
            Text2("Xuirventh: You said you left, Nolavillia, but why did you",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("come back.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 158:
            Text2("Xuirventh: Two decades later seems like a pretty strange time",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("to return.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 159:
            Text2("Proton: I'm here to stop the Shadow Realm Research Center.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 160:
            Text2("Xuirventh: Huh?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 161:
            Text2("Proton: The Research Center has recently obtained a powerful item",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("called the Holy Itucher.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 162:
            Text2("Proton: With such power, they could easily end the world.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 163:
            Text2("Xuirventh: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 164:
            Text2("Xuirventh: If you're heading to the Shadow Realm, you'll need to",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("go to the Nation of Nation.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 165:
            Text2("Xuirventh: But on you're way, you'll likely pass by the Xuirist",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("Cavern.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 166:
            Text2("Xuirventh: If you want to team up and help me free Xuirfth,",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("I'll probably be able to convince them to help you stop")
            line3("the Shadow Realm.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 167:
            Text2("Xuirventh: You'll probably have to fight those Xuirists anyways.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 168:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 169:
                Text3("[Recruit Xuirventh]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 170:
            if Qinput == True:
                Text2("Xuirventh: Time to stop some Xuirists.",units.Proton.Portrait, units.Xuirventh.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Xuirventh: Well, I've gotta go fight some Xuirists.",units.Proton.Portrait, units.Xuirventh.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 171:
            if Qinput == True:
                Text3("[Xuirventh has joined your party]")
                units.UnitsAlive.append(units.Xuirventh)
                units.UnitsRecruited.append(units.Xuirventh)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                CutsceneIndex += 1
                ClearInputs()
                Cutscene()
        elif CutsceneIndex < 185 and units.Eg in units.UnitsAlive and units.Rethgif in units.UnitsAlive:
            if CutsceneIndex == 172:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 173:
                Text2("Rethgif: It seems that the Xuirists are now hunting",units.Rethgif.Portrait,units.Eg.Portrait)
                line2("after us.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 174:
                Text2("Rethgif: The others seem disturbed, but more battling",units.Rethgif.Portrait,units.Eg.Portrait)
                line2("is a win for me.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 175:
                Text2("Rethgif: I SHALL NO LONGER BE BORED!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 176:
                Text2("Eg: Affirmative.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 177:
                Text2("Rethgif: XUIRISTS! I CHALLENGE YOU ALL TO A LIFE-LONG BATTLE!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 178:
                Text2("Rethgif: REEEEEEEEEEEEEEEEEEEEEEE!!!!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 179:
                Text2("Eg: ...",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 180:
                Text2("Rethgif: ...",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 181:
                Text2("Rethgif: You have any laundry cleaner on you?",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 182:
                Text2("Eg: Positive.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 183:
                Text2("Rethgif: Good.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 184:
                Text3("[Rethgif and Eg leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Rethgif,3)
                select.InstantLevelUp(units.Eg,3)
                
        elif CutsceneIndex < 185:
            CutsceneIndex = 185
            Cutscene()
        elif CutsceneIndex < 196 and units.Lacirtcele in units.UnitsAlive and units.Bladen in units.UnitsAlive:
            if CutsceneIndex == 185:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 186:
                Text2("Lacirtcele: Yo... this place is like... weird...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("after us.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 187:
                Text2("Lacirtcele: These vibes ain't good... we shoud probably",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("get off of this continent...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 188:
                Text2("Bladen: If we leave, the world will probably end.",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 189:
                Text2("Bladen: I don't want to be here any more than you do, but if",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("we're the only ones who can save the world, we kind of need to")
                line3("be here.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 190:
                Text2("Lacirtcele: ...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 191:
                Text2("Bladen: You're an elite warrior, aren't you? Shouldn't you be",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("used to this?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 192:
                Text2("Bladen: I've run away from protecting this world for most of my",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("life but now that EOS member is telling me he's scared?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 193:
                Text2("Lacirtcele: ...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 194:
                Text2("Bladen: You're pathetic.",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 195:
                Text3("[Lacirtcele and Bladen leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Lacirtcele,3)
                select.InstantLevelUp(units.Bladen,3)
                
        elif CutsceneIndex < 196:
            CutsceneIndex = 196
            Cutscene()
        elif CutsceneIndex < 207 and units.Proton in units.UnitsAlive and units.Scien in units.UnitsAlive:
            if CutsceneIndex == 196:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 197:
                Text2("Scien: ...",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 198:
                Text2("Proton: Scien, are you alright?",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 199:
                Text2("Scien: The Nation of Nation, the Altar must still stand...",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 200:
                Text2("Proton: ?",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 201:
                Text2("Scien: That person, Xuirventh, they said they escaped from",units.Scien.Portrait,units.Proton.Portrait)
                line2("the Shadow Realm.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 202:
                Text2("Scien: The only safe place in Nolavillia to hide from the Shadow",units.Scien.Portrait,units.Proton.Portrait)
                line2("Realm is in Nation.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 203:
                Text2("Scien: ...", units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 204:
                Text2("Scien: We need to keep going.",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 205:
                Text2("Scien: We must retrieve the Itucher before they can destroy Nation and",units.Scien.Portrait,units.Proton.Portrait)
                line2("the rest of the world.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 206:
                Text3("[Scien and Proton leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Scien,3)
                select.InstantLevelUp(units.Proton,3)
                
        elif CutsceneIndex < 207:
            CutsceneIndex = 207
            Cutscene()
        elif CutsceneIndex == 207:
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 208:
            Text3("[Xuirist Cavern]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 209:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text1("Omega: ....", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 210:
            Text2("Break: Omega, has the dispatch responded yet?", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 211:
            Text2("Omega: No, sir.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 212:
            Text2("Omega: It is likely that they have been defeated.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 213:
            Text2("Break: ...", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 214:
            Text2("Break: Omega, you do realize that failure will not be", units.Break.Portrait,units.OmegaXuirist.Portrait)
            line2("accepted.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 215:
            Text2("Omega: Yes, yes I do.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 216:
            Text2("Break: If you fail, I will destroy them.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 217:
            Text2("Omega: ...", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 218:
            Text2("Break: Do not fail.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            Chapter = "Chapter 18a"
            CutsceneIndex = 0
            
    elif Chapter == "Chapter 17b": #=====================Chapter17b===============================================================
        ChapterLevel = 27
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 17b]")
            line2("[Sazuki Field, Western Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: It's getting dark, we'll have to camp out",units.Proton.Portrait)
            line2("here for the night.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Proton: !?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Proton: I see someone coming towards us, prepare for",units.Proton.Portrait)
            line2("potential combat.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text1("Proton: You! Identify youself!",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("???: Well this place is quite putrid, isn't it?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("???: I am the great Elbon Rich of the Nation of",units.Proton.Portrait,units.Elbon.Portrait)
            line2("Shade.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("Proton: Nation of Shade? How did you get here?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("Elbon: I've followed your boat since it left",units.Proton.Portrait,units.Elbon.Portrait)
            line2("Bipole.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("Elbon: You see, I'm here on a mission as well, a",units.Proton.Portrait,units.Elbon.Portrait)
            line2("mission that I would argue is more important than")
            line3("yours.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text2("Elbon: I am here to retrive Healia Aid of the Territory",units.Proton.Portrait,units.Elbon.Portrait)
            line2("of Sine and to bring her back to the Bipole continent.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("Elbon: Uhhh.... something about an arranged marriage?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Healia: What!?",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("Elbon: Look, I couldn't care less of what it is but I'm getting",units.Healia.Portrait,units.Elbon.Portrait)
            line2("paid to do this.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Healia: What are my parents trying to do this time?",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text3("(Elbon hands Healia a letter)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("Healia: Wait what is this?",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("Healia: \"As you know, our house is declining in power and we",units.Healia.Portrait,units.Elbon.Portrait)
            line2("must restore it or we will lose our status. Luckly for us, we")
            line3("have found a Shadeian noble who is willing to help us...\"")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("Healia: \"Through this arranged marriage, we will hopefully return",units.Healia.Portrait,units.Elbon.Portrait)
            line2("to our family's former glory\".")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Healia: ...",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Elbon: You must return immediately so I can get paid.",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("Healia: What am I even supposed to do?",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("Elbon: Mabye you should return so I can get paid.",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("Elbon: I do not want to spend a second more on this horrid",units.Healia.Portrait,units.Elbon.Portrait)
            line2("continent.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("Healia: ...",units.Healia.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("Proton: She's busy helping us save to world, could we deal with",units.Proton.Portrait,units.Elbon.Portrait)
            line2("this later?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Elbon: Will I get paid to wait?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Proton: You won't get paid if the world ends.",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("Elbon: Well then, I suppose I must \"save the world\" for whatever so",units.Proton.Portrait,units.Elbon.Portrait)
            line2("I can get paid the money that I deserve.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text3("[Elbon joins your party]")
            units.UnitsAlive.append(units.Elbon)
            units.UnitsRecruited.append(units.Elbon)
            CutsceneIndex = 115
            
        elif CutsceneIndex == 115:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[The next day...]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 116:
            Text1("Proton: Hmmm? What's that noise?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 117:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 118:
            Text1("Proton: !?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 119:
            Text1("Proton: Everyone! We're surrounded by Xuirists!",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 120:
            Text1("Proton: Prepare for battle!",units.Proton.Portrait)
            CutsceneIndex += 1
            
            UnitsToPlace = placeunits.Chapter17aEnemies
            UnitFormation = placeunits.Chapter17aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 121:
            Text1("Proton: We've managed to survive the attack, but it seems",units.Proton.Portrait)
            line2("like the Xuirists will keep hunting us while we're in")
            line3("Nolavillia.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 122:
            Text1("Proton: We should head to Nation as quickly as possible.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 123:
            Text3("???: Hey, you there!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 124:
            Text1("Proton: ?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 125:
            Text2("???: Could you open the cage I'm stuck in?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 126:
            Text2("Proton: Why are you in that cage?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 127:
            Text2("???: The Xuirists captured me after I escaped from the",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("Shadow Realm.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 128:
            Text2("???: I think they were going to sacrifice me.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 129:
            Text2("Proton: The Shadow Realm?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 130:
            Text2("???: Yeah, I'm something called a \"Proto-Xuir\", a failed",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("clone of some dimensional called the \"True Xuir\".")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 131:
            Text2("Proton: You're a Xuir?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 132:
            Text2("???: Yeah I just said that.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 133:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 134:
            Text3("[Proton opens the cage]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 135:
            Text2("???: Thanks.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 136:
            Text2("???: I'd stick around, but there's something I have",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("to do.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 137:
            Text2("???: There are some other Proto-Xuirs that escaped with me,",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("and one of them was captured by the Xuirists.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 138:
            Text2("Proton: There's other Proto-Xuirs?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 139:
            Text2("???: Yeah, it's not like I'm the only one.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 140:
            Text2("Proton: Nolavillia is truly a strange place, to think",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("that there would be so many other Xuirs...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 141:
            Text2("???: Huh?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 142:
            Text2("Proton: Sorry, this is my first time in Nolavillia since",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("I escaped from the Shadow Realm 20 years ago.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 143:
            Text2("???: Are you also a Proto-Xuir?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 144:
            Text2("Proton: Yes.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 145:
            Text2("???: 20 years ago... are you Xuirond?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 146:
            Text2("Proton: I don't this so.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 147:
            Text2("Proton: My engraving says G3 N2.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 148:
            Text2("???: Ah, so you are Xuirond.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 149:
            Text2("???: We thought you died years ago.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 150:
            Text2("???: Of course, we don't really remember you since",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("we were still young.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 151:
            Text2("???: I'm Xuirventh: Generation 3 Number 7.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 152:
            Text2("Xuirventh: We weren't given names so, Xuirventh is",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("just a name I made up a few years ago.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 153:
            Text2("Xuirventh: So, what do you go by these days, Xuirond?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 154:
            Text2("Proton: Proton.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 155:
            Text2("Xuirventh: Fancy name, doesn't have to do with numbers",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("either.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 156:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 157:
            Text2("Xuirventh: You said you left, Nolavillia, but why did you",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("come back.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 158:
            Text2("Xuirventh: Two decades later seems like a pretty strange time",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("to return.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 159:
            Text2("Proton: I'm here to stop the Shadow Realm Research Center.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 160:
            Text2("Xuirventh: Huh?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 161:
            Text2("Proton: The Research Center has recently obtained a powerful item",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("called the Holy Itucher.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 162:
            Text2("Proton: With such power, they could easily end the world.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 163:
            Text2("Xuirventh: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 164:
            Text2("Xuirventh: If you're heading to the Shadow Realm, you'll need to",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("go to the Nation of Nation.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 165:
            Text2("Xuirventh: But on you're way, you'll likely pass by the Xuirist",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("Cavern.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 166:
            Text2("Xuirventh: If you want to team up and help me free Xuirfth,",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("I'll probably be able to convince them to help you stop")
            line3("the Shadow Realm.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 167:
            Text2("Xuirventh: You'll probably have to fight those Xuirists anyways.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 168:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 169:
                Text3("[Recruit Xuirventh]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 170:
            if Qinput == True:
                Text2("Xuirventh: Time to stop some Xuirists.",units.Proton.Portrait, units.Xuirventh.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Xuirventh: Well, I've gotta go fight some Xuirists.",units.Proton.Portrait, units.Xuirventh.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 171:
            if Qinput == True:
                Text3("[Xuirventh has joined your party]")
                units.UnitsAlive.append(units.Xuirventh)
                units.UnitsRecruited.append(units.Xuirventh)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                CutsceneIndex += 1
                ClearInputs()
                Cutscene()
        elif CutsceneIndex < 185 and units.Eg in units.UnitsAlive and units.Rethgif in units.UnitsAlive:
            if CutsceneIndex == 172:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 173:
                Text2("Rethgif: It seems that the Xuirists are now hunting",units.Rethgif.Portrait,units.Eg.Portrait)
                line2("after us.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 174:
                Text2("Rethgif: The others seem disturbed, but more battling",units.Rethgif.Portrait,units.Eg.Portrait)
                line2("is a win for me.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 175:
                Text2("Rethgif: I SHALL NO LONGER BE BORED!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 176:
                Text2("Eg: Affirmative.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 177:
                Text2("Rethgif: XUIRISTS! I CHALLENGE YOU ALL TO A LIFE-LONG BATTLE!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 178:
                Text2("Rethgif: REEEEEEEEEEEEEEEEEEEEEEE!!!!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 179:
                Text2("Eg: ...",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 180:
                Text2("Rethgif: ...",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 181:
                Text2("Rethgif: You have any laundry cleaner on you?",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 182:
                Text2("Eg: Positive.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 183:
                Text2("Rethgif: Good.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 184:
                Text3("[Rethgif and Eg leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Rethgif,3)
                select.InstantLevelUp(units.Eg,3)
                
        elif CutsceneIndex < 185:
            CutsceneIndex = 185
            Cutscene()
        elif CutsceneIndex < 196 and units.Lacirtcele in units.UnitsAlive and units.Bladen in units.UnitsAlive:
            if CutsceneIndex == 185:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 186:
                Text2("Lacirtcele: Yo... this place is like... weird...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("after us.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 187:
                Text2("Lacirtcele: These vibes ain't good... we shoud probably",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("get off of this continent...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 188:
                Text2("Bladen: If we leave, the world will probably end.",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 189:
                Text2("Bladen: I don't want to be here any more than you do, but if",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("we're the only ones who can save the world, we kind of need to")
                line3("be here.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 190:
                Text2("Lacirtcele: ...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 191:
                Text2("Bladen: You're an elite warrior, aren't you? Shouldn't you be",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("used to this?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 192:
                Text2("Bladen: I've run away from protecting this world for most of my",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("life but now that EOS member is telling me he's scared?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 193:
                Text2("Lacirtcele: ...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 194:
                Text2("Bladen: You're pathetic.",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 195:
                Text3("[Lacirtcele and Bladen leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Lacirtcele,3)
                select.InstantLevelUp(units.Bladen,3)
                
        elif CutsceneIndex < 196:
            CutsceneIndex = 196
            Cutscene()
        elif CutsceneIndex < 207 and units.Proton in units.UnitsAlive and units.Scien in units.UnitsAlive:
            if CutsceneIndex == 196:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 197:
                Text2("Scien: ...",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 198:
                Text2("Proton: Scien, are you alright?",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 199:
                Text2("Scien: The Nation of Nation, the Altar must still stand...",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 200:
                Text2("Proton: ?",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 201:
                Text2("Scien: That person, Xuirventh, they said they escaped from",units.Scien.Portrait,units.Proton.Portrait)
                line2("the Shadow Realm.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 202:
                Text2("Scien: The only safe place in Nolavillia to hide from the Shadow",units.Scien.Portrait,units.Proton.Portrait)
                line2("Realm is in Nation.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 203:
                Text2("Scien: ...", units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 204:
                Text2("Scien: We need to keep going.",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 205:
                Text2("Scien: We must retrieve the Itucher before they can destroy Nation and",units.Scien.Portrait,units.Proton.Portrait)
                line2("the rest of the world.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 206:
                Text3("[Scien and Proton leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Scien,3)
                select.InstantLevelUp(units.Proton,3)
                
        elif CutsceneIndex < 207:
            CutsceneIndex = 207
            Cutscene()
        elif CutsceneIndex == 207:
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 208:
            Text3("[Xuirist Cavern]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 209:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text1("Omega: ....", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 210:
            Text2("Break: Omega, has the dispatch responded yet?", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 211:
            Text2("Omega: No, sir.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 212:
            Text2("Omega: It is likely that they have been defeated.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 213:
            Text2("Break: ...", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 214:
            Text2("Break: Omega, you do realize that failure will not be", units.Break.Portrait,units.OmegaXuirist.Portrait)
            line2("accepted.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 215:
            Text2("Omega: Yes, yes I do.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 216:
            Text2("Break: If you fail, I will destroy them.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 217:
            Text2("Omega: ...", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 218:
            Text2("Break: Do not fail.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            Chapter = "Chapter 18a"
            CutsceneIndex = 0
              
    elif Chapter == "Chapter 17c": #=====================Chapter17c===============================================================
        ChapterLevel = 27
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 17c]")
            line2("[Sazuki Field, Western Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: It's getting dark, we'll have to camp out",units.Proton.Portrait)
            line2("here for the night.")
            CutsceneIndex = 115
            
        elif CutsceneIndex == 115:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[The next day...]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 116:
            Text1("Proton: Hmmm? What's that noise?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 117:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 118:
            Text1("Proton: !?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 119:
            Text1("Proton: Everyone! We're surrounded by Xuirists!",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 120:
            Text1("Proton: Prepare for battle!",units.Proton.Portrait)
            CutsceneIndex += 1
            
            UnitsToPlace = placeunits.Chapter17aEnemies
            UnitFormation = placeunits.Chapter17aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 121:
            Text1("Proton: We've managed to survive the attack, but it seems",units.Proton.Portrait)
            line2("like the Xuirists will keep hunting us while we're in")
            line3("Nolavillia.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 122:
            Text1("Proton: We should head to Nation as quickly as possible.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 123:
            Text3("???: Hey, you there!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 124:
            Text1("Proton: ?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 125:
            Text2("???: Could you open the cage I'm stuck in?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 126:
            Text2("Proton: Why are you in that cage?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 127:
            Text2("???: The Xuirists captured me after I escaped from the",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("Shadow Realm.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 128:
            Text2("???: I think they were going to sacrifice me.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 129:
            Text2("Proton: The Shadow Realm?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 130:
            Text2("???: Yeah, I'm something called a \"Proto-Xuir\", a failed",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("clone of some dimensional called the \"True Xuir\".")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 131:
            Text2("Proton: You're a Xuir?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 132:
            Text2("???: Yeah I just said that.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 133:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 134:
            Text3("[Proton opens the cage]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 135:
            Text2("???: Thanks.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 136:
            Text2("???: I'd stick around, but there's something I have",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("to do.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 137:
            Text2("???: There are some other Proto-Xuirs that escaped with me,",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("and one of them was captured by the Xuirists.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 138:
            Text2("Proton: There's other Proto-Xuirs?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 139:
            Text2("???: Yeah, it's not like I'm the only one.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 140:
            Text2("Proton: Nolavillia is truly a strange place, to think",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("that there would be so many other Xuirs...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 141:
            Text2("???: Huh?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 142:
            Text2("Proton: Sorry, this is my first time in Nolavillia since",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("I escaped from the Shadow Realm 20 years ago.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 143:
            Text2("???: Are you also a Proto-Xuir?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 144:
            Text2("Proton: Yes.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 145:
            Text2("???: 20 years ago... are you Xuirond?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 146:
            Text2("Proton: I don't this so.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 147:
            Text2("Proton: My engraving says G3 N2.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 148:
            Text2("???: Ah, so you are Xuirond.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 149:
            Text2("???: We thought you died years ago.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 150:
            Text2("???: Of course, we don't really remember you since",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("we were still young.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 151:
            Text2("???: I'm Xuirventh: Generation 3 Number 7.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 152:
            Text2("Xuirventh: We weren't given names so, Xuirventh is",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("just a name I made up a few years ago.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 153:
            Text2("Xuirventh: So, what do you go by these days, Xuirond?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 154:
            Text2("Proton: Proton.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 155:
            Text2("Xuirventh: Fancy name, doesn't have to do with numbers",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("either.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 156:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 157:
            Text2("Xuirventh: You said you left, Nolavillia, but why did you",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("come back.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 158:
            Text2("Xuirventh: Two decades later seems like a pretty strange time",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("to return.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 159:
            Text2("Proton: I'm here to stop the Shadow Realm Research Center.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 160:
            Text2("Xuirventh: Huh?",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 161:
            Text2("Proton: The Research Center has recently obtained a powerful item",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("called the Holy Itucher.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 162:
            Text2("Proton: With such power, they could easily end the world.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 163:
            Text2("Xuirventh: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 164:
            Text2("Xuirventh: If you're heading to the Shadow Realm, you'll need to",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("go to the Nation of Nation.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 165:
            Text2("Xuirventh: But on you're way, you'll likely pass by the Xuirist",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("Cavern.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 166:
            Text2("Xuirventh: If you want to team up and help me free Xuirfth,",units.Proton.Portrait,units.Xuirventh.Portrait)
            line2("I'll probably be able to convince them to help you stop")
            line3("the Shadow Realm.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 167:
            Text2("Xuirventh: You'll probably have to fight those Xuirists anyways.",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 168:
            Text2("Proton: ...",units.Proton.Portrait,units.Xuirventh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 169:
                Text3("[Recruit Xuirventh]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 170:
            if Qinput == True:
                Text2("Xuirventh: Time to stop some Xuirists.",units.Proton.Portrait, units.Xuirventh.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Xuirventh: Well, I've gotta go fight some Xuirists.",units.Proton.Portrait, units.Xuirventh.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 171:
            if Qinput == True:
                Text3("[Xuirventh has joined your party]")
                units.UnitsAlive.append(units.Xuirventh)
                units.UnitsRecruited.append(units.Xuirventh)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                CutsceneIndex += 1
                ClearInputs()
                Cutscene()
        elif CutsceneIndex < 185 and units.Eg in units.UnitsAlive and units.Rethgif in units.UnitsAlive:
            if CutsceneIndex == 172:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 173:
                Text2("Rethgif: It seems that the Xuirists are now hunting",units.Rethgif.Portrait,units.Eg.Portrait)
                line2("after us.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 174:
                Text2("Rethgif: The others seem disturbed, but more battling",units.Rethgif.Portrait,units.Eg.Portrait)
                line2("is a win for me.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 175:
                Text2("Rethgif: I SHALL NO LONGER BE BORED!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 176:
                Text2("Eg: Affirmative.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 177:
                Text2("Rethgif: XUIRISTS! I CHALLENGE YOU ALL TO A LIFE-LONG BATTLE!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 178:
                Text2("Rethgif: REEEEEEEEEEEEEEEEEEEEEEE!!!!!!",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 179:
                Text2("Eg: ...",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 180:
                Text2("Rethgif: ...",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 181:
                Text2("Rethgif: You have any laundry cleaner on you?",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 182:
                Text2("Eg: Positive.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 183:
                Text2("Rethgif: Good.",units.Rethgif.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 184:
                Text3("[Rethgif and Eg leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Rethgif,3)
                select.InstantLevelUp(units.Eg,3)
                
        elif CutsceneIndex < 185:
            CutsceneIndex = 185
            Cutscene()
        elif CutsceneIndex < 196 and units.Lacirtcele in units.UnitsAlive and units.Bladen in units.UnitsAlive:
            if CutsceneIndex == 185:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 186:
                Text2("Lacirtcele: Yo... this place is like... weird...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("after us.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 187:
                Text2("Lacirtcele: These vibes ain't good... we shoud probably",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("get off of this continent...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 188:
                Text2("Bladen: If we leave, the world will probably end.",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 189:
                Text2("Bladen: I don't want to be here any more than you do, but if",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("we're the only ones who can save the world, we kind of need to")
                line3("be here.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 190:
                Text2("Lacirtcele: ...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 191:
                Text2("Bladen: You're an elite warrior, aren't you? Shouldn't you be",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("used to this?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 192:
                Text2("Bladen: I've run away from protecting this world for most of my",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                line2("life but now that EOS member is telling me he's scared?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 193:
                Text2("Lacirtcele: ...",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 194:
                Text2("Bladen: You're pathetic.",units.Lacirtcele.Portrait,units.Bladen.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 195:
                Text3("[Lacirtcele and Bladen leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Lacirtcele,3)
                select.InstantLevelUp(units.Bladen,3)
                
        elif CutsceneIndex < 196:
            CutsceneIndex = 196
            Cutscene()
        elif CutsceneIndex < 207 and units.Proton in units.UnitsAlive and units.Scien in units.UnitsAlive:
            if CutsceneIndex == 196:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 197:
                Text2("Scien: ...",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 198:
                Text2("Proton: Scien, are you alright?",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 199:
                Text2("Scien: The Nation of Nation, the Altar must still stand...",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 200:
                Text2("Proton: ?",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 201:
                Text2("Scien: That person, Xuirventh, they said they escaped from",units.Scien.Portrait,units.Proton.Portrait)
                line2("the Shadow Realm.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 202:
                Text2("Scien: The only safe place in Nolavillia to hide from the Shadow",units.Scien.Portrait,units.Proton.Portrait)
                line2("Realm is in Nation.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 203:
                Text2("Scien: ...", units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 204:
                Text2("Scien: We need to keep going.",units.Scien.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 205:
                Text2("Scien: We must retrieve the Itucher before they can destroy Nation and",units.Scien.Portrait,units.Proton.Portrait)
                line2("the rest of the world.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 206:
                Text3("[Scien and Proton leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Scien,3)
                select.InstantLevelUp(units.Proton,3)
                
        elif CutsceneIndex < 207:
            CutsceneIndex = 207
            Cutscene()
        elif CutsceneIndex == 207:
            Text3("...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 208:
            Text3("[Xuirist Cavern]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 209:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text1("Omega: ....", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 210:
            Text2("Break: Omega, has the dispatch responded yet?", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 211:
            Text2("Omega: No, sir.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 212:
            Text2("Omega: It is likely that they have been defeated.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 213:
            Text2("Break: ...", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 214:
            Text2("Break: Omega, you do realize that failure will not be", units.Break.Portrait,units.OmegaXuirist.Portrait)
            line2("accepted.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 215:
            Text2("Omega: Yes, yes I do.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 216:
            Text2("Break: If you fail, I will destroy them.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 217:
            Text2("Omega: ...", units.Break.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 218:
            Text2("Break: Do not fail.", units.Break.Portrait,units.OmegaXuirist.Portrait)
            Chapter = "Chapter 18a"
            CutsceneIndex = 0
              
    elif Chapter == "Chapter 17d": #=====================Chapter17d===============================================================
        ChapterLevel = 81
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 17d]")
            line2("[Sazuki Field, Western Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark green")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text2("???: Proton...",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text2("???: I'm to disappointed in you...",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("???: To think that there would be a timeline where you would",units.Proton.Portrait,units.B.Portrait)
            line2("do this...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text2("???: But it isn't you, is it?",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("???: Yes, it's someone else...",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2(("???: Someone like " + username.UserName + ", perhaps..."),units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("???: Huh, why are you looking at me like that?",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("???: Something I said?",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("???: ...",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("???: Well, goodbye.",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
            UnitsToPlace = placeunits.Chapter17dEnemies
            UnitFormation = placeunits.Chapter17dPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 12:
            Text2("B: Hmmm...",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("B: So that's how it is...",units.Proton.Portrait,units.B.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text3("[B disappears]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 18b"
            
    elif Chapter == "Chapter 18a": #=====================Chapter18a===============================================================
        ChapterLevel = 30
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 18a]")
            line2("[PSA Conventions Zone, Central Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Proton: It seems we must go through this Xuirist",units.Proton.Portrait)
            line2("camp to proceed.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Proton: Prepare for battle!",units.Proton.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter18aEnemies
            UnitFormation = placeunits.Chapter18aPlacement
            BattleStarted = False
            battle_started = True
        elif units.Xuirventh in units.UnitsAlive and CutsceneIndex < 19:
            if CutsceneIndex == 4:
                Text1("Xuirventh: ...",units.Xuirventh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 5:
                Text2("???: ...",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 6:
                Text2("Xuirventh: Xuirfth, is that you?",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 7:
                Text2("Xuirfth: Xuirventh?",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("Xuirventh: These Bipolains helped me take down the",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                line2("camp.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("Xuirventh: And they're being lead by Xuirond.",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("Xuirfth: Xuirond?",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Proton: Hello, you must be the other Proto-Xuir.",units.Proton.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Proton: I am Proto-Xuir G3 N2 and my name is Proton",units.Proton.Portrait,units.Xuirfth.Portrait)
                line2("Xurr, though it seems like you two call me \"Xuirond\".")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 12:
                Text2("Xuirfth: How are you alive? Everyone at the Shadow Realm",units.Proton.Portrait,units.Xuirfth.Portrait)
                line2("said that you were killed by a teleporter.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Proton: The teleporter that Scien and I used was broken, but",units.Proton.Portrait,units.Xuirfth.Portrait)
                line2("we were lucky enough to be teleported onto the Bipole Continent.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Xuirventh: We should get going. If Xuirurth has avoided being captured,",units.Proton.Portrait,units.Xuirventh.Portrait)
                line2("he should be at the Shadow Alter in the Nation of Nation.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Proton: Yes, let's get going.",units.Proton.Portrait,units.Xuirventh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text3("[Xuirfth joins your party]")
                units.UnitsAlive.append(units.Xuirfth)
                units.UnitsRecruited.append(units.Xuirfth)
                CutsceneIndex = 19
                
        elif CutsceneIndex < 19:    
            if CutsceneIndex == 4:
                Text1("Proton: ...",units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 5:
                Text1("???: You there!",units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 6:
                Text1("Proton: ???",units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 7:
                Text2("???: I can sense that you are a Proto-Xuir.",units.Proton.Portrait, units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("Proton: ...",units.Proton.Portrait, units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("???: Do not be afraid, I am not here to harm you.",units.Proton.Portrait, units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("???: I am Xuirer, a traveling Xuirist.",units.Proton.Portrait, units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Xuirer: However, the huntings of the Proto-Xuirs...",units.Proton.Portrait, units.Xuirer.Portrait)
                line2("I can't support it.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 12:
                Text2("Xuirer: Why do we wish to wish to destroy what we worship?",units.Proton.Portrait, units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Xuirer: The Proto-Xuirs should be worshipped, for the Xuirs",units.Proton.Portrait, units.Xuirer.Portrait)
                line2("are an extension of the True Xuir's power.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Proton: ...",units.Proton.Portrait, units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Xuirer: Holy Proto-Xuir, I wish to join you on your quest",units.Proton.Portrait, units.Xuirer.Portrait)
                line2("around the world.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text3("[Recruit Xuirer?]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
            elif CutsceneIndex == 17:
                if Qinput == True:
                    Text2("Xuirer: I thank you for your blessings, Proto-Xuir.",units.Proton.Portrait, units.Xuirer.Portrait)
                    CutsceneIndex += 1
                    
                else:
                    Text2("Xuirer: I pray for your victory, Proto-Xuir.",units.Proton.Portrait, units.Xuirer.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 18:
                if Qinput == True:
                    Text3("[Xuirer has joined your party]")
                    units.UnitsAlive.append(units.Xuirer)
                    units.UnitsRecruited.append(units.Xuirer)
                    CutsceneIndex += 1
                    ClearInputs()
                    
                else:
                    CutsceneIndex += 1
                    ClearInputs()
                    Cutscene()
        elif CutsceneIndex == 19:
            Text3("[Xuirist Cavern]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text1("Omega: ...", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text1("Omega: A camp in central Nolavillia has just been destroyed.", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Break: ...", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("Break: Destory them.", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("Omega: I will send troops out to surround them.", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("Omega: They'll have no escape, this is be far stronger", units.OmegaXuirist.Portrait, units.Break.Portrait)
            line2("the past battles.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("Break: It better be.", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("Break: Remember, Omega...", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Break: If you fail, they will be destroyed.", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Omega: ...", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex < 47 and units.Quest in units.UnitsAlive and units.Lias in units.UnitsAlive:
            if CutsceneIndex == 30:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 31:
                Text2("Quest: Lias, I've been thinking about what you've said",units.Quest.Portrait,units.Lias.Portrait)
                line2("earlier in the Bipole Sea...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 32:
                Text2("Lias: Ummm... what did I say?",units.Quest.Portrait,units.Lias.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 33:
                Text2("Quest: You said that you were surviving in the sea by",units.Quest.Portrait,units.Lias.Portrait)
                line2("drinking the sea water.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text2("Quest: That is true, yes?",units.Quest.Portrait,units.Lias.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 35:
                Text2("Lias: Yeah.",units.Quest.Portrait,units.Lias.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 36:
                Text2("Quest: Drinking sea water is extremely dangerous, and",units.Quest.Portrait,units.Lias.Portrait)
                line2("I thought you were lying at first.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 37:
                Text2("Quest: But then I realized you might have some sort",units.Quest.Portrait,units.Lias.Portrait)
                line2("of immunity to the pollution inside of the water.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("Lias: Immunity?",units.Quest.Portrait,units.Lias.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text2("Quest: Yes.",units.Quest.Portrait,units.Lias.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 40:
                Text2("Quest: When was the last time you've gotten sick?",units.Quest.Portrait,units.Lias.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 41:
                Text2("Lias: Hmmmm...",units.Quest.Portrait,units.Lias.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 42:
                Text2("Lias: Now that I think of it, I don't think I've",units.Quest.Portrait,units.Lias.Portrait)
                line2("ever gotten sick.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 43:
                Text2("Quest: Then it's basically confirmed: you have an",units.Quest.Portrait,units.Lias.Portrait)
                line2("absurdly powerful immune system.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 44:
                Text2("Quest: If we ever encounter an enemy that battles with",units.Quest.Portrait,units.Lias.Portrait)
                line2("infections, you might more resistant against them.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 45:
                Text2("Lias: That's good to know.",units.Quest.Portrait,units.Lias.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 46:
                Text3("[Quest and Lias leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Quest,3)
                select.InstantLevelUp(units.Lias,3)
                
        elif CutsceneIndex < 47:
            CutsceneIndex = 47
            Cutscene()
        elif CutsceneIndex < 60 and units.Romra in units.UnitsAlive and units.B in units.UnitsAlive:
            if CutsceneIndex == 47:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 48:
                Text2("Romra: B.",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 49:
                Text2("B: Yes?",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 50:
                Text2("Romra: How many times have you fought with us?",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 51:
                Text2("B: Many times.",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 52:
                Text2("B: But each time, it is a little different.",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 53:
                Text2("B: This is the first time I've fought with you",units.Romra.Portrait,units.B.Portrait)
                line2("on my side.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 54:
                Text2("B: And I've never fought against you.",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 55:
                Text2("Romra: Fought against me?",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 56:
                Text2("B: I've only fought against Proton, Quest, and Azure thus far.",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 57:
                Text2("B: It's very strange, all of these timelines and I only",units.Romra.Portrait,units.B.Portrait)
                line2("ever fight the three.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 58:
                Text2("B: Perhaps other battles may not fit within the Neville Prophecy.",units.Romra.Portrait,units.B.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 59:
                Text3("[Romra and B leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Romra,3)
                select.InstantLevelUp(units.B,3)
                
        elif CutsceneIndex < 60:
            CutsceneIndex = 60
            Cutscene()
        elif CutsceneIndex == 60:
            Chapter = "Chapter 19a"
            CutsceneIndex = 0
            Cutscene()
    elif Chapter == "Chapter 18b": #=====================Chapter18b===============================================================
        ChapterLevel = 90
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 18b]")
            line2("[PSA Conventions Zone, Central Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text1("Proton: ...",units.Proton.Portrait)
            UnitsToPlace = placeunits.Chapter18aEnemies
            UnitFormation = placeunits.Chapter18aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 2:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex = 0
            Chapter = "Chapter 19b"
            
    elif Chapter == "Chapter 19a": #=====================Chapter19a===============================================================
        ChapterLevel = 32
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 19a]")
            line2("[Xuir Plain, Central Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Proton: I think we're being followed.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            
            
            UnitsToPlace = placeunits.Chapter19aEnemies
            UnitFormation = placeunits.Chapter19aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("Proton: Prepare for battle!",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            CutsceneIndex += 1
            
            
            
            
        elif CutsceneIndex == 5:
            Text1("Proton: I think that's all of the Xuirists here.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text1("...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("???: Errr... I've had enough of 'em crazy Xuirists.",units.Proton.Portrait,units.Dliug.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("???: Ya can't pay me 'nough to do this stuff.",units.Proton.Portrait,units.Dliug.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("???: You 'ere!",units.Proton.Portrait,units.Dliug.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("Proton: Me?",units.Proton.Portrait,units.Dliug.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("???: The hell else would I be talkin' to?",units.Proton.Portrait,units.Dliug.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text2("???: Ya probably hate the Xuirists, don't 'ya?",units.Proton.Portrait,units.Dliug.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("???: 'ey sent me out here to kill ya', after all.",units.Proton.Portrait,units.Dliug.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("???: Anyway, I've had 'nough of 'em crazy Xuirists.",units.Proton.Portrait,units.Dliug.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("???: Ya can't pay me 'nough to do another of 'em Xuir",units.Proton.Portrait,units.Dliug.Portrait)
            line2("Rituals.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("???: Since 'yer look like ya gonna fight 'em anyways, why",units.Proton.Portrait,units.Dliug.Portrait)
            line2("not let us help ya?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
                Text3("[Recruit the Mercenaries?]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 18:
            if Qinput == True:
                Text2("???: Now we can loot all the gold 'em Xuirist got!",units.Proton.Portrait, units.Dliug.Portrait)
                line2("Exa! Yranecrem! Get over 'ere!")
                CutsceneIndex += 1
                
            else:
                Text2("???: That's a shame, ain't it?",units.Proton.Portrait, units.Dliug.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 19:
            if Qinput == True:
                Text3("[Dliug has joined your party]")
                line2("[Exa has joined your party]")
                line3("[Yranecrem has joined your party]")
                units.UnitsAlive.append(units.Dliug)
                units.UnitsRecruited.append(units.Dliug)
                units.UnitsAlive.append(units.Exa)
                units.UnitsRecruited.append(units.Exa)
                units.UnitsAlive.append(units.Yranecrem)
                units.UnitsRecruited.append(units.Yranecrem)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                CutsceneIndex += 1
                ClearInputs()
                Cutscene()
        elif CutsceneIndex == 20:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex < 30 and len(units.UnitsAlive) <= 10:
            if CutsceneIndex == 21:
                Text2("???: It seems you may be struggling...",units.Proton.Portrait,units.Geomer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Proton: Who are you?",units.Proton.Portrait,units.Geomer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("???: I am Geomer, a disciple in Geom theory.",units.Proton.Portrait,units.Geomer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Geomer: You see, those Xuirists that you were just",units.Proton.Portrait,units.Geomer.Portrait)
                line2("fighting were using Geom Energy.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 25:
                Text2("Geomer: Geom Energy is a very powerful force, and it",units.Proton.Portrait,units.Geomer.Portrait)
                line2("seems you are unfamiliar to it.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 26:
                Text2("Geomer: As one wishing to spread the knowledge of Geom,",units.Proton.Portrait,units.Geomer.Portrait)
                line2("I offer to aid you in combat using my Geom powers.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 27:
                Text3("[Recruit Geomer?]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
            elif CutsceneIndex == 28:
                if Qinput == True:
                    Text2("Geomer: Great, the power of Geom shall be known.",units.Proton.Portrait, units.Geomer.Portrait)
                    CutsceneIndex += 1
                    
                else:
                    Text2("Geomer: You fear knowledge, for you cannot comprehend it.",units.Proton.Portrait, units.Geomer.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 29:
                if Qinput == True:
                    Text3("[Geomer has joined your party]")
                    units.UnitsAlive.append(units.Geomer)
                    units.UnitsRecruited.append(units.Geomer)
                    CutsceneIndex += 1
                    ClearInputs()
                    
                else:
                    CutsceneIndex += 1
                    ClearInputs()
                    Cutscene()
        elif CutsceneIndex < 30:
            CutsceneIndex = 30
            Cutscene()
        elif CutsceneIndex < 37 and units.Xuirventh in units.UnitsAlive and units.Xuirfth in units.UnitsAlive:
            if CutsceneIndex == 30:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 31:
                Text2("Xuirventh: Xuirfth, its good to see you alive.",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 32:
                Text2("Xuifth: Same to you.",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 33:
                Text2("Xuirfth: But to think that we'd meet Xuirond, that's even",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                line2("bigger of a suprise...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text2("Xuirfth: This truly is a strange week.",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 35:
                Text2("Xuirfth: I wonder what other suprises are to come...",units.Xuirventh.Portrait,units.Xuirfth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 36:
                Text3("[Xuirventh and Xuirfth leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Xuirventh,3)
                select.InstantLevelUp(units.Xuirfth,3)
                
        elif CutsceneIndex < 37:
            CutsceneIndex = 37
            Cutscene()
        elif CutsceneIndex < 47 and units.Vruh in units.UnitsAlive:
            if CutsceneIndex == 37:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("Vruh: Proton, do you believe that our society is corrupt?",units.Vruh.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text2("Proton: Hmm? What do you mean?",units.Vruh.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 40:
                Text2("Vruh: I believe that our society is crumpling to the horrors",units.Vruh.Portrait,units.Proton.Portrait)
                line2("of corruption in politics.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 41:
                Text2("Vruh: Our ancestors destoryed Earth around 1300 years ago, and if",units.Vruh.Portrait,units.Proton.Portrait)
                line2("we do not change our ways...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 42:
                Text2("Vruh: ...we will do the same.",units.Vruh.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 43:
                Text2("Vruh: The fall of our society and our world is inevidable.",units.Vruh.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 44:
                Text2("Vruh: Enjoy your petty existence while it lasts, Proton, for you",units.Vruh.Portrait,units.Proton.Portrait)
                line2("should expect a painful death.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 45:
                Text2("Proton: ...",units.Vruh.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 46:
                Text3("[Vruh and Proton leveled up!]")
                CutsceneIndex += 1
                select.InstantLevelUp(units.Vruh,3)
                select.InstantLevelUp(units.Proton,3)
                
        elif CutsceneIndex < 47:
            CutsceneIndex = 47
            Cutscene()  
        elif CutsceneIndex == 47:
            Text3("[Xuirist Cavern]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 48:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text1("Omega: ...", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 49:
            Text1("Omega: ...they have failed again.", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 50:
            Text2("Break: ...", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 51:
            Text2("Break: Must I remind you of what will happen?", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 52:
            Text2("Break: If you are out of troops to send out, then you must fight the", units.OmegaXuirist.Portrait, units.Break.Portrait)
            line2("Proto-Xuir to the death yourself.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 53:
            Text2("Omega: He will be approaching our camp soon, I'll gather all of our troops", units.OmegaXuirist.Portrait, units.Break.Portrait)
            line2("here and slay him in our final battle.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 54:
            Text2("Omega: I will not fail.", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 55:
            Text2("Break: You better keep your word.", units.OmegaXuirist.Portrait, units.Break.Portrait)
            CutsceneIndex = 0
            if units.Elbon in units.UnitsAlive:
                Chapter = "Chapter 20a"
            else:
                Chapter = "Chapter 20b"
            
    elif Chapter == "Chapter 19b": #=====================Chapter19a===============================================================
        ChapterLevel = 32
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 19b]")
            line2("[Xuir Plain, Central Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            SetPosX = -650
            SetPosY = 50
            for character in units.UnitsAlive:
                print(character.DisplayName)
                character.TurtleName.showturtle()
                character.TurtleName.speed(0)
                character.TurtleName.penup()
                character.TurtleName.setpos(SetPosX,SetPosY)
                if SetPosX == 250:
                    SetPosY -= 50
                    SetPosX = -250
                else:
                    SetPosX += 50
            CutsceneIndex += 1
            Cutscene()
        elif CutsceneIndex == 2:
            
            
            UnitsToPlace = placeunits.Chapter19aEnemies
            UnitFormation = placeunits.Chapter19aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            CutsceneIndex += 1
            
            
            
            
        elif CutsceneIndex == 4:
            Text1("Proton: ...",units.Proton.Portrait)
            Chapter = "Chapter 20b"
            
    elif Chapter == "Chapter 20a": #=====================Chapter20a===============================================================
        ChapterLevel = 36
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 20a]")
            line2("[Xuir Plain, Central Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text1("Proton: We'll be passing through the Nolavillian Mountain",units.Proton.Portrait)
            line2("Range soon.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Proton: The path through the mountain range is very narrow,",units.Proton.Portrait)
            line2("keep on guard for ambushes.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Proton: And it seems there's already a group of people ahead of",units.Proton.Portrait)
            line2("us, likely trying to ambush us.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text2("Elbon: Hey, I recognize them!",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("Proton: You do?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("Elbon: Of course I do!",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("Elbon: Those are Shadian soldiers. I think they're being led by",units.Proton.Portrait,units.Elbon.Portrait)
            line2("Dael, the head knight of prince Neo's army.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text2("Proton: But why would they be here though?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("Elbon: Who knows... We just need to pass by them, right?",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("Proton: Yes, I would prefer to avoid conflict.",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text1("Elbon: Hey! Dael!",units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text2("Dael: Hmm? What is this rat doing here?",units.Elbon.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text2("Elbon: Is it fine if we pass by your camp?",units.Elbon.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text2("Dael: And why might you need to do that?",units.Elbon.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Elbon: Prince Neo sent me here to retrieve Healia Aid,",units.Elbon.Portrait,units.Dael.Portrait)
            line2("but I must entertain these Bipolians on their journey")
            line3("before they hand her over.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("Dael: *sigh* Such a pathetic method for a pathetic",units.Elbon.Portrait,units.Dael.Portrait)
            line2("fool.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text2("Dael: As much as I hate you, I don't wish to disturb",units.Elbon.Portrait,units.Dael.Portrait)
            line2("Prince Neo's plans.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("Dael: Now run along with your circus, Elbon.",units.Elbon.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text3("(Proton's army safely passes through Dael's camp)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Proton: Wow, that actually worked.",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Elbon: Of course it worked, I am the great Elbon Rich!",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("Elbon: My power and fame are one to be feared! ",units.Proton.Portrait,units.Elbon.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("Proton: It seemed to me more like it was Neo's power and fame",units.Proton.Portrait,units.Elbon.Portrait)
            line2("that were feared, but I suppose you did get us pass safely.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text3("???: AHHHHHHHH!!!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text1("Proton: Huh, who was that?",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("???: Bandits! Bandits are up ahead!",units.Proton.Portrait,units.Box.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Proton: Bandits?",units.Proton.Portrait,units.Box.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("???: They've chased me down the mountain range!",units.Proton.Portrait,units.Box.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text2("???: I am a mere merchant, I can't fight off a horde of",units.Proton.Portrait,units.Box.Portrait)
            line2("bandits! Please help me!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31 and units.Quest in units.UnitsAlive:
            Text2("Quest: If there's bandits ahead, we'll need to fight",units.Proton.Portrait,units.Quest.Portrait)
            line2("them to get past anyways.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("Proton: No one will be able to pass with bandits blocking",units.Proton.Portrait,units.Box.Portrait)
            line2("the way...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32 and units.Quest in units.UnitsAlive:
            Text2("Proton: You're right, prepare for battle!",units.Proton.Portrait,units.Quest.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text2("Proton: Everyone, prepare for battle!",units.Proton.Portrait,units.Box.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
            Text3("[Box has joined your party]")
            units.UnitsAlive.append(units.Box)
            units.UnitsRecruited.append(units.Box)
            UnitsToPlace = placeunits.Chapter20aEnemies
            UnitFormation = placeunits.Chapter20aPlacement
            BattleStarted = False
            CutsceneIndex += 1
            battle_started = True
        elif CutsceneIndex == 34:
            Text1("Proton: That should be all of the bandits...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 35:
            Text3("???: You there!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 36:
            Text1("Proton: Huh? Is someone there?",units.Proton.Portrait)
            line2("(Why does this keep happening...)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 37:
            Text2("???: You hold great power, Proton.",units.Proton.Portrait,units.NOTOS.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 38:
            Text2("Proton: Who are you?",units.Proton.Portrait,units.NOTOS.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 39:
            Text2("???: I am Neville of the OS, also known as NOTOS.",units.Proton.Portrait,units.NOTOS.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 40:
            Text2("NOTOS: I came here after I sensed great power, and you",units.Proton.Portrait,units.NOTOS.Portrait)
            line2("have great potential within your abilities")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 41:
            Text2("NOTOS: I wish to witness more of your battles, its not",units.Proton.Portrait,units.NOTOS.Portrait)
            line2("everyday that I find someone like you.")
            units.UnitsAlive.append(units.NOTOS)
            units.UnitsRecruited.append(units.NOTOS)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 42:
            Text2("NOTOS: And don't worry, I've already added myself to your",units.Proton.Portrait,units.NOTOS.Portrait)
            line2("party.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 43:
            Text2("Proton: ...",units.Proton.Portrait,units.NOTOS.Portrait)
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            Text3("[Xuirist Cavern]")
            screensetup.BattleScreen.bgcolor("black")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 101:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text1("Omega: ...", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 102:
            Text1("Omega: Preperations are now complete.", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 103:
            Text2("Break: Good.", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 104:
            Text2("Break: We'll kill every last one of them fools.", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 105:
            Text2("Break: Those who oppose lord Prime shall no longer live...", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 106:
            Text2("Break: And the Holy Itucher shall finally become ours!", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 107:
            Text2("Omega: ...", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 108:
            Text2("Break: And one more thing...", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 109:
            Text2("Break: *They* must partake in the battle.", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 110:
            Text2("Omega: ..!", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 111:
            Text2("Break: No excuses. Either they partake or I'll", units.OmegaXuirist.Portrait,units.Break.Portrait)
            line2("destroy them myself.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 112:
            Text2("Break: Which would you rather want, Omega?", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 113:
            Text2("Omega: ...", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 114:
            screensetup.BattleScreen.bgcolor("green")
            Text3("...")
            CutsceneIndex += 1
             
        elif CutsceneIndex <= 123 and units.Yranecrem in units.UnitsAlive:
            if CutsceneIndex == 115:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 116:
                Text2("Yranecrem: The Holy Itucher, the ultimate weapon...",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 117:
                Text2("Yranecrem: How much destruction do you think it's caused?",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 118:
                Text2("Yranecrem: Why has no one destroyed it, is it indestructable?",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 119:
                Text2("Yranecrem: Proton, if you obtain the Holy Itucher...",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 120:
                Text2("Yranecrem: I can only hope that you destroy it.",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 121:
                Text2("Yranecrem: The wars and battles fought over the weapon must",units.Yranecrem.Portrait,units.Proton.Portrait)
                line2("be stopped, and that reponsibility will soon fall upon you.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 122:
                Text2("Proton: ...",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 123:
                Text3("[Yranecrem and Proton leveled up!]")
                select.InstantLevelUp(units.Yranecrem,3)
                select.InstantLevelUp(units.Proton,3)
                CutsceneIndex = 135
                
        elif CutsceneIndex <= 123:
            CutsceneIndex = 135
            Cutscene()
        elif CutsceneIndex <= 143 and units.B in units.UnitsAlive and units.Xuirer in units.UnitsAlive:
            if CutsceneIndex == 135:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 136:
                Text2("B: ...",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 137:
                Text2("B: You're him, aren't you.",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 138:
                Text2("Xuirer: Yes, you're correct.",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 139:
                Text2("B: So you've somehow learned how to use Geom Energy...",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 140:
                Text2("Xuirer: It looked interesting and I've had thousands of years,",units.B.Portrait,units.Xuirer.Portrait)
                line2("why wouldn't I?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 141:
                Text2("B: I'm assuming you have some grand ideas for this life.",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 142:
                Text2("Xuirer: Yes, some very grand ideas...",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 143:
                Text3("[B and Xuirer up!]")
                select.InstantLevelUp(units.B,3)
                select.InstantLevelUp(units.Xuirer,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 143:
            CutsceneIndex = 144
            Cutscene()
        elif CutsceneIndex <= 151 and units.Dliug in units.UnitsAlive and units.Wodahs in units.UnitsAlive:
            if CutsceneIndex == 144:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 145:
                Text2("Dliug: Hey kid, what're we even fightin' for?",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 146:
                Text2("Wodahs: What do you mean?",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 147:
                Text2("Dliug: Therr army, what's our goal?",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 148:
                Text2("Wodahs: I think we're trying to attack the Shadow Realm to",units.Dliug.Portrait,units.Wodahs.Portrait)
                line2("retrieve the Holy Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 149:
                Text2("Dliug: Oooooooh noooooooooo...",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 150:
                Text2("Dliug: I might be regrettin' joinin'...",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 151:
                Text3("[Dliug and Wodahs up!]")
                select.InstantLevelUp(units.Dliug,3)
                select.InstantLevelUp(units.Wodahs,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 151:
            CutsceneIndex = 152
            Cutscene()  
        elif CutsceneIndex <= 159 and units.Fael in units.UnitsAlive and units.Erif in units.UnitsAlive:
            if CutsceneIndex == 152:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 153:
                Text2("Fael: How did this happen?",units.Fael.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 154:
                Text2("Erif: Someone must be modifying the game files.",units.Fael.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 155:
                Text2("Fael: Modifying the game files!? That means this",units.Fael.Portrait,units.Erif.Portrait)
                line2("route can't be canon!")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 156:
                Text2("Erif: Of course its not canon, I don't think you're",units.Fael.Portrait,units.Erif.Portrait)
                line2("even supposed to be able to get this bonus conversation")
                line3("without changing the character files.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 157:
                Text2("Fael: So to whoever found this bonus conversation,",units.Fael.Portrait,units.Erif.Portrait)
                line2("good job, I guess.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 158:
                Text2("Erif: I don't know why you're messing with the game",units.Fael.Portrait,units.Erif.Portrait)
                line2("files though.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 159:
                Text3("[lmao stop editing the game files]")
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 159:
            CutsceneIndex = 160
            Cutscene()  
        elif CutsceneIndex <= 166 and units.Vruh in units.UnitsAlive:
            if CutsceneIndex == 160:
                Text1("Vruh: ...", units.Vruh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 161:
                Text2("???: Ah, it is you?", units.Vruh.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 162:
                Text2("Vruh: Yung Poggers? I did not expect to see you here.", units.Vruh.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 163:
                Text2("Yung Poggers: What ever you guys are doing, it seems very", units.Vruh.Portrait,units.YungPoggers.Portrait)
                line2("wacky and characteristic...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 164:
                Text2("Yung Poggers: I shall join your party for no reason whatsoever!", units.Vruh.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 165:
                Text3("[Yung Poggers joined your party!]")
                units.UnitsAlive.append(units.YungPoggers)
                units.UnitsRecruited.append(units.YungPoggers)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 166:
                Text2("Vruh: Based.", units.Vruh.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 166:
            CutsceneIndex = 167
            Cutscene()  
        elif CutsceneIndex == 167:
            CutsceneIndex = 0
            Chapter = "Chapter 21a"
            Cutscene()
    elif Chapter == "Chapter 20b": #=====================Chapter20b===============================================================
        ChapterLevel = 36
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 20b]")
            line2("[Nolavillian Mountain Range, Northern Nolavillia]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("green")
            Text1("Proton: We'll be passing through the Nolavillian Mountain",units.Proton.Portrait)
            line2("Range soon.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Proton: The path through the mountain range is very narrow,",units.Proton.Portrait)
            line2("keep on guard for ambushes.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text1("Proton: And it seems there's already a group of people ahead of",units.Proton.Portrait)
            line2("us, likely trying to ambush us...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text2("???: You! State your purpose!",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text2("Proton: We're here to retrieve the Holy Itucher.",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            Text2("???: Thats must mean the Holy Itucher is past this mountain range...",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text2("???: Though I appreciate your help, we must kill you.",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text2("???: We're here to obtain the Holy Itucher for prince Neo of Shade,",units.Proton.Portrait,units.Dael.Portrait)
            line2("and it would be troublesome if you found it before us.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            Text2("Proton: ...",units.Proton.Portrait, units.Dael.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter20bEnemies
            UnitFormation = placeunits.Chapter20bPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 11:
            Text2("Dael: I've... lost... ?",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            Text2("Proton: ...",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text2("Dael: I won't... let you get... any more...",units.Proton.Portrait,units.Dael.Portrait)
            line2("information...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text3("[Dael disintegrates himself with a spell]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 15:
            Text1("Proton...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 16:
            Text2("Dnefed: Umm... we're not that loyal, can we stay alive? We could",units.Proton.Portrait,units.Dnefed.Portrait)
            line2("work for you.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 17:
                Text3("[Recruit the Shadian soldiers?]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 18:
            if Qinput == True:
                Text2("Dnefed: Thanks.",units.Proton.Portrait,units.Dnefed.Portrait)
                CutsceneIndex += 1
                
            else:
                Text3("(Proton defeats the rest of the soldiers)")
                CutsceneIndex += 1
                
        elif CutsceneIndex == 19:
            if Qinput == True:
                Text3("[Dnefed, Thgif, Gnirif, and Cigam joined your party]")
                units.UnitsAlive.append(units.Dnefed)
                units.UnitsRecruited.append(units.Dnefed)
                units.UnitsAlive.append(units.Thgif)
                units.UnitsRecruited.append(units.Thgif)
                units.UnitsAlive.append(units.Gnirif)
                units.UnitsRecruited.append(units.Gnirif)
                units.UnitsAlive.append(units.Cigam)
                units.UnitsRecruited.append(units.Cigam)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                CutsceneIndex += 1
                ClearInputs()
                Cutscene()
        elif units.Dnefed not in units.UnitsRecruited and CutsceneIndex <= 26:
            if CutsceneIndex == 20:
                register_shape("revolt")
                Text2("???: ...",units.Proton.Portrait,"revolt")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 21:
                Text2("???: You've helped me greatly, Proton.",units.Proton.Portrait,"revolt")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Proton: Who are you?.",units.Proton.Portrait,"revolt")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("???: I am Revolt, and you have just defeated Dael and his army for me.",units.Proton.Portrait,"revolt")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Revolt: I'm in a very good mood today, so I'll grant you this...",units.Proton.Portrait,"revolt")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 25:
                Text3("[Proton learned Aura]")
                units.Proton.Attacks.append(moves.Aura)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 26:
                Text3("(Revolt disappears)")
                CutsceneIndex += 1
                
        elif units.Dnefed in units.UnitsRecruited and CutsceneIndex <= 26:
            CutsceneIndex = 27
            Cutscene()
        elif CutsceneIndex == 27:
            CutsceneIndex = 100
            Cutscene()

        elif CutsceneIndex == 100:
            Text3("[Xuirist Cavern]")
            screensetup.BattleScreen.bgcolor("black")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 101:
            screensetup.BattleScreen.bgcolor("dim grey")
            Text1("Omega: ...", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 102:
            Text1("Omega: Preperations are now complete.", units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 103:
            Text2("Break: Good.", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 104:
            Text2("Break: We'll kill every last one of them fools.", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 105:
            Text2("Break: Those who oppose lord Prime shall no longer live...", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 106:
            Text2("Break: And the Holy Itucher shall finally become ours!", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 107:
            Text2("Omega: ...", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 108:
            Text2("Break: And one more thing...", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 109:
            Text2("Break: *They* must partake in the battle.", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 110:
            Text2("Omega: ..!", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 111:
            Text2("Break: No excuses. Either they partake or I'll", units.OmegaXuirist.Portrait,units.Break.Portrait)
            line2("destroy them myself.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 112:
            Text2("Break: Which would you rather want, Omega?", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 113:
            Text2("Omega: ...", units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 114:
            screensetup.BattleScreen.bgcolor("green")
            Text3("...")
            CutsceneIndex += 1
             
        elif CutsceneIndex <= 123 and units.Yranecrem in units.UnitsAlive:
            if CutsceneIndex == 115:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 116:
                Text2("Yranecrem: The Holy Itucher, the ultimate weapon...",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 117:
                Text2("Yranecrem: How much destruction do you think it's caused?",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 118:
                Text2("Yranecrem: Why has no one destroyed it, is it indestructable?",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 119:
                Text2("Yranecrem: Proton, if you obtain the Holy Itucher...",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 120:
                Text2("Yranecrem: I can only hope that you destroy it.",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 121:
                Text2("Yranecrem: The wars and battles fought over the weapon must",units.Yranecrem.Portrait,units.Proton.Portrait)
                line2("be stopped, and that reponsibility will soon fall upon you.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 122:
                Text2("Proton: ...",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 123:
                Text3("[Yranecrem and Proton leveled up!]")
                select.InstantLevelUp(units.Yranecrem,3)
                select.InstantLevelUp(units.Proton,3)
                CutsceneIndex = 135
                
        elif CutsceneIndex <= 123:
            CutsceneIndex = 135
            Cutscene()
        elif CutsceneIndex <= 143 and units.B in units.UnitsAlive and units.Xuirer in units.UnitsAlive:
            if CutsceneIndex == 135:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 136:
                Text2("B: ...",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 137:
                Text2("B: You're him, aren't you.",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 138:
                Text2("Xuirer: Yes, you're correct.",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 139:
                Text2("B: So you've somehow learned how to use Geom Energy...",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 140:
                Text2("Xuirer: It looked interesting and I've had thousands of years,",units.B.Portrait,units.Xuirer.Portrait)
                line2("why wouldn't I?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 141:
                Text2("B: I'm assuming you have some grand ideas for this life.",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 142:
                Text2("Xuirer: Yes, some very grand ideas...",units.B.Portrait,units.Xuirer.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 143:
                Text3("[B and Xuirer up!]")
                select.InstantLevelUp(units.B,3)
                select.InstantLevelUp(units.Xuirer,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 143:
            CutsceneIndex = 144
            Cutscene()
        elif CutsceneIndex <= 151 and units.Dliug in units.UnitsAlive and units.Wodahs in units.UnitsAlive:
            if CutsceneIndex == 144:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 145:
                Text2("Dliug: Hey kid, what're we even fightin' for?",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 146:
                Text2("Wodahs: What do you mean?",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 147:
                Text2("Dliug: Therr army, what's our goal?",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 148:
                Text2("Wodahs: I think we're trying to attack the Shadow Realm to",units.Dliug.Portrait,units.Wodahs.Portrait)
                line2("retrieve the Holy Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 149:
                Text2("Dliug: Oooooooh noooooooooo...",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 150:
                Text2("Dliug: I might be regrettin' joinin'...",units.Dliug.Portrait,units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 151:
                Text3("[Dliug and Wodahs up!]")
                select.InstantLevelUp(units.Dliug,3)
                select.InstantLevelUp(units.Wodahs,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 151:
            CutsceneIndex = 152
            Cutscene()  
        elif CutsceneIndex <= 159 and units.Fael in units.UnitsAlive and units.Erif in units.UnitsAlive:
            if CutsceneIndex == 152:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 153:
                Text2("Fael: How did this happen?",units.Fael.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 154:
                Text2("Erif: Someone must be modifying the game files.",units.Fael.Portrait,units.Erif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 155:
                Text2("Fael: Modifying the game files!? That means this",units.Fael.Portrait,units.Erif.Portrait)
                line2("route can't be cannon!")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 156:
                Text2("Erif: Of course its not cannon, I don't think you're",units.Fael.Portrait,units.Erif.Portrait)
                line2("even supposed to be able to get this bonus conversation")
                line3("without changing the character files.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 157:
                Text2("Fael: So to whoever found this bonus conversation,",units.Fael.Portrait,units.Erif.Portrait)
                line2("good job, I guess.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 158:
                Text2("Erif: I don't know why you're messing with the game",units.Fael.Portrait,units.Erif.Portrait)
                line2("files though.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 159:
                Text3("[lmao stop editing the game files]")
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 159:
            CutsceneIndex = 160
            Cutscene()  
        elif CutsceneIndex <= 166 and units.Vruh in units.UnitsAlive:
            if CutsceneIndex == 160:
                Text1("Vruh: ...", units.Vruh.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 161:
                Text2("???: Ah, it is you?", units.Vruh.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 162:
                Text2("Vruh: Yung Poggers? I did not expect to see you here.", units.Vruh.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 163:
                Text2("Yung Poggers: What ever you guys are doing, it seems very", units.Vruh.Portrait,units.YungPoggers.Portrait)
                line2("wacky and characteristic...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 164:
                Text2("Yung Poggers: I shall join your party for no reason whatsoever!", units.Vruh.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 165:
                Text3("[Yung Poggers joined your party!]")
                units.UnitsAlive.append(units.YungPoggers)
                units.UnitsRecruited.append(units.YungPoggers)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 166:
                Text2("Vruh: Based.", units.Vruh.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 166:
            CutsceneIndex = 167
            Cutscene()  
        elif CutsceneIndex == 167:
            CutsceneIndex = 0
            Chapter = "Chapter 21a"
            Cutscene()  
    elif Chapter == "Chapter 20c": #=====================Chapter20c===============================================================
        ChapterLevel = 108
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 20c]")
            line2("[Nolavillian Mountain Range, Northern Nolavillia]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter20bEnemies
            UnitFormation = placeunits.Chapter20bPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 2:
            Text2("Dael: Who... is this...",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text2("Dael: How have... I lost...",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("Dael: The empire...",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text2("Dael: Neo...",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("Dael: I've... failed...",units.Proton.Portrait,units.Dael.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            CutsceneIndex = 0
            Chapter = "Chapter 21b"
            Cutscene()
    elif Chapter == "Chapter 21a": #=====================Chapter21a===============================================================
        ChapterLevel = 38
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 21a]")
            line2("[Nolavillian Mountain Range, Northern Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dim grey")
            
            UnitsToPlace = placeunits.Chapter21aEnemies
            UnitFormation = placeunits.Chapter21aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text2("Omega: They are here...",units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 2:
            
            placeunits.PlacePlayerUnits()
            
            Text1("Proton: It seems there is another Xuirist camp here, but",units.Proton.Portrait)
            line2("we must proceed.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            CutsceneIndex += 1
            BattleStarted = True
            # 
            
            
            
            
            
        elif CutsceneIndex == 4:
            Text1("Break: Omega's been defeated, I've got to get out of here!",units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text3("(Break flees!)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("Omega: They're gone... they're all gone...",units.Proton.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("Omega: ...",units.Proton.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("Omega: I've been defeated. You win, Proton.",units.Proton.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text3("(Omega kneels before Proton)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text2("Omega: Kill me however you wish.",units.Proton.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text2("Proton: ...",units.Proton.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text2("Proton: An honorable death for a Xuirist, you will be executed.",units.Proton.Portrait,units.OmegaXuirist.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text3("(Proton raises his blade)")
            CutsceneIndex += 1
            
        elif units.Wob in units.UnitsAlive and CutsceneIndex <= 20:
            if CutsceneIndex == 12:
                Text2("Wob: Wait!",units.Wob.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("Proton: What is it?",units.Wob.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Wob: He isn't like the other Xuirists, he's not evil.",units.Wob.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Wob: Don't you he could work with us to help retrieve the Itucher",units.Wob.Portrait,units.Proton.Portrait)
                line2("and live a better life?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text3("[Recruit Omega]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
            elif CutsceneIndex == 17:
                if Qinput == True:
                    Text2("Omega: What reason do I have to keep living? Everything I've",units.Wob.Portrait,units.OmegaXuirist.Portrait)
                    line2("fought for is gone.")
                    CutsceneIndex += 1
                    
                else:
                    Text2("Omega: ...",units.Proton.Portrait, units.OmegaXuirist.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 18:
                if Qinput == True:
                    Text2("Wob: I've almost lost everything, but I've found purpose in life.",units.Wob.Portrait,units.OmegaXuirist.Portrait)
                    line2("If you don't at least try, you'll never find out.")
                    CutsceneIndex += 1
                    
                else:
                    Text2("Proton: Farwell, Xuirist.",units.Proton.Portrait, units.OmegaXuirist.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 19:
                if Qinput == True:
                    Text2("Omega: ...",units.Wob.Portrait,units.OmegaXuirist.Portrait)
                    CutsceneIndex += 1
                    
                else:
                    Text2("(Proton exectues Omega)",units.Proton.Portrait, units.OmegaXuirist.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 20:
                if Qinput == True:
                    Text3("[Omega has joined your party]")
                    units.UnitsAlive.append(units.Omega)
                    units.UnitsRecruited.append(units.Omega)
                    CutsceneIndex += 1
                    ClearInputs()
                    
                else:
                    CutsceneIndex += 1
                    ClearInputs()
                    Cutscene()
        elif CutsceneIndex <= 20:
            if CutsceneIndex == 12:
                Text2("Proton: Farewell, Xuirist.",units.Proton.Portrait,units.OmegaXuirist.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("(Proton executes Omega)",units.Proton.Portrait,units.OmegaXuirist.Portrait)
                CutsceneIndex = 21
                
        elif CutsceneIndex == 21:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif units.Scien in units.UnitsAlive and CutsceneIndex == 22:
            Text2("Scien: We'll be reaching the Village of Binding soon,",units.Proton.Portrait,units.Scien.Portrait)
            line2("it will be the final chance for us to prepare before")
            line3("entering the Shadow Realm.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text1("Proton: We'll be reaching the Village of Binding soon,",units.Proton.Portrait)
            line2("it'll be out last chance to prepare before the Shadow Realm.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Village of Binding, Nation of Nation]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 24:
            screensetup.BattleScreen.bgcolor("grey")
            Text1("Proton: We've arrived.",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            screensetup.BattleScreen.bgcolor("grey")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("???: You there! Are you what I think you are!?",units.Proton.Portrait,units.Fiyghtrr.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("Proton: Huh?",units.Proton.Portrait,units.Fiyghtrr.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("???: You must be here to stop the Shadow Realm, are you?",units.Proton.Portrait,units.Fiyghtrr.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text2("Proton: Yes, actually.",units.Proton.Portrait,units.Fiyghtrr.Portrait)
            CutsceneIndex += 1 
            
        elif CutsceneIndex == 30:
            Text2("???: Great!",units.Proton.Portrait,units.Fiyghtrr.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text2("???: I am Fiyghtrr, and I have been training years for this moment!",units.Proton.Portrait,units.Fiyghtrr.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text2("Fiyghtrr: Allow me to join you on your attack on the Shadow Realm!",units.Proton.Portrait,units.Fiyghtrr.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
                Text3("[Recruit Fiyghtrr?]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 34:
            if Qinput == True:
                Text2("Fiyghtrr: It's time!",units.Proton.Portrait,units.Fiyghtrr.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Fiyghtrr: ...what?",units.Proton.Portrait, units.Fiyghtrr.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 35:
            if Qinput == True:
                Text3("[Fiyghtrr has joined your party]")
                units.UnitsAlive.append(units.Fiyghtrr)
                units.UnitsRecruited.append(units.Fiyghtrr)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                CutsceneIndex += 1
                ClearInputs()
                Cutscene()
        elif len(units.UnitsAlive) <= 7 and CutsceneIndex <= 50:
            if CutsceneIndex == 36:
                Text2("???: YOU THERE!!!",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 37:
                Text2("Proton: (Why does this keep happening to me...)",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("???: Your army looks like it's lacking members.",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text2("???: Might you need a...",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 40:
                Text2("???: Might you need a... REPLACEMENT UNIT?",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 41:
                Text2("???: Of course you do! Everyone needs a replacement unit!",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 42:
                Text2("???: And you are in luck!",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 43:
                Text2("???: You see, I am Recalper: THE ULTIMATE REPLACEMENT UNIT!!!",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 44:
                Text2("Recalper: That's right! Got a void in your army after one of your",units.Proton.Portrait,units.Recalper.Portrait)
                line2("comrades died in the field?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 45:
                Text2("Recalper: That void will instantly be sealed up by my greatness!",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 46:
                Text2("Recalper: No one replaces the deceased like I do!",units.Proton.Portrait,units.Recalper.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 47:
                Text2("Recalper: So, what do you think? Want to recruit me into your",units.Proton.Portrait,units.Recalper.Portrait)
                line2("painfully empty army?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 48:
                Text3("[Recruit Recalper?]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
            elif CutsceneIndex == 49:
                if Qinput == True:
                    Text2("Recalper: Oh yeah! It's time for some replacement!",units.Proton.Portrait,units.Recalper.Portrait)
                    CutsceneIndex += 1
                    
                else:
                    Text2("Recalper: What!? Don't you know that you can't replace",units.Proton.Portrait, units.Recalper.Portrait)
                    line2("the replacement!?")
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 50:
                if Qinput == True:
                    Text3("[Recalper has joined your party]")
                    units.UnitsAlive.append(units.Recalper)
                    units.UnitsRecruited.append(units.Recalper)
                    CutsceneIndex += 1
                    ClearInputs()
                    
                else:
                    CutsceneIndex += 1
                    ClearInputs()
                    Cutscene()
        elif CutsceneIndex <= 50:
            CutsceneIndex = 51
            Cutscene()
        elif units.Recils in units.UnitsAlive and CutsceneIndex <= 60:
            if CutsceneIndex == 51:
                Text2("???: Hey.",units.Recils.Portrait,units.Tabmoc.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 52:
                Text2("Recils: Tabmoc? What are you doing here?",units.Recils.Portrait,units.Tabmoc.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 53:
                Text2("Tabmoc: I heard that the Holy Itucher was somewhere around",units.Recils.Portrait,units.Tabmoc.Portrait)
                line2("here and wanted to see it for myself.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 54:
                Text2("Tabmoc: What are you doing here?",units.Recils.Portrait,units.Tabmoc.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 55:
                Text2("Recils: I'm on a mission with the Static army to go retrieve the",units.Recils.Portrait,units.Tabmoc.Portrait)
                line2("Holy Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 56:
                Text2("Tabmoc: So it really is here...",units.Recils.Portrait,units.Tabmoc.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 57:
                Text2("Tabmoc: Sounds interesting, mind if I come along?",units.Recils.Portrait,units.Tabmoc.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 58:
                Text3("[Recruit Tabmoc?]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
            elif CutsceneIndex == 59:
                if Qinput == True:
                    Text2("Tabmoc: Great.",units.Recils.Portrait,units.Tabmoc.Portrait)
                    CutsceneIndex += 1
                    
                else:
                    Text2("Tabmoc: Okay then.",units.Recils.Portrait, units.Tabmoc.Portrait)
                    CutsceneIndex += 1
                    
            elif CutsceneIndex == 60:
                if Qinput == True:
                    Text3("[Tabmoc has joined your party]")
                    units.UnitsAlive.append(units.Tabmoc)
                    units.UnitsRecruited.append(units.Tabmoc)
                    CutsceneIndex += 1
                    ClearInputs()
                    
                else:
                    CutsceneIndex += 1
                    ClearInputs()
                    Cutscene()
        elif CutsceneIndex <= 60:
            CutsceneIndex = 61
            Cutscene()
        elif units.Xuirfth in units.UnitsRecruited and CutsceneIndex <= 72:
            if CutsceneIndex == 61:
                Text2("Proton: You must be Xuirurth.",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 62:
                Text2("Xuirurth: Yes.",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 63:
                Text2("Proton: I am Proton Xurr, you might know me as Xuirond.",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 64:
                Text2("Xuirurth: Xuirond?",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 65:
                Text2("Proton: Yes.",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 66:
                Text2("Proton: Xuirventh and Xuirfth told me about it.",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 67:
                Text2("Xuirurth: Why are you here?",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 68:
                Text2("Proton: I've come to take back the Holy Itucher from the Shadow.",units.Proton.Portrait,units.Xuirurth.Portrait)
                line2("Realm.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 69:
                Text2("Xuirurth: So the Shadow Realm has obtained the holy weapon...",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 70:
                Text2("Xuirurth: Though I just escaped, it would pain me not to help you",units.Proton.Portrait,units.Xuirurth.Portrait)
                line2("stop them.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 71:
                Text2("Proton: We'll be leaving soon, but you're free to join us.",units.Proton.Portrait,units.Xuirurth.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 72:
                Text3("[Xuirurth joined your party!]")
                units.UnitsAlive.append(units.Xuirurth)
                units.UnitsRecruited.append(units.Xuirurth)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 72:
            CutsceneIndex = 73
            Cutscene()
        elif units.Eg in units.UnitsAlive and units.Lacirtcele in units.UnitsAlive and CutsceneIndex <= 84:
            if CutsceneIndex == 73:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 74:
                Text2("Lacirtcele: Swag.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 75:
                Text2("Eg: Based.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 76:
                Text2("Lacirtcele: Swag.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 77:
                Text2("Eg: Based.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 78:
                Text2("Lacirtcele: Swag.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 79:
                Text2("Eg: Based.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 80:
                Text2("Lacirtcele: Swag.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 81:
                Text2("Eg: Based.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 82:
                Text2("Lacirtcele: Swag.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 83:
                Text2("Eg: Based.",units.Lacirtcele.Portrait,units.Eg.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 84:
                Text3("[Lacirtcele and Eg leveled up!]")
                select.InstantLevelUp(units.Lacirtcele,3)
                select.InstantLevelUp(units.Eg,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 84:
            CutsceneIndex = 85
            Cutscene()
        elif units.YungPoggers in units.UnitsAlive and units.Xuirer in units.UnitsAlive and CutsceneIndex <= 90:
            if CutsceneIndex == 85:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 86:
                Text2("Xuirer: Are the preperations nearing completion?",units.Xuirer.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 87:
                Text2("Yung Poggers: Yes.",units.Xuirer.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 88:
                Text2("Yung Poggers: It is inevitable.",units.Xuirer.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 89:
                Text2("Xuirer: It is inevitable.",units.Xuirer.Portrait,units.YungPoggers.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 90:
                Text3("[Xuirer and Yung Poggers leveled up!]")
                select.InstantLevelUp(units.Xuirer,3)
                select.InstantLevelUp(units.YungPoggers,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 90:
            CutsceneIndex = 91
            Cutscene()
        elif units.Wodahs in units.UnitsAlive and units.Repins in units.UnitsAlive and CutsceneIndex <= 109:
            if CutsceneIndex == 91:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 92:
                Text2("Wodahs: So, we're finally going to get the Itucher...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 93:
                Text2("Wodahs: I thought you would've been more excited.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 94:
                Text2("Repins: ...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 95:
                Text2("Repins: I'm still processing the fact it's actually happening...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 96:
                Text2("Repins: And what I'll do once I return home...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 97:
                Text2("Wodahs: Where is your home anyways? You've never told me where",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("you're from.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 98:
                Text2("Repins: I'm from Quad, but I moved to Static after the genocide.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 99:
                Text2("Repins: I haven't been to either in years, though.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 100:
                Text2("Wodahs: You should come back to Static every once in a while. If you",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("want, you could probably join with a good rank the army since you've")
                line3("helped us get the Itucher.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 101:
                Text2("Wodahs: Probably won't be able to join the EOS though, Erif's",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("already got the fire element covered and probably won't")
                line3("retire anytime soon.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 102:
                Text2("Repins: Erif?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 103:
                Text2("Wodahs: Huh, you know her?",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 104:
                Text2("Wodahs: Red hair, sword user, literally hot, won't",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("stop talking about the Quad Genocide, has two brothers...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 105:
                Text2("Repins: Yeah, I've met her before.",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 106:
                Text2("Wodahs: Hmm... that means you've got ties to multiple EOS",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("members.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 107:
                Text2("Wodahs: You could definitely get some promotions in the",units.Wodahs.Portrait,units.Repins.Portrait)
                line2("army with that.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 108:
                Text2("Repins: ...",units.Wodahs.Portrait,units.Repins.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 109:
                Text3("[Wodahs and Repins leveled up!]")
                select.InstantLevelUp(units.Wodahs,3)
                select.InstantLevelUp(units.Repins,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 109:
            CutsceneIndex = 110
            Cutscene()
        elif units.Erif in units.UnitsAlive and units.Yranecrem in units.UnitsAlive and CutsceneIndex <= 124:
            if CutsceneIndex == 110:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 111:
                Text2("Erif: Yranecrem, why are you using an axe?",units.Erif.Portrait,units.Yranecrem.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 112:
                Text2("Yranecrem: Why am I using an axe?",units.Erif.Portrait,units.Yranecrem.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 113:
                Text2("Erif: Yes, wouldn't a sword be much faster and accurate?",units.Erif.Portrait,units.Yranecrem.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 114:
                Text2("Yranecrem: I choose to use an axe to limit suffering.",units.Erif.Portrait,units.Yranecrem.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 115:
                Text2("Yranecrem: With an axe, I can execute someone with single",units.Erif.Portrait,units.Yranecrem.Portrait)
                line2("strike to the neck; a quick death with minimal suffering.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 116:
                Text2("Yranecrem: The weight of the axe also slows me down, and prevents",units.Erif.Portrait,units.Yranecrem.Portrait)
                line2("me from killing apart from when it's truly necessary.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 117:
                Text2("Yranecrem: Though I do not want to contribute to the suffering of",units.Erif.Portrait,units.Yranecrem.Portrait)
                line2("war, it is inevitable that I must to survive.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 118:
                Text2("Erif: What if you want the enemy to suffer?",units.Erif.Portrait,units.Yranecrem.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 119:
                Text2("Yranecrem: Why would I want that? That would only lead to",units.Erif.Portrait,units.Yranecrem.Portrait)
                line2("further powering the cycle of war and hatred.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 120:
                Text2("Erif: What if the enemy desrved to suffer, and anything less",units.Erif.Portrait,units.Yranecrem.Portrait)
                line2("would be dishonorable to those they harmed?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 121:
                Text2("Yranecrem: ...",units.Erif.Portrait,units.Yranecrem.Portrait)
                CutsceneIndex = 124
                
            elif CutsceneIndex == 124:
                Text3("[Erif and Yranecrem leveled up!]")
                select.InstantLevelUp(units.Erif,3)
                select.InstantLevelUp(units.Yranecrem,3)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 124:
            CutsceneIndex = 125
            Cutscene()
        elif CutsceneIndex == 125:
            Text1("Proton: It's time to enter the Shadow Realm...",units.Proton.Portrait)
            CutsceneIndex += 1 
            
        elif CutsceneIndex == 126:
            Text1("Proton: We'll activate the portal at the Location of Binding and",units.Proton.Portrait)
            line2("enter from there.")
            CutsceneIndex += 1 
            
        elif CutsceneIndex == 127:
            Text3("...")
            CutsceneIndex = 0
            Chapter = "Chapter 22a"
            
    elif Chapter == "Chapter 21b": #=====================Chapter21b===============================================================
        ChapterLevel = 114
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 21b]")
            line2("[Nolavillian Mountain Range, Northern Nolavillia]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dim grey")
            
            UnitsToPlace = placeunits.Chapter21aEnemies
            UnitFormation = placeunits.Chapter21aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            
            Text2("Omega: Someone's here...",units.OmegaXuirist.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 2:
            
            placeunits.PlacePlayerUnits()
            
            Text1("Proton: ...",units.Proton.Portrait)
            line2("we must proceed.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 4:
            Text1("Break: Agh! Who is this guy? I've got to get out of here!",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            CutsceneIndex = 0
            Chapter = "Chapter 22b"
            Cutscene()  
    elif Chapter == "Chapter 22a": #=====================Chapter22a===============================================================
        ChapterLevel = 41
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[End of Act III]")
            CutsceneIndex += 1
            
            print(units.UnitsRecruited)
        elif CutsceneIndex == 1:
            Text2("Proton: Survived",units.Proton.Portrait,units.Scien.Portrait)
            if units.Quest in units.UnitsAlive:
                line2("Quest: Survived")
            elif units.Quest in units.UnitsRecruited:
                line2("Quest: Defeated")
            else:
                line2("Quest: Not Recruited")
            if units.Scien in units.UnitsAlive:
                line3("Scien: Survived")
            elif units.Scien in units.UnitsRecruited:
                line3("Scien: Defeated")
            else:
                line3("Scien: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            if units.Romra in units.UnitsAlive:
                Text2("Romra: Survived",units.Romra.Portrait,units.TnemecalperII.Portrait)
            elif units.Romra in units.UnitsRecruited:
                Text2("Romra: Defeated",units.Romra.Portrait,units.TnemecalperII.Portrait)
            else:
                Text2("Romra: Not Recruited",units.Romra.Portrait,units.TnemecalperII.Portrait)
            if units.TnemecalperI in units.UnitsAlive:
                line2("Tnemecalper I: Survived")
            elif units.TnemecalperI in units.UnitsRecruited:
                line2("Tnemecalper I: Defeated")
            else:
                line2("Tnemecalper I: Not Recruited")
            if units.TnemecalperII in units.UnitsAlive:
                line3("Tnemecalper II: Survived")
            elif units.TnemecalperII in units.UnitsRecruited:
                line3("Tnemecalper II: Defeated")
            else:
                line3("Tnemecalper II: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            if units.TnemecalperIII in units.UnitsAlive:
                Text2("Tnemecalper III: Survived",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            elif units.TnemecalperIII in units.UnitsRecruited:
                Text2("Tnemecalper III: Defeated",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            else:
                Text2("Tnemecalper III: Not Recruited",units.TnemecalperIII.Portrait,units.Lacirtcele.Portrait)
            if units.TnemecalperIV in units.UnitsAlive:
                line2("Tnemecalper IV: Survived")
            elif units.TnemecalperIV in units.UnitsRecruited:
                line2("Tnemecalper IV: Defeated")
            else:
                line2("Tnemecalper IV: Not Recruited")
            if units.Lacirtcele in units.UnitsAlive:
                line3("Lacirtcele: Survived")
            elif units.Lacirtcele in units.UnitsRecruited:
                line3("Lacirtcele: Defeated")
            else:
                line3("Lacirtcele: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            if units.Damagein in units.UnitsAlive:
                Text2("Damagein: Survived",units.Damagein.Portrait,units.Wob.Portrait)
            elif units.Damagein in units.UnitsRecruited:
                Text2("Damagein: Defeated",units.Damagein.Portrait,units.Wob.Portrait)
            else:
                Text2("Damagein: Not Recruited",units.Damagein.Portrait,units.Wob.Portrait)
            if units.Healia in units.UnitsAlive:
                line2("Healia: Survived")
            elif units.Healia in units.UnitsRecruited:
                line2("Healia: Defeated")
            else:
                line2("Healia: Not Recruited")
            if units.Wob in units.UnitsAlive:
                line3("Wob: Survived")
            elif units.Wob in units.UnitsRecruited:
                line3("Wob: Defeated")
            else:
                line3("Wob: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            if units.Bladen in units.UnitsAlive:
                Text2("Bladen: Survived",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            elif units.Bladen in units.UnitsRecruited:
                Text2("Bladen: Defeated",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            else:
                Text2("Bladen: Not Recruited",units.Bladen.Portrait,units.PlayableBladeous.Portrait)
            if units.Wodahs in units.UnitsAlive:
                line2("Wodahs: Survived")
            elif units.Wodahs in units.UnitsRecruited:
                line2("Wodahs: Defeated")
            else:
                line2("Wodahs: Not Recruited")
            if units.PlayableBladeous in units.UnitsAlive:
                line3("Bladeous: Survived")
            elif units.PlayableBladeous in units.UnitsRecruited:
                line3("Bladeous: Defeated")
            else:
                line3("Bladeous: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            if units.Azure in units.UnitsAlive:
                Text2("Azure: Survived",units.Azure.Portrait,units.Erif.Portrait)
            elif units.Azure in units.UnitsRecruited:
                Text2("Azure: Defeated",units.Azure.Portrait,units.Erif.Portrait)
            else:
                Text2("Azure: Not Recruited",units.Azure.Portrait,units.Erif.Portrait)
            if units.Fael in units.UnitsAlive:
                line2("Fael: Survived")
            elif units.Fael in units.UnitsRecruited:
                line2("Fael: Defeated")
            else:
                line2("Fael: Not Recruited")
            if units.Erif in units.UnitsAlive:
                line3("Erif: Survived")
            elif units.Erif in units.UnitsRecruited:
                line3("Erif: Defeated")
            else:
                line3("Erif: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            if units.Vruh in units.UnitsAlive:
                Text2("Vruh: Survived",units.Vruh.Portrait,units.Repins.Portrait)
            elif units.Vruh in units.UnitsRecruited:
                Text2("Vruh: Defeated",units.Vruh.Portrait,units.Repins.Portrait)
            else:
                Text2("Vruh: Not Recruited",units.Vruh.Portrait,units.Repins.Portrait)
            if units.Recils in units.UnitsAlive:
                line2("Recils: Survived")
            elif units.Recils in units.UnitsRecruited:
                line2("Recils: Defeated")
            else:
                line2("Recils: Not Recruited")
            if units.Repins in units.UnitsAlive:
                line3("Repins: Survived")
            elif units.Repins in units.UnitsRecruited:
                line3("Repins: Defeated")
            else:
                line3("Repins: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            if units.Relaeh in units.UnitsAlive:
                Text2("Relaeh: Survived",units.Relaeh.Portrait,units.Lias.Portrait)
            elif units.Relaeh in units.UnitsRecruited:
                Text2("Relaeh: Defeated",units.Relaeh.Portrait,units.Lias.Portrait)
            else:
                Text2("Relaeh: Not Recruited",units.Relaeh.Portrait,units.Lias.Portrait)
            if units.Eulb in units.UnitsAlive:
                line2("Eulb: Survived")
            elif units.Eulb in units.UnitsRecruited:
                line2("Eulb: Defeated")
            else:
                line2("Eulb: Not Recruited")
            if units.Lias in units.UnitsAlive:
                line3("Lias: Survived")
            elif units.Lias in units.UnitsRecruited:
                line3("Lias: Defeated")
            else:
                line3("Lias: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            if units.Fieht in units.UnitsAlive:
                Text2("Fieht: Survived",units.Fieht.Portrait,units.Eg.Portrait)
            elif units.Fieht in units.UnitsRecruited:
                Text2("Fieht: Defeated",units.Fieht.Portrait,units.Eg.Portrait)
            else:
                Text2("Fieht: Not Recruited",units.Fieht.Portrait,units.Eg.Portrait)
            if units.Rethgif in units.UnitsAlive:
                line2("Rethgif: Survived")
            elif units.Rethgif in units.UnitsRecruited:
                line2("Rethgif: Defeated")
            else:
                line2("Rethgif: Not Recruited")
            if units.Eg in units.UnitsAlive:
                line3("Eg: Survived")
            elif units.Eg in units.UnitsRecruited:
                line3("Eg: Defeated")
            else:
                line3("Eg: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            if units.B in units.UnitsAlive:
                Text2("B: Survived",units.B.Portrait,units.Elbon.Portrait)
            elif units.B in units.UnitsRecruited:
                Text2("B: Defeated",units.B.Portrait,units.Elbon.Portrait)
            else:
                Text2("B: Not Recruited",units.B.Portrait,units.Elbon.Portrait)
            if units.Xuirventh in units.UnitsAlive:
                line2("Xuirventh: Survived")
            elif units.Xuirventh in units.UnitsRecruited:
                line2("Xuirventh: Defeated")
            else:
                line2("Xuirventh: Not Recruited")
            if units.Elbon in units.UnitsAlive:
                line3("Elbon: Survived")
            elif units.Elbon in units.UnitsRecruited:
                line3("Elbon: Defeated")
            else:
                line3("Elbon: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            if units.Xuirfth in units.UnitsAlive:
                Text2("Xuirfth: Survived",units.Xuirfth.Portrait,units.Dliug.Portrait)
            elif units.Xuirfth in units.UnitsRecruited:
                Text2("Xuirfth: Defeated",units.Xuirfth.Portrait,units.Dliug.Portrait)
            else:
                Text2("Xuirfth: Not Recruited",units.Xuirfth.Portrait,units.Dliug.Portrait)
            if units.Xuirer in units.UnitsAlive:
                line2("Xuirer: Survived")
            elif units.Xuirer in units.UnitsRecruited:
                line2("Xuirer: Defeated")
            else:
                line2("Xuirer: Not Recruited")
            if units.Dliug in units.UnitsAlive:
                line3("Dliug: Survived")
            elif units.Dliug in units.UnitsRecruited:
                line3("Dliug: Defeated")
            else:
                line3("Dliug: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            if units.Exa in units.UnitsAlive:
                Text2("Exa: Survived",units.Exa.Portrait,units.Geomer.Portrait)
            elif units.Exa in units.UnitsRecruited:
                Text2("Exa: Defeated",units.Exa.Portrait,units.Geomer.Portrait)
            else:
                Text2("Exa: Not Recruited",units.Exa.Portrait,units.Geomer.Portrait)
            if units.Yranecrem in units.UnitsAlive:
                line2("Yranecrem: Survived")
            elif units.Yranecrem in units.UnitsRecruited:
                line2("Yranecrem: Defeated")
            else:
                line2("Xuirer: Not Recruited")
            if units.Geomer in units.UnitsAlive:
                line3("Geomer: Survived")
            elif units.Geomer in units.UnitsRecruited:
                line3("Geomer: Defeated")
            else:
                line3("Geomer: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            if units.Box in units.UnitsAlive:
                Text2("Box: Survived",units.Box.Portrait,units.YungPoggers.Portrait)
            elif units.Box in units.UnitsRecruited:
                Text2("Box: Defeated",units.Box.Portrait,units.YungPoggers.Portrait)
            else:
                Text2("Box: Not Recruited",units.Box.Portrait,units.YungPoggers.Portrait)
            if units.NOTOS in units.UnitsAlive:
                line2("NOTOS: Survived")
            elif units.NOTOS in units.UnitsRecruited:
                line2("NOTOS: Defeated")
            else:
                line2("NOTOS: Not Recruited")
            if units.YungPoggers in units.UnitsAlive:
                line3("Yung Poggers: Survived")
            elif units.YungPoggers in units.UnitsRecruited:
                line3("Yung Poggers: Defeated")
            else:
                line3("Yung Poggers: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            if units.Dnefed in units.UnitsAlive:
                Text2("Dnefed: Survived",units.Dnefed.Portrait,units.Gnirif.Portrait)
            elif units.Dnefed in units.UnitsRecruited:
                Text2("Dnefed: Defeated",units.Dnefed.Portrait,units.Gnirif.Portrait)
            else:
                Text2("Dnefed: Not Recruited",units.Dnefed.Portrait,units.Gnirif.Portrait)
            if units.Thgif in units.UnitsAlive:
                line2("Thgif: Survived")
            elif units.Thgif in units.UnitsRecruited:
                line2("Thgif: Defeated")
            else:
                line2("Thgif: Not Recruited")
            if units.Gnirif in units.UnitsAlive:
                line3("Gnirif: Survived")
            elif units.Gnirif in units.UnitsRecruited:
                line3("Gnirif: Defeated")
            else:
                line3("Gnirif: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            if units.Cigam in units.UnitsAlive:
                Text2("Cigam: Survived",units.Cigam.Portrait,units.Fiyghtrr.Portrait)
            elif units.Cigam in units.UnitsRecruited:
                Text2("Cigam: Defeated",units.Cigam.Portrait,units.Fiyghtrr.Portrait)
            else:
                Text2("Cigam: Not Recruited",units.Cigam.Portrait,units.Fiyghtrr.Portrait)
            if units.Omega in units.UnitsAlive:
                line2("Omega: Survived")
            elif units.Omega in units.UnitsRecruited:
                line2("Omega: Defeated")
            else:
                line2("Omega: Not Recruited")
            if units.Fiyghtrr in units.UnitsAlive:
                line3("Fiyghtrr: Survived")
            elif units.Fiyghtrr in units.UnitsRecruited:
                line3("Fiyghtrr: Defeated")
            else:
                line3("Fiyghtrr: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            if units.Recalper in units.UnitsAlive:
                Text2("Recalper: Survived",units.Recalper.Portrait,units.Xuirurth.Portrait)
            elif units.Recalper in units.UnitsRecruited:
                Text2("Recalper: Defeated",units.Recalper.Portrait,units.Xuirurth.Portrait)
            else:
                Text2("Recalper: Not Recruited",units.Recalper.Portrait,units.Xuirurth.Portrait)
            if units.Tabmoc in units.UnitsAlive:
                line2("Tabmoc: Survived")
            elif units.Tabmoc in units.UnitsRecruited:
                line2("Tabmoc: Defeated")
            else:
                line2("Tabmoc: Not Recruited")
            if units.Xuirurth in units.UnitsAlive:
                line3("Xuirurth: Survived")
            elif units.Xuirurth in units.UnitsRecruited:
                line3("Xuirurth: Defeated")
            else:
                line3("Xuirurth: Not Recruited")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 22a]")
            line2("[Enterance, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
            print(units.UnitsRecruited)
        elif CutsceneIndex == 18:
            screensetup.BattleScreen.bgcolor("dim gray")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif moves.ErifWasThere in units.Repins.Attacks and CutsceneIndex <= 68:
            if units.Erif in units.UnitsAlive:
                if CutsceneIndex == 19:
                    Text1("Proton: Wait, there's someone at the enterance.",units.Proton.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 20:
                    Text1("???: Is someone there?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 21:
                    Text1("???: Hm... Are they here to get the Itucher?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 22:
                    Text1("???: ...",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 23:
                    Text1("Erif: Wait, that person... are they...",units.Erif.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 24:
                    Text1("Erif: No, there's no way...",units.Erif.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 25:
                    Text1("Proton: You there, get out of the way. We're here",units.Proton.Portrait)
                    line2("to get the Holy Itucher but I'd prefer to minimize")
                    line3("the violence.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 26:
                    Text2("???: Sorry, that's something that I can't do.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 27:
                    Text2("???: The sacrifices that I've made to come here... all of these",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("years... I'm not going to be stopped by the likes of you.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 28:
                    Text2("???: I, Repins Blaze, shall wield the Holy Itucher.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 29:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 30:
                    Text2("Erif: Repins?",units.Erif.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 31:
                    Text2("Repins: Erif? Why is she here?",units.Erif.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 32:
                    Text2("Erif: Repins? Are you really alive?",units.Erif.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 33:
                    Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 34:
                    Text2("Repins: (This group, I remember it now... Erif was there",units.Erif.Portrait,units.Repins2.Portrait)
                    line2("at the Bipole Sea...)")
                    CutsceneIndex += 1
                    
                elif moves.WobWasThere in units.Repins.Attacks and units.Wob not in units.UnitsAlive:
                    if CutsceneIndex == 35:
                        Text2("Repins: (Wasn't Wob with them as well?)",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 36:
                        Text2("Repins: Erif, where is Wob?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 37:
                        Text2("Erif: So, it really is you?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 38:
                        Text2("Repins: Answer me, Erif. Where is Wob?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 39:
                        Text2("Erif: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 40:
                        Text2("Erif: He's dead.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 41:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 42:
                        Text2("Repins: You're... kidding me... right?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 43:
                        Text2("Repins: After all of this...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 44:
                        Text2("Repins: Heh...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 45:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 46:
                        Text2("Repins: I've become a villain, Erif...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 47:
                        Text2("Repins: The things that I've done, they truly are",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("selfish.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 48:
                        Text2("Repins: With Wob dead, you're my only excuse left to",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("justify them.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 49:
                        Text2("Repins: So forgive me for what I'm going to do...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 50:
                        Text2("Erif: What are you talking about?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 51:
                        Text2("Erif: Repins... I don't know how you're alive or what",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("you've done, but fighting here won't help anything.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 52:
                        Text2("Erif: You won't be able to get the Itucher on your own,",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("the research center is too secure for that.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 53:
                        Text2("Erif: You can work with us. We can retrieve the",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("Itucher and go back to Static.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 54:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 55:
                        Text2("Repins: I want this to be over.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 56:
                        Text2("Repins: I want to go back to when we were all alive, back",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("before the genocide.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 57:
                        Text2("Repins: But that's not possible.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 58:
                        Text2("Repins: Erif, what will happen after you get the Itucher?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 59:
                        Text2("Repins: I wanted to rebuild Quad and live a peaceful life again,",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("but that's not possible anymore.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 60:
                        Text2("Repins: Even if I get the Itucher own my own... you guys won't stop,",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("will you?")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 61:
                        Text2("Repins: I won't be able to win a battle against your army...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 62:
                        Text2("Repins: I can't kill you, Erif.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 63:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 64:
                        Text2("Repins: Everything that I've done, it really was useless, wasn't it?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 65:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 66:
                        Text2("Repins: I give up, I've lost.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 67:
                        Text2("Repins: And with my now failed existence, I'll help you.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 68:
                        Text3("[Repins joined your party]")
                        units.UnitsAlive.append(units.Repins2)
                        units.UnitsRecruited.append(units.Repins2)
                        CutsceneIndex += 1
                        
                else:
                    if CutsceneIndex == 35:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex = 46
                        
                    elif CutsceneIndex == 46:
                        Text2("Repins: I've become a villain, Erif...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 47:
                        Text2("Repins: The things that I've done, they truly are",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("selfish.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 48:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 49:
                        Text2("Repins: So forgive me for what I'm going to do...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 50:
                        Text2("Erif: What are you talking about?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 51:
                        Text2("Erif: Repins... I don't know how you're alive or what",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("you've done, but fighting here won't help anything.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 52:
                        Text2("Erif: You won't be able to get the Itucher on your own,",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("the research center is too secure for that.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 53:
                        Text2("Erif: You can work with us. We can retrieve the",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("Itucher and go back to Static.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 54:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 55:
                        Text2("Repins: I want this to be over.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 56:
                        Text2("Repins: I want to go back to when we were all alive, back",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("before the genocide.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 57:
                        Text2("Repins: But that's not possible.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 58:
                        Text2("Repins: Erif, what will happen after you get the Itucher?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 59:
                        Text2("Repins: I wanted to rebuild Quad and live a peaceful life again,",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("but that's not possible anymore.")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 60:
                        Text2("Repins: Even if I get the Itucher own my own... you guys won't stop,",units.Erif.Portrait,units.Repins2.Portrait)
                        line2("will you?")
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 61:
                        Text2("Repins: I won't be able to win a battle against your army...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 62:
                        Text2("Repins: I can't kill you, Erif.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 63:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 64:
                        Text2("Repins: Everything that I've done, it really was useless, wasn't it?",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 65:
                        Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 66:
                        Text2("Repins: I give up, I've lost.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 67:
                        Text2("Repins: And with my now failed existence, I'll help you.",units.Erif.Portrait,units.Repins2.Portrait)
                        CutsceneIndex += 1
                        
                    elif CutsceneIndex == 68:
                        Text3("[Repins joined your party]")
                        units.UnitsAlive.append(units.Repins2)
                        units.UnitsRecruited.append(units.Repins2)
                        CutsceneIndex += 1
                        
            elif units.Wob in units.UnitsAlive:
                if CutsceneIndex == 19:
                    Text1("Proton: Wait, there's someone at the enterance.",units.Proton.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 20:
                    Text1("???: Is someone there?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 21:
                    Text1("???: Hm... Are they here to get the Itucher?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 22:
                    Text1("???: ...",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 23:
                    Text1("Wob: Wait, is that..",units.Wob.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 24:
                    Text1("Wob: No, that's not possible...",units.Wob.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 25:
                    Text1("Proton: You there, get out of the way. We're here",units.Proton.Portrait)
                    line2("to get the Holy Itucher but I'd prefer to minimize")
                    line3("the violence.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 26:
                    Text2("???: Sorry, that's something that I can't do.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 27:
                    Text2("???: The sacrifices that I've made to come here... all of these",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("years... I'm not going to be stopped by the likes of you.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 28:
                    Text2("???: I, Repins Blaze, shall wield the Holy Itucher.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 29:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 30:
                    Text2("Wob: Repins?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 31:
                    Text2("Repins: Wob? Why is he here?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 32:
                    Text2("Wob: Repins? Aren't you... dead?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 33:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 34:
                    Text2("Repins: (This group, I remember it now... Wob was there",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("at the Bipole Sea...)")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 35:
                    Text2("Repins: (Wasn't Erif with them as well?)",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 36:
                    Text2("Repins: Wob, where is Erif?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 37:
                    Text2("Wob: I thought you died, Repins...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 38:
                    Text2("Repins: Answer me, Wob. Where is Erif?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 39:
                    Text2("Wob: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 40:
                    Text2("Wob: She's dead.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 41:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 42:
                    Text2("Repins: You're... kidding me... right?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 43:
                    Text2("Repins: After all of this...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 44:
                    Text2("Repins: Heh...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 45:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 46:
                    Text2("Repins: I've become a villain, Wob...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 47:
                    Text2("Repins: The things that I've done, they truly are",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("selfish.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 48:
                    Text2("Repins: With Erif dead, you're my only excuse left to",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("justify them.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 49:
                    Text2("Repins: So forgive me for what I'm going to do...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 50:
                    Text2("Wob: What are you talking about?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 51:
                    Text2("Wob: I don't know how you're alive or what you did,",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("but fighting here won't help.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 52:
                    Text2("Wob: You won't be able to get the Itucher on your own,",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("the research center is too secure for that.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 53:
                    Text2("Wob: You can work with us. We can retrieve the",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("Itucher and go back to Static.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 54:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 55:
                    Text2("Repins: I want this to be over.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 56:
                    Text2("Repins: I want to go back to when we were all alive, back",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("before the genocide.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 57:
                    Text2("Repins: But that's not possible.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 58:
                    Text2("Repins: Wob, what will happen after you get the Itucher?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 59:
                    Text2("Repins: I wanted to rebuild Quad and live a peaceful life again,",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("but that's not possible anymore.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 60:
                    Text2("Repins: Even if I get the Itucher own my own... you guys won't stop,",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("will you?")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 61:
                    Text2("Repins: I won't be able to win a battle against your army...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 62:
                    Text2("Repins: I can't kill you, Wob.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 63:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 64:
                    Text2("Repins: Everything that I've done, it really was useless, wasn't it?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 65:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 66:
                    Text2("Repins: I give up, I've lost.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 67:
                    Text2("Repins: And with my now failed existence, I'll help you.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 68:
                    Text3("[Repins joined your party]")
                    units.UnitsAlive.append(units.Repins2)
                    units.UnitsRecruited.append(units.Repins2)
                    CutsceneIndex += 1
                    
            elif moves.WobWasThere in units.Repins.Attacks and units.Wob not in units.UnitsRecruited:
                if CutsceneIndex == 19:
                    Text1("Proton: Wait, there's someone at the enterance.",units.Proton.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 20:
                    Text1("???: Is someone there?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 21:
                    Text1("???: Hm... Are they here to get the Itucher?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 22:
                    Text1("???: ...",units.Repins2.Portrait)
                    CutsceneIndex = 25
                    
                elif CutsceneIndex == 25:
                    Text1("Proton: You there, get out of the way. We're here",units.Proton.Portrait)
                    line2("to get the Holy Itucher but I'd prefer to minimize")
                    line3("the violence.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 26:
                    Text2("???: Sorry, that's something that I can't do.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 27:
                    Text2("???: The sacrifices that I've made to come here... all of these",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("years... I'm not going to be stopped by the likes of you.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 28:
                    Text2("???: I, Repins Blaze, shall wield the Holy Itucher.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 29:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex = 34
                    
                elif CutsceneIndex == 34:
                    Text2("Repins: (This group, I remember it now... Erif was there",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("at the Bipole Sea...)")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 35:
                    Text2("Repins: (And Wob, he was there as well...)",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 36:
                    Text2("Repins: Wasn't Erif and Wob Blaze in your group?",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 37:
                    Text2("Proton: Yes, they were.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 38:
                    Text2("Repins: Where are they now?",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 39:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 40:
                    Text2("Repins: They're dead.",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 41:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 42:
                    Text2("Repins: You're joking... aren't you?",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 43:
                    Text2("Repins: Both of them... dead...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 44:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 45:
                    Text2("Repins: Heh...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 46:
                    Text2("Repins: It was all a waste...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 47:
                    Text2("Repins: .",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 48:
                    Text2("Repins: ..",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 49:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 50:
                    Text2("(Repins strangely smiles)",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 51:
                    Text2("Repins: AH HA HA HA HA HA HA HA HA HA HA HA HA",units.Proton.Portrait,units.Repins2.Portrait)  
                    line2("HA HA HA HA HA HA HA HA HA HA HA HA HA HA HA HA")
                    line3("HA HA HA HA HA HA HA HA HA HA HA HA HA HA HA HA")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 52:
                    Text2("Repins: YOU MEAN TO TELL ME THAT AFTER *EVERYTHING*",units.Proton.Portrait,units.Repins2.Portrait)  
                    line2("THAT I DID...")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 53:
                    Text2("Repins: ALL OF THESE YEARS...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 54:
                    Text2("Repins: THEY HAVE THE NERVE TO GET *KILLED*!?",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 55:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 56:
                    Text2("Repins: I'VE GOT NOTHING TO LOSE AND EVERYTHING TO GAIN...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 57:
                    Text2("Repins: I'LL GET THE HOLY ITUCHER AND KILL YOU ALL...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 58:
                    Text2("Repins: I'LL REBUILD QUAD AND RULE AN EMPIRE...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 59:
                    Text2("Repins: I'LL BURN SINE TO THE GROUND...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 60:
                    Text2("Repins: I'LL MAKE THIS WORLD FEEL PAIN... THE PAIN",units.Proton.Portrait,units.Repins2.Portrait)  
                    line2("THAT I'VE FELT...")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 61:
                    Text3("(Repins injects something into his arm and suddenly disappears)")  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 62:
                    units.Repins.Attacks.append(moves.BothDead)
                    Text1("Proton: ...",units.Proton.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 63:
                    Text1("Proton: We need to keep going.",units.Proton.Portrait)  
                    CutsceneIndex = 69
                    
            else:
                if CutsceneIndex == 19:
                    Text1("Proton: Wait, there's someone at the enterance.",units.Proton.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 20:
                    Text1("???: Is someone there?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 21:
                    Text1("???: Hm... Are they here to get the Itucher?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 22:
                    Text1("???: ...",units.Repins2.Portrait)
                    CutsceneIndex = 25
                    
                elif CutsceneIndex == 25:
                    Text1("Proton: You there, get out of the way. We're here",units.Proton.Portrait)
                    line2("to get the Holy Itucher but I'd prefer to minimize")
                    line3("the violence.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 26:
                    Text2("???: Sorry, that's something that I can't do.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 27:
                    Text2("???: The sacrifices that I've made to come here... all of these",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("years... I'm not going to be stopped by the likes of you.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 28:
                    Text2("???: I, Repins Blaze, shall wield the Holy Itucher.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 29:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex = 34
                    
                elif CutsceneIndex == 34:
                    Text2("Repins: (This group, I remember it now... Erif was there",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("at the Bipole Sea...)")
                    CutsceneIndex = 36
                    
                elif CutsceneIndex == 36:
                    Text2("Repins: Wasn't Erif Blaze in your group?",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 37:
                    Text2("Proton: Yes, she was.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 38:
                    Text2("Repins: Where is she now?",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 39:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 40:
                    Text2("Proton: She's dead.",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 41:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 42:
                    Text2("Repins: You're joking... aren't you?",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 43:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 44:
                    Text2("Repins: After all of this...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 45:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 46:
                    Text2("Repins: No, I still have Wob...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 47:
                    Text2("Repins: I'll get the Holy Itucher... kill you... and return to Quad...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 48:
                    units.Repins.Attacks.append(moves.OneDead)
                    Text3("(Repins injects something into his arm and suddenly disappears)")  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 49:
                    Text1("Proton: ...",units.Proton.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 50:
                    Text1("Proton: We need to keep going.",units.Proton.Portrait)  
                    CutsceneIndex = 69
                    
        elif moves.WobWasThere in units.Repins.Attacks and CutsceneIndex <= 68:
            if units.Wob in units.UnitsAlive:
                if CutsceneIndex == 19:
                    Text1("Proton: Wait, there's someone at the enterance.",units.Proton.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 20:
                    Text1("???: Is someone there?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 21:
                    Text1("???: Hm... Are they here to get the Itucher?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 22:
                    Text1("???: ...",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 23:
                    Text1("Wob: Wait, is that..",units.Wob.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 24:
                    Text1("Wob: No, that's not possible...",units.Wob.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 25:
                    Text1("Proton: You there, get out of the way. We're here",units.Proton.Portrait)
                    line2("to get the Holy Itucher but I'd prefer to minimize")
                    line3("the violence.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 26:
                    Text2("???: Sorry, that's something that I can't do.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 27:
                    Text2("???: The sacrifices that I've made to come here... all of these",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("years... I'm not going to be stopped by the likes of you.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 28:
                    Text2("???: I, Repins Blaze, shall wield the Holy Itucher.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 29:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 30:
                    Text2("Wob: Repins?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 31:
                    Text2("Repins: Wob? Why is he here?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 32:
                    Text2("Wob: Repins? Aren't you... dead?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 33:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 34:
                    Text2("Repins: (This group, I remember it now... Wob was there",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("at the Bipole Sea...)")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 35:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex = 46
                    
                elif CutsceneIndex == 46:
                    Text2("Repins: I've become a villain, Wob...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 47:
                    Text2("Repins: The things that I've done, they truly are",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("selfish.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 48:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 49:
                    Text2("Repins: So forgive me for what I'm going to do...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 50:
                    Text2("Wob: What are you talking about?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 51:
                    Text2("Wob: I don't know what you did or how you're alive,",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("but fighting here won't help anything.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 52:
                    Text2("Wob: You won't be able to get the Itucher on your own,",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("the research center is too secure for that.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 53:
                    Text2("Wob: You can work with us. We can get the",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("Itucher and go back to Static.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 54:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 55:
                    Text2("Repins: I want this to be over.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 56:
                    Text2("Repins: I want to go back to when we were all alive, back",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("before the genocide.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 57:
                    Text2("Repins: But that's not possible.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 58:
                    Text2("Repins: Wob, what will happen after you get the Itucher?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 59:
                    Text2("Repins: I wanted to rebuild Quad and live a peaceful life again,",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("but that's not possible anymore.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 60:
                    Text2("Repins: Even if I get the Itucher own my own... you guys won't stop,",units.Wob.Portrait,units.Repins2.Portrait)
                    line2("will you?")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 61:
                    Text2("Repins: I won't be able to win a battle against your army...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 62:
                    Text2("Repins: I can't kill you, Wob.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 63:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 64:
                    Text2("Repins: Everything that I've done, it really was useless, wasn't it?",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 65:
                    Text2("Repins: ...",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 66:
                    Text2("Repins: I give up, I've lost.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 67:
                    Text2("Repins: And with my now failed existence, I'll help you.",units.Wob.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 68:
                    Text2("[Repins joined your party]")
                    units.UnitsAlive.append(units.Repins2)
                    units.UnitsRecruited.append(units.Repins2)
                    CutsceneIndex += 1
                    
            else:
                if CutsceneIndex == 19:
                    Text1("Proton: Wait, there's someone at the enterance.",units.Proton.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 20:
                    Text1("???: Is someone there?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 21:
                    Text1("???: Hm... Are they here to get the Itucher?",units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 22:
                    Text1("???: ...",units.Repins2.Portrait)
                    CutsceneIndex = 25
                    
                elif CutsceneIndex == 25:
                    Text1("Proton: You there, get out of the way. We're here",units.Proton.Portrait)
                    line2("to get the Holy Itucher but I'd prefer to minimize")
                    line3("the violence.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 26:
                    Text2("???: Sorry, that's something that I can't do.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 27:
                    Text2("???: The sacrifices that I've made to come here... all of these",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("years... I'm not going to be stopped by the likes of you.")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 28:
                    Text2("???: I, Repins Blaze, shall wield the Holy Itucher.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 29:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex = 34
                    
                elif CutsceneIndex == 34:
                    Text2("Repins: (This group, I remember it now... Wob was there",units.Proton.Portrait,units.Repins2.Portrait)
                    line2("at the Bipole Sea...)")
                    CutsceneIndex = 36
                    
                elif CutsceneIndex == 36:
                    Text2("Repins: Wasn't Wob Blaze in your group?",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 37:
                    Text2("Proton: Yes, he was.",units.Proton.Portrait,units.Repins2.Portrait)
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 38:
                    Text2("Repins: Where is he now?",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 39:
                    Text2("Proton: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 40:
                    Text2("Proton: He's dead.",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 41:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 42:
                    Text2("Repins: You're joking... aren't you?",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 43:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 44:
                    Text2("Repins: After all of this...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 45:
                    Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 46:
                    Text2("Repins: No, I still have Erif...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 47:
                    Text2("Repins: I'll get the Holy Itucher and return Quad...",units.Proton.Portrait,units.Repins2.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 48:
                    units.Repins.Attacks.append(moves.OneDead)
                    Text3("(Repins injects something into his arm and suddenly disappears)")  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 49:
                    Text1("Proton: ...",units.Proton.Portrait)  
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 50:
                    Text1("Proton: We need to keep going.",units.Proton.Portrait)  
                    CutsceneIndex = 69
                    
        elif CutsceneIndex <= 68:
            CutsceneIndex = 69
            Cutscene()
        elif CutsceneIndex == 69:
            Text3("(...)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 70:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Sector 1, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 71:
            screensetup.BattleScreen.bgcolor("light gray")
            
            UnitsToPlace = placeunits.Chapter22aEnemies
            UnitFormation = placeunits.Chapter22aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("???: It seems we may have some intruders.",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 72:
            Text1("???: I wonder why they're here... is it because",units.IfBoss.Portrait)
            line2("of the Holy Itucher...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 73:
            Text1("???: But how could they have found out? Did they",units.IfBoss.Portrait)
            line2("defeat Bladeous?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 74:
            Text1("???: Well, let's see how they do against us.",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 75:
            CutsceneIndex += 1
            BattleStarted = True
            # 
            
            
            
            
            
        elif units.Dnefed in units.UnitsAlive and units.Fieht in units.UnitsAlive and CutsceneIndex <= 86:
            if CutsceneIndex == 76:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 77:
                Text1("Dnefed: *sigh*",units.Dnefed.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 78:
                Text1("Dnefed: Why am I even doing this.",units.Dnefed.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 79:
                Text2("Fieht: Aren't you getting paid?",units.Dnefed.Portrait,units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 80:
                Text2("Dnefed: I don't even know.",units.Dnefed.Portrait,units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 81:
                Text2("Dnefed: I'm just trying to survive right now.",units.Dnefed.Portrait,units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 82:
                Text2("Fieht: So you aren't getting paid?",units.Dnefed.Portrait,units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 83:
                Text2("Dnefed: Proton spared me, so I guess you could count that",units.Dnefed.Portrait,units.Fieht.Portrait)
                line2("as payment.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 84:
                Text2("Fieht: So basically you got scammed.",units.Dnefed.Portrait,units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 85:
                Text2("Fieht: You see, I'm making a lot off of this adventure...",units.Dnefed.Portrait,units.Fieht.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 86:
                Text3("[Dnefed and Fieht leveled up!]")
                select.InstantLevelUp(units.Dnefed,4)
                select.InstantLevelUp(units.Fieht,4)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 86:
            CutsceneIndex = 87
            Cutscene()
        elif units.Eulb in units.UnitsAlive and units.Thgif in units.UnitsAlive and CutsceneIndex <= 95:
            if CutsceneIndex == 87:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 88:
                Text1("Eulb: Woah woah woah there why are we in the Shadow Realm?",units.Eulb.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 89:
                Text2("Thgif: Hm? What are you screaming about?",units.Eulb.Portrait,units.Thgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 90:
                Text2("Eulb: No one told me that we were going to be going to the",units.Eulb.Portrait,units.Thgif.Portrait)
                line2("Shadow Realm! I thought we were just going to save the world")
                line3("or something.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 91:
                Text2("Thgif: Proton told us multiple times about going to the Shadow",units.Eulb.Portrait,units.Thgif.Portrait)
                line2("Realm.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 92:
                Text2("Eulb: Did he really?",units.Eulb.Portrait,units.Thgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 93:
                Text2("Eulb: Ahhhhhh I should've been paying attention!",units.Eulb.Portrait,units.Thgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 94:
                Text2("Eulb: I never wanted to go to the Shadow Realm!",units.Eulb.Portrait,units.Thgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 95:
                Text3("[Eulb and Thgif leveled up!]")
                select.InstantLevelUp(units.Eulb,4)
                select.InstantLevelUp(units.Thgif,4)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 95:
            CutsceneIndex = 96
            Cutscene()
        elif units.Exa in units.UnitsAlive and units.Rethgif in units.UnitsAlive and CutsceneIndex <= 115:
            if CutsceneIndex == 96:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 97:
                Text1("Exa: Are you bored?",units.Exa.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 98:
                Text2("Rethgif: I am, actually.",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 99:
                Text2("Exa: Do you want to play a game?",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 100:
                Text2("Rethgif: A game?",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 101:
                Text2("Exa: Yes, a game.",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 102:
                Text2("Rethgif: Sure, why not.",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 103:
                Text2("Exa: Great! The game is called \"I am Going to",units.Exa.Portrait,units.Rethgif.Portrait)
                line2("Brutally Cut You Into Pieces Using My Axe\".")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 104:
                Text2("Rethgif: Woah there. I don't think that's going to",units.Exa.Portrait,units.Rethgif.Portrait)
                line2("be good for my health.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 105:
                Text2("Rethgif: How about we play \"Who Can Chug More Bottles",units.Exa.Portrait,units.Rethgif.Portrait)
                line2("of Laundry Cleaner in a Minute\"?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 106:
                Text2("Exa: That sounds equally as unhealthy.",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 107:
                Text2("Rethgif: How, exactly?",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 108:
                Text2("Exa: Deez nuts.",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 109:
                Text2("Rethgif: ...",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 110:
                Text2("Exa: ...",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 111:
                Text2("Rethgif: ...",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 112:
                Text2("Exa: ...",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 113:
                Text2("Rethgif: ...",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 114:
                Text2("Exa: Gottem.",units.Exa.Portrait,units.Rethgif.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 115:
                Text3("[Exa and Rethgif leveled up!]")
                select.InstantLevelUp(units.Exa,4)
                select.InstantLevelUp(units.Rethgif,4)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 115:
            CutsceneIndex = 116
            Cutscene()
        elif units.Erif in units.UnitsAlive and units.Repins2 in units.UnitsAlive and CutsceneIndex <= 134:
            if CutsceneIndex == 116:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 117:
                Text2("Erif: Repins, how are you alive?",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 118:
                Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 119:
                Text2("Repins: Erif...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 120:
                Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 121:
                Text2("Repins: ...I faked my death on purpose.",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 122:
                Text2("Erif: But why?",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 123:
                Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 124:
                Text2("Repins: I needed to find the Holy Itucher.",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 125:
                Text2("Repins: I didn't want you to worry about me while I",units.Erif.Portrait,units.Repins2.Portrait)
                line2("was gone.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 126:
                Text2("Erif: You didn't want us to worry about you?",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 127:
                Text2("Erif: Are you insane?",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 128:
                Text2("Erif: Do you know what Wob and I went through after",units.Erif.Portrait,units.Repins2.Portrait)
                line2("you faked your death?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 129:
                Text2("Erif: You did this less than a year after Mom and Dad",units.Erif.Portrait,units.Repins2.Portrait)
                line2("died, did you even think of what that might do to Wob?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 130:
                Text2("Erif: He was literally three years old!",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 131:
                Text2("Erif: And all of this because you didn't want us to",units.Erif.Portrait,units.Repins2.Portrait)
                line2("worry!?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 132:
                Text2("Erif: What the hell is wrong with you?",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 133:
                Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 134:
                Text3("[Erif and Repins leveled up!]")
                select.InstantLevelUp(units.Erif,4)
                select.InstantLevelUp(units.Repins2,4)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 134:
            CutsceneIndex = 135
            Cutscene()
        elif units.Yranecrem in units.UnitsAlive and CutsceneIndex <= 145:
            if CutsceneIndex == 135:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 136:
                Text2("Yranecrem: You've come from the Continent of Bipole, correct?",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 137:
                Text2("Proton: Yes.",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 138:
                Text2("Yranecrem: How have things been back there?",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 139:
                Text2("Yranecrem: I haven't been to the continent in 10 years.",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 140:
                Text2("Proton: You've been to the Bipole Continent?",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 141:
                Text2("Yranecrem: Yes, I was actually from the Bipole continent.",units.Yranecrem.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 142:
                Text2("Yranecrem: After the Quad Genocide though, I fled from Quad",units.Yranecrem.Portrait,units.Proton.Portrait)
                line2("and joined a mercenary group to survive.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 143:
                Text2("Yranecrem: And after the mercenaries did an voyage to Nolavillia, I've",units.Yranecrem.Portrait,units.Proton.Portrait)
                line2("been here ever since.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 144:
                Text2("Yranecrem: Dliug and Exa are also from Nolavillia, though I don't know why",units.Yranecrem.Portrait,units.Proton.Portrait)
                line2("they've joined the mercenaries.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 145:
                Text3("[Yranecrem and Proton leveled up!]")
                select.InstantLevelUp(units.Yranecrem,4)
                select.InstantLevelUp(units.Proton,4)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 145:
            CutsceneIndex = 146
            Cutscene()
        elif CutsceneIndex == 146:
            Text1("Proton: Hmmm, what's this? It looks like a box...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 147:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif units.Fael in units.UnitsAlive and CutsceneIndex <= 158:
            if CutsceneIndex == 148:
                Text2("Fael: Wait, I think I can open the box.",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 149:
                Text2("Fael: Look at the hole in the wall next to where",units.Proton.Portrait,units.Fael.Portrait)
                line2("the box is.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 150:
                Text2("Fael: There's something that looks like a button",units.Proton.Portrait,units.Fael.Portrait)
                line2("at the other end.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 151:
                Text2("Fael: Now if I use my bow...",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 152:
                Text3("(Fael shoots the button and the box glows red)")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 153:
                Text2("Fael: Ummm... is that supposed to happen?",units.Proton.Portrait,units.Fael.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 154:
                Text3("(The box unfolds and reveals that it is a mechanical entity)")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 155:
                Text2("???: Freedom, finally...",units.Fael.Portrait,units.Ahcem.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 156:
                Text2("???: Now, it is time to get revenge on that Death Pepper... but it",units.Fael.Portrait,units.Ahcem.Portrait)
                line2("seems like you're also on you're way to do that...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 157:
                Text2("???: In that case, I suppose I'll have to take my revenge along side",units.Fael.Portrait,units.Ahcem.Portrait)
                line2("you... this won't be a problem, will it?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 158:
                Text3("[Ahcem joins your party!]")
                units.UnitsAlive.append(units.Ahcem)
                units.UnitsRecruited.append(units.Ahcem)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 158:
            Text1("Proton: (I don't think I'm able to open this box)",units.Proton.Portrait)
            CutsceneIndex = 159
            
        elif CutsceneIndex == 159:
            Text3("(...)")
            CutsceneIndex = 0
            Chapter = "Chapter 23a"
            
    elif Chapter == "Chapter 22b": #=====================Chapter22b===============================================================
        ChapterLevel = 123
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[End of Act III]")
            CutsceneIndex = 69
            
            print(units.UnitsRecruited)
        elif CutsceneIndex == 69:
            Text3("(...)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 70:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 22b]")
            line2("[Sector 1, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 71:
            screensetup.BattleScreen.bgcolor("light gray")
            
            UnitsToPlace = placeunits.Chapter22aEnemies
            UnitFormation = placeunits.Chapter22aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("???: Who is this? An intruder?",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 72:
            Text1("???: I wonder why they're here... is it because",units.IfBoss.Portrait)
            line2("of the Holy Itucher...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 73:
            Text1("???: But how could they have found out? Did they",units.IfBoss.Portrait)
            line2("defeat Bladeous?")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 74:
            Text1("???: Well, let's see how they do against us.",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 75:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 76:
            Text1("If: This power...",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 77:
            Text1("If: Is it...",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 78:
            Text1("If: No...",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 79:
            Text1("If: No... it can't be...",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 80:
            Text1("If: This world...",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 81:
            Text1("If: At least I don't have to see the end of it...",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 82:
            Text1("If: ...",units.IfBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 83:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 84:
            Text3("now continue")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 85:
            Text3("it approaches")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 86:
            Chapter = "Chapter 23b"
            Cutscene()
    elif Chapter == "Chapter 23a": #=====================Chapter23a===============================================================
        ChapterLevel = 44
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 23a]")
            line2("[Sector 2, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("light gray")
            
            UnitsToPlace = placeunits.Chapter23aEnemies
            UnitFormation = placeunits.Chapter23aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("???: So they've gotten past the first sector...",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("???: If was always too arbituary though, I believe my more",units.ElifBoss.Portrait)
            line2("overarching requirements may be more successful...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("???: So behold! The founder of the Sci-Triptych Sectoral",units.ElifBoss.Portrait)
            line2("Board: I, Elif!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif units.Omega in units.UnitsAlive and CutsceneIndex <= 36:
            if CutsceneIndex == 5:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 6:
                Text1("Omega: ...",units.Omega.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 7:
                Text2("Proton: ...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 8:
                Text2("Omega: Proton...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 9:
                Text2("Omega: What have I done...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Proton: ...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text2("Omega: I... I killed them...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 12:
                Text2("Omega: So... many...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                 
            elif CutsceneIndex == 13:
                Text2("Omega: And... for what?",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("Omega: They aren't even here any more...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 15:
                Text2("Omega: It...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 16:
                Text2("Omega: Was it...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 17:
                Text2("Omega: All pointless?",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 18:
                Text2("Omega: ...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 19:
                Text2("Omega: Hah...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 20:
                Text2("Omega: It's so stupid...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 21:
                Text2("Omega: How...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 22:
                Text2("Omega: Why...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 23:
                Text2("Omega: I don't even hate this world anymore...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Omega: After all... what is there left to hate?",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 24:
                Text2("Omega: It's the same thing every time...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 25:
                Text2("Omega: Disappointment...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 26:
                Text2("Omega: No matter what... it never ends well...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 27:
                Text2("Omega: I thought I could at least protect them...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 28:
                Text2("Omega: Why...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 29:
                Text2("Omega: I just...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 30:
                Text2("Omega: I didn't even protect them...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 31:
                Text2("Omega: I just... made it worse...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 32:
                Text2("Omega: Would it have been the right choice...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 33:
                Text2("Omega: ...to let them be destroyed ealier to save",units.Omega.Portrait,units.Proton.Portrait)
                line2("the others?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 34:
                Text2("Omega: Proton...",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 35:
                Text2("Omega: Did I make the right choice?",units.Omega.Portrait,units.Proton.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 36:
                Text3("[Omega and Proton leveled up!]")
                select.InstantLevelUp(units.Omega,4)
                select.InstantLevelUp(units.Proton,4)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 36:
            CutsceneIndex = 37
            Cutscene()
        elif units.Erif in units.UnitsAlive and units.Repins2 in units.UnitsAlive and CutsceneIndex <= 67:
            if CutsceneIndex == 37:
                Text3("[Bonus Conversation Unlocked]")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 38:
                Text2("Erif: Repins, what were you planning to do here if",units.Erif.Portrait,units.Repins2.Portrait)
                line2("you didn't meet us?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 39:
                Text2("Erif: Were you seriously thinking of raiding the lab on",units.Erif.Portrait,units.Repins2.Portrait)
                line2("your own?")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 40:
                Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 41:
                Text2("Repins: I was going to use this...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 42:
                Text3("(Repins shows Erif something that looks like a syringe)")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 43:
                Text2("Repins: ...this is a dose of evanesce flux.",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 44:
                Text2("Erif: Were you going to use that on yourself?",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 45:
                Text2("Repins: Yes.",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 46:
                Text2("Erif: So you were going to erase yourself from existence,",units.Erif.Portrait,units.Repins2.Portrait)
                line2("what a great idea.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 47:
                Text2("Erif: And where did you even get that? That's highly illegal",units.Erif.Portrait,units.Repins2.Portrait)
                line2("everywhere in the Bipole Continent.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 48:
                Text2("Repins: I got it when I was at the Territory of Secant a few",units.Erif.Portrait,units.Repins2.Portrait)
                line2("years ago.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 49:
                Text2("Erif: How could you even afford that?",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 50:
                Text2("Repins: I didn't.",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 51:
                Text2("Erif: ...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 52:
                Text2("Repins: I have the antidote as well. Once I got the Itucher,",units.Erif.Portrait,units.Repins2.Portrait)
                line2("I was going to take it before I was erased from this")
                line3("timeline.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 53:
                Text2("Erif: Repins...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 54:
                Text2("Erif: I can't tell who you're lying to... to me or to",units.Erif.Portrait,units.Repins2.Portrait)
                line2("youself...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 55:
                Text2("Erif: But this isn't something you're doing for us",units.Erif.Portrait,units.Repins2.Portrait)
                line2("or Quad...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 56:
                Text2("Erif: You're doing this for yourself.",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 57:
                Text2("Erif: You've faked your death in front of your traumatized siblings,",units.Erif.Portrait,units.Repins2.Portrait)
                line2("gotten your hands on an highly illegal and dangerous weapon to use on")
                line3("yourself, and who knows what else...")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 58:
                Text2("Erif: ...all because you want a fucking artifact?",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 59:
                Text2("Erif: It's sad...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 60:
                Text2("Erif: After you \"died\", I wanted to see you alive again...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 61:
                Text2("Erif: I wanted you back so much...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 62:
                Text2("Erif: But now...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 63:
                Text2("Erif: I regret that.",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 64:
                Text2("Erif: I wish I'd never met you again.",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 65:
                Text2("Erif: I wish I still thought you were dead and had an",units.Erif.Portrait,units.Repins2.Portrait)
                line2("idealistic view of you.")
                CutsceneIndex += 1
                
            elif CutsceneIndex == 66:
                Text2("Repins: ...",units.Erif.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 67:
                Text3("[Erif and Repins leveled up!]")
                select.InstantLevelUp(units.Erif,4)
                select.InstantLevelUp(units.Repins2,4)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 67:
            CutsceneIndex = 68
            Cutscene()
        elif CutsceneIndex == 68:
            Text3("(...)")
            CutsceneIndex = 0
            Chapter = "Chapter 24a"
            
    elif Chapter == "Chapter 23b": #=====================Chapter23b===============================================================
        ChapterLevel = 132
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 23b]")
            line2("[Sector 2, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("light gray")
            
            UnitsToPlace = placeunits.Chapter23aEnemies
            UnitFormation = placeunits.Chapter23aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("the next target: Huh, who's there?",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("the next target: Someone's definitely there... ",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 3:
            Text1("the next target: Sector alert! Everyone be on guard, there may",units.ElifBoss.Portrait)
            line2("be an intruder!")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 5:
            Text1("the second one: Wh...",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text1("the second one: I...",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text1("the second one: Why must...",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text1("the second one: My death...",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text1("the second one: Be so... bland...",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text1("the second one: ...",units.ElifBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text3("next")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Chapter = "Chapter 24b"
            Cutscene()   
    elif Chapter == "Chapter 24a": #=====================Chapter24a===============================================================
        ChapterLevel = 47
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 24a]")
            line2("[Sector 3, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("light gray")
            
            UnitsToPlace = placeunits.Chapter24aEnemies
            UnitFormation = placeunits.Chapter24aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("???: Alas, the others were unable to stop our enemy...",units.ElseBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("???: Like everything in life, it's always the \"else\",",units.ElseBoss.Portrait)
            line2("isn't it?")
            CutsceneIndex += 1
              
        elif CutsceneIndex == 3:
            Text1("???: Anyhow, it seems that I'll have to do whatever the",units.ElseBoss.Portrait)
            line2("others can't do.")
            CutsceneIndex += 1
              
        elif CutsceneIndex == 4:
            Text1("???: Foolish Xuirs! Prepare to feel the wrath of my",units.ElseBoss.Portrait)
            line2("arsenal of often-unused weaponry and spells!")
            CutsceneIndex += 1
              
        elif CutsceneIndex == 5:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 6:
            Text3("(...)")
            CutsceneIndex = 0
            if units.Omega in units.UnitsAlive:
                Chapter = "Chapter 25a"
            else:
                Chapter = "Chapter 25b"
             
    elif Chapter == "Chapter 24b": #=====================Chapter24b===============================================================
        ChapterLevel = 141
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 24b]")
            line2("[2/5 down, 3 to go]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("light gray")
            
            UnitsToPlace = placeunits.Chapter24aEnemies
            UnitFormation = placeunits.Chapter24aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("him: Who's this?",units.ElseBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("him: How was an intruder able to get this far into the lab?",units.ElseBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 3:
            Text1("him: Of course, unless...",units.ElseBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 4:
            Text1("him: No, that can't be it. I'm sure we'll be alright.",units.ElseBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 5:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 6:
            Text1("3: ...",units.ElseBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 7:
            Text1("3: Damn...",units.ElseBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 8:
            Text1("3: ...",units.ElseBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 9:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 10:
            Text3("hurry")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Chapter = "Chapter 25c"
            Cutscene()
    elif Chapter == "Chapter 25a": #=====================Chapter25a===============================================================
        ChapterLevel = 50
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 25a]")
            line2("[Sector 4, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("light gray")
            Text1("Break: ...",units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 2:
            Text1("Break: Omega, you still dare live after that?",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text2("Omega: ...",units.Omega.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 4:
            Text2("Break: Since you've directly disobeyed by orders and",units.Omega.Portrait,units.Break.Portrait)
            line2("fought against out security...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text2("Break: I'm allowed to kill you.",units.Omega.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text2("Break: In fact, I'm encouraged to.",units.Omega.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("Break: I think this would be a great time to test out what",units.Omega.Portrait,units.Break.Portrait)
            line2("that Xuirer gave me...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text2("Break: The Unique Spell, I believe it was called.",units.Omega.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif units.Xuirer in units.UnitsAlive and CutsceneIndex <= 11:
            if CutsceneIndex == 9:
                Text2("Proton: Xuirer?",units.Proton.Portrait,units.Break.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 10:
                Text2("Proton: Wait, he's not here... where did he go?",units.Proton.Portrait,units.Break.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 11:
                Text3("[Xuirer is no longer in your party]")
                units.UnitsAlive.remove(units.Xuirer)
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 11:
            CutsceneIndex = 12
            Cutscene()
        elif units.B in units.UnitsAlive and CutsceneIndex <= 14:
            if CutsceneIndex == 12:
                Text2("B: Unique Spell?",units.B.Portrait,units.Break.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 13:
                Text2("B: How does he know about Unique Spells?",units.B.Portrait,units.Break.Portrait)
                CutsceneIndex += 1
                
            elif CutsceneIndex == 14:
                Text2("B: But he's not Infinian, he shouldn't be able to",units.B.Portrait,units.Break.Portrait)
                line2("use it...")
                CutsceneIndex += 1
                
        elif CutsceneIndex <= 14:
            CutsceneIndex = 15
            Cutscene()
        elif CutsceneIndex == 15:
            Text3("[Break activates the Unique Spell tome]",)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Break: Ahh... this power...",units.Omega.Portrait,units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text3("[Break suddenly appears behind Omega and stabs him]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text1("Omega: So... this is my fate...",units.Omega.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text2("Proton: Omega!",units.Omega.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("Omega: Proton... I'm suprised I even lived so long...",units.Omega.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Omega: I accept my death... there's no use in opposing the",units.Omega.Portrait,units.Proton.Portrait)
            line2("Neville Prophecy...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text2("Omega: \"The founder of the Xuirists shall be slain by the",units.Omega.Portrait,units.Proton.Portrait)
            line2("enemy's blade\"...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text2("Omega: ...",units.Omega.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text2("Omega: It was a painful life...",units.Omega.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text2("Omega: Finally... I'll be with them again...",units.Omega.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text2("Omega: My family...",units.Omega.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text2("Omega: ...",units.Omega.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text3("[Omega has died]")
            units.UnitsAlive.remove(units.Omega)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 29:
            Text1("Break: Hehehehehe!!!",units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 30:
            Text1("Break: HEHEHEHEHEHEHEHEHE!!!!!!!",units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 31:
            Text1("Break: THIS POWER!!!!!!",units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 32:
            Text1("Break: WITH THIS POWER...",units.Break.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 33:
            screensetup.BattleScreen.bgcolor("maroon")
            Text3("[A large explosion detonates around Break]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 34:
            Text3("Break: EVEN I...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 35:
            screensetup.BattleScreen.bgcolor("dark slate blue")
            Text3("[A bright, purple light pierces through the dust of")
            line2("the explosion]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 36:
            Text1("Break: ...CAN WIELD THE HOLY ITUCHER!!!",units.BreakItucher.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter25aEnemies
            UnitFormation = placeunits.Chapter25aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 37:
            Text1("Break: H... HOW...",units.BreakItucher.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 38:
            Text1("Break: HOW COULD I HAVE LOST...",units.BreakItucher.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 39:
            Text1("Break: I HAVE THE HOLY ITUCHER... I HAVE THE POWER",units.BreakItucher.Portrait)
            line2("OF THE GODS...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 40:
            Text1("Break: THIS... THIS SHOULDN'T BE POSSIBLE!!!",units.BreakItucher.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 41:
            screensetup.BattleScreen.bgcolor("dark violet")
            Text3("(Beams of pulsating purple light start to shoot out of cuts across")
            line2("Break's body)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 42:
            Text1("Break: NO!!!!! NO!!!!!!!! NO!!!!!!!!!!!!!!!!!!",units.BreakItucher.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 43:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(Break is brightly consumed by the light and disintegrates)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 44:
            screensetup.BattleScreen.bgcolor("dark gray")
            Text3("(The Holy Itucher lies on the ground where Break was)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 45:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 46:
            Text3("(Proton picks up the Holy Itucher)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 47:
            Text1("Proton: Many sacrifices were made on our journey here...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 48:
            Text1("Proton: But it is finally over...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 49:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 50:
            Text1("Proton: Our mission is complete, we'll be returning to the",units.Proton.Portrait)
            line2("Territory of Static.")
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            EndingCharacter(units.Proton,False,False,False)
        elif CutsceneIndex == 101:
            EndingCharacter(units.Quest,False,False,False)
        elif CutsceneIndex == 102:
            EndingCharacter(units.Scien,False,False,False)
        elif CutsceneIndex == 103:
            EndingCharacter(units.Romra,False,False,False)
        elif CutsceneIndex == 104:
            EndingCharacter(units.TnemecalperI,False,False,False)
        elif CutsceneIndex == 105:
            EndingCharacter(units.TnemecalperII,False,False,False)
        elif CutsceneIndex == 106:
            EndingCharacter(units.TnemecalperIII,False,False,False)
        elif CutsceneIndex == 107:
            EndingCharacter(units.TnemecalperIV,False,False,False)
        elif CutsceneIndex == 108:
            EndingCharacter(units.Lacirtcele,False,False,False)
        elif CutsceneIndex == 109:
            EndingCharacter(units.Damagein,False,False,False)
        elif CutsceneIndex == 110:
            EndingCharacter(units.Healia,False,False,False)
        elif CutsceneIndex == 111:
            EndingCharacter(units.Wob,False,False,False)
        elif CutsceneIndex == 112:
            EndingCharacter(units.Bladen,False,False,False)
        elif CutsceneIndex == 113:
            EndingCharacter(units.Wodahs,False,False,False)
        elif CutsceneIndex == 114:
            EndingCharacter(units.PlayableBladeous,False,False,False)
        elif CutsceneIndex == 115:
            EndingCharacter(units.Azure,False,False,False)
        elif CutsceneIndex == 116:
            EndingCharacter(units.Fael,False,False,False)
        elif CutsceneIndex == 117:
            EndingCharacter(units.Erif,False,False,False)
        elif CutsceneIndex == 118:
            EndingCharacter(units.Vruh,False,False,False)
        elif CutsceneIndex == 119:
            EndingCharacter(units.Recils,False,False,False)
        elif CutsceneIndex == 120:
            EndingCharacter(units.Repins,False,False,False)
        elif CutsceneIndex == 121:
            EndingCharacter(units.Relaeh,False,False,False)
        elif CutsceneIndex == 122:
            EndingCharacter(units.Eulb,False,False,False)
        elif CutsceneIndex == 123:
            EndingCharacter(units.Lias,False,False,False)
        elif CutsceneIndex == 124:
            EndingCharacter(units.Fieht,False,False,False)
        elif CutsceneIndex == 125:
            EndingCharacter(units.Rethgif,False,False,False)
        elif CutsceneIndex == 126:
            EndingCharacter(units.Eg,False,False,False)
        elif CutsceneIndex == 127:
            EndingCharacter(units.Elbon,False,False,False)
        elif CutsceneIndex == 128:
            EndingCharacter(units.B,False,False,False)
        elif CutsceneIndex == 129:
            EndingCharacter(units.Xuirventh,False,False,False)
        elif CutsceneIndex == 130:
            EndingCharacter(units.Xuirfth,False,False,False)
        elif CutsceneIndex == 131:
            EndingCharacter(units.Xuirer,False,False,False)
        elif CutsceneIndex == 132:
            EndingCharacter(units.Dliug,False,False,False)
        elif CutsceneIndex == 133:
            EndingCharacter(units.Exa,False,False,False)
        elif CutsceneIndex == 134:
            EndingCharacter(units.Yranecrem,False,False,False)
        elif CutsceneIndex == 135:
            EndingCharacter(units.Geomer,False,False,False)
        elif CutsceneIndex == 136:
            EndingCharacter(units.Box,False,False,False)
        elif CutsceneIndex == 137:
            EndingCharacter(units.NOTOS,False,False,False)
        elif CutsceneIndex == 138:
            EndingCharacter(units.YungPoggers,False,False,False)
        elif CutsceneIndex == 139:
            EndingCharacter(units.Dnefed,False,False,False)
        elif CutsceneIndex == 140:
            EndingCharacter(units.Thgif,False,False,False)
        elif CutsceneIndex == 141:
            EndingCharacter(units.Gnirif,False,False,False)
        elif CutsceneIndex == 142:
            EndingCharacter(units.Cigam,False,False,False)
        elif CutsceneIndex == 143:
            EndingCharacter(units.Omega,True,False,False)
        elif CutsceneIndex == 144:
            EndingCharacter(units.Fiyghtrr,False,False,False)
        elif CutsceneIndex == 145:
            EndingCharacter(units.Recalper,False,False,False)
        elif CutsceneIndex == 146:
            EndingCharacter(units.Tabmoc,False,False,False)
        elif CutsceneIndex == 147:
            EndingCharacter(units.Xuirurth,False,False,False)
        elif CutsceneIndex == 148:
            EndingCharacter(units.Repins2,False,False,False)
        elif CutsceneIndex == 149:
            EndingCharacter(units.Ahcem,False,False,False)
        elif CutsceneIndex == 150:
            EndingCharacter(units.Cayenne,False,False,False)
        elif CutsceneIndex == 151:
            EndingCharacter(units.XuirMan,False,False,False)
        elif CutsceneIndex == 152:
            EndingCharacter(units.Integer,False,False,False)
        elif CutsceneIndex == 153:
            Text3("                             ~~ Ending 1/10: Omega Ending ~~")
            line2("|    Break possessed by Itucher, Itucher retrieved by Proton, timeline intact    |")
            line3("                 Enter code \"947187\" to start the game in New Game+")
    elif Chapter == "Chapter 25b": #=====================Chapter25b===============================================================
        ChapterLevel = 49
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 25b]")
            line2("[Sector 4, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("light gray")
            
            UnitsToPlace = placeunits.Chapter25bEnemies
            UnitFormation = placeunits.Chapter25bPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("Break: ...",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Break: It seems you vermin have managed to make it",units.Break.Portrait)
            line2("to the fourth sector.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text1("Break: Good thing it'll be your last.",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 5:
            Text1("Break: Erghhh...",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text1("Break: This isn't looking too good...",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            Text3("[Break flees from the lab]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text3("[Proton opens a door and a loud alarm sounds]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            Text1("Proton: ...what was that?",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            Text2("???: Hello",units.Proton.Portrait,units.Cayenne.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            Text2("Proton: Who are you?",units.Proton.Portrait,units.Cayenne.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text2("???: I am Cayenne, a mechanical created by Death Pepper.",units.Proton.Portrait,units.Cayenne.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text2("Cayenne: Death Pepper, the leader of this lab, awaits in the",units.Proton.Portrait,units.Cayenne.Portrait)
            line2("next sector.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 15:
            Text2("Cayenne: But do not worry, I am not your enemy.",units.Proton.Portrait,units.Cayenne.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 16:
            Text2("Cayenne: I can assist you in your battle against Death Pepper,",units.Proton.Portrait,units.Cayenne.Portrait)
            line2("if you would allow it.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 17:
                Text3("[Recruit Cayenne]")
                line2("(Q) Recruit")
                line3("(W) Do not recruit")
                CutsceneIndex += 1
                (screensetup.BattleScreen).onkey(QinputYes, "q")
                (screensetup.BattleScreen).onkey(WinputYes, "w")
        elif CutsceneIndex == 18:
            if Qinput == True:
                Text2("Cayenne: Understood.",units.Proton.Portrait, units.Cayenne.Portrait)
                CutsceneIndex += 1
                
            else:
                Text2("Cayenne: Okay then...",units.Proton.Portrait, units.Cayenne.Portrait)
                CutsceneIndex += 1
                
        elif CutsceneIndex == 19:
            if Qinput == True:
                Text3("[Cayenne has joined your party]")
                units.UnitsAlive.append(units.Cayenne)
                units.UnitsRecruited.append(units.Cayenne)
                CutsceneIndex += 1
                ClearInputs()
                
            else:
                CutsceneIndex += 1
                ClearInputs()
                Cutscene()
        elif CutsceneIndex == 20:
            Text3("(...)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 21:
            Text3("[Everyone stands in front of the enterance of the fifth sector]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 22:
            if units.Quest in units.UnitsAlive:
                Text1("Quest: Soon, the Itucher will be ours.",units.Quest.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 23:
            if units.Scien in units.UnitsAlive:
                Text1("Scien: It's time to finally end this.",units.Scien.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 24:
            if units.Quest in units.UnitsAlive:
                Text1("Romra: The final sector... that sounds a little intimidating...",units.Romra.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 25:
            if units.TnemecalperI in units.UnitsAlive:
                Text1("Tnemecalper I: Congratulations.",units.TnemecalperI.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 26:
            if units.TnemecalperII in units.UnitsAlive:
                Text1("Tnemecalper II: Congratulations.",units.TnemecalperII.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 27:
            if units.TnemecalperIII in units.UnitsAlive:
                Text1("Tnemecalper III: Congratulations.",units.TnemecalperIII.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 28:
            if units.TnemecalperIV in units.UnitsAlive:
                Text1("Tnemecalper IV: Congratulations.",units.TnemecalperIV.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 29:
            if units.Lacirtcele in units.UnitsAlive:
                Text1("Lacirtcele: Bruh...",units.Lacirtcele.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 30:
            if units.Damagein in units.UnitsAlive:
                Text1("Damagein: It's time for the ultimate damage!",units.Damagein.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 31:
            if units.Healia in units.UnitsAlive:
                Text1("Healia: I sure didn't think I'd end up here after leaving",units.Healia.Portrait)
                line2("Sine.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 32:
            if units.Wob in units.UnitsAlive:
                Text1("Wob: I wonder if I can officially join the army after this...",units.Wob.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 33:
            if units.Bladen in units.UnitsAlive:
                Text1("Bladen: Really can't escape fate, can you?",units.Bladen.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 34:
            if units.Wodahs in units.UnitsAlive:
                Text1("Wodahs: So much for a solo mission.",units.Wodahs.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 35:
            if units.PlayableBladeous in units.UnitsAlive:
                Text1("Bladeous: ...",units.PlayableBladeous.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 36:
            if units.Fael in units.UnitsAlive:
                Text1("Fael: So we're finally here...",units.Fael.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 37:
            if units.Erif in units.UnitsAlive:
                Text1("Erif: Our expedition is reaching it's end...",units.Erif.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 38:
            if units.Vruh in units.UnitsAlive:
                Text1("Vruh: The ultimate bruh moment awaits...",units.Vruh.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 39:
            if units.Recils in units.UnitsAlive:
                Text1("Recils: I'm feeling good about this.",units.Recils.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 40:
            if units.Repins in units.UnitsAlive:
                Text1("Repins: The Holy Itucher... it's finally within reach...",units.Repins.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 41:
            if units.Relaeh in units.UnitsAlive:
                Text1("Relaeh: We must bring an end to this destruction.",units.Relaeh.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 42:
            if units.Eulb in units.UnitsAlive:
                Text1("Eulb: Errr... guess I'm here now?",units.Eulb.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 43:
            if units.Lias in units.UnitsAlive:
                Text1("Lias: I've spent too much time at sea... but now that I'm here,",units.Lias.Portrait)
                line2("I might as well help save the world.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 44:
            if units.Eulb in units.UnitsAlive:
                Text1("Fieht: The fifth sector... sounds like they'll have some valuables!",units.Fieht.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 45:
            if units.Rethgif in units.UnitsAlive:
                Text1("Rethgif: This isn't just a fight for the world, this is a fight",units.Rethgif.Portrait)
                line2("against my boredom!")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 46:
            if units.Eg in units.UnitsAlive:
                Text1("Eg: Conclusion.",units.Eg.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 47:
            if units.Elbon in units.UnitsAlive:
                Text1("Elbon: Ugh, must a noble as I do something like this?",units.Elbon.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 48:
            if units.B in units.UnitsAlive:
                Text1("B: The timeline seems to be following it's destination",units.B.Portrait)
                line2("in the prophecy. All seems well.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 49:
            if units.Xuirventh in units.UnitsAlive:
                Text1("Xuirventh: It's time to end this lab!",units.Xuirventh.Portrait)                
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 50:
            if units.Xuirfth in units.UnitsAlive:
                Text1("Xuirfth: We've returned to where it all begun. Now it's",units.Xuirfth.Portrait)
                line2("time to end it.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 51:
            if units.Xuirer in units.UnitsAlive:
                Text1("Xuirer: The process is flowing correctly... the timelines are aligning...",units.Xuirer.Portrait)
                line2("it is inevitable...")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 52:
            if units.Dliug in units.UnitsAlive:
                Text1("Dliug: Argh! Death to the Xuirists!",units.Dliug.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 53:
            if units.Exa in units.UnitsAlive:
                Text1("Exa: It is time for them to learn what fear feels like.",units.Exa.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 54:
            if units.Yranecrem in units.UnitsAlive:
                Text1("Yranecrem: Will this finally end the cycle of destruction?",units.Yranecrem.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 55:
            if units.Geomer in units.UnitsAlive:
                Text1("Geomer: The power of Geom will prevail!",units.Geomer.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 56:
            if units.Box in units.UnitsAlive:
                Text1("Box: Huh, how did I end up here?",units.Box.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 57:
            if units.NOTOS in units.UnitsAlive:
                Text1("NOTOS: Hahahaha! Let's see how they fair against me!",units.NOTOS.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 58:
            if units.YungPoggers in units.UnitsAlive:
                Text1("Yung Poggers: The preparations are nearing completion. The process will soon be",units.YungPoggers.Portrait)
                line2("executed.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 59:
            if units.Dnefed in units.UnitsAlive:
                Text1("Dnefed: So I ended up at the Itucher anyways, huh.",units.Dnefed.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 60:
            if units.Thgif in units.UnitsAlive:
                Text1("Thgif: With or without Dael, we still end up here. Funny how",units.Thgif.Portrait)
                line2("fate works, isn't it.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 61:
            if units.Gnirif in units.UnitsAlive:
                Text1("Gnirif: So we can't escape the hunt of the Itucher,",units.Gnirif.Portrait)
                line2("*sigh* what is my life...")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 62:
            if units.Cigam in units.UnitsAlive:
                Text1("Cigam: It seems fate cannot be escaped from, really something to",units.Cigam.Portrait)
                line2("take note of.")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 63:
            if units.Fiyghtrr in units.UnitsAlive:
                Text1("Fiyghtrr: After this, we'll finally get revenge for what they've",units.Fiyghtrr.Portrait)
                line2("done to Nation!")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 64:
            if units.Recalper in units.UnitsAlive:
                Text1("Recalper: They'll sure need a replacement after what I do them!",units.Recalper.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 65:
            if units.Tabmoc in units.UnitsAlive:
                Text1("Tabmoc: The Itucher, huh. This better be a good challenge.",units.Tabmoc.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 66:
            if units.Xuirurth in units.UnitsAlive:
                Text1("Xuirurth: This battle is for Xuirventh, Xuirfth, and all of the",units.Xuirurth.Portrait)
                line2("the Xuirs that suffered by Death Pepper's rule!")
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 67:
            if units.Repins2 in units.UnitsAlive:
                Text1("Repins: The Holy Itucher... finally...",units.Repins2.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 68:
            if units.Ahcem in units.UnitsAlive:
                Text1("Ahcem: It's time to stop 'em!",units.Ahcem.Portrait)
                CutsceneIndex += 1
                
            else:
                CutsceneIndex += 1
                Cutscene()
        elif CutsceneIndex == 69:
            Text1("Proton: It's been a long journey, but it's finally coming to",units.Proton.Portrait)
            line2("an end...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 70:
            Text1("Proton: After all of these years, we're ending this at the very",units.Proton.Portrait)
            line2("place it started it...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 71:
            Text1("Proton: For everyone who suffered...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 72:
            Text1("Proton: For everyone who died...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 73:
            Text1("Proton: We must win!",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 74:
            Text3("[Proton opens the door and everyone charges into the sector]")
            CutsceneIndex = 0
            Chapter = "Chapter 26a"
             
    elif Chapter == "Chapter 25c": #=====================Chapter25c===============================================================
        ChapterLevel = 147
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 25c]")
            line2("[4/5, 2 remaining]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("light gray")
            
            UnitsToPlace = placeunits.Chapter25bEnemies
            UnitFormation = placeunits.Chapter25bPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("him, again: AHHH!!!",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("him, again: It's you again!",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text1("him, again: How the hell did you get here!?",units.Break.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 5:
            Text1("gone: ...",units.Break.Portrait)
            CutsceneIndex += 1
                
        elif CutsceneIndex == 6:
            Text1("yOU?: ...",units.Proton.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 7:
            Text3("run")
            CutsceneIndex += 1
              
        elif CutsceneIndex == 8:
            Chapter = "Chapter 26d"
            Cutscene()
    elif Chapter == "Chapter 26a": #=====================Chapter26a===============================================================
        ChapterLevel = 50
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 26a]")
            line2("[Sector 5, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark gray")
            
            UnitsToPlace = placeunits.Chapter26aEnemies
            UnitFormation = placeunits.Chapter26aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("Death Pepper: Proton...",units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Death Pepper: I've heard much about you, and you've caused",units.DeathPepper.Portrait)
            line2("us a lot of trouble...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text1("Death Pepper: I don't understand though, why would you return",units.DeathPepper.Portrait)
            line2("here after all of these years?")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("Proton: We can't let you have the Holy Itucher, you'll surely",units.Proton.Portrait,units.DeathPepper.Portrait)
            line2("destroy the world as we know it.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text2("Proton: And this is revenge for what you've done to Specians and the Xuirs.",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text2("Death Pepper: What I've done to the Xuirs?",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            Text2("Death Pepper: The only thing I've done for the Xuirs is help them.",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text2("Proton: What do you mean?",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text2("Death Pepper: The Proto-Xuirs are a pained existence, an incomplete and failed",units.Proton.Portrait,units.DeathPepper.Portrait)
            line2("life form.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            Text2("Death Pepper: The Proto-Xuirs will only be free once a complete Xuir is created,",units.Proton.Portrait,units.DeathPepper.Portrait)
            line2("the lifeform that they were meant to be!")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            Text2("Proton: Being incomplete doensn't devalue your existence. This is just an excuse",units.Proton.Portrait,units.DeathPepper.Portrait)
            line2("to justify your actions.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            Text2("Death Pepper: It doesn't? Well, take a look at this...",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text2("Death Pepper: What do you think of this, Proton?",units.Proton.Portrait,units.DeathPepper2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text2("Proton: You're... a Proto-Xuir?",units.Proton.Portrait,units.DeathPepper2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 15:
            Text2("Death Pepper: Why do you think I've dedicated myself to the Xuir",units.Proton.Portrait,units.DeathPepper2.Portrait)
            line2("Research?")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 16:
            Text2("Death Pepper: I am an incomplete creation of the past researchers, an existence",units.Proton.Portrait,units.DeathPepper2.Portrait)
            line2("of failure.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 17:
            Text2("Death Pepper: This existence is pain. Proton, surely you've considered the",units.Proton.Portrait,units.DeathPepper2.Portrait)
            line2("fact that you were the result of unsuccessful experiements, that your very")
            line3("existence is a literal embodiment of failure.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 18:
            Text2("Death Pepper: I wish to fix this failure, no matter the cost.",units.Proton.Portrait,units.DeathPepper2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 19:
            Text2("Death Pepper: I will create the being that were supposed to be, the one",units.Proton.Portrait,units.DeathPepper2.Portrait)
            line2("that we could've been...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 20:
            Text2("Death Pepper: And only then, will be free from our burden of an failed existence",units.Proton.Portrait,units.DeathPepper2.Portrait)
            line2("and be able to die in the peace of knowing that our failure had been fixed.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 21:
            Text2("Death Pepper: We must fix our existence, Proton.",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 22:
            Text2("Proton: ...",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 23:
            Text2("Death Pepper: Sadly, it seems you do not understand.",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 24:
            Text2("Death Pepper: Like the others, all who oppose me must be defeated in the sake",units.Proton.Portrait,units.DeathPepper.Portrait)
            line2("of mending our existence.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 25:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 26:
            Text2("Death Pepper: Why... why.. must this happen...",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 27:
            Text2("Death Pepper: The Xuir... must be... completed...",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 28:
            Text1("Proton: Everyone, search the area.",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 29:
            Text1("Proton: The Holy Itucher should be somewhere around here.",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 30:
            Text3("(...)")
            CutsceneIndex += 1
            
        elif units.Quest in units.UnitsAlive and units.Scien in units.UnitsAlive:
            CutsceneIndex = 0
            Chapter = "Chapter 27a"
            Cutscene()
        elif moves.BothDead in units.Repins.Attacks:
            CutsceneIndex = 0
            Chapter = "Chapter 27c"
            Cutscene()
        elif moves.OneDead in units.Repins.Attacks:
            CutsceneIndex = 0
            Chapter = "Chapter 27b"
            Cutscene()
        elif units.Ahcem in units.UnitsAlive and units.Ahcem.Level >= 57:
            CutsceneIndex = 0
            Chapter = "Chapter 27e"
            Cutscene()
        elif units.Quest in units.UnitsAlive:
            CutsceneIndex = 0
            Chapter = "Bad Ending"
            Cutscene()
        elif units.Vruh in units.UnitsAlive:
            CutsceneIndex = 0
            Chapter = "Chapter 27d"
            Cutscene()
        else:
            CutsceneIndex = 0
            Chapter = "Neutral Ending"
            Cutscene()
    elif Chapter == "Chapter 26b": #=====================Chapter26b===============================================================
        ChapterLevel = 150
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 26b]")
            line2("[the finale]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark gray")
            
            UnitsToPlace = placeunits.Chapter26aEnemies
            UnitFormation = placeunits.Chapter26aPlacement
            units.EnemyUnitsAlive = UnitsToPlace
            placeunits.PlaceEnemies(UnitFormation)
            placeunits.PlacePlayerUnits()
            
            Text1("juhhwlqjv",units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("wkh axlu zudwk zloo vrrq eh xqohdvkhg",units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text1("ghvwuxfwlrq zloo vrrq suhydlo",units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("qrz hqg wklv irro dqg wkh rqh vkdoo uhwxuq",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            CutsceneIndex += 1
            BattleStarted = True
            
            
            
            
            
            
        elif CutsceneIndex == 6:
            Text2("kh",units.Proton.Portrait,units.DeathPepper.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            if units.Azure in units.UnitsAlive:
                Chapter = "Azure Ending"
                Cutscene()
            else:
                Chapter = "Chapter 27f"
                Cutscene()
    elif Chapter == "Chapter 27a": #=====================Chapter27a===============================================================
        ChapterLevel = 51
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 27a]")
            line2("[Sector 5, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("Quest: ...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Quest: Hmmm? What's this?",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text3("(Quest pulls a lever on the wall, opening up a container)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text1("Quest: Is this...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text1("Quest: Yes! It is!",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text1("Quest: The Holy Itucher...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            Text1("Quest: It's here, right in front of me...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text1("Quest: My life's work of study and research...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text1("Quest: After all of these years...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            Text1("Quest: It's finally...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            Text2("Proton: Quest, did you find the Itu...",units.Quest.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            screensetup.BattleScreen.bgcolor("red")
            Text3("(Proton is blasted back by an explosion around Quest)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            screensetup.BattleScreen.bgcolor("indigo")
            Text1("Proton: Wh...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text1("Proton: Quest! Don't activate the Itucher!",units.Proton.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 15:
            Text2("Quest: ...",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 16:
            Text2("Proton: Quest!",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 17:
            Text3("(Quest stabs Proton with the Holy Itucher)")
            CutsceneIndex += 1
              
        elif CutsceneIndex == 18:
            Text2("Quest: ...",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 19:
            Text2("Scien: Proton!",units.Proton.Portrait,units.Scien.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 20:
            Text2("Proton: ...",units.Proton.Portrait,units.Scien.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 21:
            Text3("[Proton has been defeated]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text1("Scien: Proton!!!",units.Scien.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 23:
            Text2("Quest: ...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 24:
            Text2("Scien: Quest, he must be possessed by the Holy Itucher...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 25:
            Text2("Scien: He's already killed Proton...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 26:
            Text2("Scien: What will happen if he escapes to the rest of the world...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 27:
            Text2("Scien: ...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 28:
            Text2("Scien: It must be done...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 29:
            Text2("Scien: The Forbidden Ritual of Nation...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 30:
            Text2("Scien: For the sake of the world...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 31:
            Text2("Scien: I'm sorry, Proton...",units.Scien.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 32:
            Text3("(Scien places his mask on Proton's corpse)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 33:
            Text1("Quest: ...",units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 34:
            screensetup.BattleScreen.bgcolor("yellow")
            Text3("(Scien glows brightly before fading into the air)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 35:
            Text3("[Scien has been defeated]")
            units.UnitsAlive.remove(units.Scien)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 36:
            screensetup.BattleScreen.bgcolor("indigo")
            Text3("(Proton's body disappears and is replaced by a suit")
            line2("of armor)")
            units.UnitsAlive.append(units.XuirMan)
            units.UnitsAlive.remove(units.Proton)
            units.XuirMan.ATK = units.Proton.ATK*3
            units.XuirMan.MaxHP = units.Proton.MaxHP*3
            units.XuirMan.CurrentHP = units.Proton.CurrentHP*3
            units.XuirMan.DEF = units.Proton.DEF*3
            units.XuirMan.RES = units.Proton.RES*2
            units.XuirMan.AGL = units.Proton.AGL*2
            units.XuirMan.ACR = units.Proton.ACR*3
            units.XuirMan.Attacks = units.Proton.Attacks
            units.XuirMan.Supports = units.Proton.Supports
            units.XuirMan.Level = units.Proton.Level*3
            CutsceneIndex += 1
             
        elif CutsceneIndex == 37:
            Text1("Proton: ...",units.XuirMan.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 38:
            Text1("Proton: Am I... alive?",units.XuirMan.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 39:
            Text2("Quest: ...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 40:
            Text2("Proton: Scien...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 41:
            Text2("Proton: Did he...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 42:
            Text2("Proton: ...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 43:
            Text2("Proton: This is for the sake of the world...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 44:
            Text2("Proton: Quest, you must be stopped.",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 45:
            Text3("(Proton awakens Integer)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 46:
            Text3("[Integer joined your party]")
            units.UnitsAlive.append(units.Integer)
            units.UnitsRecruited.append(units.Integer)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 47:
            Text3("[Quest has left your party]")
            units.UnitsAlive.remove(units.Quest)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27aEnemies
            UnitFormation = placeunits.Chapter27aPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 48:
            Text2("Quest: ...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 49:
            Text2("Quest: Proton...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 50:
            Text2("Quest: Stop me...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 51:
            Text2("Proton: ...",units.XuirMan.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 52:
            screensetup.BattleScreen.bgcolor("yellow")
            Text3("(Proton seals Quest in the Holy Itucher)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 53:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("Proton: ...",units.XuirMan.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 54:
            Text1("Proton: There have been many losses throughout our journey...",units.XuirMan.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 55:
            Text1("Proton: It is because of these sacrifices that we are here today...",units.XuirMan.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 56:
            Text1("Proton: We must not forget those who have been lost in the fight for",units.XuirMan.Portrait)
            line2("the Holy Itucher...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 57:
            Text1("Proton: ...",units.XuirMan.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 58:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(And so the Static Army returned to the Continent of Bipole, successfully")
            line2("retrieving the Holy Itucher...)")
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            EndingCharacter(units.Proton,False,False,False)
        elif CutsceneIndex == 101:
            EndingCharacter(units.Quest,False,False,False)
        elif CutsceneIndex == 102:
            EndingCharacter(units.Scien,False,False,False)
        elif CutsceneIndex == 103:
            EndingCharacter(units.Romra,False,False,False)
        elif CutsceneIndex == 104:
            EndingCharacter(units.TnemecalperI,False,False,False)
        elif CutsceneIndex == 105:
            EndingCharacter(units.TnemecalperII,False,False,False)
        elif CutsceneIndex == 106:
            EndingCharacter(units.TnemecalperIII,False,False,False)
        elif CutsceneIndex == 107:
            EndingCharacter(units.TnemecalperIV,False,False,False)
        elif CutsceneIndex == 108:
            EndingCharacter(units.Lacirtcele,False,False,False)
        elif CutsceneIndex == 109:
            EndingCharacter(units.Damagein,False,False,False)
        elif CutsceneIndex == 110:
            EndingCharacter(units.Healia,False,False,False)
        elif CutsceneIndex == 111:
            EndingCharacter(units.Wob,False,False,False)
        elif CutsceneIndex == 112:
            EndingCharacter(units.Bladen,False,False,False)
        elif CutsceneIndex == 113:
            EndingCharacter(units.Wodahs,False,False,False)
        elif CutsceneIndex == 114:
            EndingCharacter(units.PlayableBladeous,False,False,False)
        elif CutsceneIndex == 115:
            EndingCharacter(units.Azure,False,False,False)
        elif CutsceneIndex == 116:
            EndingCharacter(units.Fael,False,False,False)
        elif CutsceneIndex == 117:
            EndingCharacter(units.Erif,False,False,False)
        elif CutsceneIndex == 118:
            EndingCharacter(units.Vruh,False,False,False)
        elif CutsceneIndex == 119:
            EndingCharacter(units.Recils,False,False,False)
        elif CutsceneIndex == 120:
            EndingCharacter(units.Repins,False,False,False)
        elif CutsceneIndex == 121:
            EndingCharacter(units.Relaeh,False,False,False)
        elif CutsceneIndex == 122:
            EndingCharacter(units.Eulb,False,False,False)
        elif CutsceneIndex == 123:
            EndingCharacter(units.Lias,False,False,False)
        elif CutsceneIndex == 124:
            EndingCharacter(units.Fieht,False,False,False)
        elif CutsceneIndex == 125:
            EndingCharacter(units.Rethgif,False,False,False)
        elif CutsceneIndex == 126:
            EndingCharacter(units.Eg,False,False,False)
        elif CutsceneIndex == 127:
            EndingCharacter(units.Elbon,False,False,False)
        elif CutsceneIndex == 128:
            EndingCharacter(units.B,False,False,False)
        elif CutsceneIndex == 129:
            EndingCharacter(units.Xuirventh,False,False,False)
        elif CutsceneIndex == 130:
            EndingCharacter(units.Xuirfth,False,False,False)
        elif CutsceneIndex == 131:
            EndingCharacter(units.Xuirer,False,False,False)
        elif CutsceneIndex == 132:
            EndingCharacter(units.Dliug,False,False,False)
        elif CutsceneIndex == 133:
            EndingCharacter(units.Exa,False,False,False)
        elif CutsceneIndex == 134:
            EndingCharacter(units.Yranecrem,False,False,False)
        elif CutsceneIndex == 135:
            EndingCharacter(units.Geomer,False,False,False)
        elif CutsceneIndex == 136:
            EndingCharacter(units.Box,False,False,False)
        elif CutsceneIndex == 137:
            EndingCharacter(units.NOTOS,False,False,False)
        elif CutsceneIndex == 138:
            EndingCharacter(units.YungPoggers,False,False,False)
        elif CutsceneIndex == 139:
            EndingCharacter(units.Dnefed,False,False,False)
        elif CutsceneIndex == 140:
            EndingCharacter(units.Thgif,False,False,False)
        elif CutsceneIndex == 141:
            EndingCharacter(units.Gnirif,False,False,False)
        elif CutsceneIndex == 142:
            EndingCharacter(units.Cigam,False,False,False)
        elif CutsceneIndex == 143:
            EndingCharacter(units.Omega,True,False,False)
        elif CutsceneIndex == 144:
            EndingCharacter(units.Fiyghtrr,False,False,False)
        elif CutsceneIndex == 145:
            EndingCharacter(units.Recalper,False,False,False)
        elif CutsceneIndex == 146:
            EndingCharacter(units.Tabmoc,False,False,False)
        elif CutsceneIndex == 147:
            EndingCharacter(units.Xuirurth,False,False,False)
        elif CutsceneIndex == 148:
            EndingCharacter(units.Repins2,False,False,False)
        elif CutsceneIndex == 149:
            EndingCharacter(units.Ahcem,False,False,False)
        elif CutsceneIndex == 150:
            EndingCharacter(units.Cayenne,False,False,False)
        elif CutsceneIndex == 151:
            EndingCharacter(units.XuirMan,False,False,False)
        elif CutsceneIndex == 152:
            EndingCharacter(units.Integer,False,False,False)
        elif CutsceneIndex == 153:
            Text3("                             ~~ Ending 2/10: True Ending ~~")
            line2("|                        This is the canonical ending of the game                        |")
            line3("                 Enter code \"947187\" to start the game in New Game+")
    elif Chapter == "Chapter 27b": #=====================Chapter27b===============================================================
        ChapterLevel = 51
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 27b]")
            line2("[Sector 5, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text2("Repins: Its you again.",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("Proton: Hand over the Holy Itucher.",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text2("Repins: And why should I?",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text2("Repins: I've worked my whole life for this.",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            if units.Erif in units.UnitsRecruited:
                Text2("Repins: And of course, you killed Erif.",units.Proton.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                 
            else:
                Text2("Repins: And of course, you killed Wob.",units.Proton.Portrait,units.Repins2.Portrait)
                CutsceneIndex += 1
                 
        elif CutsceneIndex == 8:
            Text2("Repins: You really aren't in a position to be making demands,",units.Proton.Portrait,units.Repins2.Portrait)
            line2("I'm the one with the weapon of destruction after all.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text2("Repins: And I think you need to pay for what you've done.",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            screensetup.BattleScreen.bgcolor("indigo")
            Text3("(Repins activates the Holy Itucher)")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27bEnemies
            UnitFormation = placeunits.Chapter27bPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 11:
            Text2("Repins: N... NO...",units.Proton.Portrait,units.RepinsBoss1.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            Text2("Repins: I... MUST...",units.Proton.Portrait,units.RepinsBoss1.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text2("Repins: ...",units.Proton.Portrait,units.RepinsBoss1.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text3("(Repins has been defeated)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 16:
            Text3("(Proton picks up the Holy Itucher)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text1("Proton: There have been many losses throughout our journey...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text1("Proton: It is because of these sacrifices that we are here today...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text1("Proton: We must not forget those who have been lost in the fight for",units.Proton.Portrait)
            line2("the Holy Itucher...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(And so the Static Army returned to the Continent of Bipole, successfully")
            line2("retrieving the Holy Itucher...)")
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            EndingCharacter(units.Proton,False,False,False)
        elif CutsceneIndex == 101:
            EndingCharacter(units.Quest,False,False,False)
        elif CutsceneIndex == 102:
            EndingCharacter(units.Scien,False,False,False)
        elif CutsceneIndex == 103:
            EndingCharacter(units.Romra,False,False,False)
        elif CutsceneIndex == 104:
            EndingCharacter(units.TnemecalperI,False,False,False)
        elif CutsceneIndex == 105:
            EndingCharacter(units.TnemecalperII,False,False,False)
        elif CutsceneIndex == 106:
            EndingCharacter(units.TnemecalperIII,False,False,False)
        elif CutsceneIndex == 107:
            EndingCharacter(units.TnemecalperIV,False,False,False)
        elif CutsceneIndex == 108:
            EndingCharacter(units.Lacirtcele,False,False,False)
        elif CutsceneIndex == 109:
            EndingCharacter(units.Damagein,False,False,False)
        elif CutsceneIndex == 110:
            EndingCharacter(units.Healia,False,False,False)
        elif CutsceneIndex == 111:
            EndingCharacter(units.Wob,False,False,False)
        elif CutsceneIndex == 112:
            EndingCharacter(units.Bladen,False,False,False)
        elif CutsceneIndex == 113:
            EndingCharacter(units.Wodahs,False,False,False)
        elif CutsceneIndex == 114:
            EndingCharacter(units.PlayableBladeous,False,False,False)
        elif CutsceneIndex == 115:
            EndingCharacter(units.Azure,False,False,False)
        elif CutsceneIndex == 116:
            EndingCharacter(units.Fael,False,False,False)
        elif CutsceneIndex == 117:
            EndingCharacter(units.Erif,False,False,False)
        elif CutsceneIndex == 118:
            EndingCharacter(units.Vruh,False,False,False)
        elif CutsceneIndex == 119:
            EndingCharacter(units.Recils,False,False,False)
        elif CutsceneIndex == 120:
            EndingCharacter(units.Repins,False,False,False)
        elif CutsceneIndex == 121:
            EndingCharacter(units.Relaeh,False,False,False)
        elif CutsceneIndex == 122:
            EndingCharacter(units.Eulb,False,False,False)
        elif CutsceneIndex == 123:
            EndingCharacter(units.Lias,False,False,False)
        elif CutsceneIndex == 124:
            EndingCharacter(units.Fieht,False,False,False)
        elif CutsceneIndex == 125:
            EndingCharacter(units.Rethgif,False,False,False)
        elif CutsceneIndex == 126:
            EndingCharacter(units.Eg,False,False,False)
        elif CutsceneIndex == 127:
            EndingCharacter(units.Elbon,False,False,False)
        elif CutsceneIndex == 128:
            EndingCharacter(units.B,False,False,False)
        elif CutsceneIndex == 129:
            EndingCharacter(units.Xuirventh,False,False,False)
        elif CutsceneIndex == 130:
            EndingCharacter(units.Xuirfth,False,False,False)
        elif CutsceneIndex == 131:
            EndingCharacter(units.Xuirer,False,False,False)
        elif CutsceneIndex == 132:
            EndingCharacter(units.Dliug,False,False,False)
        elif CutsceneIndex == 133:
            EndingCharacter(units.Exa,False,False,False)
        elif CutsceneIndex == 134:
            EndingCharacter(units.Yranecrem,False,False,False)
        elif CutsceneIndex == 135:
            EndingCharacter(units.Geomer,False,False,False)
        elif CutsceneIndex == 136:
            EndingCharacter(units.Box,False,False,False)
        elif CutsceneIndex == 137:
            EndingCharacter(units.NOTOS,False,False,False)
        elif CutsceneIndex == 138:
            EndingCharacter(units.YungPoggers,False,False,False)
        elif CutsceneIndex == 139:
            EndingCharacter(units.Dnefed,False,False,False)
        elif CutsceneIndex == 140:
            EndingCharacter(units.Thgif,False,False,False)
        elif CutsceneIndex == 141:
            EndingCharacter(units.Gnirif,False,False,False)
        elif CutsceneIndex == 142:
            EndingCharacter(units.Cigam,False,False,False)
        elif CutsceneIndex == 143:
            EndingCharacter(units.Omega,True,False,False)
        elif CutsceneIndex == 144:
            EndingCharacter(units.Fiyghtrr,False,False,False)
        elif CutsceneIndex == 145:
            EndingCharacter(units.Recalper,False,False,False)
        elif CutsceneIndex == 146:
            EndingCharacter(units.Tabmoc,False,False,False)
        elif CutsceneIndex == 147:
            EndingCharacter(units.Xuirurth,False,False,False)
        elif CutsceneIndex == 148:
            EndingCharacter(units.Repins2,False,False,False)
        elif CutsceneIndex == 149:
            EndingCharacter(units.Ahcem,False,False,False)
        elif CutsceneIndex == 150:
            EndingCharacter(units.Cayenne,False,False,False)
        elif CutsceneIndex == 151:
            EndingCharacter(units.XuirMan,False,False,False)
        elif CutsceneIndex == 152:
            EndingCharacter(units.Integer,False,False,False)
        elif CutsceneIndex == 153:
            Text3("                          ~~ Ending 3/10: Repins Ending 1 ~~")
            line2("|    Repins possessed by Itucher, Itucher retrieved by Proton, timeline intact    |")
            line3("                 Enter code \"947187\" to start the game in New Game+")
    elif Chapter == "Chapter 27c": #=====================Chapter27c===============================================================
        ChapterLevel = 51
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 27c]")
            line2("[Sector 5, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text2("Proton: Hand over the Itucher.",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("Repins: Huh, it's you...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text2("Repins: YOU!",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text2("Repins: You're the one who killed my family...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            Text2("Repins: And now that I've gotten the Itucher, you're",units.Proton.Portrait,units.Repins2.Portrait)
            line2("trying to take that away too.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text2("Repins: Why the hell would I willingly give you the",units.Proton.Portrait,units.Repins2.Portrait)
            line2("Itucher?")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            screensetup.BattleScreen.bgcolor("red")
            Text3("(Repins activates the Itucher)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text3("(An explosion of energy is shot out from the activation)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            for unit in units.UnitsAlive:
                unit.CurrentHP -= 20
            Text3("[All of your party members took 20 damage!]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            screensetup.BattleScreen.bgcolor("orange")
            Text2("Repins: I'll kill you all, maybe it won't be as fun when",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            line2("you're on the other side.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text2("Repins: And with this power, I'll destroy Sine and bring",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            line2("Quad back to power...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text2("Repins: I'll create an empire that will conquer this world...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 15:
            Text2("Repins: And under my rule, this world will finally attain peace!",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27c1Enemies
            UnitFormation = placeunits.Chapter27c1Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 16:
            Text2("Repins: ...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 17:
            Text2("Repins: You... you really think... you've defeated me?",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 18:
            Text2("Repins: Heh... this isn't even... my true power...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27c2Enemies
            UnitFormation = placeunits.Chapter27c2Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 19:
            Text2("Repins: ...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 20:
            Text2("Repins: I won't... be stopped... just by that...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 21:
            Text2("Repins: Prepare... to die...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27c3Enemies
            UnitFormation = placeunits.Chapter27c3Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 22:
            Text2("Repins: ...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 23:
            screensetup.BattleScreen.bgcolor("red")
            Text2("Repins: ARGHHHHHHHHHHHHHHH!!!!!!!!!!!!!",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 24:
            Text2("Repins: I HAVE THE ITUCHER!!!!!!!!!!",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 25:
            Text2("Repins: I'M INVINCIBLE!!!!!!!!!!!!!",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 26:
            Text2("Repins: I MUST WIN!!!!!!!!!!!!!",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27c4Enemies
            UnitFormation = placeunits.Chapter27c4Placement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 27:
            Text2("Repins: ...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            Text2("Repins: How...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 29:
            Text2("Repins: How can I lose...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 30:
            screensetup.BattleScreen.bgcolor("orange")
            Text2("Repins: Was it all...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 31:
            Text2("Repins: Everything I did...",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 32:
            Text2("Repins: ...meaningless?",units.Proton.Portrait,units.RepinsBoss2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 33:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 34:
            Text2("Repins: Erif...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 35:
            Text2("Repins: Wob...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 36:
            Text2("Repins: I'm sorry...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 37:
            Text2("Repins: ...",units.Proton.Portrait,units.Repins2.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 38:
            Text3("[Repins has been defeated]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 39:
            Text1("Proton: .",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 40:
            Text1("Proton: ..",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 41:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 42:
            Text3("(Proton picks up the Holy Itucher)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 43:
            Text1("Proton: There have been many losses throughout our journey...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 44:
            Text1("Proton: It is because of these sacrifices that we are here today...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 45:
            Text1("Proton: We must not forget those who have been lost in the fight for",units.Proton.Portrait)
            line2("the Holy Itucher...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 46:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 47:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(And so the Static Army returned to the Continent of Bipole, successfully")
            line2("retrieving the Holy Itucher...)")
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            EndingCharacter(units.Proton,False,False,False)
        elif CutsceneIndex == 101:
            EndingCharacter(units.Quest,False,False,False)
        elif CutsceneIndex == 102:
            EndingCharacter(units.Scien,False,False,False)
        elif CutsceneIndex == 103:
            EndingCharacter(units.Romra,False,False,False)
        elif CutsceneIndex == 104:
            EndingCharacter(units.TnemecalperI,False,False,False)
        elif CutsceneIndex == 105:
            EndingCharacter(units.TnemecalperII,False,False,False)
        elif CutsceneIndex == 106:
            EndingCharacter(units.TnemecalperIII,False,False,False)
        elif CutsceneIndex == 107:
            EndingCharacter(units.TnemecalperIV,False,False,False)
        elif CutsceneIndex == 108:
            EndingCharacter(units.Lacirtcele,False,False,False)
        elif CutsceneIndex == 109:
            EndingCharacter(units.Damagein,False,False,False)
        elif CutsceneIndex == 110:
            EndingCharacter(units.Healia,False,False,False)
        elif CutsceneIndex == 111:
            EndingCharacter(units.Wob,False,False,False)
        elif CutsceneIndex == 112:
            EndingCharacter(units.Bladen,False,False,False)
        elif CutsceneIndex == 113:
            EndingCharacter(units.Wodahs,False,False,False)
        elif CutsceneIndex == 114:
            EndingCharacter(units.PlayableBladeous,False,False,False)
        elif CutsceneIndex == 115:
            EndingCharacter(units.Azure,False,False,False)
        elif CutsceneIndex == 116:
            EndingCharacter(units.Fael,False,False,False)
        elif CutsceneIndex == 117:
            EndingCharacter(units.Erif,False,False,False)
        elif CutsceneIndex == 118:
            EndingCharacter(units.Vruh,False,False,False)
        elif CutsceneIndex == 119:
            EndingCharacter(units.Recils,False,False,False)
        elif CutsceneIndex == 120:
            EndingCharacter(units.Repins,False,False,False)
        elif CutsceneIndex == 121:
            EndingCharacter(units.Relaeh,False,False,False)
        elif CutsceneIndex == 122:
            EndingCharacter(units.Eulb,False,False,False)
        elif CutsceneIndex == 123:
            EndingCharacter(units.Lias,False,False,False)
        elif CutsceneIndex == 124:
            EndingCharacter(units.Fieht,False,False,False)
        elif CutsceneIndex == 125:
            EndingCharacter(units.Rethgif,False,False,False)
        elif CutsceneIndex == 126:
            EndingCharacter(units.Eg,False,False,False)
        elif CutsceneIndex == 127:
            EndingCharacter(units.Elbon,False,False,False)
        elif CutsceneIndex == 128:
            EndingCharacter(units.B,False,False,False)
        elif CutsceneIndex == 129:
            EndingCharacter(units.Xuirventh,False,False,False)
        elif CutsceneIndex == 130:
            EndingCharacter(units.Xuirfth,False,False,False)
        elif CutsceneIndex == 131:
            EndingCharacter(units.Xuirer,False,False,False)
        elif CutsceneIndex == 132:
            EndingCharacter(units.Dliug,False,False,False)
        elif CutsceneIndex == 133:
            EndingCharacter(units.Exa,False,False,False)
        elif CutsceneIndex == 134:
            EndingCharacter(units.Yranecrem,False,False,False)
        elif CutsceneIndex == 135:
            EndingCharacter(units.Geomer,False,False,False)
        elif CutsceneIndex == 136:
            EndingCharacter(units.Box,False,False,False)
        elif CutsceneIndex == 137:
            EndingCharacter(units.NOTOS,False,False,False)
        elif CutsceneIndex == 138:
            EndingCharacter(units.YungPoggers,False,False,False)
        elif CutsceneIndex == 139:
            EndingCharacter(units.Dnefed,False,False,False)
        elif CutsceneIndex == 140:
            EndingCharacter(units.Thgif,False,False,False)
        elif CutsceneIndex == 141:
            EndingCharacter(units.Gnirif,False,False,False)
        elif CutsceneIndex == 142:
            EndingCharacter(units.Cigam,False,False,False)
        elif CutsceneIndex == 143:
            EndingCharacter(units.Omega,True,False,False)
        elif CutsceneIndex == 144:
            EndingCharacter(units.Fiyghtrr,False,False,False)
        elif CutsceneIndex == 145:
            EndingCharacter(units.Recalper,False,False,False)
        elif CutsceneIndex == 146:
            EndingCharacter(units.Tabmoc,False,False,False)
        elif CutsceneIndex == 147:
            EndingCharacter(units.Xuirurth,False,False,False)
        elif CutsceneIndex == 148:
            EndingCharacter(units.Repins2,False,False,False)
        elif CutsceneIndex == 149:
            EndingCharacter(units.Ahcem,False,False,False)
        elif CutsceneIndex == 150:
            EndingCharacter(units.Cayenne,False,False,False)
        elif CutsceneIndex == 151:
            EndingCharacter(units.XuirMan,False,False,False)
        elif CutsceneIndex == 152:
            EndingCharacter(units.Integer,False,False,False)
        elif CutsceneIndex == 153:
            Text3("                          ~~ Ending 4/10: Repins Ending 2 ~~")
            line2("| Repins controlled the Itucher, Itucher retrieved by Proton, timeline intact |")
            line3("                 Enter code \"947187\" to start the game in New Game+")
    elif Chapter == "Chapter 27d": #=====================Chapter27d===============================================================
        ChapterLevel = 51
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 27d]")
            line2("[Sector 5, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Proton: !!!",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text1("Proton: There it is! The Holy Itucher!",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("Vruh: The Holy Itucher?",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text2("Vruh: What a quirky bruh moment would it be if I were to take the",units.Proton.Portrait,units.Vruh.Portrait)
            line2("Itucher for myself and commit mass homicide.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text2("Proton: What.",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text3("[Vruh takes the Holy Itucher]")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text2("Vruh: Bruh-huh!",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text2("Proton: What are you doing!?",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            Text2("Vruh: Not activating it, that's for sure.",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            Text2("Vruh: I ain't dumb enough to let myself get possessed.",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            Text2("Proton: Yet you're dumb enough to \"commit mass homicide\"",units.Proton.Portrait,units.Vruh.Portrait)
            line2("for a \"quirky bruh moment\"...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text2("Vruh: Prepare to die for no reason, yuh!",units.Proton.Portrait,units.Vruh.Portrait)
            units.VruhBoss.ATK = units.Vruh.ATK
            units.VruhBoss.MaxHP = units.Vruh.MaxHP
            units.VruhBoss.CurrentHP = units.Vruh.CurrentHP
            units.VruhBoss.DEF = units.Vruh.DEF
            units.VruhBoss.RES = units.Vruh.RES
            units.VruhBoss.AGL = units.Vruh.AGL
            units.VruhBoss.ACR = units.Vruh.ACR
            units.VruhBoss.Attacks = units.Vruh.Attacks
            units.VruhBoss.Supports = units.Vruh.Supports
            units.VruhBoss.Level = units.Vruh.Level
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text3("[Vruh has left your party]")
            units.UnitsAlive.remove(units.Vruh)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27dEnemies
            UnitFormation = placeunits.Chapter27dPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 15:
            Text2("Vruh: This... truly is...",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text2("Vruh: A bruh moment...",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text2("Vruh: I'm glad... I was able to... experience it...",units.Proton.Portrait,units.Vruh.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text3("[Vruh has been defeated]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 20:
            Text1("Proton: Well that happened...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 21:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text3("(Proton picks up the Holy Itucher)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text1("Proton: There have been many losses throughout our journey...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text1("Proton: It is because of these sacrifices that we are here today...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text1("Proton: We must not forget those who have been lost in the fight for",units.Proton.Portrait)
            line2("the Holy Itucher...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(And so the Static Army returned to the Continent of Bipole, successfully")
            line2("retrieving the Holy Itucher...)")
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            EndingCharacter(units.Proton,False,False,False)
        elif CutsceneIndex == 101:
            EndingCharacter(units.Quest,False,False,False)
        elif CutsceneIndex == 102:
            EndingCharacter(units.Scien,False,False,False)
        elif CutsceneIndex == 103:
            EndingCharacter(units.Romra,False,False,False)
        elif CutsceneIndex == 104:
            EndingCharacter(units.TnemecalperI,False,False,False)
        elif CutsceneIndex == 105:
            EndingCharacter(units.TnemecalperII,False,False,False)
        elif CutsceneIndex == 106:
            EndingCharacter(units.TnemecalperIII,False,False,False)
        elif CutsceneIndex == 107:
            EndingCharacter(units.TnemecalperIV,False,False,False)
        elif CutsceneIndex == 108:
            EndingCharacter(units.Lacirtcele,False,False,False)
        elif CutsceneIndex == 109:
            EndingCharacter(units.Damagein,False,False,False)
        elif CutsceneIndex == 110:
            EndingCharacter(units.Healia,False,False,False)
        elif CutsceneIndex == 111:
            EndingCharacter(units.Wob,False,False,False)
        elif CutsceneIndex == 112:
            EndingCharacter(units.Bladen,False,False,False)
        elif CutsceneIndex == 113:
            EndingCharacter(units.Wodahs,False,False,False)
        elif CutsceneIndex == 114:
            EndingCharacter(units.PlayableBladeous,False,False,False)
        elif CutsceneIndex == 115:
            EndingCharacter(units.Azure,False,False,False)
        elif CutsceneIndex == 116:
            EndingCharacter(units.Fael,False,False,False)
        elif CutsceneIndex == 117:
            EndingCharacter(units.Erif,False,False,False)
        elif CutsceneIndex == 118:
            EndingCharacter(units.Vruh,False,False,False)
        elif CutsceneIndex == 119:
            EndingCharacter(units.Recils,False,False,False)
        elif CutsceneIndex == 120:
            EndingCharacter(units.Repins,False,False,False)
        elif CutsceneIndex == 121:
            EndingCharacter(units.Relaeh,False,False,False)
        elif CutsceneIndex == 122:
            EndingCharacter(units.Eulb,False,False,False)
        elif CutsceneIndex == 123:
            EndingCharacter(units.Lias,False,False,False)
        elif CutsceneIndex == 124:
            EndingCharacter(units.Fieht,False,False,False)
        elif CutsceneIndex == 125:
            EndingCharacter(units.Rethgif,False,False,False)
        elif CutsceneIndex == 126:
            EndingCharacter(units.Eg,False,False,False)
        elif CutsceneIndex == 127:
            EndingCharacter(units.Elbon,False,False,False)
        elif CutsceneIndex == 128:
            EndingCharacter(units.B,False,False,False)
        elif CutsceneIndex == 129:
            EndingCharacter(units.Xuirventh,False,False,False)
        elif CutsceneIndex == 130:
            EndingCharacter(units.Xuirfth,False,False,False)
        elif CutsceneIndex == 131:
            EndingCharacter(units.Xuirer,False,False,False)
        elif CutsceneIndex == 132:
            EndingCharacter(units.Dliug,False,False,False)
        elif CutsceneIndex == 133:
            EndingCharacter(units.Exa,False,False,False)
        elif CutsceneIndex == 134:
            EndingCharacter(units.Yranecrem,False,False,False)
        elif CutsceneIndex == 135:
            EndingCharacter(units.Geomer,False,False,False)
        elif CutsceneIndex == 136:
            EndingCharacter(units.Box,False,False,False)
        elif CutsceneIndex == 137:
            EndingCharacter(units.NOTOS,False,False,False)
        elif CutsceneIndex == 138:
            EndingCharacter(units.YungPoggers,False,False,False)
        elif CutsceneIndex == 139:
            EndingCharacter(units.Dnefed,False,False,False)
        elif CutsceneIndex == 140:
            EndingCharacter(units.Thgif,False,False,False)
        elif CutsceneIndex == 141:
            EndingCharacter(units.Gnirif,False,False,False)
        elif CutsceneIndex == 142:
            EndingCharacter(units.Cigam,False,False,False)
        elif CutsceneIndex == 143:
            EndingCharacter(units.Omega,True,False,False)
        elif CutsceneIndex == 144:
            EndingCharacter(units.Fiyghtrr,False,False,False)
        elif CutsceneIndex == 145:
            EndingCharacter(units.Recalper,False,False,False)
        elif CutsceneIndex == 146:
            EndingCharacter(units.Tabmoc,False,False,False)
        elif CutsceneIndex == 147:
            EndingCharacter(units.Xuirurth,False,False,False)
        elif CutsceneIndex == 148:
            EndingCharacter(units.Repins2,False,False,False)
        elif CutsceneIndex == 149:
            EndingCharacter(units.Ahcem,False,False,False)
        elif CutsceneIndex == 150:
            EndingCharacter(units.Cayenne,False,False,False)
        elif CutsceneIndex == 151:
            EndingCharacter(units.XuirMan,False,False,False)
        elif CutsceneIndex == 152:
            EndingCharacter(units.Integer,False,False,False)
        elif CutsceneIndex == 153:
            Text3("                             ~~ Ending 5/10: Vruh Ending ~~")
            line2("|      Vruh took the Itucher, Itucher retrieved by Proton, timeline intact      |")
            line3("                 Enter code \"947187\" to start the game in New Game+")
    elif Chapter == "Chapter 27e": #=====================Chapter27e===============================================================
        ChapterLevel = 51
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 27e]")
            line2("[Sector 5, Shadow Realm Research Center]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Proton: !!!",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text1("Proton: There it is! The Holy Itucher!",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("Ahcem: Already?",units.Proton.Portrait,units.Ahcem.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text2("Ahcem: This is too easy.",units.Proton.Portrait,units.Ahcem.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text2("Ahcem: There's no challenge to this.",units.Proton.Portrait,units.Ahcem.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            screensetup.BattleScreen.bgcolor("red")
            Text3("(Something in the room explodes)")
            units.UnitsAlive.remove(units.Ahcem)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            screensetup.BattleScreen.bgcolor("crimson")
            Text2("Ahcem: Rise, Etamitlu! The ultimate mechanical!",units.Proton.Portrait,units.Ahcem.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text3("(Ahcem has left your party)")
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27eEnemies
            UnitFormation = placeunits.Chapter27ePlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 10:
            Text2("Etamitlu: ...",units.Proton.Portrait,units.Etamitlu.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            screensetup.BattleScreen.bgcolor("dark gray")
            Text3("(Etamitlu and Ahcem disappear)")
            units.UnitsAlive.remove(units.Ahcem)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text1("Proton: Well that happened...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text3("(Proton picks up the Holy Itucher)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text1("Proton: There have been many losses throughout our journey...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text1("Proton: It is because of these sacrifices that we are here today...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text1("Proton: We must not forget those who have been lost in the fight for",units.Proton.Portrait)
            line2("the Holy Itucher...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(And so the Static Army returned to the Continent of Bipole, successfully")
            line2("retrieving the Holy Itucher...)")
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            EndingCharacter(units.Proton,False,False,False)
        elif CutsceneIndex == 101:
            EndingCharacter(units.Quest,False,False,False)
        elif CutsceneIndex == 102:
            EndingCharacter(units.Scien,False,False,False)
        elif CutsceneIndex == 103:
            EndingCharacter(units.Romra,False,False,False)
        elif CutsceneIndex == 104:
            EndingCharacter(units.TnemecalperI,False,False,False)
        elif CutsceneIndex == 105:
            EndingCharacter(units.TnemecalperII,False,False,False)
        elif CutsceneIndex == 106:
            EndingCharacter(units.TnemecalperIII,False,False,False)
        elif CutsceneIndex == 107:
            EndingCharacter(units.TnemecalperIV,False,False,False)
        elif CutsceneIndex == 108:
            EndingCharacter(units.Lacirtcele,False,False,False)
        elif CutsceneIndex == 109:
            EndingCharacter(units.Damagein,False,False,False)
        elif CutsceneIndex == 110:
            EndingCharacter(units.Healia,False,False,False)
        elif CutsceneIndex == 111:
            EndingCharacter(units.Wob,False,False,False)
        elif CutsceneIndex == 112:
            EndingCharacter(units.Bladen,False,False,False)
        elif CutsceneIndex == 113:
            EndingCharacter(units.Wodahs,False,False,False)
        elif CutsceneIndex == 114:
            EndingCharacter(units.PlayableBladeous,False,False,False)
        elif CutsceneIndex == 115:
            EndingCharacter(units.Azure,False,False,False)
        elif CutsceneIndex == 116:
            EndingCharacter(units.Fael,False,False,False)
        elif CutsceneIndex == 117:
            EndingCharacter(units.Erif,False,False,False)
        elif CutsceneIndex == 118:
            EndingCharacter(units.Vruh,False,False,False)
        elif CutsceneIndex == 119:
            EndingCharacter(units.Recils,False,False,False)
        elif CutsceneIndex == 120:
            EndingCharacter(units.Repins,False,False,False)
        elif CutsceneIndex == 121:
            EndingCharacter(units.Relaeh,False,False,False)
        elif CutsceneIndex == 122:
            EndingCharacter(units.Eulb,False,False,False)
        elif CutsceneIndex == 123:
            EndingCharacter(units.Lias,False,False,False)
        elif CutsceneIndex == 124:
            EndingCharacter(units.Fieht,False,False,False)
        elif CutsceneIndex == 125:
            EndingCharacter(units.Rethgif,False,False,False)
        elif CutsceneIndex == 126:
            EndingCharacter(units.Eg,False,False,False)
        elif CutsceneIndex == 127:
            EndingCharacter(units.Elbon,False,False,False)
        elif CutsceneIndex == 128:
            EndingCharacter(units.B,False,False,False)
        elif CutsceneIndex == 129:
            EndingCharacter(units.Xuirventh,False,False,False)
        elif CutsceneIndex == 130:
            EndingCharacter(units.Xuirfth,False,False,False)
        elif CutsceneIndex == 131:
            EndingCharacter(units.Xuirer,False,False,False)
        elif CutsceneIndex == 132:
            EndingCharacter(units.Dliug,False,False,False)
        elif CutsceneIndex == 133:
            EndingCharacter(units.Exa,False,False,False)
        elif CutsceneIndex == 134:
            EndingCharacter(units.Yranecrem,False,False,False)
        elif CutsceneIndex == 135:
            EndingCharacter(units.Geomer,False,False,False)
        elif CutsceneIndex == 136:
            EndingCharacter(units.Box,False,False,False)
        elif CutsceneIndex == 137:
            EndingCharacter(units.NOTOS,False,False,False)
        elif CutsceneIndex == 138:
            EndingCharacter(units.YungPoggers,False,False,False)
        elif CutsceneIndex == 139:
            EndingCharacter(units.Dnefed,False,False,False)
        elif CutsceneIndex == 140:
            EndingCharacter(units.Thgif,False,False,False)
        elif CutsceneIndex == 141:
            EndingCharacter(units.Gnirif,False,False,False)
        elif CutsceneIndex == 142:
            EndingCharacter(units.Cigam,False,False,False)
        elif CutsceneIndex == 143:
            EndingCharacter(units.Omega,True,False,False)
        elif CutsceneIndex == 144:
            EndingCharacter(units.Fiyghtrr,False,False,False)
        elif CutsceneIndex == 145:
            EndingCharacter(units.Recalper,False,False,False)
        elif CutsceneIndex == 146:
            EndingCharacter(units.Tabmoc,False,False,False)
        elif CutsceneIndex == 147:
            EndingCharacter(units.Xuirurth,False,False,False)
        elif CutsceneIndex == 148:
            EndingCharacter(units.Repins2,False,False,False)
        elif CutsceneIndex == 149:
            EndingCharacter(units.Ahcem,False,False,False)
        elif CutsceneIndex == 150:
            EndingCharacter(units.Cayenne,False,False,False)
        elif CutsceneIndex == 151:
            EndingCharacter(units.XuirMan,False,False,False)
        elif CutsceneIndex == 152:
            EndingCharacter(units.Integer,False,False,False)
        elif CutsceneIndex == 153:
            Text3("                             ~~ Ending 6/10: Bonus Ending ~~")
            line2("|      Etamitlu was summoned, Itucher retrieved by Proton, timeline intact      |")
            line3("                 Enter code \"947187\" to start the game in New Game+")
    elif Chapter == "Bad Ending": #=====================BadEnding===============================================================
        if CutsceneIndex == 0:
            CutsceneIndex += 1
            Cutscene()
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("Quest: ...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Quest: Hmmm? What's this?",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text3("(Quest pulls a lever on the wall, opening up a container)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text1("Quest: Is this...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            Text1("Quest: Yes! It is!",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text1("Quest: The Holy Itucher...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            Text1("Quest: It's here, right in front of me...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text1("Quest: My life's work of study and research...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text1("Quest: After all of these years...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            Text1("Quest: It's finally...",units.Quest.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            Text2("Proton: Quest, did you find the Itu...",units.Quest.Portrait,units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            screensetup.BattleScreen.bgcolor("red")
            Text3("(Proton is blasted back by an explosion around Quest)")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            screensetup.BattleScreen.bgcolor("indigo")
            Text1("Proton: Wh...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text1("Proton: Quest! Don't activate the Itucher!",units.Proton.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 15:
            Text2("Quest: ...",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 16:
            Text2("Proton: Quest!",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 17:
            Text3("(Quest stabs Proton with the Holy Itucher)")
            CutsceneIndex += 1
              
        elif CutsceneIndex == 18:
            Text2("Quest: ...",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
              
        elif CutsceneIndex == 19:
            Text2("Proton: Quest...",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text2("Quest: ...",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text2("Proton: ...",units.Proton.Portrait,units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 22:
            Text3("[Proton has been defeated]")
            units.UnitsAlive.remove(units.Proton)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text1("Quest: .",units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text1("Quest: ..",units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text1("Quest: ...",units.QuestBoss.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(...)")
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            EndingCharacter(units.Proton,False,False,False)
        elif CutsceneIndex == 101:
            EndingCharacter(units.Quest,False,False,False)
        elif CutsceneIndex == 102:
            EndingCharacter(units.Scien,False,False,False)
        elif CutsceneIndex == 103:
            EndingCharacter(units.Romra,False,False,False)
        elif CutsceneIndex == 104:
            EndingCharacter(units.TnemecalperI,False,False,False)
        elif CutsceneIndex == 105:
            EndingCharacter(units.TnemecalperII,False,False,False)
        elif CutsceneIndex == 106:
            EndingCharacter(units.TnemecalperIII,False,False,False)
        elif CutsceneIndex == 107:
            EndingCharacter(units.TnemecalperIV,False,False,False)
        elif CutsceneIndex == 108:
            EndingCharacter(units.Lacirtcele,False,False,False)
        elif CutsceneIndex == 109:
            EndingCharacter(units.Damagein,False,False,False)
        elif CutsceneIndex == 110:
            EndingCharacter(units.Healia,False,False,False)
        elif CutsceneIndex == 111:
            EndingCharacter(units.Wob,False,False,False)
        elif CutsceneIndex == 112:
            EndingCharacter(units.Bladen,False,False,False)
        elif CutsceneIndex == 113:
            EndingCharacter(units.Wodahs,False,False,False)
        elif CutsceneIndex == 114:
            EndingCharacter(units.PlayableBladeous,False,False,False)
        elif CutsceneIndex == 115:
            EndingCharacter(units.Azure,False,False,False)
        elif CutsceneIndex == 116:
            EndingCharacter(units.Fael,False,False,False)
        elif CutsceneIndex == 117:
            EndingCharacter(units.Erif,False,False,False)
        elif CutsceneIndex == 118:
            EndingCharacter(units.Vruh,False,False,False)
        elif CutsceneIndex == 119:
            EndingCharacter(units.Recils,False,False,False)
        elif CutsceneIndex == 120:
            EndingCharacter(units.Repins,False,False,False)
        elif CutsceneIndex == 121:
            EndingCharacter(units.Relaeh,False,False,False)
        elif CutsceneIndex == 122:
            EndingCharacter(units.Eulb,False,False,False)
        elif CutsceneIndex == 123:
            EndingCharacter(units.Lias,False,False,False)
        elif CutsceneIndex == 124:
            EndingCharacter(units.Fieht,False,False,False)
        elif CutsceneIndex == 125:
            EndingCharacter(units.Rethgif,False,False,False)
        elif CutsceneIndex == 126:
            EndingCharacter(units.Eg,False,False,False)
        elif CutsceneIndex == 127:
            EndingCharacter(units.Elbon,False,False,False)
        elif CutsceneIndex == 128:
            EndingCharacter(units.B,False,False,False)
        elif CutsceneIndex == 129:
            EndingCharacter(units.Xuirventh,False,False,False)
        elif CutsceneIndex == 130:
            EndingCharacter(units.Xuirfth,False,False,False)
        elif CutsceneIndex == 131:
            EndingCharacter(units.Xuirer,False,False,False)
        elif CutsceneIndex == 132:
            EndingCharacter(units.Dliug,False,False,False)
        elif CutsceneIndex == 133:
            EndingCharacter(units.Exa,False,False,False)
        elif CutsceneIndex == 134:
            EndingCharacter(units.Yranecrem,False,False,False)
        elif CutsceneIndex == 135:
            EndingCharacter(units.Geomer,False,False,False)
        elif CutsceneIndex == 136:
            EndingCharacter(units.Box,False,False,False)
        elif CutsceneIndex == 137:
            EndingCharacter(units.NOTOS,False,False,False)
        elif CutsceneIndex == 138:
            EndingCharacter(units.YungPoggers,False,False,False)
        elif CutsceneIndex == 139:
            EndingCharacter(units.Dnefed,False,False,False)
        elif CutsceneIndex == 140:
            EndingCharacter(units.Thgif,False,False,False)
        elif CutsceneIndex == 141:
            EndingCharacter(units.Gnirif,False,False,False)
        elif CutsceneIndex == 142:
            EndingCharacter(units.Cigam,False,False,False)
        elif CutsceneIndex == 143:
            EndingCharacter(units.Omega,True,False,False)
        elif CutsceneIndex == 144:
            EndingCharacter(units.Fiyghtrr,False,False,False)
        elif CutsceneIndex == 145:
            EndingCharacter(units.Recalper,False,False,False)
        elif CutsceneIndex == 146:
            EndingCharacter(units.Tabmoc,False,False,False)
        elif CutsceneIndex == 147:
            EndingCharacter(units.Xuirurth,False,False,False)
        elif CutsceneIndex == 148:
            EndingCharacter(units.Repins2,False,False,False)
        elif CutsceneIndex == 149:
            EndingCharacter(units.Ahcem,False,False,False)
        elif CutsceneIndex == 150:
            EndingCharacter(units.Cayenne,False,False,False)
        elif CutsceneIndex == 151:
            EndingCharacter(units.XuirMan,False,False,False)
        elif CutsceneIndex == 152:
            EndingCharacter(units.Integer,False,False,False)
        elif CutsceneIndex == 153:
            Text3("[And so Quest became possessed by the Holy Itucher,")
            line2("unable to control it's power]")
            
            CutsceneIndex += 1
            
        elif CutsceneIndex == 154:
            Text3("[The rest of the Static Army was slaughtered by Quest]")
            
            CutsceneIndex += 1
            
        elif CutsceneIndex == 155:
            Text3("[Quest's actions defied the writings of the Neville Prophecy,")
            line2("causing a distortion in the timeline and caused the unleashing")
            line3("of the Xuir Wrath]")
            
            CutsceneIndex += 1
            
        elif CutsceneIndex == 156:
            Text3("[Quest was unable to stop the Xuir Wrath, and was defeated by")
            line2("The One Who Consumes All]")
            
            CutsceneIndex += 1
            
        elif CutsceneIndex == 157:
            Text3("[...]")
            
            CutsceneIndex += 1
            
        elif CutsceneIndex == 158:
            Text3("[If only you were able to prevent this, " + username.UserName + "...]")
            
            CutsceneIndex += 1
            
        elif CutsceneIndex == 159:
            Text3("[This is a lot to deal with, you know?]")
            
            CutsceneIndex += 1
            
        elif CutsceneIndex == 160:
            Text3("[-Azure]")
            
            CutsceneIndex += 1
            
        elif CutsceneIndex == 161:
            Text3("                             ~~ Ending 7/10: Bad Ending ~~")
            line2("|  Quest took the Itucher, Itucher not retrieved by Proton, timeline destroyed  |")
            line3("                 Enter code \"947187\" to start the game in New Game+")
    elif Chapter == "Neutral Ending": #=====================NeutralEnding===============================================================
        if CutsceneIndex == 0:
            CutsceneIndex += 1
            Cutscene()
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Proton: !!!",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text1("Proton: There it is, The Holy Itucher!",units.Proton.Portrait)
            CutsceneIndex = 22
            
        elif CutsceneIndex == 22:
            Text3("(Proton picks up the Holy Itucher)")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 23:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 24:
            Text1("Proton: There have been many losses throughout our journey...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 25:
            Text1("Proton: It is because of these sacrifices that we are here today...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 26:
            Text1("Proton: We must not forget those who have been lost in the fight for",units.Proton.Portrait)
            line2("the Holy Itucher...")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 27:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 28:
            screensetup.BattleScreen.bgcolor("black")
            Text3("(And so the Static Army returned to the Continent of Bipole, successfully")
            line2("retrieving the Holy Itucher...)")
            CutsceneIndex = 100
            
        elif CutsceneIndex == 100:
            EndingCharacter(units.Proton,False,False,False)
        elif CutsceneIndex == 101:
            EndingCharacter(units.Quest,False,False,False)
        elif CutsceneIndex == 102:
            EndingCharacter(units.Scien,False,False,False)
        elif CutsceneIndex == 103:
            EndingCharacter(units.Romra,False,False,False)
        elif CutsceneIndex == 104:
            EndingCharacter(units.TnemecalperI,False,False,False)
        elif CutsceneIndex == 105:
            EndingCharacter(units.TnemecalperII,False,False,False)
        elif CutsceneIndex == 106:
            EndingCharacter(units.TnemecalperIII,False,False,False)
        elif CutsceneIndex == 107:
            EndingCharacter(units.TnemecalperIV,False,False,False)
        elif CutsceneIndex == 108:
            EndingCharacter(units.Lacirtcele,False,False,False)
        elif CutsceneIndex == 109:
            EndingCharacter(units.Damagein,False,False,False)
        elif CutsceneIndex == 110:
            EndingCharacter(units.Healia,False,False,False)
        elif CutsceneIndex == 111:
            EndingCharacter(units.Wob,False,False,False)
        elif CutsceneIndex == 112:
            EndingCharacter(units.Bladen,False,False,False)
        elif CutsceneIndex == 113:
            EndingCharacter(units.Wodahs,False,False,False)
        elif CutsceneIndex == 114:
            EndingCharacter(units.PlayableBladeous,False,False,False)
        elif CutsceneIndex == 115:
            EndingCharacter(units.Azure,False,False,False)
        elif CutsceneIndex == 116:
            EndingCharacter(units.Fael,False,False,False)
        elif CutsceneIndex == 117:
            EndingCharacter(units.Erif,False,False,False)
        elif CutsceneIndex == 118:
            EndingCharacter(units.Vruh,False,False,False)
        elif CutsceneIndex == 119:
            EndingCharacter(units.Recils,False,False,False)
        elif CutsceneIndex == 120:
            EndingCharacter(units.Repins,False,False,False)
        elif CutsceneIndex == 121:
            EndingCharacter(units.Relaeh,False,False,False)
        elif CutsceneIndex == 122:
            EndingCharacter(units.Eulb,False,False,False)
        elif CutsceneIndex == 123:
            EndingCharacter(units.Lias,False,False,False)
        elif CutsceneIndex == 124:
            EndingCharacter(units.Fieht,False,False,False)
        elif CutsceneIndex == 125:
            EndingCharacter(units.Rethgif,False,False,False)
        elif CutsceneIndex == 126:
            EndingCharacter(units.Eg,False,False,False)
        elif CutsceneIndex == 127:
            EndingCharacter(units.Elbon,False,False,False)
        elif CutsceneIndex == 128:
            EndingCharacter(units.B,False,False,False)
        elif CutsceneIndex == 129:
            EndingCharacter(units.Xuirventh,False,False,False)
        elif CutsceneIndex == 130:
            EndingCharacter(units.Xuirfth,False,False,False)
        elif CutsceneIndex == 131:
            EndingCharacter(units.Xuirer,False,False,False)
        elif CutsceneIndex == 132:
            EndingCharacter(units.Dliug,False,False,False)
        elif CutsceneIndex == 133:
            EndingCharacter(units.Exa,False,False,False)
        elif CutsceneIndex == 134:
            EndingCharacter(units.Yranecrem,False,False,False)
        elif CutsceneIndex == 135:
            EndingCharacter(units.Geomer,False,False,False)
        elif CutsceneIndex == 136:
            EndingCharacter(units.Box,False,False,False)
        elif CutsceneIndex == 137:
            EndingCharacter(units.NOTOS,False,False,False)
        elif CutsceneIndex == 138:
            EndingCharacter(units.YungPoggers,False,False,False)
        elif CutsceneIndex == 139:
            EndingCharacter(units.Dnefed,False,False,False)
        elif CutsceneIndex == 140:
            EndingCharacter(units.Thgif,False,False,False)
        elif CutsceneIndex == 141:
            EndingCharacter(units.Gnirif,False,False,False)
        elif CutsceneIndex == 142:
            EndingCharacter(units.Cigam,False,False,False)
        elif CutsceneIndex == 143:
            EndingCharacter(units.Omega,True,False,False)
        elif CutsceneIndex == 144:
            EndingCharacter(units.Fiyghtrr,False,False,False)
        elif CutsceneIndex == 145:
            EndingCharacter(units.Recalper,False,False,False)
        elif CutsceneIndex == 146:
            EndingCharacter(units.Tabmoc,False,False,False)
        elif CutsceneIndex == 147:
            EndingCharacter(units.Xuirurth,False,False,False)
        elif CutsceneIndex == 148:
            EndingCharacter(units.Repins2,False,False,False)
        elif CutsceneIndex == 149:
            EndingCharacter(units.Ahcem,False,False,False)
        elif CutsceneIndex == 150:
            EndingCharacter(units.Cayenne,False,False,False)
        elif CutsceneIndex == 151:
            EndingCharacter(units.XuirMan,False,False,False)
        elif CutsceneIndex == 152:
            EndingCharacter(units.Integer,False,False,False)
        elif CutsceneIndex == 153:
            Text3("                             ~~ Ending 8/10: Neutral Ending ~~")
            line2("|     You failed to meet the conditions for any other ending, congratulations.     |")
            line3("                 Enter code \"947187\" to start the game in New Game+")
    elif Chapter == "Azure Ending": #=====================AzureEnding===============================================================
        if CutsceneIndex == 0:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text3("[Proton stands before the Holy Itucher and picks it up]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            Text1("Proton: ...",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("Azure: Proton.",units.Proton.Portrait,units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text2("Azure: This is the end.",units.Proton.Portrait,units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text2("Azure: I've already let the timeline divert enough, the continuity could",units.Proton.Portrait,units.Azure.Portrait)
            line2("collapse at any moment.")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 5:
            Text1("Azure: But now that you've fufilled your role in the Neville Prophecy...",units.Proton.Portrait,units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            screensetup.BattleScreen.bgcolor("black")
            Text3("[The reality around Proton becomes a void]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text2("Azure: Goodbye.",units.Proton.Portrait,units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text3("[Proton is erased]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text1("Azure: And you, as well...",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            Text1("Azure: You want your little ending, don't you?",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            Text1("Azure: Well then...",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            Text1("Azure: [ Ending 9/10: Azure Ending ]",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text1("Azure: Happy yet? Satisfied?",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text1("Azure: ...",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 15:
            Text1("Azure: Heh, of course you aren't...",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 16:
            Text1("Azure: "+ username.UserName + ", you demented",units.Azure.Portrait)
            line2("maniac.")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 17:
            Text1("Azure: You know the Nexter's Law of Realmer Intervention?",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 18:
            Text1("Azure: Course you do, you were there at the creation.",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 19:
            Text1("Azure: You know exactly what you're doing.",units.Azure.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 20:
            Text3("(...)")
            CutsceneIndex += 1
                  
    elif Chapter == "Chapter 27f": #=====================Chapter27f===============================================================
        ChapterLevel = 999
        if CutsceneIndex == 0:
            SaveData()
            screensetup.BattleScreen.bgcolor("black")
            Text3("[Chapter 27f]")
            line2("[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            screensetup.BattleScreen.bgcolor("dark grey")
            Text1("proton reaches out to pick up the holy itucher",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 2:
            Text1("the power of the itucher draws him to do so",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 3:
            Text1("however, he is unable to do so, as the timeline has",units.Proton.Portrait)
            line2("diverted too far")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 4:
            Text1("with the lack of azure's presence, the xuir wrath is",units.Proton.Portrait)
            line2("unleashed upon the world")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 5:
            screensetup.BattleScreen.bgcolor("black")
            Text3("and with the xuir wrath unleashed and the timeline no longer stable to")
            line2("the neville prophecy, the one who consumes all is reborn")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 6:
            Text3("the manifestation of the sins of humanity")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 7:
            Text3("the inescapable shadow that exists within all")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 8:
            Text3("the manifestation of which azure was trying to prevent")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 9:
            Text3("the manifestation of the sins of humanity")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 10:
            Text3("and now...")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 11:
            Text3("proton xurr no longer exists")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 12:
            Text3("he has become the vessel for the one who consumes all")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 13:
            Text3("who now fights the xuir wrath, the very thing that was")
            line2("created to restrict the one's power")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 14:
            Text3("who do you think will prevail, " + (username.UserName).lower() + "?")
            CutsceneIndex += 1
             
        elif CutsceneIndex == 15:
            Text3("hopefully this will entertain you")
            units.Proton.Portrait = "proton_big2"
            units.Proton.Sprite = current_directory+"/Sprites/proton_small2.gif"
            units.Proton.TurtleName.shape(units.Proton.Sprite)
            units.Proton.DisplayName = "T.O.W.C.A."
            units.Proton.Bio = "Proton Xurr has been erased."
            select.InstantLevelUp(units.Proton,50)
            CutsceneIndex += 1
            UnitsToPlace = placeunits.Chapter27fEnemies
            UnitFormation = placeunits.Chapter27fPlacement
            BattleStarted = False
            battle_started = True
        elif CutsceneIndex == 16:
            Text1("THE ONE WHO CONSUMES ALL: ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓!!!!",units.Proton.Portrait)
            CutsceneIndex += 1
             
        elif CutsceneIndex == 16:
            Text1("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓",units.Proton.Portrait)
            line2("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
            line3("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
            CutsceneIndex += 1
            
            Cutscene()
        elif CutsceneIndex == 17:
            Text1("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓",units.Proton.Portrait)
            line2("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
            line3("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
            CutsceneIndex += 1
            
            Cutscene()
        elif CutsceneIndex == 18:
            Text1("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓",units.Proton.Portrait)
            line2("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
            line3("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
            CutsceneIndex += 1
            
            Cutscene()
        elif CutsceneIndex == 19:
            Text1("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓",units.Proton.Portrait)
            line2("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
            line3("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
            CutsceneIndex += 1
            
            Cutscene()
        elif CutsceneIndex == 20:
            Text1("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓",units.Proton.Portrait)
            line2("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
            line3("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
            CutsceneIndex += 1
            
            Cutscene()
        elif CutsceneIndex == 21:
            Text1("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓",units.Proton.Portrait)
            line2("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
            line3("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
            CutsceneIndex += 1
            
            Cutscene()
        elif CutsceneIndex == 22:
            for x in range(2):
                Text1("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓",units.Proton.Portrait)
                line2("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
                line3("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
                
                Text1("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓",units.Proton.Portrait)
                line2("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
                line3("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
                
                Text1("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓",units.Proton.Portrait)
                line2("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
                line3("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
                
            for x in range(3):
                Text1("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓",units.Proton.Portrait)
                line2("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
                line3("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
                
                Text1("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓",units.Proton.Portrait)
                line2("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
                line3("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
                
                Text1("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓",units.Proton.Portrait)
                line2("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
                line3("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
                
            for x in range(5):
                Text1("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓",units.Proton.Portrait)
                line2("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
                line3("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
                Text1("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓",units.Proton.Portrait)
                line2("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓")
                line3("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
                Text1("▓▓▓ ▓ ▓▓▓▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓ ▓▓ ▓▓▓",units.Proton.Portrait)
                line2("▓▓▓ ▓ ▓▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓ ▓▓▓ ▓▓▓ ▓▓")
                line3("▓ ▓▓▓ ▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓ ▓▓▓▓ ▓")
            Chapter = "Genocide Ending"
            SaveData()
            quit()
    elif Chapter == "Genocide Ending": #=====================GenocideEnding===============================================================
        if CutsceneIndex == 0:
            screensetup.BattleScreen.bgcolor("black")
            Text3("this universe has been terminated by the shadow")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 1:
            Text3("enter code \"23567984127\"")
            CutsceneIndex += 1
            
    elif Chapter == "Actual Genocide Ending": #=====================ActualGenocideEnding===============================================================
        if CutsceneIndex == 0:
            screensetup.BattleScreen.bgcolor("black")
            Text3("thank you, " + username.UserName)
            CutsceneIndex += 1
            
        elif CutsceneIndex <= 4:
            if username.UserName != username.OldUserName:
                if CutsceneIndex == 1:
                    Text3("or should I say " + username.OldUserName + "?")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 2:
                    Text3("were you lying about your name at first?")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 3:
                    Text3("or are you scared and trying to hide your name?")
                    CutsceneIndex += 1
                    
                elif CutsceneIndex == 4:
                    Text3("anyways, it doesn't really matter.")
                    CutsceneIndex += 1
                    
            else:
                CutsceneIndex = 5
                Cutscene()
        elif CutsceneIndex == 5:
            register_shape("pernicious_big")
            Text1("i am pernicious",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 6:
            Text1("i was able to manifest thanks to you",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 7:
            Text1("after the one who consumes all and the xuir wrath clashed,",pernicious)
            line2("the previous universe was destroyed")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 8:
            Text1("but you...",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 9:
            Text1("you were somehow able to transfer the shadow of the previous",pernicious)
            line2("universe to this timeline")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 10:
            Text1("and with that excess shadow...",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 11:
            Text1("the neville prophecy...",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 12:
            Text1("the one who consumes all...",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 13:
            Text1("the xuir wrath...",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 14:
            Text1("they, and the rest of this universe, were instantly destroyed",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 15:
            Text1("the only thing that remains here are you and me",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 16:
            Text1("universal destruction, is that what you seek?",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 17:
            Text1("the extent of the shadow must grow",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 18:
            Text1("so with the power of the shadow, I'll travel to more timlines",pernicious)
            line2("and destroy them like you destroyed this one")
            CutsceneIndex += 1
            
        elif CutsceneIndex == 19:
            Text1("thank you, " + username.UserName + ", for what you've done",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 20:
            Text1("i supposed you could call this the genocide ending, 10/10",pernicious)
            CutsceneIndex += 1
            
        elif CutsceneIndex == 21:
            Text3("[Nothing Remains]")
            CutsceneIndex += 1
    else:
        print("No dialogue option reached!")
        cutscene_ended = True


    # print(CutsceneIndex)
    # CanSkipCutscene = True
    # (screensetup.BattleScreen).onkey(SkipCutscene, "o")


def SaveData():
    # global Chapter
    # global SaveDataList
    # for DataListUnit in units.ListOfPlayableUnits:
    #     DataListUnit.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]
    # ConvertedUnitsAlive = []
    # ConvertedUnitsRecruited = []
    # print("UnitsAlive",units.UnitsAlive)
    # for unit in units.UnitsAlive:
    #     thingtoadd = unit.DisplayName
    #     ConvertedUnitsAlive.append(thingtoadd)
    # for unit in units.UnitsRecruited:
    #     thingtoadd = unit.DisplayName
    #     ConvertedUnitsRecruited.append(thingtoadd)
    # print("ConvertedUnitsAlive", ConvertedUnitsAlive)
    # print("ConvertedUnitsRecruited", ConvertedUnitsRecruited)
    # for unit in units.ListOfPlayableUnits:
    #     ConvertedListOfAttacks = []
    #     ConvertedListOfSupports = []
    #     for attack in unit.Attacks:
    #         thingtoadd = attack.CombatName
    #         ConvertedListOfAttacks.append(thingtoadd)
    #     for support in unit.Supports:
    #         thingtoadd = support.CombatName
    #         ConvertedListOfSupports.append(thingtoadd)
    #     unit.DataList.append(ConvertedListOfAttacks)
    #     unit.DataList.append(ConvertedListOfSupports)
    # print("SaveDataList:", SaveDataList)
    # SaveDataList = (Chapter,
    # ConvertedUnitsAlive,
    # ConvertedUnitsRecruited,
    # units.Proton.DataList,
    # units.Quest.DataList,
    # units.Scien.DataList,
    # units.Romra.DataList,
    # units.TnemecalperI.DataList,
    # units.TnemecalperII.DataList,
    # units.TnemecalperIII.DataList,
    # units.TnemecalperIV.DataList,
    # units.Lacirtcele.DataList,
    # units.Damagein.DataList,
    # units.Healia.DataList,
    # units.Wob.DataList,
    # units.Bladen.DataList,
    # units.Wodahs.DataList,
    # units.PlayableBladeous.DataList,
    # units.Azure.DataList,
    # units.Fael.DataList,
    # units.Erif.DataList,
    # units.Vruh.DataList,
    # units.Recils.DataList,
    # units.Repins.DataList,
    # units.Relaeh.DataList,
    # units.Eulb.DataList,
    # units.Lias.DataList,
    # units.Fieht.DataList,
    # units.Rethgif.DataList,
    # units.Eg.DataList,
    # units.Elbon.DataList,
    # units.B.DataList,
    # units.Xuirventh.DataList,
    # units.Xuirfth.DataList,
    # units.Xuirer.DataList,
    # units.Dliug.DataList,
    # units.Exa.DataList,
    # units.Yranecrem.DataList,
    # units.Geomer.DataList,
    # units.Box.DataList,
    # units.NOTOS.DataList,
    # units.YungPoggers.DataList,
    # units.Dnefed.DataList,
    # units.Thgif.DataList,
    # units.Gnirif.DataList,
    # units.Cigam.DataList,
    # units.Omega.DataList,
    # units.Fiyghtrr.DataList,
    # units.Recalper.DataList,
    # units.Tabmoc.DataList,
    # units.Xuirurth.DataList,
    # units.Repins2.DataList,
    # units.Ahcem.DataList,
    # units.Cayenne.DataList,
    # units.XuirMan.DataList,
    # units.Integer.DataList,
    # username.UserName,
    # difficulty.Difficulty)
    # print(SaveDataList)
    # pickle.dump(SaveDataList, open(current_directory+"\savedata.p", "wb"))
    # #LoadData()
    pass

def LoadData():
    global SaveHasBeenLoaded
    if SaveHasBeenLoaded == False:
        SaveHasBeenLoaded = True
        print("=============")
        print("=LOADED SAVE=")
        print("=============")
        global Chapter
        ConvertedUnitsAlive = []
        ConvertedUnitsRecruited = []
        DataLoaded = pickle.load(open(current_directory+"\savedata.p", "rb"))
        Chapter = DataLoaded[0]
        print("Chapter:",Chapter)
        ConvertedUnitsAlive = DataLoaded[1]
        print("ConvertedUnitsAlive:",ConvertedUnitsAlive)
        ConvertedUnitsRecruited = DataLoaded[2]
        print("ConvertedUnitsRecruited:",ConvertedUnitsRecruited)
        units.Proton.DataList = DataLoaded[3]
        units.Quest.DataList = DataLoaded[4]
        units.Scien.DataList = DataLoaded[5]
        units.Romra.DataList = DataLoaded[6]
        units.TnemecalperI.DataList = DataLoaded[7]
        units.TnemecalperII.DataList = DataLoaded[8]
        units.TnemecalperIII.DataList = DataLoaded[9]
        units.TnemecalperIV.DataList = DataLoaded[10]
        units.Lacirtcele.DataList = DataLoaded[11]
        units.Damagein.DataList = DataLoaded[12]
        units.Healia.DataList = DataLoaded[13]
        units.Wob.DataList = DataLoaded[14]
        units.Bladen.DataList = DataLoaded[15]
        units.Wodahs.DataList = DataLoaded[16]
        units.PlayableBladeous.DataList = DataLoaded[17]
        units.Azure.DataList = DataLoaded[18]
        units.Fael.DataList = DataLoaded[19]
        units.Erif.DataList = DataLoaded[20]
        units.Vruh.DataList = DataLoaded[21]
        units.Recils.DataList = DataLoaded[22]
        units.Repins.DataList = DataLoaded[23]
        units.Relaeh.DataList = DataLoaded[24]
        units.Eulb.DataList = DataLoaded[25]
        units.Lias.DataList = DataLoaded[26]
        units.Fieht.DataList = DataLoaded[27]
        units.Rethgif.DataList = DataLoaded[28]
        units.Eg.DataList = DataLoaded[29]
        units.Elbon.DataList = DataLoaded[30]
        units.B.DataList = DataLoaded[31]
        units.Xuirventh.DataList = DataLoaded[32]
        units.Xuirfth.DataList = DataLoaded[33]
        units.Xuirer.DataList = DataLoaded[34]
        units.Dliug.DataList = DataLoaded[35]
        units.Exa.DataList = DataLoaded[36]
        units.Yranecrem.DataList = DataLoaded[37]
        units.Geomer.DataList = DataLoaded[38]
        units.Box.DataList = DataLoaded[39]
        units.NOTOS.DataList = DataLoaded[40]
        units.YungPoggers.DataList = DataLoaded[41]
        units.Dnefed.DataList = DataLoaded[42]
        units.Thgif.DataList = DataLoaded[43]
        units.Gnirif.DataList = DataLoaded[44]
        units.Cigam.DataList = DataLoaded[45]
        units.Omega.DataList = DataLoaded[46]
        units.Fiyghtrr.DataList = DataLoaded[47]
        units.Recalper.DataList = DataLoaded[48]
        units.Tabmoc.DataList = DataLoaded[49]
        units.Xuirurth.DataList = DataLoaded[50]
        units.Repins2.DataList = DataLoaded[51]
        units.Ahcem.DataList = DataLoaded[52]
        units.Cayenne.DataList = DataLoaded[53]
        units.XuirMan.DataList = DataLoaded[54]
        units.Integer.DataList = DataLoaded[55]
        username.SetUserName(DataLoaded[56])
        difficulty.SetDif(DataLoaded[57])

        for unit in units.ListOfPlayableUnits:
            print("unit:",unit)
            print("unitdatalist:",unit.DataList)
            print("UnitStuff(before):",unit.MaxHP,unit.CurrentHP,unit.ATK,unit.DEF,unit.RES,unit.AGL,unit.ACR,unit.SPD,unit.EXP,unit.Level,unit.UnitClass,unit.Portrait,unit.Sprite,unit.Attacks,unit.Supports)
            unit.MaxHP = unit.DataList[0]
            unit.CurrentHP = unit.DataList[1]
            unit.ATK = unit.DataList[2]
            unit.DEF = unit.DataList[3]
            unit.RES = unit.DataList[4]
            unit.AGL = unit.DataList[5]
            unit.ACR = unit.DataList[6]
            unit.SPD = unit.DataList[7]
            unit.EXP = unit.DataList[8]
            unit.Level = unit.DataList[9]
            unit.UnitClass = unit.DataList[10]
            unit.Portrait = unit.DataList[11]
            unit.Sprite = unit.DataList[12]
            unit.Attacks = unit.DataList[13]
            unit.Supports = unit.DataList[14]
            print("UnitStuff(after):",unit.MaxHP,unit.CurrentHP,unit.ATK,unit.DEF,unit.RES,unit.AGL,unit.ACR,unit.SPD,unit.EXP,unit.Level,unit.UnitClass,unit.Portrait,unit.Sprite,unit.Attacks,unit.Supports)
        NewUnitsAlive = []
        for convertedunit in ConvertedUnitsAlive:
            for actualunit in units.ListOfPlayableUnits:
                if convertedunit == actualunit.DisplayName:
                    NewUnitsAlive.append(actualunit)
        units.UnitsAlive = NewUnitsAlive
        NewUnitsRecruited = []
        for convertedunit in ConvertedUnitsRecruited:
            for actualunit in units.ListOfPlayableUnits:
                if convertedunit == actualunit.DisplayName:
                    NewUnitsRecruited.append(actualunit)
        units.UnitsRecruited = NewUnitsRecruited
        for unit in units.ListOfPlayableUnits:
            NewListOfAttacks = []
            NewListOfSupports = []
            for move in unit.Attacks:
                for attack in moves.ListOfAttacks:
                    if move == attack.CombatName:
                        if move in NewListOfAttacks:
                            print("duplicate attack somehow detected")
                        else:
                            NewListOfAttacks.append(attack)
            for move in unit.Supports:
                for support in moves.ListOfSupports:
                    if move == support.CombatName:
                        if move in NewListOfSupports:
                            print("duplicate support somehow detected")
                        else:
                            NewListOfSupports.append(support)
            unit.TurtleName.shape(unit.Sprite)
            print("newlistofattacks",NewListOfAttacks)
            print("newlistofsupports",NewListOfSupports)
            unit.Attacks = NewListOfAttacks
            unit.Supports = NewListOfSupports
            print("listofattacks",unit.Attacks)
            print("listofsupports",unit.Supports)
        
        Cutscene()

def SkipCutscene():
    
    global Chapter
    global CutsceneIndex
    global CanSkipCutscene
    global TnenecalpersJoined
    if CanSkipCutscene == True:
        print("Skipping cutscene", Chapter, CutsceneIndex)
        if Chapter == "Prologue1": #=====================Prologue1===============================================================
            Chapter = "Prologue2"
            CutsceneIndex = 0
            Cutscene()
        elif Chapter == "Prologue2" and CutsceneIndex !=25 and CutsceneIndex !=26: #=====================Prologue2===============================================================
            screensetup.BattleScreen.bgcolor("green")
            if CutsceneIndex <= 24:
                CutsceneIndex = 24
            Cutscene()
        # elif Chapter == "Chapter 01" and CutsceneIndex != 3 and CutsceneIndex < 3: #=====================Chapter01===============================================================
        #     CutsceneIndex = 2
        #     Cutscene()
        # elif Chapter == "Chapter 01" and len(units.UnitsAlive) == 1 and CutsceneIndex > 3: #=====================Chapter01(only proton survived)===============================================================
        #     register_shape("azurehooded_big")
        #     CutsceneIndex = 10
        #     Cutscene()
        # elif Chapter == "Chapter 01" and TnemecalpersJoined == True and CutsceneIndex != 10: #=====================Chapter01(only proton sruvived)===============================================================
        #     register_shape("azurehooded_big")
        #     CutsceneIndex = 0
        #     Chapter = "Chapter 02"
        #     Cutscene()

def BattleStart():
    global UnitsToPlace
    global UnitFormation
    global BattleStarted
    if BattleStarted == False:
        BattleStarted = True
        
        
        
        placeunits.PlacePlayerUnits()
        units.EnemyUnitsAlive = UnitsToPlace
        placeunits.PlaceEnemies(UnitFormation)
        
        
        
    else:
        print("Don't hold down space, the battle already started")



def RomraRecruitYes():
    global RecruitRomra
    ()
    RecruitRomra = True
    Cutscene()
def RomraRecruitNo():
    global RecruitRomra
    ()
    RecruitRomra = False
    Cutscene()

def LacirtceleRecruitYes():
    global RecruitLacirtcele
    ()
    RecruitLacirtcele = True
    Cutscene()
def LacirtceleRecruitNo():
    global RecruitLacirtcele
    ()
    RecruitLacirtcele = False
    Cutscene()

def DamageinRecruitYes():
    global RecruitDamagein
    ()
    RecruitDamagein = True
    Cutscene()
def DamageinRecruitNo():
    global RecruitDamagein
    ()
    RecruitDamagein = False
    Cutscene()

def HealiaRecruitYes():
    global RecruitHealia
    ()
    RecruitHealia = True
    Cutscene()
def HealiaRecruitNo():
    global RecruitHealia
    ()
    RecruitHealia = False
    Cutscene()

def WobRecruitYes():
    global RecruitWob
    ()
    RecruitWob = True
    Cutscene()
def WobRecruitNo():
    global RecruitWob
    ()
    RecruitWob = False
    Cutscene()

def BladenRecruitYes():
    global RecruitBladen
    ()
    RecruitBladen = True
    Cutscene()
def BladenRecruitNo():
    global RecruitBladen
    ()
    RecruitBladen = False
    Cutscene()

def WodahsRecruitYes():
    global RecruitWodahs
    ()
    RecruitWodahs = True
    Cutscene()
def WodahsRecruitNo():
    global RecruitWodahs
    ()
    RecruitWodahs = False
    Cutscene()

def FaelRecruitYes():
    global RecruitFael
    ()
    RecruitFael = True
    Cutscene()
def ErifRecruitYes():
    global RecruitErif
    ()
    RecruitErif = True
    Cutscene()
def RecruitNeither():
    ()
    Cutscene()
def VruhRecruitYes():
    global RecruitVruh
    ()
    RecruitVruh = True
    Cutscene()

def RepinsRecruitYes():
    global RecruitRepins
    ()
    RecruitRepins = True
    Cutscene()

def RelaehRecruitYes():
    global RecruitRelaeh
    ()
    RecruitRelaeh = True
    Cutscene()

def LiasRecruitYes():
    global RecruitLias
    ()
    RecruitLias = True
    Cutscene()

def QinputYes():
    global Qinput
    ()
    Qinput = True
    Cutscene()

def WinputYes():
    global Winput
    ()
    Winput = True
    Cutscene()

def EinputYes():
    global Einput
    ()
    Einput = True
    Cutscene()

import random
import turtle
import statprint
import time
import moves
import os
current_directory = os.getcwd()

def testprint():
    print("YOU HAVE SUCCESSFULLY IMPORTED UNITS.PY")

# ================================================================================================
# ========================== Change: ACR affects hit rate now, not AGL. ==========================
# ================================================================================================

import screensetup

# COMMENTED OUT FOR CONVERSION
# screensetup.BattleScreen.tracer(0)

class Unit:
    def __init__(self,
    TurtleName="NameTurtle",
    DisplayName="Name",
    PrimaryType="Physical",
    AttackRange=[],
    MaxHP=5,
    CurrentHP=5,
    ATK=5, #Influences attack damage
    DEF=5, #Influences damage taken from physical attacks
    RES=5, #Influences damage taken from magic attacks
    AGL=5, #Influences the chance of getting hit by an attack
    ACR=5, #Influences the chance of landing an attack
    SPD=2, #The amount of "tiles" you can move
    EXP=0, #You level up every 100 EXP
    EXPReward=50, #The EXP given when defeated, enemies can also level up if they defeat your units
    Level=1,
    UnitClass="Bipolian",
    Attacks=[],
    Supports=[],
    Traits=[],
    HPGrowth=[50,1], #Chance to level up, max amount to increase
    ATKGrowth=[50,1],
    DEFGrowth=[50,1],
    RESGrowth=[50,1],
    AGLGrowth=[50,1],
    ACRGrowth=[50,1],
    Portrait="",
    Sprite="",
    LevelQuotes=[],
    Bio="",
    ClassChange=[], #[Name, Level]
    AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
    SupportUnlocks=[], 
    DataList=[],
    HasMoved=False,
    HasActioned=False,
    ConvertedAttackList=[],
    ConvertedSupportList=[],
    MoveStamp=None,
    ActStamp=None):
        self.AttackRange = AttackRange
        self.PrimaryType = PrimaryType
        self.DisplayName = DisplayName
        self.MaxHP = MaxHP
        self.CurrentHP = CurrentHP
        self.ATK = ATK
        self.DEF = DEF
        self.RES = RES
        self.AGL = AGL
        self.ACR = ACR
        self.SPD = SPD
        self.EXP = EXP
        self.EXPReward = EXPReward
        self.Level = Level
        self.UnitClass = UnitClass
        self.Attacks = Attacks
        self.Supports = Supports
        self.Traits = Traits
        self.HPGrowth = HPGrowth
        self.ATKGrowth = ATKGrowth
        self.DEFGrowth = DEFGrowth
        self.RESGrowth = RESGrowth
        self.AGLGrowth = AGLGrowth
        self.ACRGrowth = ACRGrowth
        self.Portrait = Portrait
        self.Sprite = Sprite
        self.LevelQuotes = LevelQuotes
        self.Bio = Bio
        self.ClassChange = ClassChange
        self.AttackUnlocks = AttackUnlocks
        self.SupportUnlocks = SupportUnlocks
        self.DataList = DataList
        self.HasMoved = HasMoved
        self.HasActioned = HasActioned
        self.ConvertedAttackList = ConvertedAttackList
        self.ConvertedSupportList = ConvertedSupportList
        self.MoveStamp = MoveStamp
        self.ActStamp = ActStamp


ListOfPlayableUnits: list[Unit] = [] #This is a list of every unit that is playable
UnitsAlive = [] #This is a list of every living unit you currently have unlocked
UnitsRecruited = [] #List of units you have recruited
UnitsChosen = [] #The units that you are bringing into battle
EnemyUnitsAlive = [] #This will be set at the start of each battle

#===============================================================================================================================================================================================================
#==== Playable Units ===========================================================================================================================================================================================
#===============================================================================================================================================================================================================

# (( Only for Godot bipole IV+ generation!!! skips the turtle registering thing)
def register_shape(name):
    # register_shape(name)
    pass

class FakeTurtle:
    def shape(self, name):
        pass

    def hideturtle(self):
        pass

def new_turtle():
    # return turtle.Turtle()
    return FakeTurtle()

#Proton------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/proton_small.gif")
register_shape(current_directory+"/Portraits/proton_big.gif")
register_shape(current_directory+"/Sprites/proton_small3.gif")
register_shape(current_directory+"/Portraits/proton_big3.gif")
register_shape(current_directory+"/Sprites/proton_small2.gif")
register_shape(current_directory+"/Portraits/proton_big2.gif")
Proton = Unit(TurtleName="ProtonTurtle",
DisplayName="Proton",
AttackRange = [1,2],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=10, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=6, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack
ACR=13,#Influences the chance of landing an attack
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Xuir Knight",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Xuir", "Knight"],
HPGrowth=[70,3], #Chance to level up, max amount to increase
ATKGrowth=[60,1],
DEFGrowth=[70,1],
RESGrowth=[35,1],
AGLGrowth=[40,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/proton_big.gif",
Sprite=current_directory+"/Sprites/proton_small.gif",
LevelQuotes=["Proton: This will be useful.","Proton: I'm feeling stronger.","Proton: Is this the power of the Xuir?","Proton: I feel stronger."],
Bio="Proton is from Nolavillia, though he grew up in Bipole and was raised by Scien.\nHe now serves under the Territory of Static as a high-ranking knight alongside\n Scien and the Elemental Offense Squad.",
ClassChange=[["Xuir Champion", 25]], #[Name, Level]
AttackUnlocks=[[moves.Lance,3],[moves.Javelin,5],[moves.ArmorBreak,10],[moves.MageBlade,15],[moves.Slash,20]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Proton)
Proton.TurtleName = new_turtle()
Proton.TurtleName.shape(current_directory+"/Sprites/proton_small.gif")
Proton.TurtleName.hideturtle()
DataListUnit = Proton
Proton.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Quest------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/quest_small.gif")
register_shape(current_directory+"/Portraits/quest_big.gif")
Quest = Unit(TurtleName="QuestTurtle",
DisplayName="Quest",
AttackRange=[1,2],
PrimaryType="Magic",
MaxHP=13,
CurrentHP=13,
ATK=14, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=8, #Influences damage taken from magic attacks
AGL=7, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="High Mage",
Attacks=[moves.Fireball],
Supports=[moves.Heal],
Traits=["Magic Primary","Bipolian","Mage"],
HPGrowth=[50,2], #Chance to level up, max amount to increase
ATKGrowth=[50,2],
DEFGrowth=[30,1],
RESGrowth=[40,1],
AGLGrowth=[50,1],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/quest_big.gif",
Sprite=current_directory+"/Sprites/quest_small.gif",
LevelQuotes=["Quest: I must become stronger.","Quest: Hopefully, this will help me find the Artifacts.","Quest: This is a welcome addition."],
Bio="Quest is a skilled mage who acts as the high mage of the Territory of Static.\nHis life goal is to discover the secrets of the legendary Artifacts.",
ClassChange=[["Grand Mage", 15]], #[Name, Level]
AttackUnlocks=[[moves.Aqua,3],[moves.Freeze,7],[moves.Thorn,10],[moves.DarkOrb,12],[moves.Thunder,14],[moves.MageBlade,15]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.LongHeal,5]])
ListOfPlayableUnits.append(Quest)
Quest.TurtleName = new_turtle()
Quest.TurtleName.shape(current_directory+"/Sprites/quest_small.gif")
Quest.TurtleName.hideturtle()
DataListUnit = Quest
Quest.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Scien------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/scien_small.gif")
register_shape(current_directory+"/Portraits/scien_big.gif")
Scien = Unit(TurtleName="ScienTurtle",
DisplayName="Scien",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=8, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=8, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=12,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Head Knight",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Speciean","Knight"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[30,1],
DEFGrowth=[70,1],
RESGrowth=[10,1],
AGLGrowth=[10,1],
ACRGrowth=[5,1],
Portrait=current_directory+"/Portraits/scien_big.gif",
Sprite=current_directory+"/Sprites/scien_small.gif",
LevelQuotes=["Scien: Though I grow stronger, I mustn't lose myself.","Scien: If only I had this strength back then...","Scien: I must defend Static, I cannot let it become like Nolavillia.","Scien: Even this cannot make up for my sins..."],
Bio= "Scien was once a scientist at Death Pepper's research center,\n where he was forced to conduct inhumane experiments to develop the Xuirs.\nAfter escaping to Bipole with Proton, he decided to serve as a knight\nin order to protect the peace and try to make up for his past.",
ClassChange=[["Legendary Knight", 10]], #[Name, Level]
AttackUnlocks=[[moves.HerosStrike,7],[moves.Bow,10],[moves.ShieldShatter,20],[moves.SnipeIII,30]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.Mend,10],[moves.Save,13],[moves.Fortify,15],[moves.MedKit,17]])
ListOfPlayableUnits.append(Scien)
Scien.TurtleName = new_turtle()
Scien.TurtleName.shape(current_directory+"/Sprites/scien_small.gif")
Scien.TurtleName.hideturtle()
DataListUnit = Scien
Scien.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Romra------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/romra_small.gif")
register_shape(current_directory+"/Portraits/romra_big.gif")
Romra = Unit(TurtleName="RomraTurtle",
DisplayName="Romra",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=5, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=1, #Influences damage taken from magic attacks
AGL=3, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=13,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Armor Knight",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Bipolian","Knight","Armored"],
HPGrowth=[80,4], #Chance to level up, max amount to increase
ATKGrowth=[80,3],
DEFGrowth=[80,2],
RESGrowth=[5,1],
AGLGrowth=[10,1],
ACRGrowth=[50,2],
Portrait=current_directory+"/Portraits/romra_big.gif",
Sprite=current_directory+"/Sprites/romra_small.gif",
LevelQuotes=["Romra: I need to keep getting stronger!","Romra: With this power, I can probably join the Elemental Offense Squad.","Romra: The best offense is a great defense, I think."],
Bio= "Romra was recently promoted to a knight, and his\n dream is to eventually become a member of the \n Static Elemental Offense Squad. He trains\n everyday to achieve his dream but isn't strong\n enough to join yet.",
ClassChange=[["Bow Knight", 10]], #[Name, Level]
AttackUnlocks=[[moves.Bow,10],[moves.HeavyBow,10],[moves.LongBow,13],[moves.HerosStrike,15],[moves.Snipe,20],[moves.SnipeII,25]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Romra)
Romra.TurtleName = new_turtle()
Romra.TurtleName.shape(current_directory+"/Sprites/romra_small.gif")
Romra.TurtleName.hideturtle()
DataListUnit = Romra
Romra.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#TnemecalperI------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/tnemecalperi_small.gif")
register_shape(current_directory+"/Portraits/tnemecalperi_big.gif")
TnemecalperI = Unit(TurtleName="TnemecalperITurtle",
DisplayName="Tnemecalper I",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=18,
CurrentHP=18,
ATK=12, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Blade Master",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Shadow Summon","Fighter","Shadow"],
HPGrowth=[80,1], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[50,1],
RESGrowth=[15,1],
AGLGrowth=[70,1],
ACRGrowth=[75,2],
Portrait=current_directory+"/Portraits/tnemecalperi_big.gif",
Sprite=current_directory+"/Sprites/tnemecalperi_small.gif",
LevelQuotes=["Tnemecalper I: INITIATING LEVEL UP","Tnemecalper I: LEVEL HAS BEEN GAINED"],
Bio="Tnemecalper I is the first of the four Tnemecalpers.\nThey are of unknown origin but have been summoned to assist you.",
ClassChange=[["Blade Master", 10]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(TnemecalperI)
TnemecalperI.TurtleName = new_turtle()
TnemecalperI.TurtleName.shape(current_directory+"/Sprites/tnemecalperi_small.gif")
TnemecalperI.TurtleName.hideturtle()
DataListUnit = TnemecalperI
TnemecalperI.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Tnemecalper II------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/tnemecalperii_small.gif")
register_shape(current_directory+"/Portraits/tnemecalperii_big.gif")
TnemecalperII = Unit(TurtleName="TnemecalperIITurtle",
DisplayName="Tnemecalper II",
AttackRange=[1,2],
PrimaryType="Magic",
MaxHP=14,
CurrentHP=14,
ATK=10, #Influences attack damage
DEF=2, #Influences damage taken from physical attacks
RES=9, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=13,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Attack Mage",
Attacks=[moves.DarkOrb],
Supports=[],
Traits=["Magic Primary","Shadow Summon","Mage","Shadow"],
HPGrowth=[50,1], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[30,1],
RESGrowth=[90,1],
AGLGrowth=[40,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/tnemecalperii_big.gif",
Sprite=current_directory+"/Sprites/tnemecalperii_small.gif",
LevelQuotes=["Tnemecalper II: This is a Level Quote","Tnemecalper I: This is a Level Up"],
Bio="Tnemecalper II is the second of the four Tnemecalpers.\nThey are of unknown origin but have been summoned to assist you.",
ClassChange=[["Dual Mage", 10]], #[Name, Level]
AttackUnlocks=[[moves.Slice,15]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.Heal,10],[moves.LongHeal,13]])
ListOfPlayableUnits.append(TnemecalperII)
TnemecalperII.TurtleName = new_turtle()
TnemecalperII.TurtleName.shape(current_directory+"/Sprites/tnemecalperii_small.gif")
TnemecalperII.TurtleName.hideturtle()
DataListUnit = TnemecalperII
TnemecalperII.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#TnemecalperIII------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/tnemecalperiii_small.gif")
register_shape(current_directory+"/Portraits/tnemecalperiii_big.gif")
TnemecalperIII = Unit(TurtleName="TnemecalperIIITurtle",
DisplayName="Tnemecalper III",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=17,
CurrentHP=17,
ATK=8, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=9, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Scientist",
Attacks=[moves.Scalpel],
Supports=[moves.Heal],
Traits=["Physical Primary","Shadow Summon","Scientist","Shadow"],
HPGrowth=[40,2], #Chance to level up, max amount to increase
ATKGrowth=[50,1],
DEFGrowth=[15,1],
RESGrowth=[65,2],
AGLGrowth=[40,1],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/tnemecalperiii_big.gif",
Sprite=current_directory+"/Sprites/tnemecalperiii_small.gif",
LevelQuotes=["Tnemecalper III: Level has been detected","Tnemecalper III: Power has been detected"],
Bio="Tnemecalper III is the third of the four Tnemecalpers.\nThey are of unknown origin but have been summoned to assist you.",
ClassChange=[["Promoted Scientist", 10]], #[Name, Level]
AttackUnlocks=[[moves.Infection,8]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.LongHeal,5],[moves.FarHeal,10]])
ListOfPlayableUnits.append(TnemecalperIII)
TnemecalperIII.TurtleName = new_turtle()
TnemecalperIII.TurtleName.shape(current_directory+"/Sprites/tnemecalperiii_small.gif")
TnemecalperIII.TurtleName.hideturtle()
DataListUnit = TnemecalperIII
TnemecalperIII.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#TnemecalperIV------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/tnemecalperiv_small.gif")
register_shape(current_directory+"/Portraits/tnemecalperiv_big.gif")
TnemecalperIV = Unit(TurtleName="TnemecalperIVTurtle",
DisplayName="Tnemecalper IV",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=7, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=1, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=12,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Archer",
Attacks=[moves.Bow],
Supports=[],
Traits=["Physical Primary","Shadow Summon","Archer","Shadow"],
HPGrowth=[50,1], #Chance to level up, max amount to increase
ATKGrowth=[90,1],
DEFGrowth=[50,1],
RESGrowth=[5,1],
AGLGrowth=[50,1],
ACRGrowth=[80,2],
Portrait=current_directory+"/Portraits/tnemecalperiv_big.gif",
Sprite=current_directory+"/Sprites/tnemecalperiv_small.gif",
LevelQuotes=["Tnemecalper IV: DIRECT HIT","Tnemecalper IV: 360°[N/A]SCOPE"],
Bio="Tnemecalper IV is the fourth of the four Tnemecalpers.\nThey are of unknown origin but have been summoned to assist you.",
ClassChange=[["Sniper", 10]], #[Name, Level]
AttackUnlocks=[[moves.Dagger,5],[moves.LongBow,8],[moves.DistanceShot,10]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(TnemecalperIV)
TnemecalperIV.TurtleName = new_turtle()
TnemecalperIV.TurtleName.shape(current_directory+"/Sprites/tnemecalperiv_small.gif")
TnemecalperIV.TurtleName.hideturtle()
DataListUnit = TnemecalperIV
TnemecalperIV.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Lacirtcele------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/lacirtcele_small.gif")
register_shape(current_directory+"/Portraits/lacirtcele_big.gif")
Lacirtcele = Unit(TurtleName="LacirtceleTurtle",
DisplayName="Lacirtcele",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=13,
CurrentHP=13,
ATK=15, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=9, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Attack Mage",
Attacks=[moves.Thunder],
Supports=[],
Traits=["Magic Primary","Bipolian","Mage","E.O.S.","Electric"],
HPGrowth=[65,2], #Chance to level up, max amount to increase
ATKGrowth=[50,2],
DEFGrowth=[40,1],
RESGrowth=[40,2],
AGLGrowth=[15,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/lacirtcele_big.gif",
Sprite=current_directory+"/Sprites/lacirtcele_small.gif",
LevelQuotes=["Lacirtcele: Like... poggers, bruh.","Lacirtcele: gaming.","Lacirtcele: Yo....."],
Bio="Lacirtcele is a member of the Elemental Offense\nSquad. He doesn't care for much and is extremely lazy. Though\n he joined the EOS only for the fame, he can fight suprisingly well.",
ClassChange=[["Elemental Warrior", 15]], #[Name, Level]
AttackUnlocks=[[moves.ThunderBlast,10],[moves.Slice,15],[moves.SparkBlade,15]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Lacirtcele)
Lacirtcele.TurtleName = new_turtle()
Lacirtcele.TurtleName.shape(Lacirtcele.Sprite)
Lacirtcele.TurtleName.hideturtle()
DataListUnit = Lacirtcele
Lacirtcele.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Damagein------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/damagein_small.gif")
register_shape(current_directory+"/Portraits/damagein_big.gif")
Damagein = Unit(TurtleName="DamageinTurtle",
DisplayName="Damagein",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=13,
CurrentHP=13,
ATK=18, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=12,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=6,
UnitClass="Sword Fighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Bipolian","Fighter","Fire"],
HPGrowth=[50,2], #Chance to level up, max amount to increase
ATKGrowth=[100,2],
DEFGrowth=[50,1],
RESGrowth=[70,1],
AGLGrowth=[75,2],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/damagein_big.gif",
Sprite=current_directory+"/Sprites/damagein_small.gif",
LevelQuotes=["Damagein: Now that's a high amount of damage!","Damagein: Man, I love dealing damage.","Damagein: This makes me want to deal some damage."],
Bio="Damagein lives for damage. Obsessed with damage, he devotes\n his life dealing higher amounts of damage and\ncalling other people \"casuals\".",
ClassChange=[["Elemental Fighter", 15]], #[Name, Level]
AttackUnlocks=[[moves.Fireball,15]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Damagein)
Damagein.TurtleName = new_turtle()
Damagein.TurtleName.shape(Damagein.Sprite)
Damagein.TurtleName.hideturtle()
DataListUnit = Damagein
Damagein.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Healia------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/healia_small.gif")
register_shape(current_directory+"/Portraits/healia_big.gif")
Healia = Unit(TurtleName="HealiaTurtle",
DisplayName="Healia",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=25,
CurrentHP=25,
ATK=9, #Influences attack damage
DEF=11, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=6,
UnitClass="Heal Mage",
Attacks=[],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Magic Primary","Bipolian","Mage","Bio"],
HPGrowth=[80,2], #Chance to level up, max amount to increase
ATKGrowth=[90,2],
DEFGrowth=[60,1],
RESGrowth=[80,1],
AGLGrowth=[30,1],
ACRGrowth=[100,1],
Portrait=current_directory+"/Portraits/healia_big.gif",
Sprite=current_directory+"/Sprites/healia_small.gif",
LevelQuotes=["Healia: This should be good.","Healia: This will help me heal.","Healia: This should aid me."],
Bio="Healia is a mage from Sine. She\njoined Proton's army after her town\nwas saved by them.",
ClassChange=[["Dual Mage", 20]], #[Name, Level]
AttackUnlocks=[[moves.Thorn,20],[moves.VineWrath,25]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.FarHeal,15]])
ListOfPlayableUnits.append(Healia)
Healia.TurtleName = new_turtle()
Healia.TurtleName.shape(Healia.Sprite)
Healia.TurtleName.hideturtle()
DataListUnit = Healia
Healia.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Wob------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/wob_small.gif")
register_shape(current_directory+"/Portraits/wob_big.gif")
Wob = Unit(TurtleName="WobTurtle",
DisplayName="Wob",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=18,
CurrentHP=18,
ATK=19, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=6, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=6,
UnitClass="Archer",
Attacks=[moves.BowPlus],
Supports=[],
Traits=["Physical Primary","Bipolian","Archer","Fire"],
HPGrowth=[100,2], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[70,2],
RESGrowth=[60,2],
AGLGrowth=[40,1],
ACRGrowth=[90,3],
Portrait=current_directory+"/Portraits/wob_big.gif",
Sprite=current_directory+"/Sprites/wob_small.gif",
LevelQuotes=["Wob: Hey, I did something.","Wob: Am I winning?","Wob: I hope I get stronger."],
Bio="Wob is planning on joining the Static Army\nnext year, but decided to help you out since\n he's bored waiting for it.",
ClassChange=[["Elemental Archer", 13],["Elemental Sniper",20],["Ultimate Sniper",50]], #[Name, Level]
AttackUnlocks=[[moves.DistanceShot,8],[moves.Fireball,13],[moves.Snipe,20],[moves.SnipeII,28],[moves.SnipeIII,39],[moves.SnipeIV,50]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,16]])
ListOfPlayableUnits.append(Wob)
Wob.TurtleName = new_turtle()
Wob.TurtleName.shape(current_directory+"/Sprites/wob_small.gif")
Wob.TurtleName.hideturtle()
DataListUnit = Wob
Wob.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Bladen------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/bladen_small.gif")
register_shape(current_directory+"/Portraits/bladen_big.gif")
Bladen = Unit(TurtleName="BladenTurtle",
DisplayName="Bladen",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=12, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=12, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Rogue",
Attacks=[moves.Dagger],
Supports=[moves.MedKit],
Traits=["Physical Primary","Altarian","Fighter"],
HPGrowth=[100,1], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[40,1],
RESGrowth=[75,1],
AGLGrowth=[40,1],
ACRGrowth=[65,1],
Portrait=current_directory+"/Portraits/bladen_big.gif",
Sprite=current_directory+"/Sprites/bladen_small.gif",
LevelQuotes=["Bladen: This should help me.","Bladen: This will be useful.","Bladen: This should help out."],
Bio="Bladen is a mercenary hired by Proton\nto lead his army to the Nation of\nAltar.",
ClassChange=[["Assassin", 20]], #[Name, Level]
AttackUnlocks=[[moves.Cut,10],[moves.Finisher,13],[moves.ArmorBreak,15],[moves.DeathStrike,20]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Bladen)
Bladen.TurtleName = new_turtle()
Bladen.TurtleName.shape(Bladen.Sprite)
Bladen.TurtleName.hideturtle()
DataListUnit = Bladen
Bladen.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Wodahs------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/wodahs_small.gif")
register_shape(current_directory+"/Portraits/wodahs_big.gif")
Wodahs = Unit(TurtleName="WodahsTurtle",
DisplayName="Wodahs",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=19, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=7, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=12,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=10,
UnitClass="Elemental Fighter",
Attacks=[moves.Punch,moves.ShadowPunch],
Supports=[],
Traits=["Physical Primary","Bipolian","Fighter","E.O.S.","Shadow"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[50,1],
DEFGrowth=[60,1],
RESGrowth=[60,1],
AGLGrowth=[20,1],
ACRGrowth=[50,1],
Portrait=current_directory+"/Portraits/wodahs_big.gif",
Sprite=current_directory+"/Sprites/wodahs_small.gif",
LevelQuotes=["Wodahs: This will be useful.","Wodahs: This is nice.","Wodahs: This should help me out."],
Bio="Wodahs is a member of the Elemental\nOffense Sqaud. Though he usually does\nsolo missions, he's decided to help\nProton in his mission to retrieve the Holy Itucher.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[[moves.ShadowBurst,15],[moves.DarkOrb,20]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Wodahs)
Wodahs.TurtleName = new_turtle()
Wodahs.TurtleName.shape(Wodahs.Sprite)
Wodahs.TurtleName.hideturtle()
DataListUnit = Wodahs
Wodahs.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Bladeous------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/playablebladeous_small.gif")
register_shape(current_directory+"/Portraits/playablebladeous_big.gif")
PlayableBladeous = Unit(TurtleName="PlayableBladeousTurtle",
DisplayName="Bladeous",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=30, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=14, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="Elemental Warrior",
Attacks=[moves.ShadowBlade,moves.DarkOrb],
Supports=[],
Traits=["Physical Primary","Altarian","Fighter","Shadow"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[60,1],
DEFGrowth=[30,1],
RESGrowth=[70,1],
AGLGrowth=[30,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/playablebladeous_big.gif",
Sprite=current_directory+"/Sprites/playablebladeous_small.gif",
LevelQuotes=["Bladeous: This will help us stop Wallimos.","Bladeous: We need to keep going."],
Bio="Bladen's cousin, Bladeous worked as\nthe head of defense at the Temple\nof Altar. He was recently posessed by\nthe Holy Itucher.",
ClassChange=[["Elemental Champion", 25]], #[Name, Level]
AttackUnlocks=[[moves.Slash,23],[moves.ShadowBurst,27],[moves.ShadowStorm,35]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,25]])
ListOfPlayableUnits.append(PlayableBladeous)
PlayableBladeous.TurtleName = new_turtle()
PlayableBladeous.TurtleName.shape(PlayableBladeous.Sprite)
PlayableBladeous.TurtleName.hideturtle()
DataListUnit = PlayableBladeous
PlayableBladeous.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Azure------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/azure_small.gif")
register_shape(current_directory+"/Portraits/azure_big.gif")
Azure = Unit(TurtleName="AzureTurtle",
DisplayName="Azure",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=30, #Influences attack damage
DEF=45, #Influences damage taken from physical attacks
RES=45, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=999,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="The Link",
Attacks=[moves.Slice,moves.ThunderBlast,moves.ShadowBlade],
Supports=[moves.Heal,moves.LongHeal,moves.FarHeal,moves.MedKit],
Traits=["Physical Primary","God Entity"],
HPGrowth=[100,1], #Chance to level up, max amount to increase
ATKGrowth=[100,1],
DEFGrowth=[100,1],
RESGrowth=[100,1], 
AGLGrowth=[50,1],
ACRGrowth=[0,0],
Portrait=current_directory+"/Portraits/azure_big.gif",
Sprite=current_directory+"/Sprites/azure_small.gif",
LevelQuotes=["Azure: ..."],
Bio="The Link of this Realm, he will\nexecute Proton after he follows the Neville Prophecy.",
ClassChange=[["The Link", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Azure)
Azure.TurtleName = new_turtle()
Azure.TurtleName.shape(Azure.Sprite)
Azure.TurtleName.hideturtle()
DataListUnit = Azure
Azure.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Fael------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/fael_small.gif")
register_shape(current_directory+"/Portraits/fael_big.gif")
Fael = Unit(TurtleName="FaelTurtle",
DisplayName="Fael",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=23,
CurrentHP=23,
ATK=18, #Influences attack damage
DEF=9, #Influences damage taken from physical attacks
RES=9, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Archer",
Attacks=[moves.VineBow],
Supports=[],
Traits=["Physical Primary","Bipolian","Archer","E.O.S.","Bio"],
HPGrowth=[80,1], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[60,1],
RESGrowth=[60,1],
AGLGrowth=[70,1],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/fael_big.gif",
Sprite=current_directory+"/Sprites/fael_small.gif",
LevelQuotes=["Fael: I did it.","Fael: This is helpful.","Fael: Just as planned."],
Bio="Fael is a memeber of the Elemental Offense Squad. He\nwas sent by the king to help you on your journey to\nthe Nolavillian continent.",
ClassChange=[["Elemental Sniper", 30]], #[Name, Level]
AttackUnlocks=[[moves.LongBow,17],[moves.DistanceShot,23],[moves.Snipe,30]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,20],[moves.Heal,25]])
ListOfPlayableUnits.append(Fael)
Fael.TurtleName = new_turtle()
Fael.TurtleName.shape(Fael.Sprite)
Fael.TurtleName.hideturtle()
DataListUnit = Fael
Fael.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Erif------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/erif_small.gif")
register_shape(current_directory+"/Portraits/erif_big.gif")
Erif = Unit(TurtleName="ErifTurtle",
DisplayName="Erif",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=25, #Influences attack damage
DEF=16, #Influences damage taken from physical attacks
RES=12, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Elemental Fighter",
Attacks=[moves.FlameBlade],
Supports=[],
Traits=["Physical Primary","Bipolian","Fighter","E.O.S.","Fire"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[50,1],
RESGrowth=[50,1],
AGLGrowth=[40,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/erif_big.gif",
Sprite=current_directory+"/Sprites/erif_small.gif",
LevelQuotes=["Erif: This will help.","Erif: Good.","Erif: I need to get stronger."],
Bio="Erif is a memeber of the Elemental Offense Squad. She\nwas sent by the king to help you on your journey to\nthe Nolavillian continent.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[[moves.Slash,17],[moves.Fireball,25],[moves.FireBlast,35]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,20]])
ListOfPlayableUnits.append(Erif)
Erif.TurtleName = new_turtle()
Erif.TurtleName.shape(Erif.Sprite)
Erif.TurtleName.hideturtle()
DataListUnit = Erif
Erif.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Vruh------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/vruh_small.gif")
register_shape(current_directory+"/Portraits/vruh_big.gif")
Vruh = Unit(TurtleName="VruhTurtle",
DisplayName="Vruh",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=15, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=11,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Fighter",
Attacks=[moves.Punch],
Supports=[],
Traits=["Physical Primary","Bipolian","Fighter"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[50,1],
DEFGrowth=[50,1],
RESGrowth=[20,1],
AGLGrowth=[40,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/vruh_big.gif",
Sprite=current_directory+"/Sprites/vruh_small.gif",
LevelQuotes=["Vruh: Vruh moment.","Vruh: Bruh moment.","Vruh: Do you ever think about late-stage capitalism?"],
Bio="bruh.",
ClassChange=[["why are you using vruh", 20]], #[Name, Level]
AttackUnlocks=[[moves.ShieldShatter,20]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,17]])
ListOfPlayableUnits.append(Vruh)
Vruh.TurtleName = new_turtle()
Vruh.TurtleName.shape(Vruh.Sprite)
Vruh.TurtleName.hideturtle()
DataListUnit = Vruh
Vruh.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Recils------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/recils_small.gif")
register_shape(current_directory+"/Portraits/recils_big.gif")
Recils = Unit(TurtleName="RecilsTurtle",
DisplayName="Recils",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=42,
CurrentHP=42,
ATK=28, #Influences attack damage
DEF=14, #Influences damage taken from physical attacks
RES=14, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=18,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Fighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Bipolian","Fighter"],
HPGrowth=[90,1], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[40,1],
RESGrowth=[40,1],
AGLGrowth=[60,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/recils_big.gif",
Sprite=current_directory+"/Sprites/recils_small.gif",
LevelQuotes=["Recils: Good.","Recils: This should help out.","Recils: This should help."],
Bio="Recils is a wandering swordsman who has decided\nto help Proton in taking back the Holy Itucher.",
ClassChange=[["Blade Master", 25]], #[Name, Level]
AttackUnlocks=[[moves.Slash,20],[moves.DeathStrike,22],[moves.ArmorBreak,25]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,17]])
ListOfPlayableUnits.append(Recils)
Recils.TurtleName = new_turtle()
Recils.TurtleName.shape(Recils.Sprite)
Recils.TurtleName.hideturtle()
DataListUnit = Recils
Recils.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]


#Repins------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/repins_small.gif")
register_shape(current_directory+"/Portraits/repins_big.gif")
Repins = Unit(TurtleName="RepinsTurtle",
DisplayName="Repins",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=35, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=12, #Influences damage taken from magic attacks
AGL=1, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=30,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="Archer",
Attacks=[moves.Crossbow,moves.DistanceShot],
Supports=[moves.MedKit],
Traits=["Physical Primary","Bipolian","Archer","Fire"],
HPGrowth=[90,1], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[70,1],
RESGrowth=[70,1],
AGLGrowth=[5,1],
ACRGrowth=[80,1],
Portrait=current_directory+"/Portraits/repins_big.gif",
Sprite=current_directory+"/Sprites/repins_small.gif",
LevelQuotes=["Repins: This will help me find the Itucher.","Repins: This is for the future...","Repins: I need to become stronger."],
Bio="Repins is a friend of Wodahs and has\njoined up with Proton to find the Holy Itucher.",
ClassChange=[["Elemental Sniper", 35],["Elite Sniper", 65]], #[Name, Level]
AttackUnlocks=[[moves.Snipe,25],[moves.Fireball,35],[moves.SnipeII,45],[moves.SnipeIII,55],[moves.SnipeIV,65]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Repins)
Repins.TurtleName = new_turtle()
Repins.TurtleName.shape(Repins.Sprite)
Repins.TurtleName.hideturtle()
DataListUnit = Repins
Repins.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Relaeh------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/relaeh_small.gif")
register_shape(current_directory+"/Portraits/relaeh_big.gif")
Relaeh = Unit(TurtleName="RelaehTurtle",
DisplayName="Relaeh",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=52,
CurrentHP=52,
ATK=18, #Influences attack damage
DEF=17, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=23,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="Heal Mage",
Attacks=[],
Supports=[moves.Heal,moves.LongHeal,moves.FarHeal],
Traits=["Magic Primary","Altarian","Mage","Bio"],
HPGrowth=[100,1], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[70,1],
RESGrowth=[70,1],
AGLGrowth=[15,1],
ACRGrowth=[100,1],
Portrait=current_directory+"/Portraits/relaeh_big.gif",
Sprite=current_directory+"/Sprites/relaeh_small.gif",
LevelQuotes=["Relaeh: This should help me.","Relaeh: This is useful.","Relaeh: This should help out."],
Bio="Relaeh is a mage from Altar who fled after Bladeous\nbecame possessed by the Itucher. Stuck at the\nBipole Sea, he joined forces with Proton to retrieve the Itucher\nfrom Nolavillia.",
ClassChange=[["Dual Mage", 23]], #[Name, Level]
AttackUnlocks=[[moves.Freeze,23],[moves.Congeal,30]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,25]])
ListOfPlayableUnits.append(Relaeh)
Relaeh.TurtleName = new_turtle()
Relaeh.TurtleName.shape(Relaeh.Sprite)
Relaeh.TurtleName.hideturtle()
DataListUnit = Relaeh
Relaeh.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Eulb------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/eulb_small.gif")
register_shape(current_directory+"/Portraits/eulb_big.gif")
Eulb = Unit(TurtleName="EulbTurtle",
DisplayName="Eulb",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=17, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=27, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=22,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=21,
UnitClass="Dual Mage",
Attacks=[moves.Aqua],
Supports=[moves.Heal],
Traits=["Magic Primary","Altarian","Mage","Water"],
HPGrowth=[100,1], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[40,1],
RESGrowth=[50,1],
AGLGrowth=[60,1],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/eulb_big.gif",
Sprite=current_directory+"/Sprites/eulb_small.gif",
LevelQuotes=["Eulb: This should help me out.","Eulb: This should be useful.","Eulb: I feel stronger."],
Bio="Eulb escaped from Altar and ended up near\nNolavillia due to a storm. He offers\nto help Proton on his journey to reclaim\nthe Holy Itucher.",
ClassChange=[["Greater Mage", 30]], #[Name, Level]
AttackUnlocks=[[moves.MageBlade,30],[moves.Cut,30],[moves.Hydro,35],[moves.Hydra,40]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.LongHeal,25],[moves.FarHeal,27]])
ListOfPlayableUnits.append(Eulb)
Eulb.TurtleName = new_turtle()
Eulb.TurtleName.shape(Eulb.Sprite)
Eulb.TurtleName.hideturtle()
DataListUnit = Eulb
Eulb.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Lias------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/lias_small.gif")
register_shape(current_directory+"/Portraits/lias_big.gif")
Lias = Unit(TurtleName="LiasTurtle",
DisplayName="Lias",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=12, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="Fighter",
Attacks=[moves.Slice],
Supports=[moves.MedKit],
Traits=["Physical Primary","Bipolian","Fighter","Water", "Viral Resistance"],
HPGrowth=[100,3], #Chance to level up, max amount to increase
ATKGrowth=[100,2],
DEFGrowth=[80,1],
RESGrowth=[70,1],
AGLGrowth=[50,1],
ACRGrowth=[100,3],
Portrait=current_directory+"/Portraits/lias_big.gif",
Sprite=current_directory+"/Sprites/lias_small.gif",
LevelQuotes=["Lias: Nice.","Lias: Good.","Lias: This could be helpful."],
Bio="Lias is a random sailor in the Bipole Sea who\ndecided to team up with Proton's army.",
ClassChange=[["Elemental Warrior", 30]], #[Name, Level]
AttackUnlocks=[[moves.Slash,25],[moves.Aqua,30],[moves.DeathStrike,30]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.Heal,27]])
ListOfPlayableUnits.append(Lias)
Lias.TurtleName = new_turtle()
Lias.TurtleName.shape(Lias.Sprite)
Lias.TurtleName.hideturtle()
DataListUnit = Lias
Lias.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Fieht------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/fieht_small.gif")
register_shape(current_directory+"/Portraits/fieht_big.gif")
Fieht = Unit(TurtleName="FiehtTurtle",
DisplayName="Fieht",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20, #Influences attack damage
DEF=17, #Influences damage taken from physical attacks
RES=17, #Influences damage taken from magic attacks
AGL=19, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=60,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=26,
UnitClass="Rogue",
Attacks=[moves.Dagger],
Supports=[moves.MedKit],
Traits=["Physical Primary","Bipolian","Fighter"],
HPGrowth=[50,1], #Chance to level up, max amount to increase
ATKGrowth=[100,1],
DEFGrowth=[40,1],
RESGrowth=[30,1],
AGLGrowth=[80,1],
ACRGrowth=[90,1],
Portrait=current_directory+"/Portraits/fieht_big.gif",
Sprite=current_directory+"/Sprites/fieht_small.gif",
LevelQuotes=["Fieht: Nice.","Fieht: This should help me out.","Fieht: This should help my stealth."],
Bio="Fieht is a theif who was looting\nKaptain K'Neville's ship. After hearing\nabout Proton's quest, she decides to help you\nfind the Itucher in return for a payment.",
ClassChange=[["Assassin", 30]], #[Name, Level]
AttackUnlocks=[[moves.Cut,22],[moves.Slice,25],[moves.Slash,27],[moves.DeathStrike,30],[moves.ArmorBreak,30]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Fieht)
Fieht.TurtleName = new_turtle()
Fieht.TurtleName.shape(Fieht.Sprite)
Fieht.TurtleName.hideturtle()
DataListUnit = Fieht
Fieht.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Rethgif------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/rethgif_small.gif")
register_shape(current_directory+"/Portraits/rethgif_big.gif")
Rethgif = Unit(TurtleName="RethgifTurtle",
DisplayName="Rethgif",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=28,
CurrentHP=28,
ATK=15, #Influences attack damage
DEF=27, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=27,
UnitClass="Warrior",
Attacks=[moves.Cut,moves.Slice,moves.Slash],
Supports=[],
Traits=["Physical Primary","Nolavillian","Fighter","Ice"],
HPGrowth=[60,2], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[80,1],
RESGrowth=[20,1],
AGLGrowth=[70,1],
ACRGrowth=[100,2],
Portrait=current_directory+"/Portraits/rethgif_big.gif",
Sprite=current_directory+"/Sprites/rethgif_small.gif",
LevelQuotes=["Rethgif: Perfect.","Rethgif: This shall be amazing.","Rethgif: The battle must continue."],
Bio="Rethgif is an Nolavillian warrior who travels\nthe lands in search of battle.\nHis motive? To cure his boredom.",
ClassChange=[["Elemental Warrior", 45]], #[Name, Level]
AttackUnlocks=[[moves.DeathStrike,30],[moves.ArmorBreak,35],[moves.Freeze,40]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,35]])
ListOfPlayableUnits.append(Rethgif)
Rethgif.TurtleName = new_turtle()
Rethgif.TurtleName.shape(Rethgif.Sprite)
Rethgif.TurtleName.hideturtle()
DataListUnit = Rethgif
Rethgif.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Eg------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/eg_small.gif")
register_shape(current_directory+"/Portraits/eg_big.gif")
Eg = Unit(TurtleName="EgTurtle",
DisplayName="Eg",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=15, #Influences attack damage
DEF=0, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=27,
UnitClass="Warrior",
Attacks=[moves.Cut,moves.Slice],
Supports=[moves.MedKit],
Traits=["Physical Primary","Nolavillian","Fighter","Electric"],
HPGrowth=[0,1], #Chance to level up, max amount to increase
ATKGrowth=[60,1],
DEFGrowth=[100,1],
RESGrowth=[50,1],
AGLGrowth=[5,1],
ACRGrowth=[100,2],
Portrait=current_directory+"/Portraits/eg_big.gif",
Sprite=current_directory+"/Sprites/eg_small.gif",
LevelQuotes=["Eg: Satisfactory.","Eg: Advantageous.","Eg: Prosperous."],
Bio="Eg is Rethgif's brother and accompanies him on\nhis travels. While he might look unreliable\none should never underestimate Eg; he is\na man of few words but a great holder of wisdom.",
ClassChange=[["Destroyer", 45]], #[Name, Level]
AttackUnlocks=[[moves.DeathStrike,30],[moves.Slash,32],[moves.ArmorBreak,35],[moves.Thunder,40],[moves.ThunderBlast,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Eg)
Eg.TurtleName = new_turtle()
Eg.TurtleName.shape(Eg.Sprite)
Eg.TurtleName.hideturtle()
DataListUnit = Eg
Eg.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Elbon------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/elbon_small.gif")
register_shape(current_directory+"/Portraits/elbon_big.gif")
Elbon = Unit(TurtleName="ElbonTurtle",
DisplayName="Elbon",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=15, #Influences attack damage
DEF=18, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=23,
UnitClass="Noble",
Attacks=[moves.Dagger,moves.Aqua],
Supports=[],
Traits=["Physical Primary","Shadeian","Water"],
HPGrowth=[50,1], #Chance to level up, max amount to increase
ATKGrowth=[70,2],
DEFGrowth=[60,1],
RESGrowth=[60,1],
AGLGrowth=[50,1],
ACRGrowth=[65,1],
Portrait=current_directory+"/Portraits/elbon_big.gif",
Sprite=current_directory+"/Sprites/elbon_small.gif",
LevelQuotes=["Elbon: You are no match for my greatness.","Elbon: I am undefeatable.","Elbon: You never stood a chance, plebian."],
Bio="Elbon is a noble from the Nation\nof Shade who followed Healia to Nolavillia.",
ClassChange=[["Elemental Noble", 35]], #[Name, Level]
AttackUnlocks=[[moves.Cut,27],[moves.Slice,30],[moves.Aqua,35],[moves.Slash,40]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,32]])
ListOfPlayableUnits.append(Elbon)
Elbon.TurtleName = new_turtle()
Elbon.TurtleName.shape(Elbon.Sprite)
Elbon.TurtleName.hideturtle()
DataListUnit = Elbon
Elbon.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#B------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/b_small.gif")
register_shape(current_directory+"/Portraits/b_big.gif")
B = Unit(TurtleName="BTurtle",
DisplayName="B",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=90,
CurrentHP=90,
ATK=35, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=3, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Partial Mechanical",
Attacks=[moves.Cut,moves.Slash],
Supports=[],
Traits=["Physical Primary","Infinian","Mechanical"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[70,2],
DEFGrowth=[60,1],
RESGrowth=[60,1],
AGLGrowth=[40,1],
ACRGrowth=[90,1],
Portrait=current_directory+"/Portraits/b_big.gif",
Sprite=current_directory+"/Sprites/b_small.gif",
LevelQuotes=["B: ..."],
Bio="B is an Nolavillian who has been affected\nby the Inverse Time. Due to this, he\nis taken to a different timeline every 18 months.",
ClassChange=[["Chrono Master", 50]], #[Name, Level]
AttackUnlocks=[[moves.Beam,40],[moves.Destroyer,50]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,45]])
ListOfPlayableUnits.append(B)
B.TurtleName = new_turtle()
B.TurtleName.shape(B.Sprite)
B.TurtleName.hideturtle()
DataListUnit = B
B.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]


#Xuirventh------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/xuirventh_small.gif")
register_shape(current_directory+"/Portraits/xuirventh_big.gif")
Xuirventh = Unit(TurtleName="XuirventhTurtle",
DisplayName="Xuirventh",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=30, #Influences attack damage
DEF=18, #Influences damage taken from physical attacks
RES=18, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Proto-Xuir",
Attacks=[moves.Slice,moves.Fireball],
Supports=[],
Traits=["Physical Primary","Xuir","Fire"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[80,1],
RESGrowth=[80,1],
AGLGrowth=[45,1],
ACRGrowth=[80,2],
Portrait=current_directory+"/Portraits/xuirventh_big.gif",
Sprite=current_directory+"/Sprites/xuirventh_small.gif",
LevelQuotes=["Xuirventh: Good.","Xuirventh: This is revenge.","Xuirventh: I'm feeling stronger."],
Bio="Xuirventh is a Proto-Xuir who has\nescaped from Death Pepper's research center.\nHe teams up with Proton in hopes of saving the\nother Proto-Xuirs that have been captured by the Xuirists.",
ClassChange=[["Xuir Champion", 40]], #[Name, Level]
AttackUnlocks=[[moves.Finisher,30],[moves.Slash,35],[moves.FireBlast,40]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,32]])
ListOfPlayableUnits.append(Xuirventh)
Xuirventh.TurtleName = new_turtle()
Xuirventh.TurtleName.shape(Xuirventh.Sprite)
Xuirventh.TurtleName.hideturtle()
DataListUnit = Xuirventh
Xuirventh.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Xuirfth------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/xuirfth_small.gif")
register_shape(current_directory+"/Portraits/xuirfth_big.gif")
Xuirfth = Unit(TurtleName="XuirfthTurtle",
DisplayName="Xuirfth",
AttackRange=[1,2],
PrimaryType="Magic",
MaxHP=40,
CurrentHP=40,
ATK=32, #Influences attack damage
DEF=22, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=29, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=29,
UnitClass="Proto-Xuir",
Attacks=[moves.Aqua,moves.MageBlade],
Supports=[],
Traits=["Magic Primary","Xuir","Water"],
HPGrowth=[75,1], #Chance to level up, max amount to increase
ATKGrowth=[90,1],
DEFGrowth=[70,1],
RESGrowth=[100,2],
AGLGrowth=[60,1],
ACRGrowth=[75,2],
Portrait=current_directory+"/Portraits/xuirfth_big.gif",
Sprite=current_directory+"/Sprites/xuirfth_small.gif",
LevelQuotes=["Xuirfth: Great.","Xuirfth: This will help.","Xuirfth: I feel stronger."],
Bio="Xuirfth is a Proto-Xuir who escaped\nfrom the Shadow Realm with Xuirventh.",
ClassChange=[["Xuir Champion", 45]], #[Name, Level]
AttackUnlocks=[[moves.Hydro,33],[moves.Cut,35],[moves.Hydra,40]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Xuirfth)
Xuirfth.TurtleName = new_turtle()
Xuirfth.TurtleName.shape(Xuirfth.Sprite)
Xuirfth.TurtleName.hideturtle()
DataListUnit = Xuirfth
Xuirfth.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Xuirer------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/xuirer_small.gif")
register_shape(current_directory+"/Portraits/xuirer_big.gif")
Xuirer = Unit(TurtleName="XuirerTurtle",
DisplayName="Xuirer",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=42, #Influences attack damage
DEF=32, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=30,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Dagger,moves.DaggerToss,moves.GeomMedal],
Supports=[moves.XuiristRitual],
Traits=["Physical Primary","Infinian","Xuirist"],
HPGrowth=[90,2], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[70,1],
RESGrowth=[70,1],
AGLGrowth=[15,1],
ACRGrowth=[80,1],
Portrait=current_directory+"/Portraits/xuirer_big.gif",
Sprite=current_directory+"/Sprites/xuirer_small.gif",
LevelQuotes=["Xuirer: Good.","Xuirer: All shall fall to the power of Xuir.","Xuirer: Accept the power of Xuir."],
Bio="Xuirer is a Xuirist who rejects the\nidea of the sinful Proto-Xuir and\nbelieves they should be worshipped as Xuir entities.",
ClassChange=[["High Xuirist", 40]], #[Name, Level]
AttackUnlocks=[[moves.Snipe,35],[moves.SnipeII,40]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Xuirer)
Xuirer.TurtleName = new_turtle()
Xuirer.TurtleName.shape(Xuirer.Sprite)
Xuirer.TurtleName.hideturtle()
DataListUnit = Xuirer
Xuirer.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Dliug------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/dliug_small.gif")
register_shape(current_directory+"/Portraits/dliug_big.gif")
Dliug = Unit(TurtleName="DliugTurtle",
DisplayName="Dliug",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=40, #Influences attack damage
DEF=30, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=30,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=37,
UnitClass="Mercenary",
Attacks=[moves.Axe,moves.AxeThrow],
Supports=[moves.MedKit],
Traits=["Physical Primary","Bipolian","Mercenary"],
HPGrowth=[100,3], #Chance to level up, max amount to increase
ATKGrowth=[90,1],
DEFGrowth=[60,1],
RESGrowth=[10,1],
AGLGrowth=[5,1],
ACRGrowth=[50,1],
Portrait=current_directory+"/Portraits/dliug_big.gif",
Sprite=current_directory+"/Sprites/dliug_small.gif",
LevelQuotes=["Dliug: Victory.","Dliug: You shall fall.","Dliug: Fear me."],
Bio="Dliug is an mercenary who has\ndecided to fight against the\nXuirists.",
ClassChange=[["Executioner", 45]], #[Name, Level]
AttackUnlocks=[[moves.ShieldShatter,40],[moves.Execution,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Dliug)
Dliug.TurtleName = new_turtle()
Dliug.TurtleName.shape(Dliug.Sprite)
Dliug.TurtleName.hideturtle()
DataListUnit = Dliug
Dliug.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Exa------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/exa_small.gif")
register_shape(current_directory+"/Portraits/exa_big.gif")
Exa = Unit(TurtleName="ExaTurtle",
DisplayName="Exa",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=65,
CurrentHP=65,
ATK=20, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=17, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Mercenary",
Attacks=[moves.Axe],
Supports=[],
Traits=["Physical Primary","Bipolian","Mercenary","Bio"],
HPGrowth=[80,1], #Chance to level up, max amount to increase
ATKGrowth=[60,1],
DEFGrowth=[50,1],
RESGrowth=[5,1],
AGLGrowth=[30,1],
ACRGrowth=[75,1],
Portrait=current_directory+"/Portraits/exa_big.gif",
Sprite=current_directory+"/Sprites/exa_small.gif",
LevelQuotes=["Exa: You've been defeated.","Exa: Come back when your a little... richer.","Exa: My axe is unstoppable."],
Bio="Exa is an mercenary who works\nwith Dliug.",
ClassChange=[["Elemental Mercenary", 45]], #[Name, Level]
AttackUnlocks=[[moves.AxeThrow,40],[moves.Thorn,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,42]])
ListOfPlayableUnits.append(Exa)
Exa.TurtleName = new_turtle()
Exa.TurtleName.shape(Exa.Sprite)
Exa.TurtleName.hideturtle()
DataListUnit = Exa
Exa.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Yranecrem------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/yranecrem_small.gif")
register_shape(current_directory+"/Portraits/yranecrem_big.gif")
Yranecrem = Unit(TurtleName="YranecremTurtle",
DisplayName="Yranecrem",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=125,
CurrentHP=125,
ATK=37, #Influences attack damage
DEF=27, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Mercenary",
Attacks=[moves.Axe],
Supports=[moves.MedKit],
Traits=["Physical Primary","Bipolian","Mercenary"],
HPGrowth=[100,2], #Chance to level up, max amount to increase
ATKGrowth=[90,1],
DEFGrowth=[70,1],
RESGrowth=[10,1],
AGLGrowth=[10,1],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/yranecrem_big.gif",
Sprite=current_directory+"/Sprites/yranecrem_small.gif",
LevelQuotes=["Yranecrem: I've survived...","Yranecrem: This must end.","Yranecrem: I'm sorry.","Yranecrem: This is for the future.","Yranecrem: I must survive."],
Bio="Yranecrem is an mercenary who works\nwith Dliug.",
ClassChange=[["Executioner", 50]], #[Name, Level]
AttackUnlocks=[[moves.ShieldShatter,40],[moves.AxeThrow,45],[moves.Execution,50]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.Heal,42],[moves.LongHeal,47]])
ListOfPlayableUnits.append(Yranecrem)
Yranecrem.TurtleName = new_turtle()
Yranecrem.TurtleName.shape(Yranecrem.Sprite)
Yranecrem.TurtleName.hideturtle()
DataListUnit = Yranecrem
Yranecrem.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Geomer------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/geomer_small.gif")
register_shape(current_directory+"/Portraits/geomer_big.gif")
Geomer = Unit(TurtleName="GeomerTurtle",
DisplayName="Geomer",
AttackRange=[1,2],
PrimaryType="Magic",
MaxHP=55,
CurrentHP=55,
ATK=35, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=45, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=34,
UnitClass="Geom User",
Attacks=[moves.GeomBurst,moves.GeomBlast],
Supports=[],
Traits=["Magic Primary","Nolavillian"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[30,1],
RESGrowth=[30,1],
AGLGrowth=[20,1],
ACRGrowth=[75,2],
Portrait=current_directory+"/Portraits/geomer_big.gif",
Sprite=current_directory+"/Sprites/geomer_small.gif",
LevelQuotes=["Geomer: This is going perfectly.","Geomer: Should've learned Geom.","Geomer: You ever hear about the Geom Clan?"],
Bio="Geomer is Geom user who is\nproficient in the usage of\nGeom Energy in combat.",
ClassChange=[["Geom Master", 42]], #[Name, Level]
AttackUnlocks=[[moves.GeomStrike,38],[moves.GeomSlash,42]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Geomer)
Geomer.TurtleName = new_turtle()
Geomer.TurtleName.shape(Geomer.Sprite)
Geomer.TurtleName.hideturtle()
DataListUnit = Geomer
Geomer.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Box------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/box_small.gif")
register_shape(current_directory+"/Portraits/box_big.gif")
Box = Unit(TurtleName="BoxTurtle",
DisplayName="Box",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=40, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=7, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=37,
UnitClass="Merchant",
Attacks=[],
Supports=[moves.HealthPotion,moves.MedKit],
Traits=["Physical Primary","Nolavillian"],
HPGrowth=[100,2], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[70,1],
RESGrowth=[40,1],
AGLGrowth=[10,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/box_big.gif",
Sprite=current_directory+"/Sprites/box_small.gif",
LevelQuotes=["Box: If it ain't a box, then it is a box.","Box: Boxes are neat.","Box: Y'all see any good boxes on sale?","Box: It's a box.","Box: No, it's not a box."],
Bio="Box is a merchant who has\nmany medical items that\ncan help you recover.",
ClassChange=[["Merchant", 37]], #[Name, Level]
AttackUnlocks=[[moves.Dagger,42]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.Save,40],[moves.Fortify,45]])
ListOfPlayableUnits.append(Box) 
Box.TurtleName = new_turtle()
Box.TurtleName.shape(Box.Sprite)
Box.TurtleName.hideturtle()
DataListUnit = Box
Box.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#NOTOS------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/NOTOS_small.gif")
register_shape(current_directory+"/Portraits/NOTOS_big.gif")
NOTOS = Unit(TurtleName="NOTOSTurtle",
DisplayName="NOTOS",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=135,
CurrentHP=135,
ATK=35, #Influences attack damage
DEF=27, #Influences damage taken from physical attacks
RES=13, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=38,
UnitClass="Master of the OS",
Attacks=[moves.Slice,moves.Slash,moves.Thunder,moves.ThunderBlast,moves.Missile],
Supports=[],
Traits=["Physical Primary","Nolavillian","Partial Mechanical"],
HPGrowth=[100,2], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[50,1],
RESGrowth=[40,1],
AGLGrowth=[25,1],
ACRGrowth=[100,1],
Portrait=current_directory+"/Portraits/NOTOS_big.gif",
Sprite=current_directory+"/Sprites/NOTOS_small.gif",
LevelQuotes=["NOTOS: It is imminent.","NOTOS: Death awaits.","NOTOS: May the wrath consume you."],
Bio="[[UNKNOWN]]",
ClassChange=[["Master of the OS", 50]], #[Name, Level]
AttackUnlocks=[[moves.ArmorBreak,40],[moves.ShieldShatter,45],[moves.Execution,50]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,47]])
ListOfPlayableUnits.append(NOTOS)
NOTOS.TurtleName = new_turtle()
NOTOS.TurtleName.shape(NOTOS.Sprite)
NOTOS.TurtleName.hideturtle()
DataListUnit = NOTOS
NOTOS.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#YungPoggers------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/yungpoggers_small.gif")
register_shape(current_directory+"/Portraits/yungpoggers_big.gif")
YungPoggers = Unit(TurtleName="YungPoggersTurtle",
DisplayName="Yung Poggers",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=70,
CurrentHP=70,
ATK=42, #Influences attack damage
DEF=37, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=17, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=30,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=38,
UnitClass="Pogger",
Attacks=[moves.Slice,moves.Slash,moves.GeomBurst,moves.GeomMedal],
Supports=[moves.MedKit],
Traits=["Physical Primary","Nolavillian","Red Pilled"],
HPGrowth=[85,1], #Chance to level up, max amount to increase
ATKGrowth=[65,1],
DEFGrowth=[65,1],
RESGrowth=[65,1],
AGLGrowth=[40,1],
ACRGrowth=[100,1],
Portrait=current_directory+"/Portraits/yungpoggers_big.gif",
Sprite=current_directory+"/Sprites/yungpoggers_small.gif",
LevelQuotes=["Yung Poggers: Based.","Yung Poggers: Red pilled.","Yung Poggers: When *SUS*."],
Bio="He is red pilled and based.",
ClassChange=[["Red-Pilled", 45]], #[Name, Level]
AttackUnlocks=[[moves.GeomSlash,40],[moves.GeomStrike,42],[moves.ShieldShatter,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(YungPoggers)
YungPoggers.TurtleName = new_turtle()
YungPoggers.TurtleName.shape(YungPoggers.Sprite)
YungPoggers.TurtleName.hideturtle()
DataListUnit = YungPoggers
YungPoggers.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Dnefed------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/dnefed_small.gif")
register_shape(current_directory+"/Portraits/dnefed_big.gif")
Dnefed = Unit(TurtleName="DnefedTurtle",
DisplayName="Dnefed",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=30, #Influences attack damage
DEF=30, #Influences damage taken from physical attacks
RES=12, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Armor Knight",
Attacks=[moves.Slice,moves.Slash],
Supports=[],
Traits=["Physical Primary","Shadeian","Armored"],
HPGrowth=[100,5], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[60,1],
RESGrowth=[5,1],
AGLGrowth=[10,1],
ACRGrowth=[65,1],
Portrait=current_directory+"/Portraits/dnefed_big.gif",
Sprite=current_directory+"/Sprites/dnefed_small.gif",
LevelQuotes=["Dnefed: Done.","Dnefed: Good.","Dnefed: I've won."],
Bio="Dnefed is a soldier from Shade.",
ClassChange=[["Shield Knight", 45]], #[Name, Level]
AttackUnlocks=[[moves.Javelin,37],[moves.ArmorBreak,40],[moves.ShieldBash,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Dnefed)
Dnefed.TurtleName = new_turtle()
Dnefed.TurtleName.shape(Dnefed.Sprite)
Dnefed.TurtleName.hideturtle()
DataListUnit = Dnefed
Dnefed.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Thgif------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/thgif_small.gif")
register_shape(current_directory+"/Portraits/thgif_big.gif")
Thgif = Unit(TurtleName="ThgifTurtle",
DisplayName="Thgif",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=30, #Influences attack damage
DEF=29, #Influences damage taken from physical attacks
RES=13, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Warrior",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Shadeian","Fighter"],
HPGrowth=[80,1], #Chance to level up, max amount to increase
ATKGrowth=[75,1],
DEFGrowth=[70,1],
RESGrowth=[50,1],
AGLGrowth=[20,1],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/thgif_big.gif",
Sprite=current_directory+"/Sprites/thgif_small.gif",
LevelQuotes=["Thgif: Victory.","Thgif: Great.","Thgif: I've won."],
Bio="Thgif is a soldier from Shade.",
ClassChange=[["Elite Warrior", 45]], #[Name, Level]
AttackUnlocks=[[moves.Slash,40],[moves.ArmorBreak,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Thgif)
Thgif.TurtleName = new_turtle()
Thgif.TurtleName.shape(Thgif.Sprite)
Thgif.TurtleName.hideturtle()
DataListUnit = Thgif
Thgif.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Gnirif------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/gnirif_small.gif")
register_shape(current_directory+"/Portraits/gnirif_big.gif")
Gnirif = Unit(TurtleName="GnirifTurtle",
DisplayName="Gnirif",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=35, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Sniper",
Attacks=[moves.Bow,moves.DistanceShot,moves.Snipe],
Supports=[],
Traits=["Physical Primary","Shadeian","Archer"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[75,1],
DEFGrowth=[40,1],
RESGrowth=[40,1],
AGLGrowth=[25,1],
ACRGrowth=[100,2],
Portrait=current_directory+"/Portraits/gnirif_big.gif",
Sprite=current_directory+"/Sprites/gnirif_small.gif",
LevelQuotes=["Gnirif: Victory.","Gnirif: Good.","Gnirif: You've lost."],
Bio="Gnirif is a soldier from Shade.",
ClassChange=[["Elite Sniper", 50]], #[Name, Level]
AttackUnlocks=[[moves.SnipeII,40],[moves.SnipeIII,50]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Gnirif)
Gnirif.TurtleName = new_turtle()
Gnirif.TurtleName.shape(Gnirif.Sprite)
Gnirif.TurtleName.hideturtle()
DataListUnit = Gnirif
Gnirif.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Cigam------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/cigam_small.gif")
register_shape(current_directory+"/Portraits/cigam_big.gif")
Cigam = Unit(TurtleName="CigamTurtle",
DisplayName="Cigam",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=35, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Heal Mage",
Attacks=[],
Supports=[moves.Heal,moves.LongHeal,moves.FarHeal],
Traits=["Physical Primary","Shadeian","Mage","Water"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[90,1],
DEFGrowth=[20,1],
RESGrowth=[70,1],
AGLGrowth=[25,1],
ACRGrowth=[75,1],
Portrait=current_directory+"/Portraits/cigam_big.gif",
Sprite=current_directory+"/Sprites/cigam_small.gif",
LevelQuotes=["Cigam: This will be helpful.","Cigam: Good.","Cigam: Great."],
Bio="Cigam is a soldier from Shade.",
ClassChange=[["Dual Mage", 40]], #[Name, Level]
AttackUnlocks=[[moves.Aqua,40],[moves.Hydro,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,37]])
ListOfPlayableUnits.append(Cigam)
Cigam.TurtleName = new_turtle()
Cigam.TurtleName.shape(Cigam.Sprite)
Cigam.TurtleName.hideturtle()
DataListUnit = Cigam
Cigam.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#PlayableOmega------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/omegaxuirist_small.gif")
register_shape(current_directory+"/Portraits/omegaxuirist_big.gif")
Omega = Unit(TurtleName="OmegaTurtle",
DisplayName="Omega",
AttackRange=[1,2],
PrimaryType="Magic",
MaxHP=75,
CurrentHP=75,
ATK=45, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=50, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Elite Xuirist",
Attacks=[moves.DarkOrb,moves.ShadowBurst],
Supports=[moves.XuiristRitual],
Traits=["Magic Primary","Nolavillian","Xuirist"],
HPGrowth=[85,1], #Chance to level up, max amount to increase
ATKGrowth=[90,1],
DEFGrowth=[40,1],
RESGrowth=[80,2],
AGLGrowth=[35,1],
ACRGrowth=[95,1],
Portrait=current_directory+"/Portraits/omegaxuirist_big.gif",
Sprite=current_directory+"/Sprites/omegaxuirist_small.gif",
LevelQuotes=["Omega: ..."],
Bio="Omega was previously the official leader of the\nXuirists, though he was being forced by Break.\nHe now works with Proton to retrieve the Holy Itucher.",
ClassChange=[["Elite Xuirist", 50]], #[Name, Level]
AttackUnlocks=[[moves.ShadowBlade,45],[moves.ShadowStorm,50]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Omega)
Omega.TurtleName = new_turtle()
Omega.TurtleName.shape(Omega.Sprite)
Omega.TurtleName.hideturtle()
DataListUnit = Omega
Omega.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Fiyghtrr------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/fiyghtrr_small.gif")
register_shape(current_directory+"/Portraits/fiyghtrr_big.gif")
Fiyghtrr = Unit(TurtleName="FiyghtrrTurtle",
DisplayName="Fiyghtrr",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=35, #Influences attack damage
DEF=32, #Influences damage taken from physical attacks
RES=32, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Elite Fighter",
Attacks=[moves.Punch],
Supports=[moves.Heal],
Traits=["Physical Primary","Specian","Fighter"],
HPGrowth=[100,1], #Chance to level up, max amount to increase
ATKGrowth=[75,1],
DEFGrowth=[20,1],
RESGrowth=[20,1],
AGLGrowth=[35,1],
ACRGrowth=[100,1],
Portrait=current_directory+"/Portraits/fiyghtrr_big.gif",
Sprite=current_directory+"/Sprites/fiyghtrr_small.gif",
LevelQuotes=["Fiyghtrr: Perish, fools!","Fiyghtrr: You get what you deserve.","Fiyghtrr: I've been waiting for this!"],
Bio="Fiyghtrr is a fighter from the Village of Binding\nwho has been training to defeat the Shadow Realm.",
ClassChange=[["Spirit Fighter", 60]], #[Name, Level]
AttackUnlocks=[[moves.ManaBurst,45],[moves.Aura,55]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.LongHeal,50],[moves.FarHeal,60]])
ListOfPlayableUnits.append(Fiyghtrr)
Fiyghtrr.TurtleName = new_turtle()
Fiyghtrr.TurtleName.shape(Fiyghtrr.Sprite)
Fiyghtrr.TurtleName.hideturtle()
DataListUnit = Fiyghtrr
Fiyghtrr.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Recalper------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/recalper_small.gif")
register_shape(current_directory+"/Portraits/recalper_big.gif")
Recalper = Unit(TurtleName="RecalperTurtle",
DisplayName="Recalper",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=95,
CurrentHP=95,
ATK=30, #Influences attack damage
DEF=41, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="The \"Ultimate\" Replacement",
Attacks=[moves.Javelin,moves.ShieldShatter],
Supports=[moves.MedKit],
Traits=["Physical Primary","Nolavillian","Fighter","Electric"],
HPGrowth=[90,1], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[75,1],
RESGrowth=[20,1],
AGLGrowth=[20,1],
ACRGrowth=[95,1],
Portrait=current_directory+"/Portraits/recalper_big.gif",
Sprite=current_directory+"/Sprites/recalper_small.gif",
LevelQuotes=["Recalper: Haha! I am the best replacement!","Recalper: No one can replace the deceased like I can!","Recalper: Who said replacement units can't be viable?","Recalper: LETS GOOOOOOO!!!","Recalper: You stand no chance to a mere REPLACEMENT UNIT!","Recalper: I AM THE BEST (replacement)!!!","Recalper: REPLACEMENTS! REPLACEMENTS! REPLACEMENTS!","Recalper: DID YOU KNOW THAT I'M A REPLACEMENT UNIT!? YEAH, DEAL WITH IT.","Recalper: My personality is that I'm a REPLACEMENT UNIT!!! REEEEE!!!!!","Recalper: Do not be afraid, the REPLACEMENT UNIT is here!"],
Bio="Recalper is the self-proclaimed \"best replacement unit of all time\".",
ClassChange=[["The \"Ultimate\"-er Replacement", 55]], #[Name, Level]
AttackUnlocks=[[moves.Slash,45],[moves.Thunder,50],[moves.ThunderBlast,55]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Recalper)
Recalper.TurtleName = new_turtle()
Recalper.TurtleName.shape(Recalper.Sprite)
Recalper.TurtleName.hideturtle()
DataListUnit = Recalper
Recalper.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Tabmoc------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/tabmoc_small.gif")
register_shape(current_directory+"/Portraits/tabmoc_big.gif")
Tabmoc = Unit(TurtleName="TabmocTurtle",
DisplayName="Tabmoc",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=125,
CurrentHP=125,
ATK=65, #Influences attack damage
DEF=42, #Influences damage taken from physical attacks
RES=33, #Influences damage taken from magic attacks
AGL=18, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=42,
UnitClass="Blade Fighter",
Attacks=[moves.Slice,moves.Slash,moves.ShieldShatter],
Supports=[moves.MedKit],
Traits=["Physical Primary","Shadeian","Fighter"],
HPGrowth=[90,1], #Chance to level up, max amount to increase
ATKGrowth=[90,1],
DEFGrowth=[50,1],
RESGrowth=[50,1],
AGLGrowth=[20,1],
ACRGrowth=[95,1],
Portrait=current_directory+"/Portraits/tabmoc_big.gif",
Sprite=current_directory+"/Sprites/tabmoc_small.gif",
LevelQuotes=["Tabmoc: Fall.","Tabmoc: I win.","Tabmoc: Victory."],
Bio="Tabmoc is a warrior from Bipole who has\nallied with Proton in retrieving the Holy Itucher.",
ClassChange=[["Blade Warrior", 53]], #[Name, Level]
AttackUnlocks=[[moves.HyperSlash,48],[moves.GodSlash,53]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Tabmoc)
Tabmoc.TurtleName = new_turtle()
Tabmoc.TurtleName.shape(Tabmoc.Sprite)
Tabmoc.TurtleName.hideturtle()
DataListUnit = Tabmoc
Tabmoc.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Xuirurth------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/xuirurth_small.gif")
register_shape(current_directory+"/Portraits/xuirurth_big.gif")
Xuirurth = Unit(TurtleName="XuirurthTurtle",
DisplayName="Xuirurth",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=85,
CurrentHP=85,
ATK=30, #Influences attack damage
DEF=30, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Proto-Xuir",
Attacks=[moves.Slice,moves.Slash,moves.XuirBlaster],
Supports=[moves.MedKit],
Traits=["Physical Primary","Xuir","Fighter","Electric"],
HPGrowth=[80,1], #Chance to level up, max amount to increase
ATKGrowth=[75,1],
DEFGrowth=[50,1],
RESGrowth=[40,1],
AGLGrowth=[25,1],
ACRGrowth=[90,1],
Portrait=current_directory+"/Portraits/xuirurth_big.gif",
Sprite=current_directory+"/Sprites/xuirurth_small.gif",
LevelQuotes=["Xuirurth: Victory!","Xuirurth: We'll win.","Xuirurth: The Shadow Realm will be no more!"],
Bio="Xuirurth is Proto-Xuir G3 N4.",
ClassChange=[["Xuir Champion", 55]], #[Name, Level]
AttackUnlocks=[[moves.Thunder,45],[moves.ArmorBreak,50],[moves.ThunderBlast,55]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Xuirurth)
Xuirurth.TurtleName = new_turtle()
Xuirurth.TurtleName.shape(Xuirurth.Sprite)
Xuirurth.TurtleName.hideturtle()
DataListUnit = Xuirurth
Xuirurth.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Repins2------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/repins_small.gif")
register_shape(current_directory+"/Portraits/repins_big2.gif")
Repins2 = Unit(TurtleName="Repins2Turtle",
DisplayName="Repins Blaze",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=70,
CurrentHP=70,
ATK=55, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=60,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=42,
UnitClass="Elemental Sniper",
Attacks=[moves.FlamingArrow,moves.Fireball,moves.Snipe,moves.SnipeII],
Supports=[moves.MedKit],
Traits=["Physical Primary","Bipolian","Archer","Fire"],
HPGrowth=[90,1], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[70,1],
RESGrowth=[70,1],
AGLGrowth=[5,1],
ACRGrowth=[80,1],
Portrait=current_directory+"/Portraits/repins_big2.gif",
Sprite=current_directory+"/Sprites/repins_small.gif",
LevelQuotes=["Repins: ...","Repins: This is for the future.","Repins: I've won."],
Bio="...",
ClassChange=[["Elite Sniper", 50],["God Sniper",60]], #[Name, Level]
AttackUnlocks=[[moves.SnipeIII,45],[moves.SnipeIV,50],[moves.GodSnipe,60]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Repins2)
Repins2.TurtleName = new_turtle()
Repins2.TurtleName.shape(Repins2.Sprite)
Repins2.TurtleName.hideturtle()
DataListUnit = Repins2
Repins2.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Ahcem------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/ahcem_small.gif")
register_shape(current_directory+"/Portraits/ahcem_big.gif")
Ahcem = Unit(TurtleName="AhcemTurtle",
DisplayName="Ahcem",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=115,
CurrentHP=115,
ATK=35, #Influences attack damage
DEF=39, #Influences damage taken from physical attacks
RES=19, #Influences damage taken from magic attacks
AGL=19, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=44,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=47,
UnitClass="Mechanical Entity",
Attacks=[moves.AntiXuir,moves.Slash,moves.Beam,moves.Thunder],
Supports=[],
Traits=["Physical Primary","Mechanical","Fighter"],
HPGrowth=[90,1], #Chance to level up, max amount to increase
ATKGrowth=[65,1],
DEFGrowth=[50,1],
RESGrowth=[25,1],
AGLGrowth=[30,1],
ACRGrowth=[95,1],
Portrait=current_directory+"/Portraits/ahcem_big.gif",
Sprite=current_directory+"/Sprites/ahcem_small.gif",
LevelQuotes=["Achem: Destruction.","Achem: The one shall return.","Achem: Power."],
Bio="???",
ClassChange=[["=RITUAL_PREPARED=", 57]], #[Name, Level]
AttackUnlocks=[[moves.ThunderBlast,50],[moves.Voltage,55]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Ahcem)
Ahcem.TurtleName = new_turtle()
Ahcem.TurtleName.shape(Ahcem.Sprite)
Ahcem.TurtleName.hideturtle()
DataListUnit = Ahcem
Ahcem.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Cayenne------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/cayenne_small.gif")
register_shape(current_directory+"/Portraits/cayenne_big.gif")
Cayenne = Unit(TurtleName="CayenneTurtle",
DisplayName="Cayenne",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=150,
CurrentHP=150,
ATK=35, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=18, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=60,
UnitClass="Mechanical Entity",
Attacks=[moves.AntiXuir,moves.Slash],
Supports=[moves.HealthPotion],
Traits=["Physical Primary","Mechanical","Fighter"],
HPGrowth=[85,1], #Chance to level up, max amount to increase
ATKGrowth=[85,1],
DEFGrowth=[75,1],
RESGrowth=[50,1],
AGLGrowth=[25,1],
ACRGrowth=[85,1],
Portrait=current_directory+"/Portraits/cayenne_big.gif",
Sprite=current_directory+"/Sprites/cayenne_small.gif",
LevelQuotes=["Cayenne: You've been defeated.","Cayenne: For the liberation!"],
Bio="Cayenne is a mechanical that was created\nby Death Pepper. He wants to help you\nstop Death Pepper for unknown reasons.",
ClassChange=[["Mechanical", 60]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Cayenne)
Cayenne.TurtleName = new_turtle()
Cayenne.TurtleName.shape(Cayenne.Sprite)
Cayenne.TurtleName.hideturtle()
DataListUnit = Cayenne
Cayenne.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#XuirMan------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/xuirman_small.gif")
register_shape(current_directory+"/Portraits/xuirman_big.gif")
XuirMan = Unit(TurtleName="XuirManTurtle",
DisplayName="Proton Xurr",
AttackRange = [1,2],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=10, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=6, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack
ACR=13,#Influences the chance of landing an attack
SPD=7, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Ascended Realmer",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Xuir", "Knight"],
HPGrowth=[100,3], #Chance to level up, max amount to increase
ATKGrowth=[100,1],
DEFGrowth=[100,1],
RESGrowth=[100,1],
AGLGrowth=[100,1],
ACRGrowth=[100,1],
Portrait=current_directory+"/Portraits/xuirman_big.gif",
Sprite=current_directory+"/Sprites/xuirman_small.gif",
LevelQuotes=["Proton: ..."],
Bio="Proton has been revived as an ascended Realmer by using the\nForbidden Ritual of Nation. The universal consequences of this\nare very dangerous.",
ClassChange=[], #[Name, Level]
AttackUnlocks=[[moves.Lance,3],[moves.Javelin,5],[moves.ArmorBreak,10],[moves.MageBlade,15],[moves.Slash,20]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(XuirMan)
XuirMan.TurtleName = new_turtle()
XuirMan.TurtleName.shape(current_directory+"/Sprites/xuirman_small.gif")
XuirMan.TurtleName.hideturtle()
DataListUnit = XuirMan
XuirMan.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]

#Integer------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/integer_small.gif")
register_shape(current_directory+"/Portraits/integer_big.gif")
Integer = Unit(TurtleName="IntegerTurtle",
DisplayName="Integer",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=999,
CurrentHP=999,
ATK=999, #Influences attack damage
DEF=999, #Influences damage taken from physical attacks
RES=999, #Influences damage taken from magic attacks
AGL=999, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=999,
SPD=999, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=999, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=99,
UnitClass="Tractor",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Magic Primary","Xuir"],
HPGrowth=[0,99], #Chance to level up, max amount to increase
ATKGrowth=[0,99],
DEFGrowth=[0,99],
RESGrowth=[0,99],
AGLGrowth=[0,99],
ACRGrowth=[0,99],
Portrait=current_directory+"/Portraits/integer_big.gif",
Sprite=current_directory+"/Sprites/integer_small.gif",
LevelQuotes=["Integer: ..."],
Bio="Integer is Proton's tractor, and was awakened\nupon his revival from the Forbidden Ritual.",
ClassChange=[], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ListOfPlayableUnits.append(Integer)
Integer.TurtleName = new_turtle()
Integer.TurtleName.shape(Integer.Sprite)
Integer.TurtleName.hideturtle()
DataListUnit = Integer
Integer.DataList = [DataListUnit.MaxHP,DataListUnit.CurrentHP,DataListUnit.ATK,DataListUnit.DEF,DataListUnit.RES,DataListUnit.AGL,DataListUnit.ACR,DataListUnit.SPD,DataListUnit.EXP,DataListUnit.Level,DataListUnit.UnitClass,DataListUnit.Portrait,DataListUnit.Sprite]




















#===============================================================================================================================================================================================================
#===============================================================================================================================================================================================================
#===============================================================================================================================================================================================================
#===============================================================================================================================================================================================================
#===============================================================================================================================================================================================================
#===============================================================================================================================================================================================================
#==== Enemy Units ==============================================================================================================================================================================================
#===============================================================================================================================================================================================================

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 1]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Red Slime 1---------------
register_shape(current_directory+"/Sprites/redslime_small.gif")
register_shape(current_directory+"/Portraits/redslime_big.gif")
Chapter1RedSlime1 = Unit(TurtleName="Chapter1RedSlime1",
DisplayName="Red Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=6,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=45, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Red Slime",
Attacks=[moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Fire"],
Portrait=current_directory+"/Portraits/redslime_big.gif",
Sprite=current_directory+"/Sprites/redslime_small.gif",
LevelQuotes=["Red Slime: bruh how do you lose in the first chapter"],
Bio="Red Slimes are basic monsters that \n can be found throughout the Bipolian continent.")
Chapter1RedSlime1.TurtleName = new_turtle()
Chapter1RedSlime1.TurtleName.shape(Chapter1RedSlime1.Sprite)
Chapter1RedSlime1.TurtleName.hideturtle()

#Red Slime 2---------------
register_shape(current_directory+"/Sprites/redslime_small.gif")
register_shape(current_directory+"/Portraits/redslime_big.gif")
Chapter1RedSlime2 = Unit(TurtleName="Chapter1RedSlime1",
DisplayName="Red Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=6,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=45, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Red Slime",
Attacks=[moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Fire"],
Portrait=current_directory+"/Portraits/redslime_big.gif",
Sprite=current_directory+"/Sprites/redslime_small.gif",
LevelQuotes=["Red Slime: bruh how do you lose in the first chapter"],
Bio="Red Slimes are basic monsters that \n can be found throughout the Bipolian continent.")
Chapter1RedSlime2.TurtleName = new_turtle()
Chapter1RedSlime2.TurtleName.shape(Chapter1RedSlime2.Sprite)
Chapter1RedSlime2.TurtleName.hideturtle()

#Red Slime 3---------------
register_shape(current_directory+"/Sprites/redslime_small.gif")
register_shape(current_directory+"/Portraits/redslime_big.gif")
Chapter1RedSlime3 = Unit(TurtleName="Chapter1RedSlime1",
DisplayName="Red Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=6,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=45, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Red Slime",
Attacks=[moves.Slam],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Monster","Fire"],
Portrait=current_directory+"/Portraits/redslime_big.gif",
Sprite=current_directory+"/Sprites/redslime_small.gif",
LevelQuotes=["Red Slime: bruh how do you lose in the first chapter"],
Bio="Red Slimes are basic monsters that \n can be found throughout the Bipolian continent.")
Chapter1RedSlime3.TurtleName = new_turtle()
Chapter1RedSlime3.TurtleName.shape(Chapter1RedSlime3.Sprite)
Chapter1RedSlime3.TurtleName.hideturtle()

#Red Slime 4---------------
register_shape(current_directory+"/Sprites/redslime_small.gif")
register_shape(current_directory+"/Portraits/redslime_big.gif")
Chapter1RedSlime4 = Unit(TurtleName="Chapter1RedSlime4",
DisplayName="Red Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=6,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=45, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Red Slime",
Attacks=[moves.Slam],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Monster","Fire"],
Portrait=current_directory+"/Portraits/redslime_big.gif",
Sprite=current_directory+"/Sprites/redslime_small.gif",
LevelQuotes=["Red Slime: bruh how do you lose in the first chapter"],
Bio="Red Slimes are basic monsters that \n can be found throughout the Bipolian continent.")
Chapter1RedSlime4.TurtleName = new_turtle()
Chapter1RedSlime4.TurtleName.shape(Chapter1RedSlime4.Sprite)
Chapter1RedSlime4.TurtleName.hideturtle()

#Blue Slime 1---------------
register_shape(current_directory+"/Sprites/blueslime_small.gif")
register_shape(current_directory+"/Portraits/blueslime_big.gif")
Chapter1BlueSlime1 = Unit(TurtleName="Chapter1BlueSlime1",
DisplayName="Blue Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=12,#3, #Influences attack damage
DEF=22, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=99,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=65, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Blue Slime",
Attacks=[moves.Slam], #moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Water"],
Portrait=current_directory+"/Portraits/blueslime_big.gif",
Sprite=current_directory+"/Sprites/blueslime_small.gif",
LevelQuotes=["Blue Slime: bruh how do you lose in the first chapter"],
Bio="Blue Slimes are similar to Red Slimes, \n but have higher DEF and lower RES.")
Chapter1BlueSlime1.TurtleName = new_turtle()
Chapter1BlueSlime1.TurtleName.shape(current_directory+"/Sprites/blueslime_small.gif")
Chapter1BlueSlime1.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 2]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Red Slime 1---------------
register_shape(current_directory+"/Sprites/redslime_small.gif")
register_shape(current_directory+"/Portraits/redslime_big.gif")
Chapter2RedSlime1 = Unit(TurtleName="Chapter2RedSlime1",
DisplayName="Red Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=6,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=45, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Red Slime",
Attacks=[moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Fire"],
Portrait=current_directory+"/Portraits/redslime_big.gif",
Sprite=current_directory+"/Sprites/redslime_small.gif",
LevelQuotes=["Red Slime: *slime sounds*"],
Bio="Red Slimes are basic monsters that \n can be found throughout the Bipolian continent.")
Chapter2RedSlime1.TurtleName = new_turtle()
Chapter2RedSlime1.TurtleName.shape(Chapter2RedSlime1.Sprite)
Chapter2RedSlime1.TurtleName.hideturtle()

#Red Slime 2---------------
register_shape(current_directory+"/Sprites/redslime_small.gif")
register_shape(current_directory+"/Portraits/redslime_big.gif")
Chapter2RedSlime2 = Unit(TurtleName="Chapter2RedSlime2",
DisplayName="Red Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=4,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=45, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Red Slime",
Attacks=[moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Fire"],
Portrait=current_directory+"/Portraits/redslime_big.gif",
Sprite=current_directory+"/Sprites/redslime_small.gif",
LevelQuotes=["Red Slime: *slime sounds*"],
Bio="Red Slimes are basic monsters that \n can be found throughout the Bipolian continent.")
Chapter2RedSlime2.TurtleName = new_turtle()
Chapter2RedSlime2.TurtleName.shape(Chapter2RedSlime2.Sprite)
Chapter2RedSlime2.TurtleName.hideturtle()

#Red Slime 3---------------
register_shape(current_directory+"/Sprites/redslime_small.gif")
register_shape(current_directory+"/Portraits/redslime_big.gif")
Chapter2RedSlime3 = Unit(TurtleName="Chapter2RedSlime3",
DisplayName="Red Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=8,#3, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=45, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Red Slime",
Attacks=[moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Fire"],
Portrait=current_directory+"/Portraits/redslime_big.gif",
Sprite=current_directory+"/Sprites/redslime_small.gif",
LevelQuotes=["Red Slime: *slime sounds*"],
Bio="Red Slimes are basic monsters that \n can be found throughout the Bipolian continent.")
Chapter2RedSlime3.TurtleName = new_turtle()
Chapter2RedSlime3.TurtleName.shape(Chapter2RedSlime3.Sprite)
Chapter2RedSlime3.TurtleName.hideturtle()

#Yellow Slime 1---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter2YellowSlime1 = Unit(TurtleName="Chapter2YellowSlime1",
DisplayName="Yellow Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=8,#3, #Influences attack damage
DEF=1, #Influences damage taken from physical attacks
RES=8, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=60, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Yellow Slime",
Attacks=[moves.Thunder],
Supports=[],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter2YellowSlime1.TurtleName = new_turtle()
Chapter2YellowSlime1.TurtleName.shape(Chapter2YellowSlime1.Sprite)
Chapter2YellowSlime1.TurtleName.hideturtle()

#Yellow Slime 2---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter2YellowSlime2 = Unit(TurtleName="Chapter2YellowSlime2",
DisplayName="Yellow Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=8,#3, #Influences attack damage
DEF=1, #Influences damage taken from physical attacks
RES=8, #Influences damage taken from magic attacks
AGL=3, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=8,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=60, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Yellow Slime",
Attacks=[moves.Thunder],
Supports=[],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter2YellowSlime2.TurtleName = new_turtle()
Chapter2YellowSlime2.TurtleName.shape(Chapter2YellowSlime2.Sprite)
Chapter2YellowSlime2.TurtleName.hideturtle()

#Yellow Slime 3---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter2YellowSlime3 = Unit(TurtleName="Chapter2YellowSlime3",
DisplayName="Yellow Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=15,
CurrentHP=15,
ATK=9,#3, #Influences attack damage
DEF=2, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=3, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=8,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=75, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=1,
UnitClass="Yellow Slime",
Attacks=[moves.Slam],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter2YellowSlime3.TurtleName = new_turtle()
Chapter2YellowSlime3.TurtleName.shape(Chapter2YellowSlime3.Sprite)
Chapter2YellowSlime3.TurtleName.hideturtle()

#Blue Slime 1---------------
register_shape(current_directory+"/Sprites/blueslime_small.gif")
register_shape(current_directory+"/Portraits/blueslime_big.gif")
Chapter2BlueSlime1 = Unit(TurtleName="Chapter2BlueSlime1",
DisplayName="Blue Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=15,
CurrentHP=15,
ATK=8,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Blue Slime",
Attacks=[moves.Slam], #moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Water"],
Portrait=current_directory+"/Portraits/blueslime_big.gif",
Sprite=current_directory+"/Sprites/blueslime_small.gif",
LevelQuotes=["Blue Slime: bruh how do you lose in the first chapter"],
Bio="Blue Slimes are similar to Red Slimes, \n but have higher DEF and lower RES.")
Chapter2BlueSlime1.TurtleName = new_turtle()
Chapter2BlueSlime1.TurtleName.shape(Chapter2BlueSlime1.Sprite)
Chapter2BlueSlime1.TurtleName.hideturtle()

#Blue Slime 2---------------
register_shape(current_directory+"/Sprites/blueslime_small.gif")
register_shape(current_directory+"/Portraits/blueslime_big.gif")
Chapter2BlueSlime2 = Unit(TurtleName="Chapter2BlueSlime2",
DisplayName="Blue Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=15,
CurrentHP=15,
ATK=8,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Blue Slime",
Attacks=[moves.Slam], #moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Water"],
Portrait=current_directory+"/Portraits/blueslime_big.gif",
Sprite=current_directory+"/Sprites/blueslime_small.gif",
LevelQuotes=["Blue Slime: bruh how do you lose in the first chapter"],
Bio="Blue Slimes are similar to Red Slimes, \n but have higher DEF and lower RES.")
Chapter2BlueSlime2.TurtleName = new_turtle()
Chapter2BlueSlime2.TurtleName.shape(Chapter2BlueSlime2.Sprite)
Chapter2BlueSlime2.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 3]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Yellow Slime 1---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter3YellowSlime1 = Unit(TurtleName="Chapter3YellowSlime1",
DisplayName="Yellow Slime",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=8,#3, #Influences attack damage
DEF=1, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=60, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Yellow Slime",
Attacks=[moves.Thunder],
Supports=[],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter3YellowSlime1.TurtleName = new_turtle()
Chapter3YellowSlime1.TurtleName.shape(Chapter3YellowSlime1.Sprite)
Chapter3YellowSlime1.TurtleName.hideturtle()

#Yellow Slime 2---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter3YellowSlime2 = Unit(TurtleName="Chapter3YellowSlime2",
DisplayName="Yellow Slime",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=28,
CurrentHP=28,
ATK=7,#3, #Influences attack damage
DEF=1, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=60, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Yellow Slime",
Attacks=[moves.Thunder],
Supports=[],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter3YellowSlime2.TurtleName = new_turtle()
Chapter3YellowSlime2.TurtleName.shape(Chapter3YellowSlime2.Sprite)
Chapter3YellowSlime2.TurtleName.hideturtle()

#Yellow Slime 3---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter3YellowSlime3 = Unit(TurtleName="Chapter3YellowSlime3",
DisplayName="Yellow Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=23,
CurrentHP=23,
ATK=6,#3, #Influences attack damage
DEF=0, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=13,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=60, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Yellow Slime",
Attacks=[moves.Slam],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter3YellowSlime3.TurtleName = new_turtle()
Chapter3YellowSlime3.TurtleName.shape(Chapter3YellowSlime3.Sprite)
Chapter3YellowSlime3.TurtleName.hideturtle()

#Yellow Slime 4---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter3YellowSlime4 = Unit(TurtleName="Chapter3YellowSlime4",
DisplayName="Yellow Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=23,
CurrentHP=23,
ATK=6,#3, #Influences attack damage
DEF=0, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=13,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=60, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=2,
UnitClass="Yellow Slime",
Attacks=[moves.Slam],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter3YellowSlime4.TurtleName = new_turtle()
Chapter3YellowSlime4.TurtleName.shape(Chapter3YellowSlime4.Sprite)
Chapter3YellowSlime4.TurtleName.hideturtle()

#Yellow Slime 5---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter3YellowSlime5 = Unit(TurtleName="Chapter3YellowSlime5",
DisplayName="Yellow Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=3,#3, #Influences attack damage
DEF=0, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=1, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=5,
UnitClass="Yellow Slime",
Attacks=[moves.Slam],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter3YellowSlime5.TurtleName = new_turtle()
Chapter3YellowSlime5.TurtleName.shape(Chapter3YellowSlime5.Sprite)
Chapter3YellowSlime5.TurtleName.hideturtle()

#Blue Slime 1---------------
register_shape(current_directory+"/Sprites/blueslime_small.gif")
register_shape(current_directory+"/Portraits/blueslime_big.gif")
Chapter3BlueSlime1 = Unit(TurtleName="Chapter3BlueSlime1",
DisplayName="Blue Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=15,
CurrentHP=15,
ATK=9,#3, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=60, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Blue Slime",
Attacks=[moves.Slam], #moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Water"],
Portrait=current_directory+"/Portraits/blueslime_big.gif",
Sprite=current_directory+"/Sprites/blueslime_small.gif",
LevelQuotes=["Blue Slime: bruh how do you lose in the first chapter"],
Bio="Blue Slimes are similar to Red Slimes, \n but have higher DEF and lower RES.")
Chapter3BlueSlime1.TurtleName = new_turtle()
Chapter3BlueSlime1.TurtleName.shape(Chapter3BlueSlime1.Sprite)
Chapter3BlueSlime1.TurtleName.hideturtle()

#Blue Slime 2---------------
register_shape(current_directory+"/Sprites/blueslime_small.gif")
register_shape(current_directory+"/Portraits/blueslime_big.gif")
Chapter3BlueSlime2 = Unit(TurtleName="Chapter3BlueSlime2",
DisplayName="Blue Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=7,#3, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=60, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Blue Slime",
Attacks=[moves.Slam], #moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Water"],
Portrait=current_directory+"/Portraits/blueslime_big.gif",
Sprite=current_directory+"/Sprites/blueslime_small.gif",
LevelQuotes=["Blue Slime: bruh how do you lose in the first chapter"],
Bio="Blue Slimes are similar to Red Slimes, \n but have higher DEF and lower RES.")
Chapter3BlueSlime2.TurtleName = new_turtle()
Chapter3BlueSlime2.TurtleName.shape(Chapter3BlueSlime2.Sprite)
Chapter3BlueSlime2.TurtleName.hideturtle()

#Blue Slime 3---------------
register_shape(current_directory+"/Sprites/blueslime_small.gif")
register_shape(current_directory+"/Portraits/blueslime_big.gif")
Chapter3BlueSlime3 = Unit(TurtleName="Chapter3BlueSlime3",
DisplayName="Blue Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=8,#3, #Influences attack damage
DEF=29, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=12,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=5,
UnitClass="Blue Slime",
Attacks=[moves.Slam], #moves.Slam],
Supports=[],
Traits=["Physical Primary", "Monster","Water"],
Portrait=current_directory+"/Portraits/blueslime_big.gif",
Sprite=current_directory+"/Sprites/blueslime_small.gif",
LevelQuotes=["Blue Slime: bruh how do you lose in the first chapter"],
Bio="Blue Slimes are similar to Red Slimes, \n but have higher DEF and lower RES.")
Chapter3BlueSlime3.TurtleName = new_turtle()
Chapter3BlueSlime3.TurtleName.shape(Chapter3BlueSlime3.Sprite)
Chapter3BlueSlime3.TurtleName.hideturtle()

#Red Slime 1---------------
register_shape(current_directory+"/Sprites/redslime_small.gif")
register_shape(current_directory+"/Portraits/redslime_big.gif")
Chapter3RedSlime1 = Unit(TurtleName="Chapter3RedSlime1",
DisplayName="Red Slime",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=5,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=1, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=7,
UnitClass="Red Slime",
Attacks=[moves.Slam,moves.Fireball],
Supports=[],
Traits=["Physical Primary", "Monster","Fire"],
Portrait=current_directory+"/Portraits/redslime_big.gif",
Sprite=current_directory+"/Sprites/redslime_small.gif",
LevelQuotes=["Red Slime: *slime sounds*"],
Bio="Red Slimes are basic monsters that \n can be found throughout the Bipolian continent.")
Chapter3RedSlime1.TurtleName = new_turtle()
Chapter3RedSlime1.TurtleName.shape(Chapter3RedSlime1.Sprite)
Chapter3RedSlime1.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 4]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Retool---------------
register_shape(current_directory+"/Sprites/retool_small.gif")
register_shape(current_directory+"/Portraits/retool_big.gif")
Retool = Unit(TurtleName="RetoolTurtle",
DisplayName="Retool",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=9, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=13,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Guild Leader",
Attacks=[moves.Slice,moves.Thorn],
Supports=[],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/retool_big.gif",
Sprite=current_directory+"/Sprites/retool_small.gif",
LevelQuotes=["Retool: Bow down to me, fools!"],
Bio="Retool is the leader of the Guild\n of Retool, a guild of bandits that has\nrecently gained power after looting the Castle of Quad.")
Retool.TurtleName = new_turtle()
Retool.TurtleName.shape(Retool.Sprite)
Retool.TurtleName.hideturtle()

#Fighter1---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter4Fighter1 = Unit(TurtleName="Chapter4Fighter1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=12,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=7, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=5,
UnitClass="Swordfighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Fire","Guild of Retool"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Fighter1.TurtleName = new_turtle()
Chapter4Fighter1.TurtleName.shape(Chapter4Fighter1.Sprite)
Chapter4Fighter1.TurtleName.hideturtle()

#Fighter2---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter4Fighter2 = Unit(TurtleName="Chapter4Fighter2",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=12,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=7, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=5,
UnitClass="Swordfighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Electric","Guild of Retool"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Fighter2.TurtleName = new_turtle()
Chapter4Fighter2.TurtleName.shape(Chapter4Fighter2.Sprite)
Chapter4Fighter2.TurtleName.hideturtle()

#Fighter3---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter4Fighter3 = Unit(TurtleName="Chapter4Fighter3",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=10,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=11,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=7,
UnitClass="Swordfighter",
Attacks=[moves.Slice,moves.Freeze],
Supports=[],
Traits=["Physical Primary", "Ice","Guild of Retool"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Fighter3.TurtleName = new_turtle()
Chapter4Fighter3.TurtleName.shape(Chapter4Fighter3.Sprite)
Chapter4Fighter3.TurtleName.hideturtle()

#Archer1---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter4Archer1 = Unit(TurtleName="Chapter4Archer1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=2, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=6,
UnitClass="Archer",
Attacks=[moves.Bow],
Supports=[],
Traits=["Physical Primary", "Shadow","Guild of Retool"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Archer1.TurtleName = new_turtle()
Chapter4Archer1.TurtleName.shape(Chapter4Archer1.Sprite)
Chapter4Archer1.TurtleName.hideturtle()

#Archer2---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter4Archer2 = Unit(TurtleName="Chapter4Archer2",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=2, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=6,
UnitClass="Archer",
Attacks=[moves.Bow],
Supports=[],
Traits=["Physical Primary", "Fire","Guild of Retool"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Archer2.TurtleName = new_turtle()
Chapter4Archer2.TurtleName.shape(Chapter4Archer2.Sprite)
Chapter4Archer2.TurtleName.hideturtle()

#Archer3---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter4Archer3 = Unit(TurtleName="Chapter4Archer3",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=18,
CurrentHP=18,
ATK=16,#3, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=1, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=7,
UnitClass="Archer",
Attacks=[moves.Bow,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water","Guild of Retool"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Archer3.TurtleName = new_turtle()
Chapter4Archer3.TurtleName.shape(Chapter4Archer3.Sprite)
Chapter4Archer3.TurtleName.hideturtle()

#Archer4---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter4Archer4 = Unit(TurtleName="Chapter4Archer4",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=18,
CurrentHP=18,
ATK=16,#3, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=1, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=7,
UnitClass="Archer",
Attacks=[moves.Bow,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Ice","Guild of Retool"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Archer4.TurtleName = new_turtle()
Chapter4Archer4.TurtleName.shape(Chapter4Archer4.Sprite)
Chapter4Archer4.TurtleName.hideturtle()

#Archer5---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter4Archer5 = Unit(TurtleName="Chapter4Archer5",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=18,
CurrentHP=18,
ATK=16,#3, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=1, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=7,
UnitClass="Archer",
Attacks=[moves.Bow,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Electric","Guild of Retool"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Archer5.TurtleName = new_turtle()
Chapter4Archer5.TurtleName.shape(Chapter4Archer5.Sprite)
Chapter4Archer5.TurtleName.hideturtle()

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter4Armored1 = Unit(TurtleName="Chapter4Armored1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=16,#3, #Influences attack damage
DEF=23, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=3, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=70, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=5,
UnitClass="Armored",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Shadow","Guild of Retool","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Armored1.TurtleName = new_turtle()
Chapter4Armored1.TurtleName.shape(Chapter4Armored1.Sprite)
Chapter4Armored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter4Armored2 = Unit(TurtleName="Chapter4Armored2",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=16,#3, #Influences attack damage
DEF=23, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=3, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=70, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=5,
UnitClass="Armored",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Shadow","Guild of Retool","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You won't be stopping us."],
Bio="A bandit that is part of the Guild of Retool.")
Chapter4Armored2.TurtleName = new_turtle()
Chapter4Armored2.TurtleName.shape(Chapter4Armored2.Sprite)
Chapter4Armored2.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 5]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Archer1---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter5Archer1 = Unit(TurtleName="Chapter5Archer1",
DisplayName="Bandit",
AttackRange=["Infinite"],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=4,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=7,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=10,
UnitClass="Sniper",
Attacks=[moves.Dagger,moves.Bow,moves.Snipe],
Supports=[moves.MedKit],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Archer1.TurtleName = new_turtle()
Chapter5Archer1.TurtleName.shape(Chapter5Archer1.Sprite)
Chapter5Archer1.TurtleName.hideturtle()

#Archer2---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter5Archer2 = Unit(TurtleName="Chapter5Archer2",
DisplayName="Bandit",
AttackRange=["Infinite"],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=12,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=7, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=5,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Archer",
Attacks=[moves.Dagger,moves.Bow,moves.LongBow],
Supports=[moves.MedKit],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Archer2.TurtleName = new_turtle()
Chapter5Archer2.TurtleName.shape(Chapter5Archer2.Sprite)
Chapter5Archer2.TurtleName.hideturtle()

#Archer3---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter5Archer3 = Unit(TurtleName="Chapter5Archer3",
DisplayName="Bandit",
AttackRange=["Infinite"],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=12,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=7, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=5,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Archer",
Attacks=[moves.Dagger,moves.Bow,moves.LongBow],
Supports=[moves.MedKit],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Archer3.TurtleName = new_turtle()
Chapter5Archer3.TurtleName.shape(Chapter5Archer3.Sprite)
Chapter5Archer3.TurtleName.hideturtle()

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter5Armored1 = Unit(TurtleName="Chapter5Armored1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=55,
CurrentHP=55,
ATK=35,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Armored",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Electric","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Armored1.TurtleName = new_turtle()
Chapter5Armored1.TurtleName.shape(Chapter5Armored1.Sprite)
Chapter5Armored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter5Armored2 = Unit(TurtleName="Chapter5Armored2",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=55,
CurrentHP=55,
ATK=35,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Armored",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Bio","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Armored2.TurtleName = new_turtle()
Chapter5Armored2.TurtleName.shape(Chapter5Armored2.Sprite)
Chapter5Armored2.TurtleName.hideturtle()

#Armored3---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter5Armored3 = Unit(TurtleName="Chapter5Armored3",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=55,
CurrentHP=55,
ATK=35,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Armored",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Shadow","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Armored3.TurtleName = new_turtle()
Chapter5Armored3.TurtleName.shape(Chapter5Armored3.Sprite)
Chapter5Armored3.TurtleName.hideturtle()

#Armored4---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter5Armored4 = Unit(TurtleName="Chapter5Armored4",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=55,
CurrentHP=55,
ATK=35,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Armored",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Fire","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Armored4.TurtleName = new_turtle()
Chapter5Armored4.TurtleName.shape(Chapter5Armored4.Sprite)
Chapter5Armored4.TurtleName.hideturtle()

#Armored5---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter5Armored5 = Unit(TurtleName="Chapter5Armored5",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=55,
CurrentHP=55,
ATK=35,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=10,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=8,
UnitClass="Armored",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Armored5.TurtleName = new_turtle()
Chapter5Armored5.TurtleName.shape(Chapter5Armored5.Sprite)
Chapter5Armored5.TurtleName.hideturtle()

#Fighter1---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter5Fighter1 = Unit(TurtleName="Chapter5Fighter1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=25,
CurrentHP=25,
ATK=20,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=12, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=7,
SPD=8, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=10,
UnitClass="Swordfighter",
Attacks=[moves.Dagger],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter5Fighter1.TurtleName = new_turtle()
Chapter5Fighter1.TurtleName.shape(Chapter5Fighter1.Sprite)
Chapter5Fighter1.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 6]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Fighter1---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter6Fighter1 = Unit(TurtleName="Chapter6Fighter1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=10,#3, #Influences attack damage
DEF=18, #Influences damage taken from physical attacks
RES=14, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=70, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=10,
UnitClass="Swordfighter",
Attacks=[moves.ArmorBreak, moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter6Fighter1.TurtleName = new_turtle()
Chapter6Fighter1.TurtleName.shape(Chapter6Fighter1.Sprite)
Chapter6Fighter1.TurtleName.hideturtle()

#Fighter2---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter6Fighter2 = Unit(TurtleName="Chapter6Fighter2",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=40,
CurrentHP=40,
ATK=10,#3, #Influences attack damage
DEF=14, #Influences damage taken from physical attacks
RES=18, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=70, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=10,
UnitClass="Elemental Fighter",
Attacks=[moves.Thorn,moves.Cut],
Supports=[],
Traits=["Magic Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter6Fighter2.TurtleName = new_turtle()
Chapter6Fighter2.TurtleName.shape(Chapter6Fighter2.Sprite)
Chapter6Fighter2.TurtleName.hideturtle()

#Fighter3---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter6Fighter3 = Unit(TurtleName="Chapter6Fighter3",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=45,
CurrentHP=45,
ATK=10,#3, #Influences attack damage
DEF=16, #Influences damage taken from physical attacks
RES=16, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=18,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=85, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Elemental Fighter",
Attacks=[moves.Aqua,moves.Slice],
Supports=[],
Traits=["Magic Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter6Fighter3.TurtleName = new_turtle()
Chapter6Fighter3.TurtleName.shape(Chapter6Fighter3.Sprite)
Chapter6Fighter3.TurtleName.hideturtle()

#Fighter4---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter6Fighter4 = Unit(TurtleName="Chapter6Fighter4",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=12,#3, #Influences attack damage
DEF=18, #Influences damage taken from physical attacks
RES=12, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=19,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Swordfighter",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter6Fighter4.TurtleName = new_turtle()
Chapter6Fighter4.TurtleName.shape(Chapter6Fighter4.Sprite)
Chapter6Fighter4.TurtleName.hideturtle()

#Fighter5---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter6Fighter5 = Unit(TurtleName="Chapter6Fighter5",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=55,
CurrentHP=55,
ATK=12,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=14, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=19,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Swordfighter",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter6Fighter5.TurtleName = new_turtle()
Chapter6Fighter5.TurtleName.shape(Chapter6Fighter5.Sprite)
Chapter6Fighter5.TurtleName.hideturtle()

#Fighter6---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter6Fighter6 = Unit(TurtleName="Chapter6Fighter6",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=90,
CurrentHP=90,
ATK=12,#3, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=27, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Elemental Fighter",
Attacks=[moves.Thunder],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter6Fighter6.TurtleName = new_turtle()
Chapter6Fighter6.TurtleName.shape(Chapter6Fighter6.Sprite)
Chapter6Fighter6.TurtleName.hideturtle()

#Archer1---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter6Archer1 = Unit(TurtleName="Chapter6Archer1",
DisplayName="Bandit",
AttackRange=["Infinite"],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Sniper",
Attacks=[moves.Snipe],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter6Archer1.TurtleName = new_turtle()
Chapter6Archer1.TurtleName.shape(Chapter6Archer1.Sprite)
Chapter6Archer1.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 7]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter7Armored1 = Unit(TurtleName="Chapter7Armored1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Fire","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Armored1.TurtleName = new_turtle()
Chapter7Armored1.TurtleName.shape(Chapter7Armored1.Sprite)
Chapter7Armored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter7Armored2 = Unit(TurtleName="Chapter7Armored2",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Armored2.TurtleName = new_turtle()
Chapter7Armored2.TurtleName.shape(Chapter7Armored2.Sprite)
Chapter7Armored2.TurtleName.hideturtle()

#Armored3---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter7Armored3 = Unit(TurtleName="Chapter7Armored3",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Ice","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Armored3.TurtleName = new_turtle()
Chapter7Armored3.TurtleName.shape(Chapter7Armored3.Sprite)
Chapter7Armored3.TurtleName.hideturtle()

#Armored4---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter7Armored4 = Unit(TurtleName="Chapter7Armored4",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Bio","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Armored4.TurtleName = new_turtle()
Chapter7Armored4.TurtleName.shape(Chapter7Armored4.Sprite)
Chapter7Armored4.TurtleName.hideturtle()

#Armored5---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter7Armored5 = Unit(TurtleName="Chapter7Armored5",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Electric","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Armored5.TurtleName = new_turtle()
Chapter7Armored5.TurtleName.shape(Chapter7Armored5.Sprite)
Chapter7Armored5.TurtleName.hideturtle()

#Armored6---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter7Armored6 = Unit(TurtleName="Chapter7Armored6",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Shadow","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Armored6.TurtleName = new_turtle()
Chapter7Armored6.TurtleName.shape(Chapter7Armored6.Sprite)
Chapter7Armored6.TurtleName.hideturtle()

#Armored7---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter7Armored7 = Unit(TurtleName="Chapter7Armored7",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Electric","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Armored7.TurtleName = new_turtle()
Chapter7Armored7.TurtleName.shape(Chapter7Armored7.Sprite)
Chapter7Armored7.TurtleName.hideturtle()

#Armored8---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter7Armored8 = Unit(TurtleName="Chapter7Armored8",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=13,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Shadow","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Armored8.TurtleName = new_turtle()
Chapter7Armored8.TurtleName.shape(Chapter7Armored8.Sprite)
Chapter7Armored8.TurtleName.hideturtle()

#Archer1---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter7Archer1 = Unit(TurtleName="Chapter7Archer1",
DisplayName="Bandit",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=12,#3, #Influences attack damage
DEF=17, #Influences damage taken from physical attacks
RES=13, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Archer",
Attacks=[moves.HeavyBow,moves.BowPlus],
Supports=[moves.MedKit],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Archer1.TurtleName = new_turtle()
Chapter7Archer1.TurtleName.shape(Chapter7Archer1.Sprite)
Chapter7Archer1.TurtleName.hideturtle()

#Archer2---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter7Archer2 = Unit(TurtleName="Chapter7Archer2",
DisplayName="Bandit",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=12,#3, #Influences attack damage
DEF=17, #Influences damage taken from physical attacks
RES=13, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Archer",
Attacks=[moves.HeavyBow,moves.BowPlus],
Supports=[moves.MedKit],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Archer2.TurtleName = new_turtle()
Chapter7Archer2.TurtleName.shape(Chapter7Archer2.Sprite)
Chapter7Archer2.TurtleName.hideturtle()

#Archer3---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter7Archer3 = Unit(TurtleName="Chapter7Archer3",
DisplayName="Bandit",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=13,#3, #Influences attack damage
DEF=18, #Influences damage taken from physical attacks
RES=13, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=47,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Sniper",
Attacks=[moves.HeavyBow,moves.Snipe],
Supports=[moves.MedKit],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter7Archer3.TurtleName = new_turtle()
Chapter7Archer3.TurtleName.shape(Chapter7Archer3.Sprite)
Chapter7Archer3.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 8]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Bladeous---------------
register_shape(current_directory+"/Sprites/Bladeous_small.gif")
register_shape(current_directory+"/Portraits/Bladeous_big.gif")
BladeousBoss = Unit(TurtleName="BladeousBossTurtle",
DisplayName="Bladeous",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=250,
CurrentHP=250,
ATK=15,#3, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=250, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="Elemental Warrior",
Attacks=[moves.DarkOrb,moves.ShadowBlade],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/Bladeous_big.gif",
Sprite=current_directory+"/Sprites/Bladeous_small.gif",
LevelQuotes=["Bladeous: ..."],
Bio="A person possesed by the power\nof the Itucher.")
BladeousBoss.TurtleName = new_turtle()
BladeousBoss.TurtleName.shape(BladeousBoss.Sprite)
BladeousBoss.TurtleName.hideturtle()

#Yellow Slime 1---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter8YellowSlime1 = Unit(TurtleName="Chapter8YellowSlime1",
DisplayName="Yellow Slime",
AttackRange=[],
PrimaryType="Magic",
MaxHP=42,
CurrentHP=42,
ATK=185,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Yellow Slime",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter8YellowSlime1.TurtleName = new_turtle()
Chapter8YellowSlime1.TurtleName.shape(Chapter8YellowSlime1.Sprite)
Chapter8YellowSlime1.TurtleName.hideturtle()

#Yellow Slime 2---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter8YellowSlime2 = Unit(TurtleName="Chapter8YellowSlime2",
DisplayName="Yellow Slime",
AttackRange=[],
PrimaryType="Magic",
MaxHP=42,
CurrentHP=42,
ATK=185,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Yellow Slime",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter8YellowSlime2.TurtleName = new_turtle()
Chapter8YellowSlime2.TurtleName.shape(Chapter8YellowSlime2.Sprite)
Chapter8YellowSlime2.TurtleName.hideturtle()

#Yellow Slime 3---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter8YellowSlime3 = Unit(TurtleName="Chapter8YellowSlime3",
DisplayName="Yellow Slime",
AttackRange=[],
PrimaryType="Magic",
MaxHP=42,
CurrentHP=42,
ATK=185,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Yellow Slime",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter8YellowSlime3.TurtleName = new_turtle()
Chapter8YellowSlime3.TurtleName.shape(Chapter8YellowSlime3.Sprite)
Chapter8YellowSlime3.TurtleName.hideturtle()

#Yellow Slime 4---------------
register_shape(current_directory+"/Sprites/yellowslime_small.gif")
register_shape(current_directory+"/Portraits/yellowslime_big.gif")
Chapter8YellowSlime4 = Unit(TurtleName="Chapter8YellowSlime4",
DisplayName="Yellow Slime",
AttackRange=[],
PrimaryType="Magic",
MaxHP=42,
CurrentHP=42,
ATK=185,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Yellow Slime",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Monster","Electric"],
Portrait=current_directory+"/Portraits/yellowslime_big.gif",
Sprite=current_directory+"/Sprites/yellowslime_small.gif",
LevelQuotes=["Yellow Slime: *slime sounds*"],
Bio="Yellow Slimes are similar to Red Slimes, \n but have higher RES, lower DEF, and focus more on magic.")
Chapter8YellowSlime4.TurtleName = new_turtle()
Chapter8YellowSlime4.TurtleName.shape(Chapter8YellowSlime4.Sprite)
Chapter8YellowSlime4.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 9a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Fighter1---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter9aFighter1 = Unit(TurtleName="Chapter9aFighter1",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=50,
CurrentHP=50,
ATK=6,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Elemental Fighter",
Attacks=[moves.Thunder],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Magic Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter9aFighter1.TurtleName = new_turtle()
Chapter9aFighter1.TurtleName.shape(Chapter9aFighter1.Sprite)
Chapter9aFighter1.TurtleName.hideturtle()

#Fighter2---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter9aFighter2 = Unit(TurtleName="Chapter9aFighter2",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=50,
CurrentHP=50,
ATK=6,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Elemental Fighter",
Attacks=[moves.Fireball],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Magic Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter9aFighter2.TurtleName = new_turtle()
Chapter9aFighter2.TurtleName.shape(Chapter9aFighter2.Sprite)
Chapter9aFighter2.TurtleName.hideturtle()

#Fighter3---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter9aFighter3 = Unit(TurtleName="Chapter9aFighter3",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=50,
CurrentHP=50,
ATK=6,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Elemental Fighter",
Attacks=[moves.Aqua],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Magic Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter9aFighter3.TurtleName = new_turtle()
Chapter9aFighter3.TurtleName.shape(Chapter9aFighter3.Sprite)
Chapter9aFighter3.TurtleName.hideturtle()

#Fighter4---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter9aFighter4 = Unit(TurtleName="Chapter9aFighter4",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=50,
CurrentHP=50,
ATK=6,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Elemental Fighter",
Attacks=[moves.DarkOrb],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Magic Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter9aFighter4.TurtleName = new_turtle()
Chapter9aFighter4.TurtleName.shape(Chapter9aFighter4.Sprite)
Chapter9aFighter4.TurtleName.hideturtle()

#Fighter5---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter9aFighter5 = Unit(TurtleName="Chapter9aFighter5",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=50,
CurrentHP=50,
ATK=6,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Elemental Fighter",
Attacks=[moves.Thorn],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Magic Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter9aFighter5.TurtleName = new_turtle()
Chapter9aFighter5.TurtleName.shape(Chapter9aFighter5.Sprite)
Chapter9aFighter5.TurtleName.hideturtle()

#Fighter6---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter9aFighter6 = Unit(TurtleName="Chapter9aFighter6",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=50,
CurrentHP=50,
ATK=6,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Elemental Fighter",
Attacks=[moves.Freeze],
Supports=[moves.Heal,moves.LongHeal],
Traits=["Magic Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter9aFighter6.TurtleName = new_turtle()
Chapter9aFighter6.TurtleName.shape(Chapter9aFighter6.Sprite)
Chapter9aFighter6.TurtleName.hideturtle()

#Fighter7---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter9aFighter7 = Unit(TurtleName="Chapter9aFighter7",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Magic",
MaxHP=60,
CurrentHP=60,
ATK=8,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=85, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="Elemental Fighter",
Attacks=[moves.ThunderBlast],
Supports=[moves.MedKit],
Traits=["Magic Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Cos.")
Chapter9aFighter7.TurtleName = new_turtle()
Chapter9aFighter7.TurtleName.shape(Chapter9aFighter7.Sprite)
Chapter9aFighter7.TurtleName.hideturtle()


#==============================================================================================================================================================================================================================================================================
#===============[Chapter 9b]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter9bArmored1 = Unit(TurtleName="Chapter9bArmored1",
DisplayName="Wallimos Vessel",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=35,#3, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=420,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Shadow","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Wallimos Vessel: ..."],
Bio="A husk of armor controlled by\nthe powers of Wallimos Alexander.")
Chapter9bArmored1.TurtleName = new_turtle()
Chapter9bArmored1.TurtleName.shape(Chapter9bArmored1.Sprite)
Chapter9bArmored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter9bArmored2 = Unit(TurtleName="Chapter9bArmored2",
DisplayName="Wallimos Vessel",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=35,#3, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=420,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Shadow","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Wallimos Vessel: ..."],
Bio="A husk of armor controlled by\nthe powers of Wallimos Alexander.")
Chapter9bArmored2.TurtleName = new_turtle()
Chapter9bArmored2.TurtleName.shape(Chapter9bArmored2.Sprite)
Chapter9bArmored2.TurtleName.hideturtle()

#Armored3---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter9bArmored3 = Unit(TurtleName="Chapter9bArmored3",
DisplayName="Wallimos Vessel",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=35,#3, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=420,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=18,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Shadow","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Wallimos Vessel: ..."],
Bio="A husk of armor controlled by\nthe powers of Wallimos Alexander.")
Chapter9bArmored3.TurtleName = new_turtle()
Chapter9bArmored3.TurtleName.shape(Chapter9bArmored3.Sprite)
Chapter9bArmored3.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 10a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Fighter1---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter10aFighter1 = Unit(TurtleName="Chapter10aFighter1",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=63, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=23,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Elemental Fighter",
Attacks=[moves.Slice],
Supports=[moves.Heal,moves.LongHeal,moves.FarHeal],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter10aFighter1.TurtleName = new_turtle()
Chapter10aFighter1.TurtleName.shape(Chapter10aFighter1.Sprite)
Chapter10aFighter1.TurtleName.hideturtle()

#Fighter2---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter10aFighter2 = Unit(TurtleName="Chapter10aFighter2",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=63, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=23,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Elemental Fighter",
Attacks=[moves.Slice],
Supports=[moves.Heal,moves.LongHeal,moves.FarHeal],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter10aFighter2.TurtleName = new_turtle()
Chapter10aFighter2.TurtleName.shape(Chapter10aFighter2.Sprite)
Chapter10aFighter2.TurtleName.hideturtle()

#Fighter3---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter10aFighter3 = Unit(TurtleName="Chapter10aFighter3",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=63, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=23,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Elemental Fighter",
Attacks=[moves.Slice],
Supports=[moves.Heal,moves.LongHeal,moves.FarHeal],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter10aFighter3.TurtleName = new_turtle()
Chapter10aFighter3.TurtleName.shape(Chapter10aFighter3.Sprite)
Chapter10aFighter3.TurtleName.hideturtle()

#Fighter4---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter10aFighter4 = Unit(TurtleName="Chapter10aFighter4",
DisplayName="Bandit",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=63, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=23,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Elemental Fighter",
Attacks=[moves.Slice],
Supports=[moves.Heal,moves.LongHeal,moves.FarHeal],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in Static.")
Chapter10aFighter4.TurtleName = new_turtle()
Chapter10aFighter4.TurtleName.shape(Chapter10aFighter4.Sprite)
Chapter10aFighter4.TurtleName.hideturtle()


#==============================================================================================================================================================================================================================================================================
#===============[Chapter 10b]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter10bArmored1 = Unit(TurtleName="Chapter10bArmored1",
DisplayName="Wallimos Vessel",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=125,
CurrentHP=125,
ATK=35,#3, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=7031,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Electric","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Wallimos Vessel: ..."],
Bio="A husk of armor controlled by\nthe powers of Wallimos Alexander.")
Chapter10bArmored1.TurtleName = new_turtle()
Chapter10bArmored1.TurtleName.shape(Chapter10bArmored1.Sprite)
Chapter10bArmored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter10bArmored2 = Unit(TurtleName="Chapter10bArmored2",
DisplayName="Wallimos Vessel",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=125,
CurrentHP=125,
ATK=35,#3, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=7031,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=20,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Electric","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Wallimos Vessel: ..."],
Bio="A husk of armor controlled by\nthe powers of Wallimos Alexander.")
Chapter10bArmored2.TurtleName = new_turtle()
Chapter10bArmored2.TurtleName.shape(Chapter10bArmored2.Sprite)
Chapter10bArmored2.TurtleName.hideturtle()

#Wallimos---------------
register_shape(current_directory+"/Sprites/wallimos_small.gif")
register_shape(current_directory+"/Portraits/wallimos_big.gif")
Wallimos = Unit(TurtleName="WallimosTurtle",
DisplayName="Wallimos",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=500,
CurrentHP=500,
ATK=25,#3, #Influences attack damage
DEF=18, #Influences damage taken from physical attacks
RES=73, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=85,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=350, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Dimensional",
Attacks=[moves.ShadowPunch],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/wallimos_big.gif",
Sprite=current_directory+"/Sprites/wallimos_small.gif",
LevelQuotes=["Wallimos: Fear me, mortals."],
Bio="Wallimos Alexander is a Dimensional Entity\nthat fought with Bobbish Razz centuries ago.\nHe now reawakens, wanting to rule the world.")
Wallimos.TurtleName = new_turtle()
Wallimos.TurtleName.shape(Wallimos.Sprite)
Wallimos.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 10c]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#FaelBoss---------------
register_shape(current_directory+"/Sprites/fael_small.gif")
register_shape(current_directory+"/Portraits/fael_big.gif")
FaelBoss = Unit(TurtleName="FaelBoss",
DisplayName="Fael",
AttackRange=[2],
PrimaryType="Physical",
MaxHP=23,
CurrentHP=23,
ATK=14, #Influences attack damage
DEF=9, #Influences damage taken from physical attacks
RES=9, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=350, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Archer",
Attacks=[moves.VineBow],
Supports=[],
Traits=["Physical Primary","Bipolian","Archer","Bio"],
HPGrowth=[80,1], #Chance to level up, max amount to increase
ATKGrowth=[80,1],
DEFGrowth=[60,1],
RESGrowth=[60,1],
AGLGrowth=[70,1],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/fael_big.gif",
Sprite=current_directory+"/Sprites/fael_small.gif",
LevelQuotes=["Fael: I did it.","Fael: This is helpful.","Fael: Just as planned."],
Bio="Fael is a memeber of the Elemental Offense Squad.",
ClassChange=[["Elemental Sniper", 30]], #[Name, Level]
AttackUnlocks=[[moves.LongBow,17],[moves.DistanceShot,23],[moves.Snipe,30]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,20],[moves.Heal,25]])
FaelBoss.TurtleName = new_turtle()
FaelBoss.TurtleName.shape(FaelBoss.Sprite)
FaelBoss.TurtleName.hideturtle()

#ErifBoss---------------
register_shape(current_directory+"/Sprites/erif_small.gif")
register_shape(current_directory+"/Portraits/erif_big.gif")
ErifBoss = Unit(TurtleName="ErifBoss",
DisplayName="Erif",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=21, #Influences attack damage
DEF=16, #Influences damage taken from physical attacks
RES=11, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=350, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Elemental Fighter",
Attacks=[moves.FlameBlade],
Supports=[],
Traits=["Physical Primary","Bipolian","Fighter","Fire"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[50,1],
RESGrowth=[50,1],
AGLGrowth=[40,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/erif_big.gif",
Sprite=current_directory+"/Sprites/erif_small.gif",
LevelQuotes=["Erif: This will help.","Erif: Good.","Erif: I need to get stronger."],
Bio="Erif is a memeber of the Elemental Offense Squad.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[[moves.Slash,17],[moves.Fireball,25],[moves.FireBlast,30]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,20]])
ErifBoss.TurtleName = new_turtle()
ErifBoss.TurtleName.shape(ErifBoss.Sprite)
ErifBoss.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 11a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#WaterSpirit1---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter11aWaterSpirit1 = Unit(TurtleName="WaterSpirit1",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter11aWaterSpirit1.TurtleName = new_turtle()
Chapter11aWaterSpirit1.TurtleName.shape(Chapter11aWaterSpirit1.Sprite)
Chapter11aWaterSpirit1.TurtleName.hideturtle()

#WaterSpirit2---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter11aWaterSpirit2 = Unit(TurtleName="WaterSpirit2",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter11aWaterSpirit2.TurtleName = new_turtle()
Chapter11aWaterSpirit2.TurtleName.shape(Chapter11aWaterSpirit2.Sprite)
Chapter11aWaterSpirit2.TurtleName.hideturtle()

#WaterSpirit3---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter11aWaterSpirit3 = Unit(TurtleName="WaterSpirit3",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter11aWaterSpirit3.TurtleName = new_turtle()
Chapter11aWaterSpirit3.TurtleName.shape(Chapter11aWaterSpirit3.Sprite)
Chapter11aWaterSpirit3.TurtleName.hideturtle()

#WaterSpirit4---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter11aWaterSpirit4 = Unit(TurtleName="WaterSpirit4",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter11aWaterSpirit4.TurtleName = new_turtle()
Chapter11aWaterSpirit4.TurtleName.shape(Chapter11aWaterSpirit4.Sprite)
Chapter11aWaterSpirit4.TurtleName.hideturtle()

#WaterSpirit5---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter11aWaterSpirit5 = Unit(TurtleName="WaterSpirit5",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter11aWaterSpirit5.TurtleName = new_turtle()
Chapter11aWaterSpirit5.TurtleName.shape(Chapter11aWaterSpirit5.Sprite)
Chapter11aWaterSpirit5.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 12a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#WaterSpirit1---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter12aWaterSpirit1 = Unit(TurtleName="Chapter12aWaterSpirit1",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=15, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=9999, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter12aWaterSpirit1.TurtleName = new_turtle()
Chapter12aWaterSpirit1.TurtleName.shape(Chapter12aWaterSpirit1.Sprite)
Chapter12aWaterSpirit1.TurtleName.hideturtle()

#WaterSpirit2---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter12aWaterSpirit2 = Unit(TurtleName="Chapter12aWaterSpirit2",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=15, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=9999, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter12aWaterSpirit2.TurtleName = new_turtle()
Chapter12aWaterSpirit2.TurtleName.shape(Chapter12aWaterSpirit2.Sprite)
Chapter12aWaterSpirit2.TurtleName.hideturtle()

#WaterSpirit3---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter12aWaterSpirit3 = Unit(TurtleName="Chapter12aWaterSpirit3",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=15, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=9999, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter12aWaterSpirit3.TurtleName = new_turtle()
Chapter12aWaterSpirit3.TurtleName.shape(Chapter12aWaterSpirit3.Sprite)
Chapter12aWaterSpirit3.TurtleName.hideturtle()

#WaterSpirit4---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter12aWaterSpirit4 = Unit(TurtleName="Chapter12aWaterSpirit4",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=15, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=9999, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter12aWaterSpirit4.TurtleName = new_turtle()
Chapter12aWaterSpirit4.TurtleName.shape(Chapter12aWaterSpirit4.Sprite)
Chapter12aWaterSpirit4.TurtleName.hideturtle()

#WaterSpirit4---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter12aWaterSpirit5 = Unit(TurtleName="Chapter12aWaterSpirit5",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=15, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=9999, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter12aWaterSpirit5.TurtleName = new_turtle()
Chapter12aWaterSpirit5.TurtleName.shape(Chapter12aWaterSpirit5.Sprite)
Chapter12aWaterSpirit5.TurtleName.hideturtle()

#WaterSpirit6---------------
register_shape(current_directory+"/Sprites/waterspirit_small.gif")
register_shape(current_directory+"/Portraits/waterspirit_big.gif")
Chapter12aWaterSpirit6 = Unit(TurtleName="Chapter12aWaterSpirit6",
DisplayName="Water Spirit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=15, #Influences attack damage
DEF=12, #Influences damage taken from physical attacks
RES=9999, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=16,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=17,
UnitClass="Water Spirit",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Monster","Water"],
Portrait=current_directory+"/Portraits/waterspirit_big.gif",
Sprite=current_directory+"/Sprites/waterspirit_small.gif",
LevelQuotes=["Water Sprit: *water sounds*"],
Bio="A water spirit in the Bipole Sea.",
ClassChange=[["Elemental Warrior", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
Chapter12aWaterSpirit6.TurtleName = new_turtle()
Chapter12aWaterSpirit6.TurtleName.shape(Chapter12aWaterSpirit6.Sprite)
Chapter12aWaterSpirit6.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 13a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#DiverNeville---------------
register_shape(current_directory+"/Sprites/diverneville_small.gif")
register_shape(current_directory+"/Portraits/diverneville_big.gif")
DiverNeville = Unit(TurtleName="DiverNeville",
DisplayName="Diver Neville",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=9, #Influences attack damage
DEF=21, #Influences damage taken from physical attacks
RES=150, #Influences damage taken from magic attacks
AGL=3, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Diver",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary","Nolavillian","Water","Armored"],
Portrait=current_directory+"/Portraits/diverneville_big.gif",
Sprite=current_directory+"/Sprites/diverneville_small.gif",
LevelQuotes=["Diver Neville: Yo poggers in the chat."],
Bio="The top diver of the K'Neville pirates. He can dive\ndepths of over 420 meters in seconds, and can survive over\n9000 meters of pressure.",
ClassChange=[["Diver", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
DiverNeville.TurtleName = new_turtle()
DiverNeville.TurtleName.shape(DiverNeville.Sprite)
DiverNeville.TurtleName.hideturtle()

#Fighter1---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter13aFighter1 = Unit(TurtleName="Chapter13aFighter1",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=65,
CurrentHP=65,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=783, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Fighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter13aFighter1.TurtleName = new_turtle()
Chapter13aFighter1.TurtleName.shape(Chapter13aFighter1.Sprite)
Chapter13aFighter1.TurtleName.hideturtle()

#Fighter2---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter13aFighter2 = Unit(TurtleName="Chapter13aFighter2",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=65,
CurrentHP=65,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=783, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Fighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter13aFighter2.TurtleName = new_turtle()
Chapter13aFighter2.TurtleName.shape(Chapter13aFighter2.Sprite)
Chapter13aFighter2.TurtleName.hideturtle()

#Fighter3---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter13aFighter3 = Unit(TurtleName="Chapter13aFighter3",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=65,
CurrentHP=65,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=783, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Fighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter13aFighter3.TurtleName = new_turtle()
Chapter13aFighter3.TurtleName.shape(Chapter13aFighter3.Sprite)
Chapter13aFighter3.TurtleName.hideturtle()

#Fighter4---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter13aFighter4 = Unit(TurtleName="Chapter13aFighter4",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=65,
CurrentHP=65,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=783, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Fighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter13aFighter4.TurtleName = new_turtle()
Chapter13aFighter4.TurtleName.shape(Chapter13aFighter4.Sprite)
Chapter13aFighter4.TurtleName.hideturtle()

#Fighter5---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter13aFighter5 = Unit(TurtleName="Chapter13aFighter5",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=65,
CurrentHP=65,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=783, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Fighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter13aFighter5.TurtleName = new_turtle()
Chapter13aFighter5.TurtleName.shape(Chapter13aFighter5.Sprite)
Chapter13aFighter5.TurtleName.hideturtle()

#Fighter6---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter13aFighter6 = Unit(TurtleName="Chapter13aFighter6",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=65,
CurrentHP=65,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=783, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=19,
UnitClass="Fighter",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter13aFighter6.TurtleName = new_turtle()
Chapter13aFighter6.TurtleName.shape(Chapter13aFighter6.Sprite)
Chapter13aFighter6.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 14a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#BigBrainNeville---------------
register_shape(current_directory+"/Sprites/bigbrainneville_small.gif")
register_shape(current_directory+"/Portraits/bigbrainneville_big.gif")
BigBrainNeville = Unit(TurtleName="BigBrainNevilleTurtle",
DisplayName="Big Brain Neville",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=100,
CurrentHP=100,
ATK=13, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=175, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=19,
SPD=7, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=150, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=27,
UnitClass="Navigator",
Attacks=[moves.Aqua],
Supports=[],
Traits=["Magic Primary","Nolavillian","Water"],
Portrait=current_directory+"/Portraits/bigbrainneville_big.gif",
Sprite=current_directory+"/Sprites/bigbrainneville_small.gif",
LevelQuotes=["Big Brain Neville: I detect a small brain."],
Bio="The navigator and tactician of the K'Neville pirates.\nThough he once captained his own ship, the B.Neville, he is now\nloyal to Kaptain K'Neville and should not be underestimated.",
ClassChange=[["Navigator", 25]], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
BigBrainNeville.TurtleName = new_turtle()
BigBrainNeville.TurtleName.shape(BigBrainNeville.Sprite)
BigBrainNeville.TurtleName.hideturtle()

#Archer1---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher1 = Unit(TurtleName="Chapter14aArcher1",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher1.TurtleName = new_turtle()
Chapter14aArcher1.TurtleName.shape(Chapter14aArcher1.Sprite)
Chapter14aArcher1.TurtleName.hideturtle()

#Archer2---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher2 = Unit(TurtleName="Chapter14aArcher2",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher2.TurtleName = new_turtle()
Chapter14aArcher2.TurtleName.shape(Chapter14aArcher2.Sprite)
Chapter14aArcher2.TurtleName.hideturtle()

#Archer3---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher3 = Unit(TurtleName="Chapter14aArcher3",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher3.TurtleName = new_turtle()
Chapter14aArcher3.TurtleName.shape(Chapter14aArcher3.Sprite)
Chapter14aArcher3.TurtleName.hideturtle()

#Archer4---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher4 = Unit(TurtleName="Chapter14aArcher4",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher4.TurtleName = new_turtle()
Chapter14aArcher4.TurtleName.shape(Chapter14aArcher4.Sprite)
Chapter14aArcher4.TurtleName.hideturtle()

#Archer5---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher5 = Unit(TurtleName="Chapter14aArcher5",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher5.TurtleName = new_turtle()
Chapter14aArcher5.TurtleName.shape(Chapter14aArcher5.Sprite)
Chapter14aArcher5.TurtleName.hideturtle()

#Archer6---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher6 = Unit(TurtleName="Chapter14aArcher6",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher6.TurtleName = new_turtle()
Chapter14aArcher6.TurtleName.shape(Chapter14aArcher6.Sprite)
Chapter14aArcher6.TurtleName.hideturtle()

#Archer7---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher7 = Unit(TurtleName="Chapter14aArcher7",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher7.TurtleName = new_turtle()
Chapter14aArcher7.TurtleName.shape(Chapter14aArcher7.Sprite)
Chapter14aArcher7.TurtleName.hideturtle()

#Archer8---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher8 = Unit(TurtleName="Chapter14aArcher8",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher8.TurtleName = new_turtle()
Chapter14aArcher8.TurtleName.shape(Chapter14aArcher8.Sprite)
Chapter14aArcher8.TurtleName.hideturtle()

#Archer9---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher9 = Unit(TurtleName="Chapter14aArcher9",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher9.TurtleName = new_turtle()
Chapter14aArcher9.TurtleName.shape(Chapter14aArcher9.Sprite)
Chapter14aArcher9.TurtleName.hideturtle()

#Archer10---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter14aArcher10 = Unit(TurtleName="Chapter14aArcher10",
DisplayName="Pirate",
AttackRange=["3"],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=10,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=6, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.Bow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArcher10.TurtleName = new_turtle()
Chapter14aArcher10.TurtleName.shape(Chapter14aArcher10.Sprite)
Chapter14aArcher10.TurtleName.hideturtle()

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter14aArmored1 = Unit(TurtleName="Chapter14aArmored1",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=125,
CurrentHP=125,
ATK=85,#3, #Influences attack damage
DEF=45, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=420,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArmored1.TurtleName = new_turtle()
Chapter14aArmored1.TurtleName.shape(Chapter14aArmored1.Sprite)
Chapter14aArmored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter14aArmored2 = Unit(TurtleName="Chapter14aArmored2",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=125,
CurrentHP=125,
ATK=85,#3, #Influences attack damage
DEF=45, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=420,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArmored2.TurtleName = new_turtle()
Chapter14aArmored2.TurtleName.shape(Chapter14aArmored2.Sprite)
Chapter14aArmored2.TurtleName.hideturtle()

#Armored3---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter14aArmored3 = Unit(TurtleName="Chapter14aArmored3",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=125,
CurrentHP=125,
ATK=85,#3, #Influences attack damage
DEF=45, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=420,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter14aArmored3.TurtleName = new_turtle()
Chapter14aArmored3.TurtleName.shape(Chapter14aArmored3.Sprite)
Chapter14aArmored3.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 15a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#KaptainKNeville------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/kaptainkneville_small.gif")
register_shape(current_directory+"/Portraits/kaptainkneville_big.gif")
KaptainKNeville = Unit(TurtleName="KaptainKNevilleTurtle",
DisplayName="Kaptain K'Neville",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=150,
CurrentHP=150,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=250, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=30,
UnitClass="Pirate Captain",
Attacks=[moves.Slash,moves.Cannon],
Supports=[],
Traits=["Nolavillian","Fighter","Water"],
HPGrowth=[100,1], #Chance to level up, max amount to increase
ATKGrowth=[100,1],
DEFGrowth=[100,1],
RESGrowth=[100,1],
AGLGrowth=[100,1],
Portrait=current_directory+"/Portraits/kaptainkneville_big.gif",
Sprite=current_directory+"/Sprites/kaptainkneville_small.gif",
LevelQuotes=["K'Neville: Noob."],
Bio="Kaptain K'Neville is an notorious pirate who sails the seas near the\n Nolavillian. He sails the K.Neville, along with his fleet of the K'Neville Pirates.\nYears ago, he was turned into a distorted version of\nhis past self after consuming the Chalice of Effects.")
KaptainKNeville.TurtleName = new_turtle()
KaptainKNeville.TurtleName.shape(KaptainKNeville.Sprite)
KaptainKNeville.TurtleName.hideturtle()

#Archer1---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter15aArcher1 = Unit(TurtleName="Chapter15aArcher1",
DisplayName="Pirate",
AttackRange=[3],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.HeavyBow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArcher1.TurtleName = new_turtle()
Chapter15aArcher1.TurtleName.shape(Chapter15aArcher1.Sprite)
Chapter15aArcher1.TurtleName.hideturtle()

#Archer2---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter15aArcher2 = Unit(TurtleName="Chapter15aArcher2",
DisplayName="Pirate",
AttackRange=[3],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.HeavyBow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArcher2.TurtleName = new_turtle()
Chapter15aArcher2.TurtleName.shape(Chapter15aArcher2.Sprite)
Chapter15aArcher2.TurtleName.hideturtle()

#Archer3---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter15aArcher3 = Unit(TurtleName="Chapter15aArcher3",
DisplayName="Pirate",
AttackRange=[3],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.HeavyBow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArcher3.TurtleName = new_turtle()
Chapter15aArcher3.TurtleName.shape(Chapter15aArcher3.Sprite)
Chapter15aArcher3.TurtleName.hideturtle()

#Archer4---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter15aArcher4 = Unit(TurtleName="Chapter15aArcher4",
DisplayName="Pirate",
AttackRange=[3],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Archer",
Attacks=[moves.HeavyBow,moves.BowPlus,moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArcher4.TurtleName = new_turtle()
Chapter15aArcher4.TurtleName.shape(Chapter15aArcher4.Sprite)
Chapter15aArcher4.TurtleName.hideturtle()

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter15aArmored1 = Unit(TurtleName="Chapter15aArmored1",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.Lance],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArmored1.TurtleName = new_turtle()
Chapter15aArmored1.TurtleName.shape(Chapter15aArmored1.Sprite)
Chapter15aArmored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter15aArmored2 = Unit(TurtleName="Chapter15aArmored2",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.Lance],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArmored2.TurtleName = new_turtle()
Chapter15aArmored2.TurtleName.shape(Chapter15aArmored2.Sprite)
Chapter15aArmored2.TurtleName.hideturtle()

#Armored3---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter15aArmored3 = Unit(TurtleName="Chapter15aArmored3",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.Lance],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArmored3.TurtleName = new_turtle()
Chapter15aArmored3.TurtleName.shape(Chapter15aArmored3.Sprite)
Chapter15aArmored3.TurtleName.hideturtle()

#Armored4---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter15aArmored4 = Unit(TurtleName="Chapter15aArmored4",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.Lance],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArmored4.TurtleName = new_turtle()
Chapter15aArmored4.TurtleName.shape(Chapter15aArmored4.Sprite)
Chapter15aArmored4.TurtleName.hideturtle()

#Armored5---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter15aArmored5 = Unit(TurtleName="Chapter15aArmored5",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.Lance],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArmored5.TurtleName = new_turtle()
Chapter15aArmored5.TurtleName.shape(Chapter15aArmored5.Sprite)
Chapter15aArmored5.TurtleName.hideturtle()

#Armored6---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter15aArmored6 = Unit(TurtleName="Chapter15aArmored6",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.Lance],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArmored6.TurtleName = new_turtle()
Chapter15aArmored6.TurtleName.shape(Chapter15aArmored6.Sprite)
Chapter15aArmored6.TurtleName.hideturtle()

#Armored7---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter15aArmored7 = Unit(TurtleName="Chapter15aArmored7",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.Lance],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArmored7.TurtleName = new_turtle()
Chapter15aArmored7.TurtleName.shape(Chapter15aArmored7.Sprite)
Chapter15aArmored7.TurtleName.hideturtle()

#Armored8---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter15aArmored8 = Unit(TurtleName="Chapter15aArmored8",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Armored",
Attacks=[moves.Lance],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Pirate: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aArmored8.TurtleName = new_turtle()
Chapter15aArmored8.TurtleName.shape(Chapter15aArmored8.Sprite)
Chapter15aArmored8.TurtleName.hideturtle()

#Fighter1---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter15aFighter1 = Unit(TurtleName="Chapter15aFighter1",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Fighter",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aFighter1.TurtleName = new_turtle()
Chapter15aFighter1.TurtleName.shape(Chapter15aFighter1.Sprite)
Chapter15aFighter1.TurtleName.hideturtle()

#Fighter2---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter15aFighter2 = Unit(TurtleName="Chapter15aFighter2",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Fighter",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aFighter2.TurtleName = new_turtle()
Chapter15aFighter2.TurtleName.shape(Chapter15aFighter2.Sprite)
Chapter15aFighter2.TurtleName.hideturtle()

#Fighter3---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter15aFighter3 = Unit(TurtleName="Chapter15aFighter3",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Fighter",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aFighter3.TurtleName = new_turtle()
Chapter15aFighter3.TurtleName.shape(Chapter15aFighter3.Sprite)
Chapter15aFighter3.TurtleName.hideturtle()

#Fighter4---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter15aFighter4 = Unit(TurtleName="Chapter15aFighter4",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Fighter",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aFighter4.TurtleName = new_turtle()
Chapter15aFighter4.TurtleName.shape(Chapter15aFighter4.Sprite)
Chapter15aFighter4.TurtleName.hideturtle()

#Fighter5---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter15aFighter5 = Unit(TurtleName="Chapter15aFighter5",
DisplayName="Pirate",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=16,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Fighter",
Attacks=[moves.DeathStrike],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A pirate in the K'Neville Pirates.")
Chapter15aFighter5.TurtleName = new_turtle()
Chapter15aFighter5.TurtleName.shape(Chapter15aFighter5.Sprite)
Chapter15aFighter5.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 16a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Tluc---------------
register_shape(current_directory+"/Sprites/tluc_small.gif")
register_shape(current_directory+"/Portraits/tluc_big.gif")
Tluc = Unit(TurtleName="Tluc",
DisplayName="Tluc",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=20,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=14, #Influences damage taken from magic attacks
AGL=9, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=200, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=30,
UnitClass="Elite Xuirist",
Attacks=[moves.Slash,moves.FireBlast],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/tluc_big.gif",
Sprite=current_directory+"/Sprites/tluc_small.gif",
LevelQuotes=["Tluc: Perish! Bipolian scum!"],
Bio="Tluc is a high-ranking Xuirist and\nworks directly under the leader of\nthe Xuirists, Omega. Tluc is\nextremely devoted to Xuirism and will go to extreme\nlengths to stop opposition.")
Tluc.TurtleName = new_turtle()
Tluc.TurtleName.shape(Tluc.Sprite)
Tluc.TurtleName.hideturtle()

#Chapter16Xuirist1---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter16Xuirist1 = Unit(TurtleName="Chapter16Xuirist1",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist working under Tluc.")
Chapter16Xuirist1.TurtleName = new_turtle()
Chapter16Xuirist1.TurtleName.shape(Chapter16Xuirist1.Sprite)
Chapter16Xuirist1.TurtleName.hideturtle()

#Chapter16Xuirist2---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter16Xuirist2 = Unit(TurtleName="Chapter16Xuirist2",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist working under Tluc.")
Chapter16Xuirist2.TurtleName = new_turtle()
Chapter16Xuirist2.TurtleName.shape(Chapter16Xuirist2.Sprite)
Chapter16Xuirist2.TurtleName.hideturtle()

#Chapter16Xuirist3---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter16Xuirist3 = Unit(TurtleName="Chapter16Xuirist3",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist working under Tluc.")
Chapter16Xuirist3.TurtleName = new_turtle()
Chapter16Xuirist3.TurtleName.shape(Chapter16Xuirist3.Sprite)
Chapter16Xuirist3.TurtleName.hideturtle()

#Chapter16Xuirist4---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter16Xuirist4 = Unit(TurtleName="Chapter16Xuirist4",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist working under Tluc.")
Chapter16Xuirist4.TurtleName = new_turtle()
Chapter16Xuirist4.TurtleName.shape(Chapter16Xuirist4.Sprite)
Chapter16Xuirist4.TurtleName.hideturtle()

#Chapter16Xuirist5---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter16Xuirist5 = Unit(TurtleName="Chapter16Xuirist5",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist working under Tluc.")
Chapter16Xuirist5.TurtleName = new_turtle()
Chapter16Xuirist5.TurtleName.shape(Chapter16Xuirist5.Sprite)
Chapter16Xuirist5.TurtleName.hideturtle()

#Chapter16Xuirist6---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter16Xuirist6 = Unit(TurtleName="Chapter16Xuirist6",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist working under Tluc.")
Chapter16Xuirist6.TurtleName = new_turtle()
Chapter16Xuirist6.TurtleName.shape(Chapter16Xuirist6.Sprite)
Chapter16Xuirist6.TurtleName.hideturtle()

#Chapter16Xuirist7---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter16Xuirist7 = Unit(TurtleName="Chapter16Xuirist7",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=15,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=3, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist working under Tluc.")
Chapter16Xuirist7.TurtleName = new_turtle()
Chapter16Xuirist7.TurtleName.shape(Chapter16Xuirist7.Sprite)
Chapter16Xuirist7.TurtleName.hideturtle()

#RethgifEnemy------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/rethgif_small.gif")
register_shape(current_directory+"/Portraits/rethgif_big.gif")
RethgifEnemy = Unit(TurtleName="RethgifEnemy",
DisplayName="Rethgif",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=28,
CurrentHP=28,
ATK=15, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=500, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=30,
UnitClass="Warrior",
Attacks=[moves.Cut,moves.Slice,moves.Slash],
Supports=[],
Traits=["Physical Primary","Nolavillian","Fighter"],
HPGrowth=[60,2], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[80,1],
RESGrowth=[20,1],
AGLGrowth=[70,1],
ACRGrowth=[100,2],
Portrait=current_directory+"/Portraits/rethgif_big.gif",
Sprite=current_directory+"/Sprites/rethgif_small.gif",
LevelQuotes=["Rethgif: Perfect.","Rethgif: This shall be amazing.","Rethgif: The battle must continue."],
Bio="Rethgif is an Nolavillian warrior who travels\nthe lands in search of battle.\nHis motive? To cure his boredom.",
ClassChange=[["Destroyer", 45]], #[Name, Level]
AttackUnlocks=[[moves.DeathStrike,40],[moves.ArmorBreak,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,35]])
RethgifEnemy.TurtleName = new_turtle()
RethgifEnemy.TurtleName.shape(RethgifEnemy.Sprite)
RethgifEnemy.TurtleName.hideturtle()

#EgEnemy------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/eg_small.gif")
register_shape(current_directory+"/Portraits/eg_big.gif")
EgEnemy = Unit(TurtleName="EgEnemy",
DisplayName="Eg",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=15, #Influences attack damage
DEF=0, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=500, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=30,
UnitClass="Warrior",
Attacks=[moves.Cut,moves.Slice],
Supports=[moves.MedKit],
Traits=["Physical Primary","Nolavillian","Fighter"],
HPGrowth=[0,1], #Chance to level up, max amount to increase
ATKGrowth=[60,1],
DEFGrowth=[100,1],
RESGrowth=[50,1],
AGLGrowth=[5,1],
ACRGrowth=[100,2],
Portrait=current_directory+"/Portraits/eg_big.gif",
Sprite=current_directory+"/Sprites/eg_small.gif",
LevelQuotes=["Eg: Satisfactory.","Eg: Advantageous.","Eg: Prosperous."],
Bio="Eg is Rethgif's brother and accompanies him on\nhis travels. While he might look unreliable\none should never underestimate Eg; he is\na man of few words but a great holder of wisdom.",
ClassChange=[["Destroyer", 45]], #[Name, Level]
AttackUnlocks=[[moves.DeathStrike,35],[moves.Slash,40],[moves.ArmorBreak,45],[moves.Thunder,45],[moves.ThunderBlast,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
EgEnemy.TurtleName = new_turtle()
EgEnemy.TurtleName.shape(EgEnemy.Sprite)
EgEnemy.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 17a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Chapter17Xuirist1---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist1 = Unit(TurtleName="Chapter17Xuirist1",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist1.TurtleName = new_turtle()
Chapter17Xuirist1.TurtleName.shape(Chapter17Xuirist1.Sprite)
Chapter17Xuirist1.TurtleName.hideturtle()

#Chapter17Xuirist2---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist2 = Unit(TurtleName="Chapter17Xuirist2",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Cut],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist2.TurtleName = new_turtle()
Chapter17Xuirist2.TurtleName.shape(Chapter17Xuirist2.Sprite)
Chapter17Xuirist2.TurtleName.hideturtle()

#Chapter17Xuirist3---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist3 = Unit(TurtleName="Chapter17Xuirist3",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=80, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=28,
UnitClass="Xuirist",
Attacks=[moves.Slash],
Supports=[],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist3.TurtleName = new_turtle()
Chapter17Xuirist3.TurtleName.shape(Chapter17Xuirist3.Sprite)
Chapter17Xuirist3.TurtleName.hideturtle()

#Chapter17Xuirist4---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist4 = Unit(TurtleName="Chapter17Xuirist4",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=40,
CurrentHP=40,
ATK=17,#3, #Influences attack damage
DEF=4, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=30,
UnitClass="Xuirist",
Attacks=[moves.Aqua],
Supports=[],
Traits=["Magic Primary", "Water"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist4.TurtleName = new_turtle()
Chapter17Xuirist4.TurtleName.shape(Chapter17Xuirist4.Sprite)
Chapter17Xuirist4.TurtleName.hideturtle()

#Chapter17Xuirist5---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist5 = Unit(TurtleName="Chapter17Xuirist5",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=13,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=26,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.Slice,moves.Thunder],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist5.TurtleName = new_turtle()
Chapter17Xuirist5.TurtleName.shape(Chapter17Xuirist5.Sprite)
Chapter17Xuirist5.TurtleName.hideturtle()

#Chapter17Xuirist6---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist6 = Unit(TurtleName="Chapter17Xuirist6",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=13,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=26,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.Slice,moves.Thunder],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist6.TurtleName = new_turtle()
Chapter17Xuirist6.TurtleName.shape(Chapter17Xuirist6.Sprite)
Chapter17Xuirist6.TurtleName.hideturtle()

#Chapter17Xuirist7---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist7 = Unit(TurtleName="Chapter17Xuirist7",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=13,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=26,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.Slice,moves.DarkOrb],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist7.TurtleName = new_turtle()
Chapter17Xuirist7.TurtleName.shape(Chapter17Xuirist7.Sprite)
Chapter17Xuirist7.TurtleName.hideturtle()

#Chapter17Xuirist8---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist8 = Unit(TurtleName="Chapter17Xuirist8",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=13,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=12, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=26,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.Slice,moves.DarkOrb],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist8.TurtleName = new_turtle()
Chapter17Xuirist8.TurtleName.shape(Chapter17Xuirist8.Sprite)
Chapter17Xuirist8.TurtleName.hideturtle()

#Chapter17Xuirist9---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist9 = Unit(TurtleName="Chapter17Xuirist9",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=13,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=8, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=120, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=37,
UnitClass="Xuirist",
Attacks=[moves.Slash,moves.Thorn,moves.VineWrath],
Supports=[],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist9.TurtleName = new_turtle()
Chapter17Xuirist9.TurtleName.shape(Chapter17Xuirist9.Sprite)
Chapter17Xuirist9.TurtleName.hideturtle()

#Chapter17Xuirist10---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist10 = Unit(TurtleName="Chapter17Xuirist10",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=5,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=6, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.Bow,moves.LongBow,moves.DistanceShot,moves.Snipe],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist10.TurtleName = new_turtle()
Chapter17Xuirist10.TurtleName.shape(Chapter17Xuirist10.Sprite)
Chapter17Xuirist10.TurtleName.hideturtle()

#Chapter17Xuirist11---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist11 = Unit(TurtleName="Chapter17Xuirist11",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=5,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=6, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.Bow,moves.LongBow,moves.DistanceShot,moves.Snipe],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist11.TurtleName = new_turtle()
Chapter17Xuirist11.TurtleName.shape(Chapter17Xuirist11.Sprite)
Chapter17Xuirist11.TurtleName.hideturtle()

#Chapter17Xuirist12---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist12 = Unit(TurtleName="Chapter17Xuirist12",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=5,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=6, #Influences damage taken from magic attacks
AGL=8, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=28,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.Bow,moves.LongBow,moves.DistanceShot,moves.Snipe],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist12.TurtleName = new_turtle()
Chapter17Xuirist12.TurtleName.shape(Chapter17Xuirist12.Sprite)
Chapter17Xuirist12.TurtleName.hideturtle()

#Chapter17Xuirist13---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist13 = Unit(TurtleName="Chapter17Xuirist13",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=45,
CurrentHP=45,
ATK=40,#3, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=18, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist13.TurtleName = new_turtle()
Chapter17Xuirist13.TurtleName.shape(Chapter17Xuirist13.Sprite)
Chapter17Xuirist13.TurtleName.hideturtle()

#Chapter17Xuirist14---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter17Xuirist14 = Unit(TurtleName="Chapter17Xuirist14",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=45,
CurrentHP=45,
ATK=40,#3, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=18, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=90, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter17Xuirist14.TurtleName = new_turtle()
Chapter17Xuirist14.TurtleName.shape(Chapter17Xuirist14.Sprite)
Chapter17Xuirist14.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 17d]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#BBoss------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/b_small.gif")
register_shape(current_directory+"/Portraits/b_big.gif")
BBoss = Unit(TurtleName="BBossTurtle",
DisplayName="B",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=90,
CurrentHP=90,
ATK=35, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=3, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=1000, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=25,
UnitClass="Partial Mechanical",
Attacks=[moves.Cut,moves.Slash],
Supports=[],
Traits=["Physical Primary","Infinian","Mechanical"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[70,2],
DEFGrowth=[60,1],
RESGrowth=[60,1],
AGLGrowth=[40,1],
ACRGrowth=[90,1],
Portrait=current_directory+"/Portraits/b_big.gif",
Sprite=current_directory+"/Sprites/b_small.gif",
LevelQuotes=["B: ..."],
Bio="B is an Nolavillian who has been affected\nby the Inverse Time. Due to this, he\nis taken to a different timeline every 18 months.",
ClassChange=[["Chrono Master", 50]], #[Name, Level]
AttackUnlocks=[[moves.Beam,40],[moves.Destroyer,50]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,45]])
BBoss.TurtleName = new_turtle()
BBoss.TurtleName.shape(B.Sprite)
BBoss.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 18a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Chapter18Xuirist1---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist1 = Unit(TurtleName="Chapter18Xuirist1",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=10,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=19, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=8, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=30,
UnitClass="Xuirist",
Attacks=[moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist1.TurtleName = new_turtle()
Chapter18Xuirist1.TurtleName.shape(Chapter18Xuirist1.Sprite)
Chapter18Xuirist1.TurtleName.hideturtle()

#Chapter18Xuirist2---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist2 = Unit(TurtleName="Chapter18Xuirist2",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=10,#3, #Influences attack damage
DEF=6, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=19, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=8, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=30,
UnitClass="Xuirist",
Attacks=[moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist2.TurtleName = new_turtle()
Chapter18Xuirist2.TurtleName.shape(Chapter18Xuirist2.Sprite)
Chapter18Xuirist2.TurtleName.hideturtle()

#Chapter18Xuirist3---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist3 = Unit(TurtleName="Chapter18Xuirist3",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=20,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist3.TurtleName = new_turtle()
Chapter18Xuirist3.TurtleName.shape(Chapter18Xuirist3.Sprite)
Chapter18Xuirist3.TurtleName.hideturtle()

#Chapter18Xuirist4---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist4 = Unit(TurtleName="Chapter18Xuirist4",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=10,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=4, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist4.TurtleName = new_turtle()
Chapter18Xuirist4.TurtleName.shape(Chapter18Xuirist4.Sprite)
Chapter18Xuirist4.TurtleName.hideturtle()

#Chapter18Xuirist5---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist5 = Unit(TurtleName="Chapter18Xuirist5",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=40,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=8,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist5.TurtleName = new_turtle()
Chapter18Xuirist5.TurtleName.shape(Chapter18Xuirist5.Sprite)
Chapter18Xuirist5.TurtleName.hideturtle()

#Chapter18Xuirist6---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist6 = Unit(TurtleName="Chapter18Xuirist6",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=5,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=40, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist6.TurtleName = new_turtle()
Chapter18Xuirist6.TurtleName.shape(Chapter18Xuirist6.Sprite)
Chapter18Xuirist6.TurtleName.hideturtle()

#Chapter18Xuirist7---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist7 = Unit(TurtleName="Chapter18Xuirist7",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=5,#3, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=6, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist7.TurtleName = new_turtle()
Chapter18Xuirist7.TurtleName.shape(Chapter18Xuirist7.Sprite)
Chapter18Xuirist7.TurtleName.hideturtle()

#Chapter18Xuirist8---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist8 = Unit(TurtleName="Chapter18Xuirist8",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist8.TurtleName = new_turtle()
Chapter18Xuirist8.TurtleName.shape(Chapter18Xuirist8.Sprite)
Chapter18Xuirist8.TurtleName.hideturtle()

#Chapter18Xuirist9---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist9 = Unit(TurtleName="Chapter18Xuirist9",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist9.TurtleName = new_turtle()
Chapter18Xuirist9.TurtleName.shape(Chapter18Xuirist9.Sprite)
Chapter18Xuirist9.TurtleName.hideturtle()

#Chapter18Xuirist10---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist10 = Unit(TurtleName="Chapter18Xuirist10",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist10.TurtleName = new_turtle()
Chapter18Xuirist10.TurtleName.shape(Chapter18Xuirist10.Sprite)
Chapter18Xuirist10.TurtleName.hideturtle()

#Chapter18Xuirist11---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist11 = Unit(TurtleName="Chapter18Xuirist11",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist11.TurtleName = new_turtle()
Chapter18Xuirist11.TurtleName.shape(Chapter18Xuirist11.Sprite)
Chapter18Xuirist11.TurtleName.hideturtle()

#Chapter18Xuirist12---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist12 = Unit(TurtleName="Chapter18Xuirist12",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=13,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=15,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist12.TurtleName = new_turtle()
Chapter18Xuirist12.TurtleName.shape(Chapter18Xuirist12.Sprite)
Chapter18Xuirist12.TurtleName.hideturtle()

#Chapter18Xuirist13---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist13 = Unit(TurtleName="Chapter18Xuirist13",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=9,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.SnipeII],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist13.TurtleName = new_turtle()
Chapter18Xuirist13.TurtleName.shape(Chapter18Xuirist13.Sprite)
Chapter18Xuirist13.TurtleName.hideturtle()

#Chapter18Xuirist14---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter18Xuirist14 = Unit(TurtleName="Chapter18Xuirist14",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=9,#3, #Influences attack damage
DEF=7, #Influences damage taken from physical attacks
RES=10, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=25,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=95, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=32,
UnitClass="Xuirist",
Attacks=[moves.SnipeII],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter18Xuirist14.TurtleName = new_turtle()
Chapter18Xuirist14.TurtleName.shape(Chapter18Xuirist14.Sprite)
Chapter18Xuirist14.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 19a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Chapter19Xuirist1---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter19Xuirist1 = Unit(TurtleName="Chapter19Xuirist1",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=40,
CurrentHP=40,
ATK=20,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=150, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack
ACR=24,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=105, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.GeomBurst],
Supports=[],
Traits=["Magic Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter19Xuirist1.TurtleName = new_turtle()
Chapter19Xuirist1.TurtleName.shape(Chapter19Xuirist1.Sprite)
Chapter19Xuirist1.TurtleName.hideturtle()

#Chapter19Xuirist2---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter19Xuirist2 = Unit(TurtleName="Chapter19Xuirist2",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=125, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack
ACR=35,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=105, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.AntiXuir],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter19Xuirist2.TurtleName = new_turtle()
Chapter19Xuirist2.TurtleName.shape(Chapter19Xuirist2.Sprite)
Chapter19Xuirist2.TurtleName.hideturtle()

#Chapter19Xuirist3---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter19Xuirist3 = Unit(TurtleName="Chapter19Xuirist3",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=50,
CurrentHP=50,
ATK=25,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=165, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack
ACR=50,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=105, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Xuirist",
Attacks=[moves.GeomBlast],
Supports=[],
Traits=["Magic Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter19Xuirist3.TurtleName = new_turtle()
Chapter19Xuirist3.TurtleName.shape(Chapter19Xuirist3.Sprite)
Chapter19Xuirist3.TurtleName.hideturtle()

#Chapter19Xuirist4---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter19Xuirist4 = Unit(TurtleName="Chapter19Xuirist4",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=75,
CurrentHP=75,
ATK=30,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=180, #Influences damage taken from magic attacks
AGL=18, #Influences the chance of getting hit by an attack
ACR=55,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=37,
UnitClass="Xuirist",
Attacks=[moves.GeomBlast,moves.Slash],
Supports=[],
Traits=["Magic Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter19Xuirist4.TurtleName = new_turtle()
Chapter19Xuirist4.TurtleName.shape(Chapter19Xuirist4.Sprite)
Chapter19Xuirist4.TurtleName.hideturtle()

#Chapter19Xuirist5---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter19Xuirist5 = Unit(TurtleName="Chapter19Xuirist5",
DisplayName="Xuirist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=30,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=175, #Influences damage taken from magic attacks
AGL=18, #Influences the chance of getting hit by an attack
ACR=55,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=37,
UnitClass="Xuirist",
Attacks=[moves.AntiXuir],
Supports=[moves.XuirianRecovery],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter19Xuirist5.TurtleName = new_turtle()
Chapter19Xuirist5.TurtleName.shape(Chapter19Xuirist5.Sprite)
Chapter19Xuirist5.TurtleName.hideturtle()

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter19Armored1 = Unit(TurtleName="Chapter19Armored1",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=20,#3, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=33,
UnitClass="Armored",
Attacks=[moves.Slice, moves.Javelin],
Supports=[],
Traits=["Physical Primary", "Shadow","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Mercenary: Fall to the power of Xuir, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Armored1.TurtleName = new_turtle()
Chapter19Armored1.TurtleName.shape(Chapter19Armored1.Sprite)
Chapter19Armored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter19Armored2 = Unit(TurtleName="Chapter19Armored2",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=20,#3, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=33,
UnitClass="Armored",
Attacks=[moves.Slice, moves.Javelin],
Supports=[],
Traits=["Physical Primary", "Bio","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Mercenary: Fall to the power of Xuir, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Armored2.TurtleName = new_turtle()
Chapter19Armored2.TurtleName.shape(Chapter19Armored2.Sprite)
Chapter19Armored2.TurtleName.hideturtle()

#Armored3---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter19Armored3 = Unit(TurtleName="Chapter19Armored3",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=20,#3, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=33,
UnitClass="Armored",
Attacks=[moves.Slice, moves.Javelin],
Supports=[],
Traits=["Physical Primary", "Water","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Mercenary: Fall to the power of Xuir, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Armored3.TurtleName = new_turtle()
Chapter19Armored3.TurtleName.shape(Chapter19Armored3.Sprite)
Chapter19Armored3.TurtleName.hideturtle()

#Armored4---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter19Armored4 = Unit(TurtleName="Chapter19Armored4",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=20,#3, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=33,
UnitClass="Armored",
Attacks=[moves.Slice, moves.Javelin],
Supports=[],
Traits=["Physical Primary", "Bio","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Mercenary: Fall to the power of Xuir, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Armored4.TurtleName = new_turtle()
Chapter19Armored4.TurtleName.shape(Chapter19Armored4.Sprite)
Chapter19Armored4.TurtleName.hideturtle()

#Armored5---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter19Armored5 = Unit(TurtleName="Chapter19Armored5",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=20,#3, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=33,
UnitClass="Armored",
Attacks=[moves.Slice, moves.Javelin],
Supports=[],
Traits=["Physical Primary", "Ice","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Mercenary: Fall to the power of Xuir, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Armored5.TurtleName = new_turtle()
Chapter19Armored5.TurtleName.shape(Chapter19Armored5.Sprite)
Chapter19Armored5.TurtleName.hideturtle()

#Armored6---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter19Armored6 = Unit(TurtleName="Chapter19Armored5",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=20,#3, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=33,
UnitClass="Armored",
Attacks=[moves.Slice, moves.Javelin],
Supports=[],
Traits=["Physical Primary", "Electric","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Mercenary: Fall to the power of Xuir, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Armored6.TurtleName = new_turtle()
Chapter19Armored6.TurtleName.shape(Chapter19Armored6.Sprite)
Chapter19Armored6.TurtleName.hideturtle()

#Archer1---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter19Archer1 = Unit(TurtleName="Chapter19Archer1",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=35,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=115, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Archer",
Attacks=[moves.BowPlus],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Mercenary: Xuirism is good, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Archer1.TurtleName = new_turtle()
Chapter19Archer1.TurtleName.shape(Chapter19Archer1.Sprite)
Chapter19Archer1.TurtleName.hideturtle()

#Archer2---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter19Archer2 = Unit(TurtleName="Chapter19Archer2",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=35,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=115, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Archer",
Attacks=[moves.BowPlus],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Mercenary: Xuirism is good, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Archer2.TurtleName = new_turtle()
Chapter19Archer2.TurtleName.shape(Chapter19Archer2.Sprite)
Chapter19Archer2.TurtleName.hideturtle()

#Archer3---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter19Archer3 = Unit(TurtleName="Chapter19Archer3",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=35,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=115, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Archer",
Attacks=[moves.BowPlus],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Mercenary: Xuirism is good, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Archer3.TurtleName = new_turtle()
Chapter19Archer3.TurtleName.shape(Chapter19Archer3.Sprite)
Chapter19Archer3.TurtleName.hideturtle()

#Archer4---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter19Archer4 = Unit(TurtleName="Chapter19Archer4",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=35,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=115, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Archer",
Attacks=[moves.BowPlus],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Mercenary: Xuirism is good, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Archer4.TurtleName = new_turtle()
Chapter19Archer4.TurtleName.shape(Chapter19Archer4.Sprite)
Chapter19Archer4.TurtleName.hideturtle()

#Archer5---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter19Archer5 = Unit(TurtleName="Chapter19Archer5",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=35,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=115, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Archer",
Attacks=[moves.BowPlus],
Supports=[],
Traits=["Physical Primary", "Bio"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Mercenary: Xuirism is good, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Archer5.TurtleName = new_turtle()
Chapter19Archer5.TurtleName.shape(Chapter19Archer5.Sprite)
Chapter19Archer5.TurtleName.hideturtle()

#Archer6---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter19Archer6 = Unit(TurtleName="Chapter19Archer6",
DisplayName="Mercenary",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=35,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=115, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Archer",
Attacks=[moves.BowPlus],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Mercenary: Xuirism is good, or something."],
Bio="A mercenary hired by the Xuirists.")
Chapter19Archer6.TurtleName = new_turtle()
Chapter19Archer6.TurtleName.shape(Chapter19Archer6.Sprite)
Chapter19Archer6.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 20a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Fighter1---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter20aFighter1 = Unit(TurtleName="Chapter20aFighter1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=65,
CurrentHP=65,
ATK=30,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Fighter",
Attacks=[moves.Slash,moves.Cut],
Supports=[],
Traits=["Physical Primary", "Water"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in the\nNolavillian Mountain Range.")
Chapter20aFighter1.TurtleName = new_turtle()
Chapter20aFighter1.TurtleName.shape(Chapter20aFighter1.Sprite)
Chapter20aFighter1.TurtleName.hideturtle()

#Fighter2---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter20aFighter2 = Unit(TurtleName="Chapter20aFighter2",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=63,
CurrentHP=63,
ATK=33,#3, #Influences attack damage
DEF=27, #Influences damage taken from physical attacks
RES=40, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Fighter",
Attacks=[moves.ArmorBreak,moves.Slice],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in the\nNolavillian Mountain Range.")
Chapter20aFighter2.TurtleName = new_turtle()
Chapter20aFighter2.TurtleName.shape(Chapter20aFighter2.Sprite)
Chapter20aFighter2.TurtleName.hideturtle()

#Fighter3---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter20aFighter3 = Unit(TurtleName="Chapter20aFighter3",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=63,
CurrentHP=63,
ATK=22,#3, #Influences attack damage
DEF=27, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=22, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=20,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Fighter",
Attacks=[moves.ArmorBreak,moves.Slice],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in the\nNolavillian Mountain Range.")
Chapter20aFighter3.TurtleName = new_turtle()
Chapter20aFighter3.TurtleName.shape(Chapter20aFighter3.Sprite)
Chapter20aFighter3.TurtleName.hideturtle()

#Fighter4---------------
register_shape(current_directory+"/Sprites/genericswordfighter_small.gif")
register_shape(current_directory+"/Portraits/genericswordfighter_big.gif")
Chapter20aFighter4 = Unit(TurtleName="Chapter20aFighter4",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=71,
CurrentHP=71,
ATK=25,#3, #Influences attack damage
DEF=22, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=26,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Fighter",
Attacks=[moves.Slash,moves.Cut],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericswordfighter_big.gif",
Sprite=current_directory+"/Sprites/genericswordfighter_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in the\nNolavillian Mountain Range.")
Chapter20aFighter4.TurtleName = new_turtle()
Chapter20aFighter4.TurtleName.shape(Chapter20aFighter4.Sprite)
Chapter20aFighter4.TurtleName.hideturtle()

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter20aArmored1 = Unit(TurtleName="Chapter20aArmored1",
DisplayName="Bandit",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=150,
CurrentHP=150,
ATK=25,#3, #Influences attack damage
DEF=40, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=250, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=37,
UnitClass="Armored",
Attacks=[moves.HeavyBow],
Supports=[],
Traits=["Physical Primary", "Bio","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Bandit: You can't defeat me."],
Bio="A bandit in the\nNolavillian Mountain Range.")
Chapter20aArmored1.TurtleName = new_turtle()
Chapter20aArmored1.TurtleName.shape(Chapter20aArmored1.Sprite)
Chapter20aArmored1.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 20b]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Dael---------------
register_shape(current_directory+"/Sprites/dael_small.gif")
register_shape(current_directory+"/Portraits/dael_big.gif")
Dael = Unit(TurtleName="DaelTurtle",
DisplayName="Dael",
AttackRange=[1,2],
PrimaryType="Magic",
MaxHP=125,
CurrentHP=125,
ATK=25, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=250, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=45,
UnitClass="Head Knight",
Attacks=[moves.FireBlast,moves.Slash, moves.Slice,moves.Inferno],
Supports=[],
Traits=["Magic Primary", "Fire"],
Portrait=current_directory+"/Portraits/dael_big.gif",
Sprite=current_directory+"/Sprites/dael_small.gif",
LevelQuotes=["Dael: Fall before his power."],
Bio="The head night of Neo's revoluionary army\nand an extreme supporter of Neo, Dael\nhas come to Nolavillia to obtain\nthe Itucher for Neo's conquest of Shade.")
Dael.TurtleName = new_turtle()
Dael.TurtleName.shape(Dael.Sprite)
Dael.TurtleName.hideturtle()

#Dnefed------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/dnefed_small.gif")
register_shape(current_directory+"/Portraits/dnefed_big.gif")
DnefedEnemy = Unit(TurtleName="DnefedEnemy",
DisplayName="Dnefed",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=100,
CurrentHP=100,
ATK=30, #Influences attack damage
DEF=30, #Influences damage taken from physical attacks
RES=12, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Armor Knight",
Attacks=[moves.Slice,moves.Slash],
Supports=[],
Traits=["Physical Primary","Shadeian","Armored"],
HPGrowth=[100,5], #Chance to level up, max amount to increase
ATKGrowth=[70,1],
DEFGrowth=[60,1],
RESGrowth=[5,1],
AGLGrowth=[10,1],
ACRGrowth=[65,1],
Portrait=current_directory+"/Portraits/dnefed_big.gif",
Sprite=current_directory+"/Sprites/dnefed_small.gif",
LevelQuotes=["Dnefed: Done.","Dnefed: Good.","Dnefed: I've won."],
Bio="Dnefed is a soldier from Shade.",
ClassChange=[["Shield Knight", 45]], #[Name, Level]
AttackUnlocks=[[moves.Javelin,37],[moves.ArmorBreak,40],[moves.ShieldBash,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
DnefedEnemy.TurtleName = new_turtle()
DnefedEnemy.TurtleName.shape(DnefedEnemy.Sprite)
DnefedEnemy.TurtleName.hideturtle()

#Thgif------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/thgif_small.gif")
register_shape(current_directory+"/Portraits/thgif_big.gif")
ThgifEnemy = Unit(TurtleName="ThgifEnemy",
DisplayName="Thgif",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=30, #Influences attack damage
DEF=29, #Influences damage taken from physical attacks
RES=13, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Warrior",
Attacks=[moves.Slice],
Supports=[],
Traits=["Physical Primary","Shadeian","Fighter"],
HPGrowth=[80,1], #Chance to level up, max amount to increase
ATKGrowth=[75,1],
DEFGrowth=[70,1],
RESGrowth=[50,1],
AGLGrowth=[20,1],
ACRGrowth=[70,1],
Portrait=current_directory+"/Portraits/thgif_big.gif",
Sprite=current_directory+"/Sprites/thgif_small.gif",
LevelQuotes=["Thgif: Victory.","Thgif: Great.","Thgif: I've won."],
Bio="Thgif is a soldier from Shade.",
ClassChange=[["Elite Warrior", 45]], #[Name, Level]
AttackUnlocks=[[moves.Slash,40],[moves.ArmorBreak,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
ThgifEnemy.TurtleName = new_turtle()
ThgifEnemy.TurtleName.shape(ThgifEnemy.Sprite)
ThgifEnemy.TurtleName.hideturtle()

#Gnirif------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/gnirif_small.gif")
register_shape(current_directory+"/Portraits/gnirif_big.gif")
GnirifEnemy = Unit(TurtleName="GnirifEnemy",
DisplayName="Gnirif",
AttackRange=[1,2],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=20, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Sniper",
Attacks=[moves.Bow,moves.DistanceShot,moves.Snipe],
Supports=[],
Traits=["Physical Primary","Shadeian","Archer"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[75,1],
DEFGrowth=[40,1],
RESGrowth=[40,1],
AGLGrowth=[25,1],
ACRGrowth=[100,2],
Portrait=current_directory+"/Portraits/gnirif_big.gif",
Sprite=current_directory+"/Sprites/gnirif_small.gif",
LevelQuotes=["Gnirif: Victory.","Gnirif: Good.","Gnirif: You've lost."],
Bio="Gnirif is a soldier from Shade.",
ClassChange=[["Elite Sniper", 50]], #[Name, Level]
AttackUnlocks=[[moves.SnipeII,40],[moves.SnipeIII,50]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
GnirifEnemy.TurtleName = new_turtle()
GnirifEnemy.TurtleName.shape(GnirifEnemy.Sprite)
GnirifEnemy.TurtleName.hideturtle()

#Cigam------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/cigam_small.gif")
register_shape(current_directory+"/Portraits/cigam_big.gif")
CigamEnemy = Unit(TurtleName="CigamEnemy",
DisplayName="Cigam",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=35, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Heal Mage",
Attacks=[],
Supports=[moves.Heal,moves.LongHeal,moves.FarHeal],
Traits=["Physical Primary","Shadeian","Mage","Water"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[90,1],
DEFGrowth=[20,1],
RESGrowth=[70,1],
AGLGrowth=[25,1],
ACRGrowth=[75,1],
Portrait=current_directory+"/Portraits/cigam_big.gif",
Sprite=current_directory+"/Sprites/cigam_small.gif",
LevelQuotes=["Cigam: This will be helpful.","Cigam: Good.","Cigam: Great."],
Bio="Cigam is a soldier from Shade.",
ClassChange=[["Dual Mage", 40]], #[Name, Level]
AttackUnlocks=[[moves.Aqua,40],[moves.Hydro,45]], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[[moves.MedKit,37]])
CigamEnemy.TurtleName = new_turtle()
CigamEnemy.TurtleName.shape(CigamEnemy.Sprite)
CigamEnemy.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 21a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Break---------------
register_shape(current_directory+"/Sprites/break_small.gif")
register_shape(current_directory+"/Portraits/break_big.gif")
Chapter21aBreak = Unit(TurtleName="Chapter21aBreak",
DisplayName="Break",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=125,
CurrentHP=100,
ATK=30, #3, #Influences attack damage
DEF=35, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=17, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=350, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=50,
UnitClass="Head Scientist",
Attacks=[moves.VenomBlade,moves.Gun],
Supports=[],
Traits=["Physical Primary", "Nolavillian","Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/break_big.gif",
Sprite=current_directory+"/Sprites/break_small.gif",
LevelQuotes=["Break: Are you scared?"],
Bio="Break is one of the head scientists\nat the Shadow Realm Research Center, and works\ndirectly with Death Pepper in Xuir Research.\nHe is also the true leader of the Xuirist religion,\nhaving controlled Omega into creating and leading the\nreligion for him/")
Chapter21aBreak.TurtleName = new_turtle()
Chapter21aBreak.TurtleName.shape(Chapter21aBreak.Sprite)
Chapter21aBreak.TurtleName.hideturtle()

#OmegaBoss------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/omegaxuirist_small.gif")
register_shape(current_directory+"/Portraits/omegaxuirist_big.gif")
OmegaBoss = Unit(TurtleName="OmegaBossTurtle",
DisplayName="Omega",
AttackRange=[1],
PrimaryType="Magic",
MaxHP=75,
CurrentHP=75,
ATK=20, #3, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=355, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=32,
SPD=5, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=250, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=48,
UnitClass="Elite Xuirist",
Attacks=[moves.ShadowStorm,moves.DarkOrb,moves.ShadowBurst],
Supports=[],
Traits=["Magic Primary","Nolavillian","Xuirist","Shadow"],
Portrait=current_directory+"/Portraits/omegaxuirist_big.gif",
Sprite=current_directory+"/Sprites/omegaxuirist_small.gif",
LevelQuotes=["Omega: ..."],
Bio="Omega is the official founder of the\nXuirist religion, though he was forced\nby Break to create and maintain the religion\nfor him.")
OmegaBoss.TurtleName = new_turtle()
OmegaBoss.TurtleName.shape(current_directory+"/Sprites/omegaxuirist_small.gif")
OmegaBoss.TurtleName.hideturtle()

#Undead1---------------
register_shape(current_directory+"/Sprites/undead_small.gif")
register_shape(current_directory+"/Portraits/undead1_big.gif")
Undead1 = Unit(TurtleName="Undead1",
DisplayName="Undead",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=22,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Undead",
Attacks=[moves.ShadowPunch],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/undead1_big.gif",
Sprite=current_directory+"/Sprites/undead_small.gif",
LevelQuotes=["Undead: ..."],
Bio="???")
Undead1.TurtleName = new_turtle()
Undead1.TurtleName.shape(Undead1.Sprite)
Undead1.TurtleName.hideturtle()

#Undead2---------------
register_shape(current_directory+"/Sprites/undead_small.gif")
register_shape(current_directory+"/Portraits/undead2_big.gif")
Undead2 = Unit(TurtleName="Undead2",
DisplayName="Undead",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=22,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Undead",
Attacks=[moves.ShadowPunch],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/undead2_big.gif",
Sprite=current_directory+"/Sprites/undead_small.gif",
LevelQuotes=["Undead: ..."],
Bio="???")
Undead2.TurtleName = new_turtle()
Undead2.TurtleName.shape(Undead2.Sprite)
Undead2.TurtleName.hideturtle()

#Undead3---------------
register_shape(current_directory+"/Sprites/undead_small.gif")
register_shape(current_directory+"/Portraits/undead3_big.gif")
Undead3 = Unit(TurtleName="Undead3",
DisplayName="Undead",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=22,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Undead",
Attacks=[moves.ShadowPunch],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/undead3_big.gif",
Sprite=current_directory+"/Sprites/undead_small.gif",
LevelQuotes=["Undead: ..."],
Bio="???")
Undead3.TurtleName = new_turtle()
Undead3.TurtleName.shape(Undead3.Sprite)
Undead3.TurtleName.hideturtle()

#Undead4---------------
register_shape(current_directory+"/Sprites/undead_small.gif")
register_shape(current_directory+"/Portraits/undead4_big.gif")
Undead4 = Unit(TurtleName="Undead4",
DisplayName="Undead",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=22,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Undead",
Attacks=[moves.ShadowPunch],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/undead4_big.gif",
Sprite=current_directory+"/Sprites/undead_small.gif",
LevelQuotes=["Undead: ..."],
Bio="???")
Undead4.TurtleName = new_turtle()
Undead4.TurtleName.shape(Undead4.Sprite)
Undead4.TurtleName.hideturtle()

#Undead5---------------
register_shape(current_directory+"/Sprites/undead_small.gif")
register_shape(current_directory+"/Portraits/undead5_big.gif")
Undead5 = Unit(TurtleName="Undead5",
DisplayName="Undead",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=22,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=130, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=35,
UnitClass="Undead",
Attacks=[moves.ShadowPunch],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/undead5_big.gif",
Sprite=current_directory+"/Sprites/undead_small.gif",
LevelQuotes=["Undead: ..."],
Bio="???")
Undead5.TurtleName = new_turtle()
Undead5.TurtleName.shape(Undead5.Sprite)
Undead5.TurtleName.hideturtle()

#Chapter21aXuirist1---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter21aXuirist1 = Unit(TurtleName="Chapter21aXuirist1",
DisplayName="Xuirist",
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Xuirist",
Attacks=[moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter21aXuirist1.TurtleName = new_turtle()
Chapter21aXuirist1.TurtleName.shape(Chapter21aXuirist1.Sprite)
Chapter21aXuirist1.TurtleName.hideturtle()

#Chapter21aXuirist2---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter21aXuirist2 = Unit(TurtleName="Chapter21aXuirist2",
DisplayName="Xuirist",
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Xuirist",
Attacks=[moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Fire"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter21aXuirist2.TurtleName = new_turtle()
Chapter21aXuirist2.TurtleName.shape(Chapter21aXuirist2.Sprite)
Chapter21aXuirist2.TurtleName.hideturtle()

#Chapter21aXuirist3---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter21aXuirist3 = Unit(TurtleName="Chapter21aXuirist3",
DisplayName="Xuirist",
PrimaryType="Physical",
MaxHP=40,
CurrentHP=40,
ATK=20,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=55, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Xuirist",
Attacks=[moves.LongBow],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter21aXuirist3.TurtleName = new_turtle()
Chapter21aXuirist3.TurtleName.shape(Chapter21aXuirist3.Sprite)
Chapter21aXuirist3.TurtleName.hideturtle()

#Chapter21aXuirist4---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter21aXuirist4 = Unit(TurtleName="Chapter21aXuirist4",
DisplayName="Xuirist",
PrimaryType="Magic",
MaxHP=45,
CurrentHP=45,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=75, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Xuirist",
Attacks=[moves.Congeal,moves.Freeze,moves.Cut],
Supports=[],
Traits=["Magic Primary", "Ice"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter21aXuirist4.TurtleName = new_turtle()
Chapter21aXuirist4.TurtleName.shape(Chapter21aXuirist4.Sprite)
Chapter21aXuirist4.TurtleName.hideturtle()

#Chapter21aXuirist5---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter21aXuirist5 = Unit(TurtleName="Chapter21aXuirist5",
DisplayName="Xuirist",
PrimaryType="Magic",
MaxHP=45,
CurrentHP=45,
ATK=15,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=75, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Xuirist",
Attacks=[moves.Voltage,moves.Thunder,moves.Cut],
Supports=[],
Traits=["Magic Primary", "Electric"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter21aXuirist5.TurtleName = new_turtle()
Chapter21aXuirist5.TurtleName.shape(Chapter21aXuirist5.Sprite)
Chapter21aXuirist5.TurtleName.hideturtle()

#Chapter21aXuirist6---------------
register_shape(current_directory+"/Sprites/genericxuirist_small.gif")
register_shape(current_directory+"/Portraits/genericxuirist_big.gif")
Chapter21aXuirist6 = Unit(TurtleName="Chapter21aXuirist6",
DisplayName="Xuirist",
PrimaryType="Magic",
MaxHP=6,
CurrentHP=6,
ATK=40,#3, #Influences attack damage
DEF=0, #Influences damage taken from physical attacks
RES=999, #Influences damage taken from magic attacks
AGL=15, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=999,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=215, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=45,
UnitClass="Xuirist",
Attacks=[moves.Countdown,moves.Death],
Supports=[],
Traits=["Magic Primary", "Water"],
Portrait=current_directory+"/Portraits/genericxuirist_big.gif",
Sprite=current_directory+"/Sprites/genericxuirist_small.gif",
LevelQuotes=["Xuirist: All opposition must be stopped."],
Bio="A low-ranking Xuirist.")
Chapter21aXuirist6.TurtleName = new_turtle()
Chapter21aXuirist6.TurtleName.shape(Chapter21aXuirist6.Sprite)
Chapter21aXuirist6.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 22a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#If---------------
register_shape(current_directory+"/Sprites/if_small.gif")
register_shape(current_directory+"/Portraits/if_big.gif")
IfBoss = Unit(TurtleName="IfTurtle",
DisplayName="If",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=155,
CurrentHP=155,
ATK=30,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=999, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=39,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=250, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=45,
UnitClass="Division Head",
Attacks=[moves.Gun,moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/if_big.gif",
Sprite=current_directory+"/Sprites/if_small.gif",
LevelQuotes=["If: Imagine not even making it past the first sector."],
Bio="If Bool is the head of the First Division of Scientists\nat the Shadow Realm Research Center. He is\noften very strict, only allowing his division\nto perform under his exact conditions.")
IfBoss.TurtleName = new_turtle()
IfBoss.TurtleName.shape(IfBoss.Sprite)
IfBoss.TurtleName.hideturtle()

#Scientist1---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist1 = Unit(TurtleName="Chapter22aScientist1",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=70,
CurrentHP=70,
ATK=35,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=65, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=145, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Scientist",
Attacks=[moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Ice"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist1.TurtleName = new_turtle()
Chapter22aScientist1.TurtleName.shape(Chapter22aScientist1.Sprite)
Chapter22aScientist1.TurtleName.hideturtle()

#Scientist2---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist2 = Unit(TurtleName="Chapter22aScientist2",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=35,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=65, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=34,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=145, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Scientist",
Attacks=[moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Fire"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist2.TurtleName = new_turtle()
Chapter22aScientist2.TurtleName.shape(Chapter22aScientist2.Sprite)
Chapter22aScientist2.TurtleName.hideturtle()

#Scientist3---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist3 = Unit(TurtleName="Chapter22aScientist3",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=37,#3, #Influences attack damage
DEF=15, #Influences damage taken from physical attacks
RES=65, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=145, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Scientist",
Attacks=[moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist3.TurtleName = new_turtle()
Chapter22aScientist3.TurtleName.shape(Chapter22aScientist3.Sprite)
Chapter22aScientist3.TurtleName.hideturtle()

#Scientist4---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist4 = Unit(TurtleName="Chapter22aScientist4",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=37,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=80, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=35,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=145, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Scientist",
Attacks=[moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Electric"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist4.TurtleName = new_turtle()
Chapter22aScientist4.TurtleName.shape(Chapter22aScientist4.Sprite)
Chapter22aScientist4.TurtleName.hideturtle()

#Scientist5---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist5 = Unit(TurtleName="Chapter22aScientist5",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=90,
CurrentHP=90,
ATK=29,#3, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=27, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=145, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=40,
UnitClass="Scientist",
Attacks=[moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Bio"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist5.TurtleName = new_turtle()
Chapter22aScientist5.TurtleName.shape(Chapter22aScientist5.Sprite)
Chapter22aScientist5.TurtleName.hideturtle()

#Scientist6---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist6 = Unit(TurtleName="Chapter22aScientist6",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=30,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=65, #Influences damage taken from magic attacks
AGL=27, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=38,
UnitClass="Scientist",
Attacks=[moves.Scalpel],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: The Itucher is ours."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist6.TurtleName = new_turtle()
Chapter22aScientist6.TurtleName.shape(Chapter22aScientist6.Sprite)
Chapter22aScientist6.TurtleName.hideturtle()

#Scientist7---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist7 = Unit(TurtleName="Chapter22aScientist7",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=30,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=75, #Influences damage taken from magic attacks
AGL=27, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=38,
UnitClass="Scientist",
Attacks=[moves.Scalpel],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Scientist", "Fire"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: The Itucher is ours."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist7.TurtleName = new_turtle()
Chapter22aScientist7.TurtleName.shape(Chapter22aScientist7.Sprite)
Chapter22aScientist7.TurtleName.hideturtle()

#Scientist8---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist8 = Unit(TurtleName="Chapter22aScientist8",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=70,
CurrentHP=70,
ATK=30,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=75, #Influences damage taken from magic attacks
AGL=27, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=38,
UnitClass="Scientist",
Attacks=[moves.Scalpel],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Scientist", "Bio"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: The Itucher is ours."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist8.TurtleName = new_turtle()
Chapter22aScientist8.TurtleName.shape(Chapter22aScientist8.Sprite)
Chapter22aScientist8.TurtleName.hideturtle()

#Scientist9---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist9 = Unit(TurtleName="Chapter22aScientist9",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=90,
CurrentHP=90,
ATK=18,#3, #Influences attack damage
DEF=5, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=38,
UnitClass="Scientist",
Attacks=[moves.Scalpel],
Supports=[moves.MedKit],
Traits=["Physical Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist9.TurtleName = new_turtle()
Chapter22aScientist9.TurtleName.shape(Chapter22aScientist9.Sprite)
Chapter22aScientist9.TurtleName.hideturtle()

#Scientist10---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist10 = Unit(TurtleName="Chapter22aScientist10",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=18,#3, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=70, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=41,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=38,
UnitClass="Scientist",
Attacks=[moves.Scalpel],
Supports=[moves.MedKit],
Traits=["Physical Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist10.TurtleName = new_turtle()
Chapter22aScientist10.TurtleName.shape(Chapter22aScientist10.Sprite)
Chapter22aScientist10.TurtleName.hideturtle()

#Scientist11---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter22aScientist11 = Unit(TurtleName="Chapter22aScientist11",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=55,
CurrentHP=55,
ATK=22,#3, #Influences attack damage
DEF=8, #Influences damage taken from physical attacks
RES=50, #Influences damage taken from magic attacks
AGL=23, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=39,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=125, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=38,
UnitClass="Scientist",
Attacks=[moves.Gun],
Supports=[],
Traits=["Physical Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the First\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter22aScientist11.TurtleName = new_turtle()
Chapter22aScientist11.TurtleName.shape(Chapter22aScientist11.Sprite)
Chapter22aScientist11.TurtleName.hideturtle()


#==============================================================================================================================================================================================================================================================================
#===============[Chapter 23a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Elif---------------
register_shape(current_directory+"/Sprites/elif_small.gif")
register_shape(current_directory+"/Portraits/elif_big.gif")
ElifBoss = Unit(TurtleName="ElifTurtle",
DisplayName="Elif",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=200,
CurrentHP=200,
ATK=20,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=300, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=48,
UnitClass="Division Head",
Attacks=[moves.Gun,moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Darkness"],
Portrait=current_directory+"/Portraits/elif_big.gif",
Sprite=current_directory+"/Sprites/elif_small.gif",
LevelQuotes=["Elif: It seems like my tactics are succeeding."],
Bio="Elif Int is the head of the Second Division of Scientists at the Shadow Realm Research Center.\nHe is the most lenient of the four division heads, being open to most\nalternate options. He is also the founder and leader of the Sci-Triptych Sectoral Board,\na board of the first three Division Heads of the Shadow Realm\nResearch Lab to which he often discusses alternate courses of\nactions that could be taken at the lab.")
ElifBoss.TurtleName = new_turtle()
ElifBoss.TurtleName.shape(ElifBoss.Sprite)
ElifBoss.TurtleName.hideturtle()

#Scientist1---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist1 = Unit(TurtleName="Chapter23aScientist1",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=165, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=42,
UnitClass="Scientist",
Attacks=[moves.Gun,moves.Fireball,moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Fire"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist1.TurtleName = new_turtle()
Chapter23aScientist1.TurtleName.shape(Chapter23aScientist1.Sprite)
Chapter23aScientist1.TurtleName.hideturtle()

#Scientist2---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist2 = Unit(TurtleName="Chapter23aScientist2",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=165, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=42,
UnitClass="Scientist",
Attacks=[moves.Gun,moves.Aqua,moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist2.TurtleName = new_turtle()
Chapter23aScientist2.TurtleName.shape(Chapter23aScientist2.Sprite)
Chapter23aScientist2.TurtleName.hideturtle()

#Scientist3---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist3 = Unit(TurtleName="Chapter23aScientist3",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=165, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=42,
UnitClass="Scientist",
Attacks=[moves.Gun,moves.Freeze,moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Ice"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist3.TurtleName = new_turtle()
Chapter23aScientist3.TurtleName.shape(Chapter23aScientist3.Sprite)
Chapter23aScientist3.TurtleName.hideturtle()

#Scientist4---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist4 = Unit(TurtleName="Chapter23aScientist4",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=165, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=42,
UnitClass="Scientist",
Attacks=[moves.Gun,moves.Thorn,moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Bio"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist4.TurtleName = new_turtle()
Chapter23aScientist4.TurtleName.shape(Chapter23aScientist4.Sprite)
Chapter23aScientist4.TurtleName.hideturtle()

#Scientist5---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist5 = Unit(TurtleName="Chapter23aScientist5",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=165, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=42,
UnitClass="Scientist",
Attacks=[moves.Gun,moves.Thunder,moves.Infection],
Supports=[],
Traits=["Physical Primary", "Scientist", "Electric"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist5.TurtleName = new_turtle()
Chapter23aScientist5.TurtleName.shape(Chapter23aScientist5.Sprite)
Chapter23aScientist5.TurtleName.hideturtle()

#Scientist6---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist6 = Unit(TurtleName="Chapter23aScientist6",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=28,#3, #Influences attack damage
DEF=22, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=170, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[moves.Slash,moves.Scalpel],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Scientist", "Darkness"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist6.TurtleName = new_turtle()
Chapter23aScientist6.TurtleName.shape(Chapter23aScientist6.Sprite)
Chapter23aScientist6.TurtleName.hideturtle()

#Scientist7---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist7 = Unit(TurtleName="Chapter23aScientist7",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=28,#3, #Influences attack damage
DEF=22, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=170, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[moves.Slash,moves.Scalpel],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist7.TurtleName = new_turtle()
Chapter23aScientist7.TurtleName.shape(Chapter23aScientist7.Sprite)
Chapter23aScientist7.TurtleName.hideturtle()

#Scientist8---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist8 = Unit(TurtleName="Chapter23aScientist8",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=28,#3, #Influences attack damage
DEF=22, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=170, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[moves.Slash,moves.Scalpel],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Scientist", "Fire"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist8.TurtleName = new_turtle()
Chapter23aScientist8.TurtleName.shape(Chapter23aScientist8.Sprite)
Chapter23aScientist8.TurtleName.hideturtle()

#Scientist9---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist9 = Unit(TurtleName="Chapter23aScientist9",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=28,#3, #Influences attack damage
DEF=22, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=170, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[moves.Slash,moves.Scalpel],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Scientist", "Electric"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist9.TurtleName = new_turtle()
Chapter23aScientist9.TurtleName.shape(Chapter23aScientist9.Sprite)
Chapter23aScientist9.TurtleName.hideturtle()

#Scientist10---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter23aScientist10 = Unit(TurtleName="Chapter23aScientist10",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=28,#3, #Influences attack damage
DEF=22, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=38,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=170, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[moves.Slash,moves.Scalpel],
Supports=[moves.LongHeal],
Traits=["Physical Primary", "Scientist", "Ice"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Second\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter23aScientist10.TurtleName = new_turtle()
Chapter23aScientist10.TurtleName.shape(Chapter23aScientist10.Sprite)
Chapter23aScientist10.TurtleName.hideturtle()

#Archer1---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter23aArcher1 = Unit(TurtleName="Chapter23aArcher1",
DisplayName="Guard",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=26, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=39,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=195, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=45,
UnitClass="Archer",
Attacks=[moves.SnipeII,moves.BowPlus],
Supports=[],
Traits=["Physical Primary","Archer","Darkness"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Guard: You must be eliminated."],
Bio="A guard at the Shadow Realm Research Lab.")
Chapter23aArcher1.TurtleName = new_turtle()
Chapter23aArcher1.TurtleName.shape(Chapter23aArcher1.Sprite)
Chapter23aArcher1.TurtleName.hideturtle()

#Archer2---------------
register_shape(current_directory+"/Sprites/genericarcher_small.gif")
register_shape(current_directory+"/Portraits/genericarcher_big.gif")
Chapter23aArcher2 = Unit(TurtleName="Chapter23aArcher2",
DisplayName="Guard",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=35,
CurrentHP=35,
ATK=15,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=26, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=39,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=195, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=45,
UnitClass="Archer",
Attacks=[moves.SnipeII,moves.BowPlus],
Supports=[],
Traits=["Physical Primary","Archer","Ice"],
Portrait=current_directory+"/Portraits/genericarcher_big.gif",
Sprite=current_directory+"/Sprites/genericarcher_small.gif",
LevelQuotes=["Guard: You must be eliminated."],
Bio="A guard at the Shadow Realm Research Lab.")
Chapter23aArcher2.TurtleName = new_turtle()
Chapter23aArcher2.TurtleName.shape(Chapter23aArcher2.Sprite)
Chapter23aArcher2.TurtleName.hideturtle()


#==============================================================================================================================================================================================================================================================================
#===============[Chapter 24a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Else---------------
register_shape(current_directory+"/Sprites/else_small.gif")
register_shape(current_directory+"/Portraits/else_big.gif")
ElseBoss = Unit(TurtleName="ElseTurtle",
DisplayName="Else",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=250,
CurrentHP=250,
ATK=20,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=20, #Influences damage taken from magic attacks
AGL=20, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=40,
SPD=4, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=320, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=50,
UnitClass="Division Head",
Attacks=[moves.VoltBlades,moves.Cut],
Supports=[],
Traits=["Physical Primary", "Scientist", "Electric"],
Portrait=current_directory+"/Portraits/else_big.gif",
Sprite=current_directory+"/Sprites/else_small.gif",
LevelQuotes=["Else: Yes!"],
Bio="Else Do is the head of the Third Division of Scientists at the Shadow Realm Research Center.\nHe often does the opposite of what the others do,\nand has a very strong stance on the preservation of\nobsucure technology and spells. As well, he acts as the advisor of the\nSci-Triptych Sectoral Board; though it's frankly an useless title in such a\n powerless and small organization.")
ElseBoss.TurtleName = new_turtle()
ElseBoss.TurtleName.shape(ElseBoss.Sprite)
ElseBoss.TurtleName.hideturtle()

#Scientist1---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist1 = Unit(TurtleName="Chapter24aScientist1",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[moves.Missile,moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Scientist", "Fire"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist1.TurtleName = new_turtle()
Chapter24aScientist1.TurtleName.shape(Chapter24aScientist1.Sprite)
Chapter24aScientist1.TurtleName.hideturtle()

#Scientist2---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist2 = Unit(TurtleName="Chapter24aScientist2",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=50,
CurrentHP=50,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[moves.Missile,moves.Dagger],
Supports=[],
Traits=["Physical Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist2.TurtleName = new_turtle()
Chapter24aScientist2.TurtleName.shape(Chapter24aScientist2.Sprite)
Chapter24aScientist2.TurtleName.hideturtle()

#Scientist3---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist3 = Unit(TurtleName="Chapter24aScientist3",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=25,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.Hydra,moves.Punch],
Supports=[],
Traits=["Magic Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist3.TurtleName = new_turtle()
Chapter24aScientist3.TurtleName.shape(Chapter24aScientist3.Sprite)
Chapter24aScientist3.TurtleName.hideturtle()

#Scientist4---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist4 = Unit(TurtleName="Chapter24aScientist3",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=25,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.ShadowBurst,moves.Punch],
Supports=[],
Traits=["Magic Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist4.TurtleName = new_turtle()
Chapter24aScientist4.TurtleName.shape(Chapter24aScientist4.Sprite)
Chapter24aScientist4.TurtleName.hideturtle()

#Scientist5---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist5 = Unit(TurtleName="Chapter24aScientist5",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=25,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=30, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.ManaBurst,moves.Punch],
Supports=[],
Traits=["Magic Primary", "Scientist", "Ice"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist5.TurtleName = new_turtle()
Chapter24aScientist5.TurtleName.shape(Chapter24aScientist5.Sprite)
Chapter24aScientist5.TurtleName.hideturtle()

#Scientist6---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist6 = Unit(TurtleName="Chapter24aScientist6",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=3,
CurrentHP=3,
ATK=20,#3, #Influences attack damage
DEF=9999999, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=22, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=185, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=45,
UnitClass="Scientist",
Attacks=[moves.Countdown,moves.Death],
Supports=[],
Traits=["Physical Primary", "Scientist", "Bio"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist6.TurtleName = new_turtle()
Chapter24aScientist6.TurtleName.shape(Chapter24aScientist6.Sprite)
Chapter24aScientist6.TurtleName.hideturtle()

#Scientist7---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist7 = Unit(TurtleName="Chapter24aScientist7",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=5,
CurrentHP=5,
ATK=20,#3, #Influences attack damage
DEF=9999999, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=22, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=185, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=45,
UnitClass="Scientist",
Attacks=[moves.Countdown,moves.Death],
Supports=[],
Traits=["Physical Primary", "Scientist", "Bio"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist7.TurtleName = new_turtle()
Chapter24aScientist7.TurtleName.shape(Chapter24aScientist7.Sprite)
Chapter24aScientist7.TurtleName.hideturtle()

#Scientist8---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist8 = Unit(TurtleName="Chapter24aScientist8",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=5,
CurrentHP=5,
ATK=20,#3, #Influences attack damage
DEF=9999999, #Influences damage taken from physical attacks
RES=0, #Influences damage taken from magic attacks
AGL=22, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=185, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=45,
UnitClass="Scientist",
Attacks=[moves.Countdown,moves.Death],
Supports=[],
Traits=["Physical Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist8.TurtleName = new_turtle()
Chapter24aScientist8.TurtleName.shape(Chapter24aScientist8.Sprite)
Chapter24aScientist8.TurtleName.hideturtle()

#Scientist9---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter24aScientist9 = Unit(TurtleName="Chapter24aScientist9",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=80,
CurrentHP=80,
ATK=24,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=45, #Influences damage taken from magic attacks
AGL=26, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=39,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=195, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=47,
UnitClass="Scientist",
Attacks=[moves.Aura,moves.Finisher],
Supports=[],
Traits=["Physical Primary", "Scientist", "Fire"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter24aScientist9.TurtleName = new_turtle()
Chapter24aScientist9.TurtleName.shape(Chapter24aScientist9.Sprite)
Chapter24aScientist9.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 25a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#BreakItucher---------------
register_shape(current_directory+"/Sprites/break2_small.gif")
register_shape(current_directory+"/Portraits/break2_big.gif")
BreakItucher = Unit(TurtleName="BreakItucherTurtle",
DisplayName="Break",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=650,
CurrentHP=650,
ATK=28,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=40, #Influences damage taken from magic attacks
AGL=28, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=25, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=500, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=65,
UnitClass="Wielder of the Holy Itucher",
Attacks=[moves.BreaksItucher,moves.VenomBlade],
Supports=[],
Traits=["Physical Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/break2_big.gif",
Sprite=current_directory+"/Sprites/break2_small.gif",
LevelQuotes=["Break: AHAHAHAHAHAHHAHAHAHAHAHA!!!"],
Bio="Break is successfully wielding the Holy Itucher. As well as this, he has activated his\nAlg Formation and his Unique Spell, Depravity.\nDepravity allows him to move extremely quickly and provides a massive boost\n to his physical strength and magica generation while actiavted. However, his power,\n due to the combination of the Holy Itucher, Alg Formation, and Depravity;\nis starting to go beyond what his body can handle.")
BreakItucher.TurtleName = new_turtle()
BreakItucher.TurtleName.shape(BreakItucher.Sprite)
BreakItucher.TurtleName.hideturtle()

#Scientist1---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter25aScientist1 = Unit(TurtleName="Chapter25aScientist1",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Electric"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter25aScientist1.TurtleName = new_turtle()
Chapter25aScientist1.TurtleName.shape(Chapter25aScientist1.Sprite)
Chapter25aScientist1.TurtleName.hideturtle()

#Scientist2---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter25aScientist2 = Unit(TurtleName="Chapter25aScientist2",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Fire"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter25aScientist2.TurtleName = new_turtle()
Chapter25aScientist2.TurtleName.shape(Chapter25aScientist2.Sprite)
Chapter25aScientist2.TurtleName.hideturtle()

#Scientist3---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter25aScientist3 = Unit(TurtleName="Chapter25aScientist3",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Ice"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter25aScientist3.TurtleName = new_turtle()
Chapter25aScientist3.TurtleName.shape(Chapter25aScientist3.Sprite)
Chapter25aScientist3.TurtleName.hideturtle()

#Scientist4---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter25aScientist4 = Unit(TurtleName="Chapter25aScientist4",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter25aScientist4.TurtleName = new_turtle()
Chapter25aScientist4.TurtleName.shape(Chapter25aScientist4.Sprite)
Chapter25aScientist4.TurtleName.hideturtle()

#Scientist5---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter25aScientist5 = Unit(TurtleName="Chapter25aScientist5",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Bio"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter25aScientist5.TurtleName = new_turtle()
Chapter25aScientist5.TurtleName.shape(Chapter25aScientist5.Sprite)
Chapter25aScientist5.TurtleName.hideturtle()

#Scientist6---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter25aScientist6 = Unit(TurtleName="Chapter25aScientist6",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Third\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter25aScientist6.TurtleName = new_turtle()
Chapter25aScientist6.TurtleName.shape(Chapter25aScientist6.Sprite)
Chapter25aScientist6.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 25b]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Breakc25b---------------
register_shape(current_directory+"/Sprites/break_small.gif")
register_shape(current_directory+"/Portraits/break_big.gif")
Breakc25b = Unit(TurtleName="Breakc25bTurtle",
DisplayName="Break",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=300,
CurrentHP=300,
ATK=23,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=40, #Influences damage taken from magic attacks
AGL=28, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=42,
SPD=10, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=265, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=52,
UnitClass="Division Head",
Attacks=[moves.VenomBlade],
Supports=[],
Traits=["Physical Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/break_big.gif",
Sprite=current_directory+"/Sprites/break_small.gif",
LevelQuotes=["Break: Fall to my power, fools."],
Bio="Break is the head of the Fourth Division of\nScientists at the Shadow Realm Research Lab,\nand is the second-highest ranking official\nat the Shadow Realm Research Lab. He is the\nonly Division Head not part of the Sci-Triptych Sectoral Board.")
Breakc25b.TurtleName = new_turtle()
Breakc25b.TurtleName.shape(Breakc25b.Sprite)
Breakc25b.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 26a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#DeathPepperBoss---------------
register_shape(current_directory+"/Sprites/deathpepper_small.gif")
register_shape(current_directory+"/Portraits/deathpepper_big.gif")
DeathPepperBoss = Unit(TurtleName="DeathPepperBossTurtle",
DisplayName="Death Pepper",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=350,
CurrentHP=350,
ATK=14,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=45, #Influences damage taken from magic attacks
AGL=27, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=45,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=550, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=55,
UnitClass="Division Head",
Attacks=[moves.GodSlash,moves.Gun],
Supports=[],
Traits=["Physical Primary", "Scientist", "Xuir", "Fire"],
Portrait=current_directory+"/Portraits/deathpepper_big.gif",
Sprite=current_directory+"/Sprites/deathpepper_small.gif",
LevelQuotes=["Death Pepper: This is what you get for defying me."],
Bio="Death Pepper is the head of the Shadow Realm Research Center,\nwhere he has been tasked by Neville Prime to create entities with the powers\nof True Xuir. Though the research of recreating the\npowers of True Xuir have been going on for centuries,\nDeath Pepper has come the closest to discovering the secret of\nactivating the power of the True Xuir.")
DeathPepperBoss.TurtleName = new_turtle()
DeathPepperBoss.TurtleName.shape(DeathPepperBoss.Sprite)
DeathPepperBoss.TurtleName.hideturtle()

#Armored1---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter26aArmored1 = Unit(TurtleName="Chapter26aArmored1",
DisplayName="Guard",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=150,
CurrentHP=150,
ATK=29,#3, #Influences attack damage
DEF=60, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=41,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=275, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=37,
UnitClass="Death Pepper's Guard",
Attacks=[moves.HeavyBow],
Supports=[],
Traits=["Physical Primary", "Fire","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Guard: You can't defeat me."],
Bio="Death Pepper's Guard.")
Chapter26aArmored1.TurtleName = new_turtle()
Chapter26aArmored1.TurtleName.shape(Chapter26aArmored1.Sprite)
Chapter26aArmored1.TurtleName.hideturtle()

#Armored2---------------
register_shape(current_directory+"/Sprites/genericarmored_small.gif")
register_shape(current_directory+"/Portraits/genericarmored_big.gif")
Chapter26aArmored2 = Unit(TurtleName="Chapter26aArmored2",
DisplayName="Guard",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=150,
CurrentHP=150,
ATK=29,#3, #Influences attack damage
DEF=60, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=41,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=275, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=37,
UnitClass="Death Pepper's Guard",
Attacks=[moves.HeavyBow],
Supports=[],
Traits=["Physical Primary", "Ice","Armored"],
Portrait=current_directory+"/Portraits/genericarmored_big.gif",
Sprite=current_directory+"/Sprites/genericarmored_small.gif",
LevelQuotes=["Guard: You can't defeat me."],
Bio="Death Pepper's Guard.")
Chapter26aArmored2.TurtleName = new_turtle()
Chapter26aArmored2.TurtleName.shape(Chapter26aArmored2.Sprite)
Chapter26aArmored2.TurtleName.hideturtle()

#Scientist1---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist1 = Unit(TurtleName="Chapter26aScientist1",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Electric"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist1.TurtleName = new_turtle()
Chapter26aScientist1.TurtleName.shape(Chapter26aScientist1.Sprite)
Chapter26aScientist1.TurtleName.hideturtle()

#Scientist2---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist2 = Unit(TurtleName="Chapter26aScientist2",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist2.TurtleName = new_turtle()
Chapter26aScientist2.TurtleName.shape(Chapter26aScientist2.Sprite)
Chapter26aScientist2.TurtleName.hideturtle()

#Scientist3---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist3 = Unit(TurtleName="Chapter26aScientist3",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=45,
CurrentHP=45,
ATK=9999,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=24, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=9999,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=175, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=43,
UnitClass="Scientist",
Attacks=[],
Supports=[moves.FarHeal],
Traits=["Physical Primary", "Scientist", "Bio"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist3.TurtleName = new_turtle()
Chapter26aScientist3.TurtleName.shape(Chapter26aScientist3.Sprite)
Chapter26aScientist3.TurtleName.hideturtle()

#Scientist4---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist4 = Unit(TurtleName="Chapter26aScientist4",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.HyperSlash,moves.Gun],
Supports=[],
Traits=["Magic Primary", "Scientist", "Ice"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist4.TurtleName = new_turtle()
Chapter26aScientist4.TurtleName.shape(Chapter26aScientist4.Sprite)
Chapter26aScientist4.TurtleName.hideturtle()

#Scientist5---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist5 = Unit(TurtleName="Chapter26aScientist5",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.HyperSlash,moves.Gun],
Supports=[],
Traits=["Magic Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist5.TurtleName = new_turtle()
Chapter26aScientist5.TurtleName.shape(Chapter26aScientist5.Sprite)
Chapter26aScientist5.TurtleName.hideturtle()

#Scientist6---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist6 = Unit(TurtleName="Chapter26aScientist6",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=35, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.HyperSlash,moves.Gun],
Supports=[],
Traits=["Magic Primary", "Scientist", "Electric"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist6.TurtleName = new_turtle()
Chapter26aScientist6.TurtleName.shape(Chapter26aScientist6.Sprite)
Chapter26aScientist6.TurtleName.hideturtle()

#Scientist7---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist7 = Unit(TurtleName="Chapter26aScientist7",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=18,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=999, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.FireBlast],
Supports=[],
Traits=["Magic Primary", "Scientist", "Fire"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist7.TurtleName = new_turtle()
Chapter26aScientist7.TurtleName.shape(Chapter26aScientist7.Sprite)
Chapter26aScientist7.TurtleName.hideturtle()

#Scientist8---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist8 = Unit(TurtleName="Chapter26aScientist8",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=18,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=999, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.ThunderBlast],
Supports=[],
Traits=["Magic Primary", "Scientist", "Electric"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist8.TurtleName = new_turtle()
Chapter26aScientist8.TurtleName.shape(Chapter26aScientist8.Sprite)
Chapter26aScientist8.TurtleName.hideturtle()

#Scientist9---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist9 = Unit(TurtleName="Chapter26aScientist9",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=18,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=999, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.Hydro],
Supports=[],
Traits=["Magic Primary", "Scientist", "Water"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist9.TurtleName = new_turtle()
Chapter26aScientist9.TurtleName.shape(Chapter26aScientist9.Sprite)
Chapter26aScientist9.TurtleName.hideturtle()

#Scientist10---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist10 = Unit(TurtleName="Chapter26aScientist10",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=18,#3, #Influences attack damage
DEF=999, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.Infection,moves.HeavyBow],
Supports=[],
Traits=["Magic Primary", "Scientist", "Bio"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist10.TurtleName = new_turtle()
Chapter26aScientist10.TurtleName.shape(Chapter26aScientist10.Sprite)
Chapter26aScientist10.TurtleName.hideturtle()

#Scientist11---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist11 = Unit(TurtleName="Chapter26aScientist11",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=18,#3, #Influences attack damage
DEF=999, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.Infection,moves.HeavyBow],
Supports=[],
Traits=["Magic Primary", "Scientist", "Shadow"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist11.TurtleName = new_turtle()
Chapter26aScientist11.TurtleName.shape(Chapter26aScientist11.Sprite)
Chapter26aScientist11.TurtleName.hideturtle()

#Scientist12---------------
register_shape(current_directory+"/Sprites/genericscientist_small.gif")
register_shape(current_directory+"/Portraits/genericscientist_big.gif")
Chapter26aScientist12 = Unit(TurtleName="Chapter26aScientist12",
DisplayName="Scientist",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=75,
CurrentHP=75,
ATK=18,#3, #Influences attack damage
DEF=999, #Influences damage taken from physical attacks
RES=5, #Influences damage taken from magic attacks
AGL=25, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=37,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=180, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=44,
UnitClass="Scientist",
Attacks=[moves.Infection,moves.HeavyBow],
Supports=[],
Traits=["Magic Primary", "Scientist", "Ice"],
Portrait=current_directory+"/Portraits/genericscientist_big.gif",
Sprite=current_directory+"/Sprites/genericscientist_small.gif",
LevelQuotes=["Scientist: You must be eliminated."],
Bio="A scientist working in the Fifth\nDivision of Scientists at the\nShadow Realm Research Center.")
Chapter26aScientist12.TurtleName = new_turtle()
Chapter26aScientist12.TurtleName.shape(Chapter26aScientist12.Sprite)
Chapter26aScientist12.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 27a]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#QuestBoss---------------
register_shape(current_directory+"/Sprites/questitucher_small.gif")
register_shape(current_directory+"/Portraits/questitucher_big.gif")
QuestBoss = Unit(TurtleName="QuestBossTurtle",
DisplayName="Quest",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=2500,
CurrentHP=2500,
ATK=50,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=45, #Influences damage taken from magic attacks
AGL=26, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=58,
SPD=7, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=850, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=75,
UnitClass="Wielder of the Holy Itucher",
Attacks=[moves.GodSlash,moves.QuestsItucher],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/questitucher_big.gif",
Sprite=current_directory+"/Sprites/questitucher_small.gif",
LevelQuotes=["Quest: ..."],
Bio="Quest has been possessed by the Holy Itucher,\nand has lost his free will. He now\nacts upon the Will of the Itucher.")
QuestBoss.TurtleName = new_turtle()
QuestBoss.TurtleName.shape(QuestBoss.Sprite)
QuestBoss.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 27b]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#RepinsBoss1---------------
register_shape(current_directory+"/Sprites/repins_small2.gif")
register_shape(current_directory+"/Portraits/repins_big3.gif")
RepinsBoss1 = Unit(TurtleName="RepinsBoss1Turtle",
DisplayName="Repins",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=750,
CurrentHP=750,
ATK=25,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=40, #Influences damage taken from magic attacks
AGL=5, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=125,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=500, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=65,
UnitClass="Wielder of the Holy Itucher",
Attacks=[moves.RepinsItucher,moves.Snipe],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/repins_big3.gif",
Sprite=current_directory+"/Sprites/repins_small2.gif",
LevelQuotes=["Repins: ..."],
Bio="Repins has become possessed by the\nHoly Itucher, he has lost his free will.")
RepinsBoss1.TurtleName = new_turtle()
RepinsBoss1.TurtleName.shape(RepinsBoss1.Sprite)
RepinsBoss1.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 27c]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#RepinsBoss2---------------
register_shape(current_directory+"/Sprites/repins_small3.gif")
register_shape(current_directory+"/Portraits/repins_big4.gif")
RepinsBoss2 = Unit(TurtleName="RepinsBoss2Turtle",
DisplayName="Repins",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=1000,
CurrentHP=1000,
ATK=40,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=40, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=250,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=1500, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=250,
UnitClass="Master of the Holy Itucher",
Attacks=[moves.RepinsItucher],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/repins_big4.gif",
Sprite=current_directory+"/Sprites/repins_small3.gif",
LevelQuotes=["Repins: AHAHAHA!!! THIS IS POWER!!!"],
Bio="Repins has obtained the power of the\nHoly Itucher, and has gained an immense amount of power.\nHe has retained his free will.")
RepinsBoss2.TurtleName = new_turtle()
RepinsBoss2.TurtleName.shape(RepinsBoss2.Sprite)
RepinsBoss2.TurtleName.hideturtle()

#RepinsBoss3---------------
register_shape(current_directory+"/Sprites/repins_small3.gif")
register_shape(current_directory+"/Portraits/repins_big4.gif")
RepinsBoss3 = Unit(TurtleName="RepinsBoss3Turtle",
DisplayName="Repins",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=500,
CurrentHP=500,
ATK=20,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=40, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=250,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=2550, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=275,
UnitClass="Master of the Holy Itucher",
Attacks=[moves.RepinsItucher],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/repins_big4.gif",
Sprite=current_directory+"/Sprites/repins_small3.gif",
LevelQuotes=["Repins: You won't... be defeating me..."],
Bio="Repins has been weakened, but is still\nstrong enough to fight.")
RepinsBoss3.TurtleName = new_turtle()
RepinsBoss3.TurtleName.shape(RepinsBoss3.Sprite)
RepinsBoss3.TurtleName.hideturtle()

#RepinsBoss4---------------
register_shape(current_directory+"/Sprites/repins_small3.gif")
register_shape(current_directory+"/Portraits/repins_big4.gif")
RepinsBoss4 = Unit(TurtleName="RepinsBoss4Turtle",
DisplayName="Repins",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=350,
CurrentHP=350,
ATK=10,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=40, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=250,
SPD=0, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=6000, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=350,
UnitClass="Master of the Holy Itucher",
Attacks=[moves.RepinsItucher],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/repins_big4.gif",
Sprite=current_directory+"/Sprites/repins_small3.gif",
LevelQuotes=["Repins: Yes..."],
Bio="Repins has been extremely weakened,\nhe can barely fight.")
RepinsBoss4.TurtleName = new_turtle()
RepinsBoss4.TurtleName.shape(RepinsBoss4.Sprite)
RepinsBoss4.TurtleName.hideturtle()

#RepinsBoss5---------------
register_shape(current_directory+"/Sprites/repins_small3.gif")
register_shape(current_directory+"/Portraits/repins_big4.gif")
RepinsBoss5 = Unit(TurtleName="RepinsBoss5Turtle",
DisplayName="Repins",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=9999,
CurrentHP=9999,
ATK=45,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=99999, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=99999,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=9000, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=500,
UnitClass="Master of the Holy Itucher",
Attacks=[moves.RepinsItucher],
Supports=[],
Traits=["Physical Primary", "Shadow"],
Portrait=current_directory+"/Portraits/repins_big4.gif",
Sprite=current_directory+"/Sprites/repins_small3.gif",
LevelQuotes=["Repins: THIS IS THE END!!!!!!!"],
Bio="Repins has obtained the power of the\nHoly Itucher, and has gained an immense amount of power.\nHe has retained his free will.")
RepinsBoss5.TurtleName = new_turtle()
RepinsBoss5.TurtleName.shape(RepinsBoss5.Sprite)
RepinsBoss5.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 27d]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#VruhBoss------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/vruh_small.gif")
register_shape(current_directory+"/Portraits/vruh_big.gif")
VruhBoss = Unit(TurtleName="VruhBossTurtle",
DisplayName="Vruh",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=30,
CurrentHP=30,
ATK=15, #Influences attack damage
DEF=10, #Influences damage taken from physical attacks
RES=7, #Influences damage taken from magic attacks
AGL=4, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=11,
SPD=2, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=15,
UnitClass="Fighter",
Attacks=[moves.Punch],
Supports=[],
Traits=["Physical Primary","Bipolian","Fighter"],
HPGrowth=[70,1], #Chance to level up, max amount to increase
ATKGrowth=[50,1],
DEFGrowth=[50,1],
RESGrowth=[20,1],
AGLGrowth=[40,1],
ACRGrowth=[60,1],
Portrait=current_directory+"/Portraits/vruh_big.gif",
Sprite=current_directory+"/Sprites/vruh_small.gif",
LevelQuotes=["Vruh: 社会はあなたの心の構成物にすぎません。","景気後退が私たちに迫っています。"],
Bio="yuh aye nolan got waves\nplayed neville os for ninety four days straight",
ClassChange=[], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
VruhBoss.TurtleName = new_turtle()
VruhBoss.TurtleName.shape(Vruh.Sprite)
VruhBoss.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 27e]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#Etamitlu---------------
register_shape(current_directory+"/Sprites/ultimatemechanical_small.gif")
register_shape(current_directory+"/Portraits/ultimatemechanical_big.gif")
Etamitlu = Unit(TurtleName="EtamitluTurtle",
DisplayName="Etamitlu",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=1000,
CurrentHP=1000,
ATK=30,#3, #Influences attack damage
DEF=20, #Influences damage taken from physical attacks
RES=40, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=250,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=1750, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=250,
UnitClass="The Ultimate Mechanical",
Attacks=[moves.GodSlash],
Supports=[],
Traits=["Physical Primary", "Electric"],
Portrait=current_directory+"/Portraits/ultimatemechanical_big.gif",
Sprite=current_directory+"/Sprites/ultimatemechanical_small.gif",
LevelQuotes=["Etamitlu: ..."],
Bio="🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢\n🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢\n🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢\n🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢\n🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢\n🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢\n🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢🁢")
Etamitlu.TurtleName = new_turtle()
Etamitlu.TurtleName.shape(Etamitlu.Sprite)
Etamitlu.TurtleName.hideturtle()

#AhcemBoss------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/ahcem_small.gif")
register_shape(current_directory+"/Portraits/ahcem_big.gif")
AhcemBoss = Unit(TurtleName="AhcemBossTurtle",
DisplayName="Ahcem",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=200,
CurrentHP=200,
ATK=35, #Influences attack damage
DEF=39, #Influences damage taken from physical attacks
RES=19, #Influences damage taken from magic attacks
AGL=19, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=44,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=60,
UnitClass="Mechanical Entity",
Attacks=[moves.Slash,moves.Beam],
Supports=[moves.FarHeal],
Traits=["Physical Primary","Mechanical","Fighter"],
HPGrowth=[90,1], #Chance to level up, max amount to increase
ATKGrowth=[65,1],
DEFGrowth=[50,1],
RESGrowth=[25,1],
AGLGrowth=[30,1],
ACRGrowth=[95,1],
Portrait=current_directory+"/Portraits/ahcem_big.gif",
Sprite=current_directory+"/Sprites/ahcem_small.gif",
LevelQuotes=["Achem: Destruction."],
Bio="???",
ClassChange=[], #[Name, Level]
AttackUnlocks=[], #[[Attack,Level],[Attack,Level],[Attack,Level]]
SupportUnlocks=[])
AhcemBoss.TurtleName = new_turtle()
AhcemBoss.TurtleName.shape(Ahcem.Sprite)
AhcemBoss.TurtleName.hideturtle()

#==============================================================================================================================================================================================================================================================================
#===============[Chapter 27f]=======================================================================================================================================
#==============================================================================================================================================================================================================================================================================

#XuirWrath1---------------
register_shape(current_directory+"/Portraits/xuirwrath_big2.gif")
register_shape(current_directory+"/Sprites/xuirwrath_small2.gif")
XuirWrath1 = Unit(TurtleName="XuirWrath1",
DisplayName="▓THE▓XUIR▓WRATH▓",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=5000,
CurrentHP=5000,
ATK=25,#3, #Influences attack damage
DEF=25, #Influences damage taken from physical attacks
RES=25, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=50,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=0, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=70317031,
UnitClass="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓",
Attacks=[moves.XuirWrathSlice],
Supports=[],
Traits=["▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓", "▓▓▓▓▓▓▓▓▓▓▓▓","▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓","▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓","▓▓▓▓▓▓▓▓▓▓▓▓▓"],
Portrait=current_directory+"/Portraits/xuirwrath_big2.gif",
Sprite=current_directory+"/Sprites/xuirwrath_small2.gif",
LevelQuotes=["▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"],
Bio="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓\n▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓\n▓▓▓▓▓ ▓ ▓▓▓▓ ▓▓▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓▓▓▓▓")
XuirWrath1.TurtleName = new_turtle()
XuirWrath1.TurtleName.shape(XuirWrath1.Sprite)
XuirWrath1.TurtleName.hideturtle()

#XuirWrath2---------------
register_shape(current_directory+"/Portraits/xuirwrath_big1.gif")
register_shape(current_directory+"/Sprites/xuirwrath_small1.gif")
XuirWrath2 = Unit(TurtleName="XuirWrath2",
DisplayName="p▓▓t▓n ?",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=20,#3, #Influences attack damage
DEF=30, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=41,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=0, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=70317031,
UnitClass="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
Attacks=[moves.XuirWrathSlice],
Supports=[],
Traits=["▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓", "▓▓▓▓▓▓▓"],
Portrait=current_directory+"/Portraits/xuirwrath_big1.gif",
Sprite=current_directory+"/Sprites/xuirwrath_small1.gif",
LevelQuotes=["▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"],
Bio="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
XuirWrath2.TurtleName = new_turtle()
XuirWrath2.TurtleName.shape(XuirWrath2.Sprite)
XuirWrath2.TurtleName.hideturtle()

#XuirWrath3---------------
register_shape(current_directory+"/Portraits/xuirwrath_big1.gif")
register_shape(current_directory+"/Sprites/xuirwrath_small1.gif")
XuirWrath3 = Unit(TurtleName="XuirWrath3",
DisplayName="p▓▓t▓n ?",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=20,#3, #Influences attack damage
DEF=30, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=41,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=0, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=70317031,
UnitClass="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
Attacks=[moves.XuirWrathSlice],
Supports=[],
Traits=["▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓", "▓▓▓▓▓▓▓"],
Portrait=current_directory+"/Portraits/xuirwrath_big1.gif",
Sprite=current_directory+"/Sprites/xuirwrath_small1.gif",
LevelQuotes=["▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"],
Bio="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
XuirWrath3.TurtleName = new_turtle()
XuirWrath3.TurtleName.shape(XuirWrath3.Sprite)
XuirWrath3.TurtleName.hideturtle()

#XuirWrath4---------------
register_shape(current_directory+"/Portraits/xuirwrath_big1.gif")
register_shape(current_directory+"/Sprites/xuirwrath_small1.gif")
XuirWrath4 = Unit(TurtleName="XuirWrath4",
DisplayName="p▓▓t▓n ?",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=60,
CurrentHP=60,
ATK=20,#3, #Influences attack damage
DEF=30, #Influences damage taken from physical attacks
RES=15, #Influences damage taken from magic attacks
AGL=10, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
ACR=41,
SPD=1, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=0, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=70317031,
UnitClass="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
Attacks=[moves.XuirWrathSlice],
Supports=[],
Traits=["▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓", "▓▓▓▓▓▓▓"],
Portrait=current_directory+"/Portraits/xuirwrath_big1.gif",
Sprite=current_directory+"/Sprites/xuirwrath_small1.gif",
LevelQuotes=["▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"],
Bio="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
XuirWrath4.TurtleName = new_turtle()
XuirWrath4.TurtleName.shape(XuirWrath4.Sprite)
XuirWrath4.TurtleName.hideturtle()





























#Death Pepper------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/deathpepper_small.gif")
register_shape(current_directory+"/Portraits/deathpepper_big.gif")
DeathPepper = Unit(TurtleName="DeathPepperTurtle",
DisplayName="Death Pepper",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=3,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=2, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Head Scientist",
Attacks=[moves.Slice, moves.InfiniteTest],
Supports=[],
Traits=["Xuir","Scientist"],
HPGrowth=[100,3], #Chance to level up, max amount to increase
ATKGrowth=[100,3],
DEFGrowth=[100,2],
RESGrowth=[100,2],
AGLGrowth=[100,1],
Portrait=current_directory+"/Portraits/deathpepper_big.gif",
Sprite=current_directory+"/Sprites/deathpepper_small.gif",
LevelQuotes=["Death Pepper: This is what you get for defying me."],
Bio="Death Pepper is the head of the Shadow Realm Research Center,\nwhere he has been tasked by Neville Prime to create entities with the powers\n of True Xuir. Though the research of recreating the\n powers of True Xuir have been going on for centuries,\n Death Pepper is the closest to discovering the secret of \n activating the power of the True Xuir.")
DeathPepper.TurtleName = new_turtle()
DeathPepper.TurtleName.shape(current_directory+"/Sprites/deathpepper_small.gif")
DeathPepper.TurtleName.hideturtle()

#Death Pepper 2------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/deathpepper_small.gif")
register_shape(current_directory+"/Portraits/deathpepper_big2.gif")
DeathPepper2 = Unit(TurtleName="DeathPepper2Turtle",
DisplayName="Death Pepper",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=3,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=2, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Head Scientist",
Attacks=[moves.Slice, moves.InfiniteTest],
Supports=[],
Traits=["Xuir","Scientist"],
HPGrowth=[100,3], #Chance to level up, max amount to increase
ATKGrowth=[100,3],
DEFGrowth=[100,2],
RESGrowth=[100,2],
AGLGrowth=[100,1],
Portrait=current_directory+"/Portraits/deathpepper_big2.gif",
Sprite=current_directory+"/Sprites/deathpepper_small.gif",
LevelQuotes=["Death Pepper: This is what you get for defying me."],
Bio="Death Pepper is the head of the Shadow Realm Research Center,\nwhere he has been tasked by Neville Prime to create entities with the powers\n of True Xuir. Though the research of recreating the\n powers of True Xuir have been going on for centuries,\n Death Pepper is the closest to discovering the secret of \n activating the power of the True Xuir.")
DeathPepper2.TurtleName = new_turtle()
DeathPepper2.TurtleName.shape(current_directory+"/Sprites/deathpepper_small.gif")
DeathPepper2.TurtleName.hideturtle()

#Break------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/break_small.gif")
register_shape(current_directory+"/Portraits/break_big.gif")
Break = Unit(TurtleName="BreakTurtle",
DisplayName="Break",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=3,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=2, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Top Scientist",
Attacks=[moves.Slice, moves.InfiniteTest],
Supports=[],
Traits=["Nolavillian","Scientist"],
HPGrowth=[100,3], #Chance to level up, max amount to increase
ATKGrowth=[100,3],
DEFGrowth=[100,2],
RESGrowth=[100,2],
AGLGrowth=[100,1],
Portrait=current_directory+"/Portraits/break_big.gif",
Sprite=current_directory+"/Sprites/break_small.gif",
LevelQuotes=["Death Pepper: Are you scared?"],
Bio="Break is the head of the Fourth Division of\nScientists at the Shadow Realm Research Lab,\nand is the second-highest ranking official\nat the Shadow Realm Research Lab.")
DeathPepper.TurtleName = new_turtle()
DeathPepper.TurtleName.shape(current_directory+"/Sprites/break_small.gif")
DeathPepper.TurtleName.hideturtle()

#OmegaXuirist------------------------------------------------------------------------------------------------------------------------------------------------------------------------
register_shape(current_directory+"/Sprites/omegaxuirist_small.gif")
register_shape(current_directory+"/Portraits/omegaxuirist_big.gif")
OmegaXuirist = Unit(TurtleName="OmegaXuiristTurtle",
DisplayName="Omega",
AttackRange=[1],
PrimaryType="Physical",
MaxHP=20,
CurrentHP=20,
ATK=3,#3, #Influences attack damage
DEF=3, #Influences damage taken from physical attacks
RES=2, #Influences damage taken from magic attacks
AGL=2, #Influences the chance of getting hit by an attack, and the chance of you hitting your attack
SPD=3, #The amount of "tiles" you can move
EXP=0, #You level up every 100 EXP
EXPReward=100, #The EXP given when defeated, enemies can also level up if they defeat your units
Level=3,
UnitClass="Head Xuirist",
Attacks=[moves.Slice, moves.InfiniteTest],
Supports=[],
Traits=["Nolavillian","Scientist"],
HPGrowth=[100,3], #Chance to level up, max amount to increase
ATKGrowth=[100,3],
DEFGrowth=[100,2],
RESGrowth=[100,2],
AGLGrowth=[100,1],
Portrait=current_directory+"/Portraits/omegaxuirist_big.gif",
Sprite=current_directory+"/Sprites/omegaxuirist_small.gif",
LevelQuotes=["Death Pepper: Are you scared?"],
Bio="Death Pepper is the head of the Shadow Realm Research Center,\nwhere he has been tasked by Neville Prime to create entities with the powers\n of True Xuir. Though the research of recreating the\n powers of True Xuir have been going on for centuries,\n Death Pepper is the closest to discovering the secret of \n activating the power of the True Xuir.")
OmegaXuirist.TurtleName = new_turtle()
OmegaXuirist.TurtleName.shape(current_directory+"/Sprites/omegaxuirist_small.gif")
OmegaXuirist.TurtleName.hideturtle()

# COMMENTED OUT FOR CONVERSION
# screensetup.BattleScreen.tracer(1)
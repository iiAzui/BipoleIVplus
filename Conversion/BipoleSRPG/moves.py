ListOfAttacks = []
ListOfSupports = []
import os
current_directory = os.getcwd()

class Attack:
    def __init__(self,
    DisplayName=None,
    CombatName=None,
    MoveType=None,
    HPCost=0,
    MoveRange=1,
    PWR=1,
    HIT=1,
    HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
    Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
    ExtraMul=1.5):
        self.DisplayName = DisplayName
        self.CombatName = CombatName
        self.MoveType = MoveType
        self.HPCost = HPCost
        self.MoveRange = MoveRange
        self.PWR = PWR
        self.HIT = HIT
        self.HasExtra = HasExtra
        self.Extra = Extra
        self.ExtraMul = ExtraMul

class Support:
    def __init__(self,
    DisplayName=None,
    CombatName=None,
    MoveType=None,
    HPCost=0,
    MoveRange=1,
    PWR=1,
    HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
    Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
    ExtraMul=1.5):
        self.DisplayName = DisplayName
        self.CombatName = CombatName
        self.MoveType = MoveType
        self.HPCost = HPCost
        self.MoveRange = MoveRange
        self.PWR = PWR
        self.HasExtra = HasExtra
        self.Extra = Extra
        self.ExtraMul = ExtraMul

InfiniteTest = Attack(
DisplayName="InfiniteTest (1)",
CombatName="InfiniteTest",
MoveType="Magic",
HPCost=1,
MoveRange="Infinite",
PWR=1.5,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(InfiniteTest)

DeclinedRepins = Attack(
DisplayName="DeclinedRepins",
CombatName="DeclinedRepins",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(DeclinedRepins)

ErifWasThere = Attack(
DisplayName="ErifWasThere",
CombatName="ErifWasThere",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(ErifWasThere)

WobWasThere = Attack(
DisplayName="WobWasThere",
CombatName="WobWasThere",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(WobWasThere)

BothDead = Attack(
DisplayName="BothDead",
CombatName="BothDead",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(BothDead)

OneDead = Attack(
DisplayName="OneDead",
CombatName="OneDead",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(OneDead)

Slice = Attack(
DisplayName="Slice",
CombatName="Slice",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.5,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Slice)

XuirWrathSlice = Attack(
DisplayName="XuirWrathSlice",
CombatName="#####",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.5,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(XuirWrathSlice)

Axe = Attack(
DisplayName="Axe",
CombatName="Axe",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.75,
HIT=0.8,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Axe)

AxeThrow = Attack(
DisplayName="Axe Throw",
CombatName="Axe Throw",
MoveType="Physical",
HPCost=0,
MoveRange=2,
PWR=1.75,
HIT=0.7,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(AxeThrow)

Execution = Attack(
DisplayName="Execution (5)",
CombatName="Execution",
MoveType="Physical",
HPCost=5,
MoveRange=1,
PWR=2,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Execution)

ShieldShatter = Attack(
DisplayName="Shield Shatter",
CombatName="Shield Shatter",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1,
HIT=0.8,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Armored", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=5)
ListOfAttacks.append(ShieldShatter)

Slash = Attack(
DisplayName="Slash (3)",
CombatName="Slash",
MoveType="Physical",
HPCost=3,
MoveRange=1,
PWR=1.75,
HIT=1.1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Slash)

HyperSlash = Attack(
DisplayName="Hyper Slash (25)",
CombatName="Hyper Slash",
MoveType="Physical",
HPCost=25,
MoveRange=1,
PWR=2.25,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(HyperSlash)

VoltBlades = Attack(
DisplayName="Volt Blades (3)",
CombatName="Volt Blades",
MoveType="Physical",
HPCost=3,
MoveRange=1,
PWR=1.8,
HIT=1.2,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Shadow", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(VoltBlades)

GodSlash = Attack(
DisplayName="God Slash (75)",
CombatName="God Slash",
MoveType="Physical",
HPCost=75,
MoveRange=1,
PWR=5.5,
HIT=3,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(GodSlash)

BreaksItucher = Attack(
DisplayName="The Holy Itucher (75)",
CombatName="The Holy Itucher",
MoveType="Physical",
HPCost=75,
MoveRange=2,
PWR=2.5,
HIT=1.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(BreaksItucher)

QuestsItucher = Attack(
DisplayName="The Holy Itucher (50)",
CombatName="The Holy Itucher",
MoveType="Physical",
HPCost=50,
MoveRange=3,
PWR=5,
HIT=1.1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(QuestsItucher)

VenomBlade = Attack(
DisplayName="Venom Blade",
CombatName="Venom Blade",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=2.5,
HIT=5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Viral Resistance", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=0.25)
ListOfAttacks.append(VenomBlade)

Gun = Attack(
DisplayName="Gun",
CombatName="Gun",
MoveType="Physical",
HPCost=0,
MoveRange=3,
PWR=1.5,
HIT=1.2,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Mage", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.25)
ListOfAttacks.append(Gun)

ShieldBash = Attack(
DisplayName="Shield Bash (5)",
CombatName="Shield Bash",
MoveType="Physical",
HPCost=5,
MoveRange=1,
PWR=2,
HIT=1.2,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(ShieldBash)

FlameBlade = Attack(
DisplayName="Flame Blade",
CombatName="Flame Blade",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.5,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Ice", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(FlameBlade)

MageBlade = Attack(
DisplayName="Mage Blade",
CombatName="Mage Blade",
MoveType="Magic",
HPCost=0,
MoveRange=1,
PWR=1.5,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(MageBlade)

Slam = Attack(
DisplayName="Slam",
CombatName="Slam",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=2,
HIT=1.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Slam)

Fireball = Attack(
DisplayName="Fireball (1)",
CombatName="Fireball",
MoveType="Magic",
HPCost=1,
MoveRange=2,
PWR=1.5,
HIT=1.5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Ice", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Fireball)

Aqua = Attack(
DisplayName="Aqua (1)",
CombatName="Aqua",
MoveType="Magic",
HPCost=1,
MoveRange=2,
PWR=1.5,
HIT=1.5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Fire", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Aqua)

Freeze = Attack(
DisplayName="Freeze (1)",
CombatName="Freeze",
MoveType="Magic",
HPCost=1,
MoveRange=2,
PWR=1.5,
HIT=1.5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Bio", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Freeze)

Thorn = Attack(
DisplayName="Thorn (1)",
CombatName="Thorn",
MoveType="Magic",
HPCost=1,
MoveRange=2,
PWR=1.5,
HIT=1.5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Water", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Thorn)

DarkOrb = Attack(
DisplayName="Dark Orb (1)",
CombatName="Dark Orb",
MoveType="Magic",
HPCost=1,
MoveRange=2,
PWR=1.5,
HIT=1.5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Electric", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(DarkOrb)

Thunder = Attack(
DisplayName="Thunder (1)",
CombatName="Thunder",
MoveType="Magic",
HPCost=1,
MoveRange=2,
PWR=1.5,
HIT=1.5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Shadow", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Thunder)

Lance = Attack(
DisplayName="Lance",
CombatName="Lance",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.8,
HIT=0.7,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Lance)

Javelin = Attack(
DisplayName="Javelin",
CombatName="Javelin",
MoveType="Physical",
HPCost=0,
MoveRange=2,
PWR=1.3,
HIT=0.6,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Javelin)

Scalpel = Attack(
DisplayName="Scalpel",
CombatName="Scalpel",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1,
HIT=2,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Scalpel)

Infection = Attack(
DisplayName="Infection",
CombatName="Infection",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.5,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Viral Resistance", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=0.25)
ListOfAttacks.append(Infection)

Bow = Attack(
DisplayName="Bow",
CombatName="Bow",
MoveType="Physical",
HPCost=0,
MoveRange=2,
PWR=1,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Bow)

Crossbow = Attack(
DisplayName="Crossbow",
CombatName="Crossbow",
MoveType="Physical",
HPCost=0,
MoveRange=2,
PWR=1,
HIT=1.2,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Crossbow)

VineBow = Attack(
DisplayName="Vine Bow",
CombatName="Vine Bow",
MoveType="Physical",
HPCost=0,
MoveRange=2,
PWR=1.2,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Water", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(VineBow)

FlamingArrow = Attack(
DisplayName="Flaming Arrow",
CombatName="Flaming Arrow",
MoveType="Physical",
HPCost=0,
MoveRange=2,
PWR=1.5,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Ice", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(FlamingArrow)

XuirBlaster = Attack(
DisplayName="XuirBlaster",
CombatName="XuirBlaster",
MoveType="Physical",
HPCost=0,
MoveRange=3,
PWR=0.9,
HIT=1.75,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(XuirBlaster)

BowPlus = Attack(
DisplayName="Bow+",
CombatName="Bow+",
MoveType="Physical",
HPCost=0,
MoveRange=3,
PWR=1,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(BowPlus)

HeavyBow = Attack(
DisplayName="Heavy Bow",
CombatName="Heavy Bow",
MoveType="Physical",
HPCost=3,
MoveRange=2,
PWR=1.5,
HIT=1.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(HeavyBow)

Beam = Attack(
DisplayName="Beam (5)",
CombatName="Beam",
MoveType="Physical",
HPCost=5,
MoveRange=2,
PWR=2,
HIT=0.75,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Beam)

Destroyer = Attack(
DisplayName="Destroyer (15)",
CombatName="Destroyer",
MoveType="Physical",
HPCost=15,
MoveRange=1,
PWR=2.5,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Destroyer)

Cannon = Attack(
DisplayName="Cannon",
CombatName="Cannon",
MoveType="Physical",
HPCost=0,
MoveRange=5,
PWR=1.5,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Cannon)

LongBow = Attack(
DisplayName="Long Bow",
CombatName="Long Bow",
MoveType="Physical",
HPCost=0,
MoveRange=4,
PWR=1,
HIT=0.75,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(LongBow)

DistanceShot = Attack(
DisplayName="Distance Shot",
CombatName="Distance Shot",
MoveType="Physical",
HPCost=0,
MoveRange=6,
PWR=1,
HIT=0.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(DistanceShot)

Dagger = Attack(
DisplayName="Dagger",
CombatName="Dagger",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.1,
HIT=1.25,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Dagger)

DaggerToss = Attack(
DisplayName="Dagger Toss",
CombatName="Dagger Toss",
MoveType="Physical",
HPCost=0,
MoveRange=2,
PWR=1.1,
HIT=1.25,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(DaggerToss)

SparkBlade = Attack(
DisplayName="Spark Blade",
CombatName="Spark Blade",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.5,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Shadow", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(SparkBlade)

FireBlast = Attack(
DisplayName="Fire Blast (3)",
CombatName="Fire Blast",
MoveType="Magic",
HPCost=3,
MoveRange=3,
PWR=1.75,
HIT=1.2,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Ice", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(FireBlast)

Missile = Attack(
DisplayName="Missile (5)",
CombatName="Missile",
MoveType="Physical",
HPCost=5,
MoveRange=3,
PWR=1.6,
HIT=1.2,
HasExtra=None, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Missile)


Aura = Attack(
DisplayName="Aura (20)",
CombatName="Aura",
MoveType="Magic",
HPCost=20,
MoveRange=7,
PWR=2,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Aura)

Inferno = Attack(
DisplayName="Inferno (10)",
CombatName="Inferno",
MoveType="Magic",
HPCost=10,
MoveRange=7,
PWR=2,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Ice", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Inferno)

Congeal = Attack(
DisplayName="Congeal (10)",
CombatName="Congeal",
MoveType="Magic",
HPCost=10,
MoveRange=7,
PWR=2,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Bio", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Congeal)

Voltage = Attack(
DisplayName="Voltage (10)",
CombatName="Voltage",
MoveType="Magic",
HPCost=10,
MoveRange=7,
PWR=2,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Shadow", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Voltage)

ThunderBlast = Attack(
DisplayName="Thunder Blast (3)",
CombatName="Thunder Blast",
MoveType="Magic",
HPCost=3,
MoveRange=3,
PWR=1.75,
HIT=1.2,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Shadow", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(ThunderBlast)

VineWrath = Attack(
DisplayName="Vine Wrath (3)",
CombatName="Vine Wrath",
MoveType="Magic",
HPCost=3,
MoveRange=3,
PWR=1.75,
HIT=1.2,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Water", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(VineWrath)

Hydro = Attack(
DisplayName="Hydro (3)",
CombatName="Hydro",
MoveType="Magic",
HPCost=3,
MoveRange=3,
PWR=1.75,
HIT=1.2,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Fire", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(Hydro)

Hydra = Attack(
DisplayName="Hydra (5)",
CombatName="Hydra",
MoveType="Physical",
HPCost=5,
MoveRange=1,
PWR=2,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Fire", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.5)
ListOfAttacks.append(Hydra)

HerosStrike = Attack(
DisplayName="Hero's Strike",
CombatName="Hero's Strike",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.5,
HIT=1.25,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Monster", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.5)
ListOfAttacks.append(HerosStrike)

RepinsItucher = Attack(
DisplayName="The Holy Itucher (50)",
CombatName="The Holy Itucher",
MoveType="Physical",
HPCost=50,
MoveRange="Infinite",
PWR=2.5,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(RepinsItucher)

Snipe = Attack(
DisplayName="Snipe",
CombatName="Snipe",
MoveType="Physical",
HPCost=0,
MoveRange="Infinite",
PWR=0.5,
HIT=0.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Snipe)

SnipeII = Attack(
DisplayName="Snipe II (15)",
CombatName="Snipe II",
MoveType="Physical",
HPCost=15,
MoveRange="Infinite",
PWR=0.75,
HIT=0.75,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(SnipeII)

SnipeIII = Attack(
DisplayName="Snipe III (25)",
CombatName="Snipe III",
MoveType="Physical",
HPCost=25,
MoveRange="Infinite",
PWR=1,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(SnipeIII)

SnipeIV = Attack(
DisplayName="Snipe IV (50)",
CombatName="Snipe IV",
MoveType="Physical",
HPCost=50,
MoveRange="Infinite",
PWR=1.5,
HIT=1.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(SnipeIV)

GodSnipe = Attack(
DisplayName="God Snipe (100)",
CombatName="God Snipe",
MoveType="Physical",
HPCost=100,
MoveRange="Infinite",
PWR=2.5,
HIT=2.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(GodSnipe)

Cut = Attack(
DisplayName="Cut",
CombatName="Cut",
MoveType="Physical",
HPCost=1,
MoveRange=1,
PWR=1,
HIT=2,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Cut)

Finisher = Attack(
DisplayName="Finisher",
CombatName="Finisher",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=0.5,
HIT=3,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Finisher)

DeathStrike = Attack(
DisplayName="Death Strike",
CombatName="Death Strike",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=5,
HIT=0.25,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(DeathStrike)

ArmorBreak = Attack(
DisplayName="Armor Break (1)",
CombatName="Armor Break",
MoveType="Physical",
HPCost=1,
MoveRange=1,
PWR=1,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Armored", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=3)
ListOfAttacks.append(ArmorBreak)

Punch = Attack(
DisplayName="Punch",
CombatName="Punch",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.25,
HIT=1.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Punch)

ShadowPunch = Attack(
DisplayName="Shadow Punch (1)",
CombatName="Shadow Punch",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.375,
HIT=1.5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Electric", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(ShadowPunch)

ManaBurst = Attack(
DisplayName="Mana Burst (3)",
CombatName="Mana Burst",
MoveType="Magic",
HPCost=3,
MoveRange=1,
PWR=1.35,
HIT=1.25,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(ManaBurst)

ShadowBurst = Attack(
DisplayName="Shadow Burst (1)",
CombatName="Shadow Burst",
MoveType="Magic",
HPCost=1,
MoveRange=1,
PWR=1.25,
HIT=1.25,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Electric", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(ShadowBurst)

ShadowBlade = Attack(
DisplayName="Shadow Blade",
CombatName="Shadow Blade",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.5,
HIT=1.5,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Electric", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(ShadowBlade)

ShadowStorm = Attack(
DisplayName="Shadow Storm (3)",
CombatName="Shadow Storm",
MoveType="Magic",
HPCost=3,
MoveRange=3,
PWR=1.75,
HIT=1.2,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Electric", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1.3)
ListOfAttacks.append(ShadowStorm)

GeomBurst = Attack(
DisplayName="Geom Burst (1)",
CombatName="Geom Burst",
MoveType="Magic",
HPCost=1,
MoveRange=1,
PWR=1.3,
HIT=1.3,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(GeomBurst)

GeomBlast = Attack(
DisplayName="Geom Blast (3)",
CombatName="Geom Blast",
MoveType="Magic",
HPCost=3,
MoveRange=2,
PWR=1.6,
HIT=1.6,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(GeomBlast)

GeomMedal = Attack(
DisplayName="Geom Medal (7)",
CombatName="Geom Medal",
MoveType="Magic",
HPCost=7,
MoveRange=2,
PWR=2,
HIT=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(GeomMedal)

GeomStrike = Attack(
DisplayName="Geom Strike (15)",
CombatName="Geom Strike",
MoveType="Magic",
HPCost=15,
MoveRange=4,
PWR=1.7,
HIT=0.9,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(GeomStrike)

GeomSlash = Attack(
DisplayName="Geom Slash (10)",
CombatName="Geom Slash",
MoveType="Magic",
HPCost=10,
MoveRange=1,
PWR=1.8,
HIT=1.4,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(GeomSlash)

AntiXuir = Attack(
DisplayName="Anti-Xuir",
CombatName="Anti-Xuir",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1,
HIT=1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="Xuir", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=3)
ListOfAttacks.append(AntiXuir)

Countdown = Attack(
DisplayName="Countdown (1)",
CombatName="Countdown",
MoveType="Physical",
HPCost=1,
MoveRange="Infinite",
PWR=0.1,
HIT=5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Countdown)

Death = Attack(
DisplayName="Death",
CombatName="Death",
MoveType="Physical",
HPCost=0,
MoveRange="Infinite",
PWR=999999,
HIT=999999,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfAttacks.append(Death)

#===Supports========================================================================================================================================

XuiristRitual = Support(
DisplayName="Xuirist Ritual (2)",
CombatName="Xuirist Ritual",
MoveType="Magic",
HPCost=2,
MoveRange=2,
PWR=1.1,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra= "Xuir", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=2)
ListOfSupports.append(XuiristRitual)

XuirianRecovery = Support(
DisplayName="Xuirian Recovery",
CombatName="Xuirian Recovery",
MoveType="Magic",
HPCost=0,
MoveRange=0,
PWR=2,
HasExtra=True, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra= "Xuir", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=2)
ListOfSupports.append(XuirianRecovery)

Heal = Support(
DisplayName="Heal (1)",
CombatName="Heal",
MoveType="Magic",
HPCost=1,
MoveRange=1,
PWR=1.2,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(Heal)

HealthPotion = Support(
DisplayName="Health Potion",
CombatName="Health Potion",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=1.3,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(HealthPotion)

Mend = Support(
DisplayName="Mend",
CombatName="Mend",
MoveType="Physical",
HPCost=0,
MoveRange=1,
PWR=2,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(Mend)

Save = Support(
DisplayName="Save (5)",
CombatName="Save",
MoveType="Physical",
HPCost=5,
MoveRange=3,
PWR=2,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(Save)

Fortify = Support(
DisplayName="Fortify (10)",
CombatName="Fortify (10)",
MoveType="Physical",
HPCost=10,
MoveRange=1,
PWR=4,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(Fortify)

LongHeal = Support(
DisplayName="Long Heal (3)",
CombatName="Long Heal",
MoveType="Magic",
HPCost=3,
MoveRange=2,
PWR=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(LongHeal)

FarHeal = Support(
DisplayName="Far Heal (5)",
CombatName="Far Heal",
MoveType="Magic",
HPCost=5,
MoveRange="Infinite",
PWR=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(FarHeal)

MedKit = Support(
DisplayName="Med Kit",
CombatName="Med Kit",
MoveType="Physical",
HPCost=0,
MoveRange=0,
PWR=1.5,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(MedKit)

Purify = Support(
DisplayName="Purify [1]",
CombatName="Purify",
MoveType="Magic",
HPCost=1,
MoveRange=2,
PWR=1,
HasExtra=False, #If true, then deal extra damage if target has the Extra trait (total damage will be mul by ExtraMul)
Extra="", #Trait to deal extra damage to (total damage will be mul by ExtraMul)
ExtraMul=1)
ListOfSupports.append(Purify)
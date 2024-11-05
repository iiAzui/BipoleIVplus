import moves
import turtle
import select
import screensetup
import units
import statprint
import placeunits
import os

def export_unit(unit: units.Unit, destination_folder: str):
    move_names = ', '.join(['\"'+attack.CombatName+'\"' for attack in unit.Attacks])
    move_unlock_names = ', '.join(['\"'+unlock[0].CombatName+'\"' for unlock in unit.AttackUnlocks])
    move_unlock_levels = ', '.join([str(unlock[1]) for unlock in unit.AttackUnlocks])
    traits = ', '.join(['\"'+trait+'\"' for trait in unit.Traits])

    tres_content = f"""
[gd_resource type="Resource" script_class="Unit" load_steps=3 format=3]

[ext_resource type="Script" path="res://Scripts/Move.gd" id="2_pja1r"]
[ext_resource type="Script" path="res://Scripts/Unit.gd" id="3_hyhyt"]

[resource]
script = ExtResource("3_hyhyt")
moves = Array[ExtResource("2_pja1r")]([])
move_unlocks = Array[ExtResource("2_pja1r")]([])
move_unlock_levels = Array[int]([])
exported_move_names = Array[String]([{move_names}])
exported_move_unlock_names = Array[String]([{move_unlock_names}])
exported_move_unlock_levels = Array[int]([{move_unlock_levels}])
level = {unit.Level}
hp = {unit.MaxHP}
attack = {unit.ATK}
defense = {unit.DEF}
resistance = {unit.RES}
agility = {unit.AGL}
accuracy = {unit.ACR}
speed = {unit.SPD}
exp_reward = {unit.EXPReward}
primary_type = "{unit.PrimaryType}"
traits = Array[String]([{traits}])
unit_class = "{unit.UnitClass}"
class_change = "{unit.ClassChange[0][0] if len(unit.ClassChange)>0 else ''}"
class_change_level = {unit.ClassChange[0][1] if len(unit.ClassChange)>0 else '0'}
hp_growth = Vector2i({unit.HPGrowth[0]}, {unit.HPGrowth[1]})
atk_growth = Vector2i({unit.ATKGrowth[0]}, {unit.ATKGrowth[1]})
def_growth = Vector2i({unit.DEFGrowth[0]}, {unit.DEFGrowth[1]})
res_growth = Vector2i({unit.RESGrowth[0]}, {unit.RESGrowth[1]})
agl_growth = Vector2i({unit.AGLGrowth[0]}, {unit.AGLGrowth[1]})
acr_growth = Vector2i({unit.ACRGrowth[0]}, {unit.ACRGrowth[1]})
    """

    file_path = os.path.join(destination_folder, f"{unit.DisplayName}.tres")
    with open(file_path, "w") as file:
        file.write(tres_content)

for unit in units.ListOfPlayableUnits:
    export_unit(unit, "./Database/RecruitedUnits")
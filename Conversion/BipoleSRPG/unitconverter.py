import moves
import turtle
import select
import screensetup
import units
import statprint
import placeunits
import os

def export_unit(unit: units.Unit, destination_folder: str, use_turtle_name: bool = False, x: int = -1, y: int = -1):
    resource_name = unit.TurtleName if use_turtle_name else unit.DisplayName
    character_name = unit.Portrait[:-4]

    print("Exporting unit "+resource_name+"...")
    
    move_names = ', '.join(['\"'+move.CombatName+'\"' for move in unit.Attacks + unit.Supports])
    move_unlock_names = ', '.join(['\"'+unlock[0].CombatName+'\"' for unlock in unit.AttackUnlocks + unit.SupportUnlocks])
    move_unlock_levels = ', '.join([str(unlock[1]) for unlock in unit.AttackUnlocks + unit.SupportUnlocks])
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
exported_portrait_name = "{unit.Portrait}"
exported_overworld_name = "{unit.Sprite}"
exported_character_name = "{character_name}"
exported_y = 0
exported_x = 0
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

    file_path = os.path.join(destination_folder, f"{resource_name}.tres")
    # if os.path.exists(file_path):
    #     return
    with open(file_path, "w") as file:
        file.write(tres_content)

already_exported_characters = []

def export_character(unit: units.Unit, destination_folder: str, use_portrait_name: bool = False):
    resource_name = unit.Portrait[:-4] if use_portrait_name else unit.DisplayName

    if resource_name in already_exported_characters:
        return
    already_exported_characters.append(resource_name)

    print("Exporting character "+resource_name+"...")

    bio = unit.Bio.replace("\n", " ")
    level_quotes = ','.join(f'\"{quote[quote.index(": ")+2:] if ":" in quote else quote}\"' for quote in unit.LevelQuotes)

    # Character - contains name, sprites, quotes, basically visual-only information
    tres_content = f"""
[gd_resource type="Resource" script_class="Character" load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/Character.gd" id="3_qsxlm"]

[resource]
script = ExtResource("3_qsxlm")
display_name = "{unit.DisplayName}"
bio = "{bio}"
level_quotes = Array[String]([{level_quotes}])
"""

    file_path = os.path.join(destination_folder, f"{resource_name}.tres")
    # if os.path.exists(file_path):
    #     return
    with open(file_path, "w") as file:
        file.write(tres_content)


if __name__ == "__main__":
    for unit in units.ListOfPlayableUnits:
        export_unit(unit, "./Database/RecruitedUnits")
        export_character(unit, "./Database/Characters")
import moves
import turtle
import select
import screensetup
import units
import statprint
import placeunits
import os

INFERRED_ELEMENTS_TABLE = {
    "Fire": "Water",
    "Water": "Bio",
    "Bio": "Ice",
    "Ice": "Fire",
    "Shadow": "Electric",
    "Electric": "Shadow"
}

def export_attack(move: moves.Attack):
    print("Exporting "+move.CombatName+"...")
    # Maps trait extra damage to the element likely attributed to the move
    
    inferred_element = INFERRED_ELEMENTS_TABLE[move.Extra] if move.Extra in INFERRED_ELEMENTS_TABLE else "None"

    tres_content = f"""
[gd_resource type="Resource" script_class="Move" load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/Move.gd" id="1_308sg"]

[resource]
script = ExtResource("1_308sg")
display_name = "{move.CombatName}"
move_type = "Attack"
damage_type = "{move.MoveType}"
hp_cost = {move.HPCost}
range = {999 if move.MoveRange == "Infinite" else move.MoveRange}
power = {move.PWR}
hit_rate = 100.0
accuracy_multiplier = {move.HIT}
element = "{inferred_element}"
extra_damage_trait = "{move.Extra}"
extra_multiplier = {move.ExtraMul}"""

    file_path = os.path.join("./Database/Moves", f"{move.CombatName}.tres")
    with open(file_path, "w") as file:
        file.write(tres_content)

for attack in moves.ListOfAttacks:
    export_attack(attack)
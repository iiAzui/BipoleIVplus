import moves
import turtle
import select
import screensetup
import units
import statprint
import placeunits

import os
import math

import unitconverter

def export_chapter(chapter_name: str, units: list[units.Unit | None]):
    chapter_units = []
    chapter_unit_positions = []

    unit_num = 1
    for i in range(len(units)):
        unit = units[i]
        if unit is None:
            continue

        y = math.floor(i / 19)
        x = i % 19

        unit_resource_name = f"{chapter_name}Unit{unit_num}"
        chapter_units.append(unit_resource_name)
        chapter_unit_positions.append((x, y))

        unitconverter.export_unit(unit, "./Database/EnemyUnits", unit_resource_name)
        unitconverter.export_character(unit, "./Database/Characters", True)
        unit_num += 1

    tres_content = f"""
[gd_resource type="Resource" script_class="ChapterPlacements" load_steps=2 format=3 uid="uid://bkhl1kl5604v5"]

[ext_resource type="Script" path="res://Scripts/ChapterPlacements.gd" id="1_kp6pv"]

[resource]
script = ExtResource("1_kp6pv")
unit_names = Array[String]([{', '.join(f'"{name}"' for name in chapter_units)}])
unit_coords = Array[Vector2i]([{', '.join(f'Vector2i{position}' for position in chapter_unit_positions)}])
"""
    
    file_path = os.path.join("./Database/ChapterPlacements", f"{chapter_name}.tres")
    with open(file_path, "w") as file:
        file.write(tres_content)

for i, chapter_name in enumerate(placeunits.all_chapter_names):
    chapter_placements = placeunits.all_chapter_placements[i]
    export_chapter(chapter_name, chapter_placements)
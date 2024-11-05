import moves
import turtle
import select
import screensetup
import units
import statprint
import placeunits
import os

for unit in units.ListOfPlayableUnits:
    print(unit.DisplayName)

def export_unit(unit: units.Unit):
    tres_content = f"""
        [gd_resource type="Resource" load_steps=2 format=2]

        [resource]
    """

    file_path = os.path.join("./Conversion/ExportedUnits", f"{unit.DisplayName}.tres")
    with open(file_path, "w") as file:
        file.write(tres_content)

export_unit(units.Scien)
import os
import json

import cutscenes
import screensetup
import placeunits

cutscenes.Chapter = "Prologue1"

def export_chapter(cutscene_name: str):
    ref_name = cutscene_name.replace(' ', '')
    print("exporting ", ref_name)

    dialogue_lines = []
    
    max_iters_left = 2000
    while cutscenes.Chapter == cutscene_name:
        cutscenes.current_string = ""
        cutscenes.current_left = ""
        cutscenes.current_right = ""

        cutscenes.Cutscene()

        if cutscenes.cutscene_ended:
            cutscenes.Chapter = None
            break

        line = {}

        if cutscenes.current_string:
            line["text"] = cutscenes.current_string
        if cutscenes.current_left:
            line["left"] = cutscenes.current_left
        if cutscenes.current_right:
            line["right"] = cutscenes.current_right

        if screensetup.bg_color_changed:
            line["bgcolor"] = screensetup.bg_color_changed
            screensetup.bg_color_changed = None

        if cutscenes.Chapter != cutscene_name:
            line["startchapter"] = cutscenes.Chapter

        if placeunits.battle_started:
            line["battle"] = ref_name

        dialogue_lines.append(line)

        max_iters_left -= 1
        if max_iters_left <= 0:
            break

    json_data = json.dumps(dialogue_lines, indent="\t")
    
    file_path = os.path.join("./Database/Cutscenes", f"{ref_name}.json")
    with open(file_path, "w") as file:
        file.write(json_data)

max_iters_left = 2000
while cutscenes.Chapter:
    export_chapter(cutscenes.Chapter)
    max_iters_left -= 1
    if max_iters_left <= 0:
        break
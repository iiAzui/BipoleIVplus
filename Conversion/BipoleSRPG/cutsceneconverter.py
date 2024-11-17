import select
import cutscenes
import screensetup
import placeunits
import units

import os
import json
import re

cutscenes.Chapter = "Prologue1"

# won't export these ones
skip_chapters = ["Chapter01", "Chapter02", "Chapter03"]

prev_index = -1

speaker_pattern = r'([a-zA-Z ?\'])+: '

units.UnitsAlive.append(units.Proton)
units.UnitsAlive.append(units.Quest)
units.UnitsRecruited.append(units.Quest)
units.UnitsAlive.append(units.Scien)
units.UnitsRecruited.append(units.Scien)
units.UnitsAlive.append(units.TnemecalperI)
units.UnitsAlive.append(units.TnemecalperII)
units.UnitsAlive.append(units.TnemecalperIII)
units.UnitsAlive.append(units.TnemecalperIV)
units.UnitsRecruited.append(units.TnemecalperI)
units.UnitsRecruited.append(units.TnemecalperII)
units.UnitsRecruited.append(units.TnemecalperIII)
units.UnitsRecruited.append(units.TnemecalperIV)

def export_chapter(cutscene_name: str):
    global prev_index
    
    ref_name = cutscene_name.replace(' ', '')
    print("exporting ", ref_name)

    dialogue_lines = []
    
    max_iters_left = 2000
    while cutscenes.Chapter == cutscene_name:
        cutscenes.current_string = ""
        cutscenes.current_left = ""
        cutscenes.current_right = ""

        cutscenes.Cutscene()

        if cutscenes.CutsceneIndex == prev_index:
            print("index didn't change, leaving now")
            cutscenes.cutscene_ended = True
            break

        if cutscenes.cutscene_ended:
            cutscenes.Chapter = None
            break

        line = {}

        if cutscenes.current_left:
            line["left"] = cutscenes.current_left
        if cutscenes.current_right:
            line["right"] = cutscenes.current_right
        if cutscenes.current_string:
            match = re.search(speaker_pattern, cutscenes.current_string)
            if match:
                if match.group(0)[:-2].lower().replace(" ","") in cutscenes.current_left.lower().replace(" ",""):
                    line["speaker"] = "left"
                    line["text"] = re.sub(speaker_pattern, "", cutscenes.current_string)
                    line["name_left"] = match.group(0)[:-2]
                elif match.group(0)[:-2].lower().replace(" ","") in cutscenes.current_right.lower().replace(" ",""):
                    line["speaker"] = "right"
                    line["text"] = re.sub(speaker_pattern, "", cutscenes.current_string)
                    line["name_right"] = match.group(0)[:-2]           
                else:
                    line["text"] = cutscenes.current_string      
            else:
                line["text"] = cutscenes.current_string    
            
            

        if screensetup.bg_color_changed:
            line["bgcolor"] = screensetup.bg_color_changed
            screensetup.bg_color_changed = None

        if cutscenes.Chapter != cutscene_name:
            line["startchapter"] = cutscenes.Chapter.replace(" ","")

        if cutscenes.battle_started:
            line["battle"] = ref_name
            cutscenes.battle_started = False

        if select.instant_level_ups:
            line["instant_level_ups"] = select.instant_level_ups
            select.instant_level_ups = []

        if len(screensetup.current_branches) > 0:
            print("branches found: ", screensetup.current_branches)
            screensetup.current_branches[0]()
            screensetup.current_branches.clear()

        if len(line.keys()) > 0:
            dialogue_lines.append(line)

        max_iters_left -= 1
        if max_iters_left <= 0:
            break

        prev_index = cutscenes.CutsceneIndex

    json_data = json.dumps(dialogue_lines, indent="\t")
    
    if not ref_name in skip_chapters:
        file_path = os.path.join("./Database/Cutscenes", f"{ref_name}.json")
        with open(file_path, "w") as file:
            file.write(json_data)

max_iters_left = 2000
while cutscenes.Chapter and not cutscenes.cutscene_ended:
    export_chapter(cutscenes.Chapter)
    max_iters_left -= 1
    if max_iters_left <= 0:
        break
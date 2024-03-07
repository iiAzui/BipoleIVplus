# Converts a cutscene from Bipole IV python format to bipole IV+ text format.

import sys
import re
import os

if len(sys.argv) < 1:
    print("Usage: cutsceneconverter.py [filename]")
    exit()
filepath = sys.argv[1]

f = open(filepath, "r")
text = f.read()
f.close()

# ==== remove lines that won't serve any purpose for the new cutscenes
text = text.replace('CutsceneIndex += 1', '')
text = re.sub(r'turtle.+\n', '\n', text)
text = text.replace('CutsceneIndex = 0', '')
text = text.replace('Cutscene()', '') # usually used in if/else to skip a dialogue on some branch

text = re.sub(r'UnitFormation = \S+\n', '', text)
text = re.sub(r'BattleStarted = \S+\n', '', text)

# use this line to determine the battle that should be started after the current dialogue
text = re.sub(r'UnitsToPlace = placeunits\.(\S+)Enemies\n', r'/battle \1\n', text)

# remove cutsceneindex if/elif branches without important conditions
text = re.sub(r'(el)?if CutsceneIndex == \d+:\n', '', text)

# turn onkey listener into just a '==' which will signify to the interpreter to wait for input before next dialogue/battle
# HOWEVER if it has 2 or more tabs in fornt if it, it is within a cutscene-specific conditional branch. this is marked by just = which will not reset ifelse branches
text = re.sub(r'        +\(screensetup.BattleScreen\).onkey\(Cutscene, "space"\)', '=', text)
text = re.sub(r'\t\t+\(screensetup.BattleScreen\).onkey\(Cutscene, "space"\)', '=', text)

text = text.replace('(screensetup.BattleScreen).onkey(Cutscene, "space")', '==')

text = text.replace('(screensetup.BattleScreen).onkey(BattleStart, "space")', '==')

# convert text calls to ust the inner string - inside the double quotes, match any amt of characters that is not a double quote

# text1: one portrait + top line
# desired txt format: 
# {portrait_left:Proton}
# dialogue...
text = re.sub(r'Text1\(\"([^"]*)\",\s*units.([^.]*).Portrait\)', r'{portrait_left:\2}\n\1', text)

# text2: two portraits + top line
# for some reason this shows up in 2 different formats in the bipole iv cutscene code...
# desired txt format:
# {portrait_left:Proton} {portrait_right:Scien}
# dialogue...
text = re.sub(r'Text2\(\"([^"]*)\",\s*units.([^.]*).Portrait,\s*units.([^.]*).Portrait\)', 
              r'{portrait_left:\2} {portrait_right:\3}\n\1', text)
text = re.sub(r'Text2\(\"([^"]*)\",\s*units.([^.]*).Portrait,\s*current_directory\+"\/Portraits\/([^.]*).gif"\)', 
              r'{portrait_left:\2} {portrait_right:\3}\n\1', text)

# text3: no portraits, just top line
text = re.sub(r'Text3\(\"([^"]*)\"\)', r'\1', text)

# line2 & line 3 just convert to strings that will appear under the first line which is always Text1/2/3
text = re.sub(r'line[23]\(\"([^"]*)\"\)', r'\1', text)

# ==== COMMANDS ====
# set color command - sets bg color, may need to be integrated with godot a little better idk
text = re.sub(r'screensetup.BattleScreen.bgcolor\("([^"]+)"\)', r'/bgcolor \1', text)

# set chapter - will define the next chapter to run in the game
text = re.sub(r'Chapter = "([^"]+)"', r'/startchapter \1', text)

# add alive unit - this can probably be handled automatically... so ima just replace with nothing for now
text = re.sub(r'units.UnitsAlive.append.+\n', '\n', text)

# recruit unit command
text = re.sub(r'units.UnitsRecruited.append\(units.(\w+)\)', r'/recruit \1', text)

# save command (could be removed to just save after every battle since this just appears after each battle)
# DISABLED figure it out in the code, these are placed too randomly across the cutscenes, just save after a battle is won...
# text = text.replace('SaveData()', '/save')
text = text.replace('SaveData()\n', '')


# recruitment choice
recruit_choice_regex = r'\(screensetup\.BattleScreen\)\.onkey\((\w+)RecruitYes, "q"\)\n\s*\(screensetup\.BattleScreen\)\.onkey\((\w+)RecruitNo, "w"\)'
text = re.sub(recruit_choice_regex, r'/choice Recruit\1', text)

# chapter level set command
text = re.sub(r'ChapterLevel = (\d+)', r'/chapterlevel \1', text)

# reformat if statements just a little so theyre easier to interpret
# in the game's cutscene interpreter there should be string flags that are set and read from for the current cutscene, or a similar system
text = re.sub(r'if (\w+) == True:', r'/if \1', text)

# check if unit is alive
# Will check for a flag called (unit)Alive to decide between true or false branch. This should be set and checked in the cutscene interpreter
# ex. to check if Scien is alive, would be /if IsAlive Scien
# (ignore cutsceneIndex checks)
text = re.sub(r'(if|elif) units\.(\w+) in units\.UnitsAlive:?( and CutsceneIndex.*+)?\n', r'/\1 IsAlive \2\n', text)

# check if certain amount of units are alive
# syntax: /if UnitsAliveGreater {number}
text = re.sub(r'(if|elif) len\(units.UnitsAlive\) > (\d+):?( and CutsceneIndex.*+)?\n', r'/\1 UnitsAliveGreater \2\n', text)

# same thing but equal instead of greater
text = re.sub(r'(if|elif) len\(units.UnitsAlive\) == (\d+):?( and CutsceneIndex.*+)?\n', r'/\1 UnitsAliveEqual \2\n', text)

# else command - when interpreted, lines under here will only run if the current if statement was false and lines up to here are being ignored
text = text.replace('else:', '/else')
# since tab indentation is being scrapped there is no branch end marker,
# so when /if and /else are interpreted, the == at the end of the line should serve as also ending the current branch if any.

# ---- final cleanup
# remove all tab indents that may still be lying around from python
text = re.sub(r'\t+', '', text)
text = re.sub(r'\n\s+', '\n', text)

# OPTIONAL
# remove the q/w choice lines that are written as line2 & line3. /choice can handle this
text = re.sub(r'\(Q\) Recruit\s*\n\(W\) Do not recruit\n', '', text)
# remove the [Recruit (unit)?] that also appears on these choices
text = re.sub(r'\[Recruit ([^\]]+)?\]\s*\n', '', text)

# [(unit) has joined your party] - the recruit function can take care of this emssage, dont want to clutter up the cutscene file with logic that can be automated
text = re.sub(r'\[(\w+) has joined your party\]\n', '', text)

directory, filename = os.path.split(filepath)
name, extension = os.path.splitext(filename)
new_filepath = os.path.join(directory, name + '_converted.txt')
print("new file: "+new_filepath)

wf = open(new_filepath, "w")
wf.write(text)
wf.close()

print("converted!")
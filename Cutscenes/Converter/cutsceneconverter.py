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

# remove lines that won't serve any purpose for the new cutscenes
text = text.replace('CutsceneIndex += 1', '')
text = text.replace('(screensetup.BattleScreen).onkey(Cutscene, "space")', '')
text = re.sub(r'turtle.+\n', '\n', text)
text = text.replace('CutsceneIndex = 0', '')

# turn if/elif branches into == which will signify wait for user input
text = re.sub(r'(el)?if CutsceneIndex == \d+:', '==', text)

# convert text calls to ust the inner string - inside the double quotes, match any amt of characters that is not a double quote

# text1: one portrait + top line
# desired txt format: 
# {portrait_left:Proton}
# dialogue...
text = re.sub(r'Text1\(\"([^"]*)\",\s*units.([^.]*).Portrait\)', r'{portrait_left:\2}\n\1', text)

# text2: two portraits + top line
# for some reason this shows up in 2 different formats in the bipole iv cutscene code...
# desired txt format:
# {portrait_left:Proton portrait_right:Scien}
# dialogue...
text = re.sub(r'Text2\(\"([^"]*)\",\s*units.([^.]*).Portrait,\s*units.([^.]*).Portrait\)', 
              r'{portrait_left:\2} {portrait_right:\3}\n\1', text)
text = re.sub(r'Text2\(\"([^"]*)\",\s*units.([^.]*).Portrait,\s*current_directory\+"\/Portraits\/([^.]*).gif"\)', 
              r'{portrait_left:\2} {portrait_right:\3}\n\1', text)

# text3: no portraits, just top line
text = re.sub(r'Text3\(\"([^"]*)\"\)', r'\1', text)

# line2 & line 3 just convert to strings that will appear under the first line which is always Text1/2/3
text = re.sub(r'line[23]\(\"([^"]*)\"\)', r'\1', text)

# set color command - sets bg color, may need to be integrated with godot a little better idk
text = re.sub(r'screensetup.BattleScreen.bgcolor\("([^"]+)"\)', r'/bgcolor \1', text)

# set chapter - will define the next chapter to run in the game
text = re.sub(r'Chapter = "([^"]+)"', r'/startchapter \1', text)

# remove all tab indents that may still be around from python
text = re.sub(r'\t+', '', text)
text = re.sub(r'\n\s+', '\n', text)

directory, filename = os.path.split(filepath)
name, extension = os.path.splitext(filename)
new_filepath = os.path.join(directory, name + '_converted.txt')

wf = open(new_filepath, "w")
wf.write(text)
wf.close()

print("converted!")
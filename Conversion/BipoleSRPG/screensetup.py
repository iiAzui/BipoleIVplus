import turtle
import os
import cutscenes
current_directory = os.getcwd()

bg_color_changed = None

# TODO: possible improvement: exporting branches by running the function for each branches' onkey. probably more work than just copyi and pasting the lines over in separate lists though.

# Contains all functions that are called per branch.
# Ex. RomraRecruitYes, RomraRecruitNo,
# by default, first branch will be on "true" key, second branch will be on "false" key, and all others will be on "branch#" for the branch number
current_branches = []

class FakeBattleScreen:
    def bgcolor(self, color):
        global bg_color_changed
        bg_color_changed = color

    def onkey(self, func, key):
        current_branches.append(func)

# COMMENTED OUT FOR CONVERSION ONLY
BattleScreen = FakeBattleScreen()
# BattleScreen.setup(1450,800,0,0)
# BattleScreen.setup(800,800,0,0)
# BattleScreen.screensize(800,800,"green")




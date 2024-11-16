import turtle
import os
current_directory = os.getcwd()

bg_color_changed = None

class FakeBattleScreen:
    def bgcolor(self, color):
        global bg_color_changed
        bg_color_changed = color

    def onkey(self, func, key):
        pass

# COMMENTED OUT FOR CONVERSION ONLY
BattleScreen = FakeBattleScreen()
# BattleScreen.setup(1450,800,0,0)
# BattleScreen.setup(800,800,0,0)
# BattleScreen.screensize(800,800,"green")




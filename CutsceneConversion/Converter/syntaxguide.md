Anytime there is an array of {} objects in the JSON file, this is a list of dialogue lines.
The root list is a list of dialogue lines, as well as the "true" and "false" values in branch dialogue lines.

======== DIALOGUE LINE KEYS ========
"battle"
    The battle associated with the current chapter is started after this dialogue option is completed.
    After the battle is completed, the cutscene resumes where it left off on the next dialogue line.

"bgcolor"
    Flat color of the background. Later, this may be turned into a background sprite.

"left", "right"
    Character that shows up on this side of the screen.
    Value is a string.
    If a character with this name is found in the database, their portrait and their name are displayed.
    If there is no character with this name, check the Portraits folder to see if there is a portrait image with this name. Make sure that "name_left" and "name_right" are set if needed.
    If neither a character or a portrait are found, an error should be logged, and the portait/name should be blank.

"name_left", "name_right"
    The name displayed by the left and right portraits. This value will override the name of the actual character that is the left or right speaker, if there is a character there.

"speaker"
    Value is either "left" or "right". Defaults to "left" if this key is not present. 
    The character on this side will be highlighted, and their name is displayed above the dialogue text, unless name is overridden.

"startchapter"
    After the current dialogue line, end the current dialogue and begin the next chapter's dialogue with the given id. The game should also probably auto-save here.

"text"
    The text that will show up. Unlike in the original Bipole IV, this should be all in 1 string instead of split between 3 lines.


======== BRANCHES ========
If a dialogue line has the "condition" key, it will be treated as a conditional branch, and none of the tags above will have any effect.
"true" will be the dialogue lines displayed if the conditions passes, if the key exists.
"false" will be the dialogue lines displayed if the condition does not pass, if the key exists.
After either of these dialogue lists are played all the way through or neither, then the next dialogue line will be run.

========= CONDITIONS ==========
The "condition" key's value will be a list of conditions. Here are the conditions:

"is_alive": []
    All units in the passed list must be alive.

"units_alive_greater": #
    Total amount of living units must be greater than this number.

"units_alive_equal": #
    Must have exactly this many units alive in the party.
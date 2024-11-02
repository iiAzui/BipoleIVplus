Anytime there is an array of {} objects in the JSON file, this is a list of dialogue lines.
The root list is a list of dialogue lines.

======== DIALOGUE LINE KEYS ========

"battle"
    The battle associated with the current chapter is started after this dialogue option is completed.
    After the battle is completed, the cutscene resumes where it left off on the next dialogue line.

"bgcolor"
    Flat color of the background. Later, this may be turned into a background sprite.

"portrait_left"
    Portrait that shows up on the left side of the screen.

"portrait_right"
    Portrait that shows up on the right side of the screen.

"text"
    The text that will show up. Unlike in the original Bipole IV, this should be all in 1 string instead of split between 3 lines.


======== BRANCHES ========
If a dialogue line has the "condition" key, it will be treated as a conditional branch, and none of the tags above will have any effect.
"true" will be the dialogue lines displayed if the conditions passes, if the key exists.
"false" will be the dialogue lines displayed if the condition does not pass, if the key exists.
After either of these dialogue lists are played all the way through or neither, then the next dialogue line will be run.

========= CONDITIONS ==========
The "condition" key's value will be a list of conditions. Here are the conditions:

"is_alive": []. All units in the passed list must be alive.

"units_alive_greater": #. Total amount of living units must be greater than this number.

"units_alive_equal": #. Must have exactly this many units alive in the party.
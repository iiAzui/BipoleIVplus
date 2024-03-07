CONVERTED CUTSCENE SYNTAX
contains what each token should do

---------- GENERAL ----------
=
Wait for user input before moving to the next dialogue.
(only do a wait for input after this if not currently within an ignored branch section)

==
Same as ==, but also close any opened ifelse branches.

---------- BRANCHING ----------
/if {condition}
condition - see the --CONDITIONS-- tab a bit lower than this to see how to handle these
Open an if branch. These shoud be kep track of using a stack list of bools. Check the condition; if true add a true to the stack, if false add a false to the stack. 
There is no designated inner code ending token or anything like tabs in python or } in javascript All lines should be considered inside of the statement's body UNTIL a /elif, /else, or == is reached. == will remove ALL stacks and /elif will replace the current highest in the stack.
example: /if UniteAliveGreater 1 - add true to stack if more than 1 unit, add false to stack if 1 or less

/elif {condition}
Same as an if branch, but only check to run this branch if the previous if statement was not true.
NOTE: this will show up even when there is not an if statement before it!! just treat it as a normal if statement if that's the case. I would try to somehow write some extra code to make sure an elif will always come after an if but I don't get paid enough to do this.

/else
Only interpret below if previous if statement was not true. Inner code will only be ended by a. Equivalent to /elif True if that makes it easier to implement with less keywords.

---------- CONDITIONS ----------
These conditions will appear after an /if or /elif statement.
ALSO: something like this might showup: /if IsAlive Romra and IsAlive Scien
make sure that in some way, check to see if there is an additional 'and' after all the arguments of a condition.
if so, also check to see if the condition after the and is true as well.
as far as I know, I havent seen any or operations yet. hopefully it stays that way..

UnitsAliveGreater {number}
If player has more than N units alive in their party, and false if equal or less.
example: /elif UnitsAliveGreater 1

UnitsAliveEqual {number}
If player has exactly N units alive in the party.

IsAlive {unitName}
If the unit with the given name is alive in the party.
example: /elif IsAlive Scien

ChoiceSelected {index}
If, on the last choice prompt, the player responded with choice index N.
0 = Q ("Recruit" on most prompts)
1 = W ("Do not recruit" on most prompts)
2 = E? I think the only choice with a third option is the Fael/Erif/Neither choice.

---------- COMMANDS ----------
If a line starts with a slash /, it contains a command, likely with some preceding arguments. Parse and evaluate this command immediately, and then move onto the next line.

/battle {battleName}
Set the battle that will be started next. Store this info somewhere. /startbattlenextinput, /placeenemyunits and /startbattlenow may use this stored value.
example: /battle Chapter1

/bgcolor {color}
color - black, green, etc.
set the cutscene background color to this color.

/chapterlevel
Sets the current chapter level variable. (If there is some sort of chapter object, this could/should probably be taken out of the cutscene and moved there, for less global variable cluttering shenanigans)

/enablebattlecontrol
Used when a cutscnee happens during the setup of a battle, like in Ch. 4. When this is called, the cutscene should stop running for now and let the player play out the battle. Once the battle is done, resume playing the cutscene at the the index under this command.

/instantlevelup {unitName} {levels}
Instantly add N levels to the given unit. Called after bonus conversations typically

/jump {line}
Jump to the given line index in the current cutscene and parse from there.

/hidedialogue
Hides the dialogue box, BUT the cutscene system will keep running. Mainly used for when a cutscene happens during a battle and units are being placed but no dialogue is happening.

/placeplayerunits
Sometimes, player and enemy units are placed during a cutscene. First example of this is in chapter 4 before the retool boss.
in this example, place all the player's units down and then proceed with the cutscene.

/placeenemyunits
Will retrieve the battle stored by /battle {battleName} and place the enemy units stored in that battle's formation. Called when a cutscene happens in the middle of placing units like in ch4.

/recruit {unitName}
add the unit with the given name to the party as an alive unit.
example: /recruit Romra - will add romra to the party.

/recruitchoice {unitName}
This is NOT an if branch but will probably always be used directly before one. 
In the original code, these 3 lines are repeated before each recruitment:
"[Recruit {unitName}?]"
"(Q) Recruit"
"(W) Do not recruit"
You may choose to follow this format or use a different format. I just made to so not all those lines are repeated for every recriutment so you may handle it as you with within the interpreter.
Also, when this choice happens, when the next = or == is reached, listen for Q or W instead of space before moving on, or whatever the inputs are in the new project.
After the player selects, store an internal integer for the choice they selected: 0 for Q/recruited, 1 for W/no recruited. This variable will be used by other instructions so make sure to store it somewhere outside the parse line loop.

/startbattlenextinput
Set some sort of flag to let this interpreter know that on the next space input, instead of moving to the next line, start a battle: place player units, place enemy units, and so on. When that battle is finished, THEN go back to the cutscene and continue from where the cutscene left off.

/startchapter {chapter name}
THIS is what will swap to a new cutscene file. Remove any current branches, change cutscene to the one specified, and start interpreting at the top of that cutscene file at index 0.
example: /startchapter Chapter 01

/wait {seconds}
Wait for N seconds before parsing the next line.
example: /wait 2

---------- INLINE COMMANDS ----------
These commands should ideally be able to be put anywhere outside of a slash command line and be evaluated as soon as the cursor reaches it, in case the dialogue system is changed to one where the text is written typewriter-style character per character. Assuming the game becomes something like that, as soon as a { character is reached, immediately parse everything up until the } and evaluate the command.

{portrait_left:{sprite}}
Set the left portrait.

{portrait_right:{sprite}}
Set the right portrait.
example: {portrait_left:Scien} {portrait_right:Proton}

this is what it would look like if more inline functionality were added:
Proton: Hello, my name is {textsize:999}Proton Xurr!!!!

---------- DIALOGUE -----------
If a line doesn't have any of the afforementioned tokens at the start, it is just an ordinary dialogue line. Display it to the screen.
Note that the linecounts have been removed so if they are being displayed seperately for each line like the original than just increase the line count each time a new line is interpreted and reset that count to 0 when dialogue is cleared by a = or ==.
example: Proton: Hey, wait a second...
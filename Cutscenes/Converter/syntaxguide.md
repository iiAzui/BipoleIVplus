CONVERTED CUTSCENE SYNTAX
contains what each token should do

---------- GENERAL ----------
=
Wait for user input before moving to the next dialogue.

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
UnitsAliveGreater {number}
If player has more than N units alive in their party, and false if equal or less.
example: /elif UnitsAliveGreater 1

UnitsAliveEqual {number}
If player has exactly N units alive in the party.

IsAlive {unitName}
If the unit with the given name is alive in the party.
example: /elif IsAlive Scien

---------- COMMANDS ----------
If a line starts with a slash /, it contains a command, likely with some preceding arguments. Parse and evaluate this command immediately, and then move onto the next line.

/chapterlevel
Sets the current chapter level variable. (If there is some sort of chapter object, this could/should probably be taken out of the cutscene and moved there, for less global variable cluttering shenanigans)

/bgcolor {color}
color - black, green, etc.
set the cutscene background color to this color.

/battle {battleName}
After the current dialogue line, AkA the moment the next = or == is reached, start a battle. Is important that the current line index in the file is saved somewhere! When a battle is completed in the original game it does not call some kind of cutscene start function; rather, control is given back to the cutscene file and the cutscene function is called to resume the cutscene loop at the current index. SO store the current cutscene and index in the cutscene somewhere in memory.
example: /battle Chapter1

/startchapter {chapter name}
THIS is what will swap to a new cutscene file. Remove any current branches, change cutscene to the one specified, and start interpreting at the top of that cutscene file at index 0.
example: /startchapter Chapter 01

/recruit {unitName}


/choice RecruitRomra
This is NOT an if branch but will probably always be used directly before one. Prompt the user with a choice on the screen

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
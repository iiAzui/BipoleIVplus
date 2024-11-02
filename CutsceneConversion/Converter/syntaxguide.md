# Converted Cutscene Syntax Specification

This document contains what each token should do in Converted Cutscene language, a purely functional programming language for cutscenes.

## General

### `=`

Wait for user input before moving to the next dialogue.
It'll only wait for input after this if it's not currently within an ignored branch section.

### `==`

This is the same as `=`, but also close any opened [`if-else`](#if-condition) branches.

## Branching

### `/if {condition}`

:condition: - see [conditions](#conditions).

Open an if statement. These shoud be kep track of using a stack list of bools.
Check the condition; if `true`, add a `true` to the stack, if `false`, add a `false` to the stack. 
There is no designated inner code ending token or anything like tabs in Python or `}` in JavaScript.
All lines should be considered inside of the statement's body until an [`/elif`](#elif-condition), [`/else`]((#else)), or [`==`](#-1) is reached.
`==` should remove all stacks and /elif will replace the current highest in the stack.

Example:

```
/if UniteAliveGreater 1
````

Add `true` to the stack if there's more than 1 unit, add `false` to the stack if 1 or less.


### `/elif {condition}`

This is the same as an [`if`](#if-condition) branch, but it will only check if it should run this branch if the previous `if` statement was not true.

> [!NOTE]
> This will show up even when there is not an if statement before it!
> Just treat it as a normal if statement if that's the case.
> I would try to somehow write some extra code to make sure an elif will always come after an if, but I don't get paid enough to do this.

### `/else`

Only interpret the below if previous if statement was not true.
Inner code will only be ended by a [`==`](#-1).
Equivalent to `/elif True if` that makes it easier to implement with less keywords.

## Conditions

These conditions will appear after an [`if`](#if-condition) or [`/elif`](#elif-condition) statement.
Also, something like this might show up: `/if IsAlive Romra and IsAlive Scien`
If there is an additional `and` after all the arguments of a condition, it will also check to see if the condition after the `and` is true as well.
As far as I know, I havent seen any `or` operations yet.
Hopefully it stays that way.

### `UnitsAliveGreater {N: number}`

Returns true if player has more than `N` units alive in their party, and false if equal or less.

Example: 

```
/elif UnitsAliveGreater 1
```

### `UnitsAliveEqual {N: number}`

If player has exactly `N` units alive in the party.

### `IsAlive {unitName}`

If the unit with the given `unitName` is alive in the party.

Example: 

```
/elif IsAlive Scien
```

### `ChoiceSelected {N: number}`

If, on the last choice prompt, the player responded with index `N`.

| Index | Key            | Standard Usage                                                               |
| ----- | -------------- | ---------------------------------------------------------------------------- |
| `0`   | <kbd>Q</kbd>   | Recruit                                                                      |
| `1`   | <kbd>W</kbd>   | Do not recruit                                                               |
| `2`   | <kbd>E</kbd>?  | I think the only choice with a third option is the Fael/Erif/Neither choice. |


## Commands

If a line starts with a `/`, it contains a command, likely followed with arguments.
Parse and evaluate this command immediately, and then move on to the next line.

### `/battle {battleName}`

Set the battle that will be started next.
Store this info somewhere.
[`/startbattlenextinput`](#startbattlenextinput), [`/placeenemyunits`](#placeenemyunits) and [`/startbattlenow`](#startbattlenow) may use this stored value.

Example:

```
/battle Chapter1
```

### `/bgcolor {color}`

:color: `black`, `green`, etc.

Set the cutscene background color to this color.

### `/chapterlevel`

Sets the current chapter level variable.
If there is some sort of chapter object, this should probably be taken out of the cutscene and moved there, to reduce global variable cluttering shenanigans.

### `/enablebattlecontrol`

Used when a cutscene happens during the setup of a battle, like in Chapter 4.
When this is called, the cutscene should stop running for now and let the player play out the battle.
Once the battle is done, resume playing the cutscene at the the index under this command.

### `/instantlevelup {unitName} {N}`

Instantly add `N` levels to the given unit.
Typically called after bonus conversations.

### `/jump {line}`

Jump to the given line index in the current cutscene and parse from there.
A form of `GOTO`.

> [!CAUTION]
> Before using, read the original [Letters to the editor: GOTO Considered Harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf), [xkcd #292: goto](https://xkcd.com/292/), [Goto Considered Harmful](https://wiki.c2.com/?GotoConsideredHarmful) on Wiki, and [Go statement considered harmful](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/) (The last one's optional).
> TL;DR?
> Structured programming in all forms is superior to any form of GOTO.

### `/hidedialogue`

Hides the dialogue box, **but** the cutscene system will keep running.
Mainly used for when a cutscene happens during a battle and units are being placed, but no dialogue is happening.

> [!NOTE]
> Whenever a dialogue happens while hidden, the dialogue box should reappear.

### `/placeplayerunits`

Sometimes, player and enemy units are placed during a cutscene.
Currently, the first example of this is in Chapter 4 before the ReTool boss.
In that example, you'd place all the player's units down and before proceeding on with the cutscene.

### `/placeenemyunits`

Will retrieve the battle stored by [`/battle {battleName}`](#battle-battlename) and place the enemy units stored in that battle's formation.
It's called when a cutscene happens in the middle of placing units like in Chapter 4.

### `/recruit {unitName}`

Add the unit with the given name to the party as an alive unit.

Example:

```
/recruit Romra
```

### `/recruitchoice {unitName}`

This is **not** an if branch, but will probably always be used directly before one. 
In the original code, these 3 lines are repeated before each recruitment:

```
[Recruit {unitName}?]
(Q) Recruit
(W) Do not recruit
```

You may choose to follow this format or use a different format.
I just made it so that not all those lines are repeated for every recruitment so that it may handled specially within the interpreter if necessary.
Also, once this choice is made, when the next `=` or [`==`](#-1) is reached, it listens for <kbd>Q</kbd> or <kbd>W</kbd> instead of </kbd>␣</kbd> before moving on, or whatever the inputs are in the project.
After the player selects a choice, store an internal integer for the choice they selected: `0` for <kbd>Q</kbd>/recruited, `1` for <kbd>W</kbd>/not recruited. This variable will be used by other instructions so make sure to store it somewhere outside the parse line loop.

### `/startbattlenextinput`

Set some sort of flag to let this interpreter know that on the next <kbd>␣</kbd> input, instead of moving to the next line, it should start a battle: place player units, place enemy units, and so on.
When that battle is finished, **then** go back to the cutscene and continue from where the cutscene left off.

### `/startchapter {chapter name}`

**This** is what will swap to a new cutscene file.
Remove any current branches, change cutscene to the one specified, and start interpreting from the top of that cutscene file at index `0`.

Example:

```
/startchapter Chapter 01
```

### `/wait {N: number}`

Wait for `N` seconds before parsing the next line.
Keep in mind that this sleeping is synchronous, not asynchronous, and therefore blocks _all_ further computions.

Example:

```
/wait 2
```

## Inline Commands

These commands should ideally be able to be put anywhere outside of a slash command line, and be evaluated as soon as the cursor reaches it in case the dialogue system is changed to one where the text is written typewriter-style character per character.
Assuming the game becomes something like that, as soon as a `{` character is reached, immediately parse everything up until the `}` and evaluate the command.

### `{portrait_left:{sprite}}` & `{portrait_right:{sprite}}`

Set the left and right portraits, respectively.

Example:

```
{portrait_left:Scien} {portrait_right:Proton}
```

This is what it would look like if more inline functionality were added:

```
Proton: Hello, my name is {textsize:999}Proton Xurr!!!!
```

## Dialogue
If a line doesn't have any of the afforementioned tokens at the start, it is just an ordinary dialogue line.
It will be displayed on the screen.
Note that the linecounts have been removed, so if they are being displayed seperately for each line, like the original, than just increase the line count each time a new line is interpreted and reset that count to 0 when dialogue is cleared by an `=` or a [`==`](#-1).

Example:

```
Proton: First line
Second line
Third line
```

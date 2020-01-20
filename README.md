# dicedissector
Python function for extracting data from standard RPG dice roll text (e.g. "roll 2d6+1 damage"). 

Features:
-developed in and tested with Python 3
-uses re (regular expression) module from Python standard library to extract values from dice roll information in text.
-returns results as dictionaries within a list, with either a single or multiple entries
-if no compatible dice information is found, returns None
-requires explicit declaration of the size of a die (e.g. 2d6+1). Incompatible with text from systems such as Steve Jackson Games' GURPS where the value of the dice is assumed (e.g. 2d+1)

Guide to dictionary values:
'dicenum' = Number of dice to roll
'dicevalue' = Highest face value of the die (six-sided, ten-sided, twenty-sided)
'mod' = Any modifiers, whether positive or negative (+1, -3)
'high' = Highest possible value that can be generated with that dice and modifier combination
'low = Lowest possible value that can be generate with that dice and modifier combination

Example of use:
import dicedissector as d

testvalue1 = "To generate your character's ability scores, roll 3d6 for Strength, Dexterity, Constitution, Intelligence, Wisdom and Charisma"
testvalue2 = "Roll 2d6+4 for damage, or 4d6-1 if using the Ray of Cold."

d.diceReader(testValue1)
[{'dicenum': 3, 'dicevalue': 6, 'mod': 0, 'high': 18, 'low': 3}]

d.diceReader(testValue2)
[{'dicenum': 2, 'dicevalue': 6, 'mod': 4, 'high': 16, 'low': 6}, {'dicenum': 4, 'dicevalue': 6, 'mod': -1, 'high': 23, 'low': 3}]

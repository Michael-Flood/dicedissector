import re

def diceReader(value):	
	"""
	Function to read strings containing RPG dice roll information (e.g. "roll 2d6" and return a list of dictionaries
	of integer values expressing the number of dice, the value of the dice (e.g. six-sided), the modifier (e.g. -2, +3), 
	and the highest and lowest possible rolls for that dice set.
	Uses a a regular expression to find the dice values. In the event of multiple dice roll values, returns multiple dictionaries
	within the list in the order the dice roll values are encounter.
	In the event the function cannot find a dice value in the string, returns None.
	Example:
	diceReader("Roll 2d6+2") -> [{'dicenum':2,
								 'dicevalue':6,
								 'mod':2
								 'high':14
								 'low':4}]
	diceReader("Roll either 4d6+3 if PC is a cleric, or 3d6-2 if any other class") ->
								[ {'dicenum':4,
								   'dicevalue':6,
								   'mod':3,
								   'high':27,
								   'low':7},
								  {'dicenum':3,
								   'dicevalue':6,
								   'mod':-2,
								   'high':20,
								   'low':5} ]
	"""
	def getDiceValues(dicestring):
		"""
		Embeeded function to extract dice values from strings and return them as a list to the outer function
		Example: 
		getDiceValues('roll 2d6 or 3d6+1 if PC is a fighter') -> ['2d6', '3d6+1']
		"""
		regex_full = '(\d+d\d+[+-]\d+)|(\d+d\d+)'
		dicelist = re.findall(regex_full, value)
		# clear empty values from dicelist
		alldice = []
		for d in dicelist:
			for e in d:
				if len(e) > 0:
					alldice.append(e)
				else:
					pass
		return alldice
	
	def makeDiceDict(dicevalue):
		"""
		Embedded function to transform a dice string (e.g. '2d6+1') into a dice dictionary that the outer function
		can return to the main program.
		Example:
		makeDiceDict('2d20-2') -> {'dicenum':2,
								   'dicevalue':20,
								   'mod':-2,
								   'high':38,
								   'low':0}
		"""
		dicedict = {'dicenum':0,
					'dicevalue':0,
					'mod':0,
					'high':0,
					'low':0}
		# fill in dicedict values
		# (1) calculate the number of dice
		step_one = dicevalue.split('d')
		numdice = step_one[0] # dicenum is first value in list
		dicedict['dicenum'] = int(numdice)
		# (2) check whether there is a modifier
		step_two = step_one[1] # dicevalue and modifier (if present) are second value in list
		if '+' in dicevalue:
			step_three = step_two.split('+')
			modvalue = step_three[1] # modifier value is second value in step_two list
			dicedict['mod'] = int(modvalue)
			dicedict['dicevalue'] = int(step_three[0])
		elif '-' in dicevalue:
			step_three = step_two.split('-')
			modvalue = step_three[1]
			dicedict['mod'] = -int(modvalue)
			dicedict['dicevalue'] = int(step_three[0])
		else:
			dicedict['dicevalue'] = int(step_two)
		# calculate high and lowvalue
		dicedict['high'] = (dicedict['dicenum'] * dicedict['dicevalue']) + dicedict['mod']
		dicedict['low'] = (dicedict['dicenum'] * 1) + dicedict['mod']
		return dicedict
	
	# main function
	dice = getDiceValues(value)
	dicelist = []
	if len(dice) == 1:
		dicelist.append( makeDiceDict( dice[0] ) )
		return dicelist
	elif len(dice) > 1:
		for d in dice:
			dicelist.append( makeDiceDict(d) )
		return dicelist

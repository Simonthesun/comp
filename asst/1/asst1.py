def swapchars(string):
	s = string.lower()
	most = 0
	least = 0
	most_letter = ""
	least_letter = ""
	new_string = ""
	letter_count = {}
	for letter in s:
		if letter in letter_count:
			letter_count[letter] = letter_count[letter] + 1
		else:
			letter_count[letter] = 1
	for key in letter_count:
		count = letter_count[key]
		if count > most:
			most = count
			most_letter = key
	least = most
	for key in letter_count:
		count = letter_count[key]
		if count <= least:
			least = count
			least_letter = key
	for letter in string:
		if letter == most_letter:
			new_string += least_letter
		elif letter.lower() == most_letter:
			new_string += least_letter.upper()
		elif letter == least_letter:
			new_string += most_letter
		elif letter.lower() == least_letter:
			new_string += most_letter.upper()
		else:
			new_string += letter
	return new_string

def swapcat(n, *args):
	strings = []
	ordered = []
	catted = ""
	for string in args:
		strings.append(string)
	for count in args:
		length = 0
		curr = ""
		for string in strings:
			if len(string) > length:
				length = len(string)
				curr = string
		ordered.append(curr)
		strings.remove(curr)
	i = 0
	while i < n:
		catted += ordered[i]
		i += 1
	return catted

with open('states.txt') as f:
    lines = f.read().splitlines()
abbrev = {}
for state in lines:
	name = state.split(',')[0]
	abbreviation = state.split(',')[1]
	abbrev[abbreviation] = name

def bluesclues(abbreviation):
	if abbreviation in abbrev:
		return abbrev[abbreviation]
	else:
		raise NameError('Not a valid state abbreviation')

def bluesbooze(name):
	for abbreviation in abbrev:
		if abbrev[abbreviation] == name:
			return abbreviation
	raise NameError('Not a valid state name')
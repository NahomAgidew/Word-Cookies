"""
	A script to solve the game "Word Cookies" by
	calculating the permutation of the letters and
	finding a valid English word from that.
	
	Author: Nahom Abi
	Email: nahomagidew@gmail.com
"""

from itertools import permutations
from PyDictionary import PyDictionary

dictionary = PyDictionary()

letters = raw_input('Input Letters (separated by comma): ').split(',')
length = int(raw_input('Input length of word: '))
perms = permutations(letters, length)

for perm in perms:
	word = ''.join(perm)
	try:
		meaning = dictionary.meaning(word)
		print 'Found word:', word
	except Error as e:
		pass

# -*- coding: utf8 -*-
import random
from pattern.en import pluralize

nouns = [x.strip() for x in open("n_lemmas.txt").readlines() \
		if not(x.endswith('s\n'))]
adjs = [x.strip() for x in open("a_lemmas_no_proper.txt").readlines()]
adverbs = [x.strip() for x in open("r_lemmas.txt").readlines()]

class Symbol(object):
	def __init__(self, x=None):
		self.contents = x
	def gen(self):
		raise NotImplemented

class random_pos(Symbol):
	def gen(self, context):
		return random.choice({
			'n': nouns,
			'adj': adjs,
			'adv': adverbs
		}[self.contents])

class random_shape(Symbol):
	def gen(self, context):
		return random.choice(["square", "circle", "rectangle", "triangle",
				"parallelogram", "diamond", "arc", "star", "cross", "bullet",
				"ornament", "arrow", "oval", "bubble"])

class random_style(Symbol):
	def gen(self, context):
		styles = ["shadowed", "notched", "heavy", "turned", "reversed",
				"sideways", "clockwise", "anticlockwise", "circled", "inverted",
				"broken", "thin", "small", "large", "medium", "squared", "ascending",
				"descending", "dotted", "oblique", "wiggly", "double"]
		choose_from = list(set(styles) - set(context))
		return random.choice(choose_from)

class word(Symbol):
	def gen(self, context):
		return self.contents

class random_number(Symbol):
	def gen(self, context):
		return random.choice(["two", "two", "two", "two", "three",
				"three", "three", "four", "five", "six"])

class random_plural_n(Symbol):
	def gen(self, context):
		return pluralize(random.choice(nouns))

class random_dir(Symbol):
	def gen(self, context):
		return random.choice(["left hand", "right hand", "right", "left",
				"lower left", "lower right", "upper right", "upper left",
				"left-facing", "right-facing",
				"up-pointing", "down-pointing", "northeast-pointing",
				"northwest-pointing", "southeast-pointing", "southwest-pointing",
				"ascending", "descending", "vertical", "horizontal"])

class random_prep(Symbol):
	def gen(self, context):
		return random.choice(["over", "above", "on top of", "beneath", "under",
				"next to", "beside", "behind", "in", "outside of"])

def expand(rules, axiom):
	expansion_list = random.choice(rules[axiom])
	expanded = list()
	for elem in expansion_list:
		if isinstance(elem, Symbol):
			expanded.append(elem.gen(expanded))
		else:
			expanded.extend(expand(rules, elem))
	return expanded

if __name__ == "__main__":

	rules = {
		'simple-emoji': [
			(random_pos('adv'), random_pos('adj'), random_pos('n')),
			(random_pos('adv'), random_pos('adj'), random_pos('n')),
			(random_pos('adv'), random_pos('adj'), random_pos('n')),
			('np',),
			('np',),
			('np',),
			('np',),
			('np',),
			('np',),
			('np',),
			(random_pos('n'), random_pos('n')),
			(random_pos('n'), random_pos('n')),
			(random_pos('n'), random_pos('n')),
			(random_number(), 'np-plural'),
			(random_number(), 'np-plural')
		],
		'compound-emoji': [
			(random_shape(), word('with'), 'np'),
			('np', word('symbol')),
			('np', word('sign')),
			(random_pos('adj'), word('symbol')),
			(random_pos('adj'), word('symbol'), word('for'), 'simple-emoji'),
			(random_pos('adj'), word('sign')),
			(random_pos('adj'), word('sign'), word('for'), 'simple-emoji'),
			(word('symbol'), word('for'), 'simple-emoji'),
			(word('symbol'), word('for'), 'simple-emoji'),
			(word('sign'), word('for'), 'simple-emoji'),
			(random_pos('adj'), word('symbol'), word('for'), 'simple-emoji'),
			(random_pos('adj'), word('symbol'), word('for'), 'simple-emoji'),
			(random_pos('adj'), word('sign'), word('for'), 'simple-emoji'),
			(random_dir(), 'simple-emoji'),
			(random_dir(), 'simple-emoji'),
			(random_dir(), 'simple-emoji'),
			(random_style(), 'simple-emoji'),
			(random_style(), 'simple-emoji'),
			(random_style(), 'simple-emoji'),
			(random_style(), random_style(), 'simple-emoji'),
			(random_style(), random_style(), random_style(), 'simple-emoji'),
			('simple-emoji', word('with'), 'simple-emoji'),
			('simple-emoji', word('and'), 'simple-emoji'),
			('simple-emoji', random_prep(), 'simple-emoji'),
			('simple-emoji', random_prep(), 'simple-emoji'),
			(random_number(), 'np-plural'),
			(random_pos('n'), word('face')),
			(random_pos('adj'), word('face')),
			(random_pos('n'), word('face'), word('with'), 'simple-emoji'),
			(random_pos('adj'), word('face'), word('with'), 'simple-emoji'),
		],
		'np': [
			(random_pos('n'),),
			(random_pos('n'),),
			(random_pos('adj'), random_pos('n'))
		],
		'np-plural': [
			(random_plural_n(),),
			(random_plural_n(),),
			(random_pos('adj'), random_plural_n())
		],
		'emoji': [
			('simple-emoji',),
			('compound-emoji',)
		]
	}

	while True:
		print ' '.join(expand(rules, 'emoji')).upper()


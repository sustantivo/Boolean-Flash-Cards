# flash cards for learning Boolean expresions in python
# DO NOT type in your answer, just think it and hit enter
# Thanks

import random
import time

print("""\n\t!!Flash cards!!
	\n\tPress ENTER to reveal card
	\n\tPress CTRL-C to quit
	\n Let's go!!""")

# list of questions and answers
not_false = ["\nnot False", "True\nNOT operator reverses the result, returns False if the result is true"]
not_true = ["\nnot True", "False\nNOT operator reverses the result, returns False if the result is true"]
true_or_false = ["\nTrue or False", "True\nOR operator returns True if one of the statements is true"]
true_or_true = ["\nTrue or True", "True\nOR operator returns True if one of the statements is true"]
false_or_true = ["\nFalse or True", "True\nOR operator returns True if one of the statements is true"]
false_or_false = ["\nFalse or False", "False\nOR operator returns True if one of the statements is true"]
true_and_false = ["\nTrue and False", "False\nAND operator Returns True if both statements are true"]
true_and_true = ["\nTrue and True", "True\nAND operator Returns True if both statements are true"]
false_and_true = ["\nFalse and True", "False\nAND operator Returns True if both statements are true"]
false_and_false = ["\nFalse and False", "False\nAND operator Returns True if both statements are true"]
not_true_or_false = ["\nnot True or False", "False\nNOT operator reverses the result, returns False if the result is true\nOR operator returns True if one of the statements is true"]
not_true_or_true = ["\nnot True or True", "True\nNOT operator reverses the result, returns False if the result is true\nOR operator returns True if one of the statements is true"]
not_false_or_true = ["\nnot False or True", "True\nNOT operator reverses the result, returns False if the result is true\nOR operator returns True if one of the statements is true"]
not_false_or_false = ["\nnot False or False", "True\nNOT operator reverses the result, returns False if the result is true\nOR operator returns True if one of the statements is true"]
not_true_and_false = ["\nnot True and False", "False\nNOT operator reverses the result, returns False if the result is true\nAND operator Returns True if both statements are true"]
not_true_and_true = ["\nnot True and True", "False\nNOT operator reverses the result, returns False if the result is true\nAND operator Returns True if both statements are true"]
not_false_and_true = ["\nnot False and True", "True\nNOT operator reverses the result, returns False if the result is true\nAND operator Returns True if both statements are true"]
not_false_and_false = ["\nnot False and False", "False\nNOT operator reverses the result, returns False if the result is true\nAND operator Returns True if both statements are true"]
adoesnotb = ["\n1 != 0", "True\n!= operator means not equal"]
adoesnota = ["\n1 != 1", "False\n!= operator means not equal"]
bdoesnta = ["\n0 != 1", "True\n!= operator means not equal"]
bdoesnotb = ["\n0 != 0", "False\n!= operator means not equal"]
a__b = ["\n1 == 0", "False\n== operator means is equal"]
a__a = ["\n1 == 1", "True\n== operator means is equal"]
b__a = ["\n0 == 1", "False\n== operator means is equal"]
b__b = ["\n0 == 0", "True\n== operator means is equal"]

# all question variables in list for rand_question
global question_list
question_list = [
	not_false, not_true, 
	true_or_false, true_or_true, false_or_true, false_or_false, 
	true_and_false, true_and_true, false_and_true, false_and_false, 
	not_true_or_false, not_true_or_true, not_false_or_true, not_false_or_false, 
	not_true_and_false, not_true_and_true, not_false_and_true, not_false_and_false, 
	adoesnotb, adoesnota, bdoesnta, bdoesnotb, 
	a__b, a__a, b__a, b__b
]

# returns a random variable from question_list
def rand_question(l):
	random_question = random.choice(l)
	return random_question

# ask's user questions and gives result
def question(q):
	print(q[0], end=' ')
	quit = input("")
	print(q[1])


# loops
def flash_card_game():
	question(rand_question(question_list))
	time.sleep(.5)
	flash_card_game()


flash_card_game()

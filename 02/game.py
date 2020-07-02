#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """
    Pick NUM_LETTERS letters randomly. Hint: use stdlib random
    output: list
    """

    # initialize list for drawn letters
    letters = []

    # run loop to draw 7 letters at random
    counter = 0
    while counter < NUM_LETTERS:
        letters += random.choice(POUCH)
        counter += 1

    return letters

def input_word(draw):
    """
    Ask player for a word and validate against draw.
    Use _validation(word, draw) helper.
    input: list of drawn letters
    output: string
    """

    # set up loop to keep asking for inputs until input
    # conforms to drawn letters and is a valid word
    validated = False
    while validated == False:
        word = input("Give a word!: ").upper()
        if _validation(word,draw) == (True, True):
            # print("validated!")
            validated = True
            return word
        else:
            print("Not a valid word, try again!")


def _validation(word, draw):
    """
    Validations: 1) only use letters of draw, 2) valid dictionary word
    input: string, list
    output: tuple of two booleans
    """
    in_draw = ''
    in_dictionary = ''

    # check that input word only uses letters of draw
    for l in word:
        if l not in draw:
            in_draw = False
        else:
            in_draw = True

    # check that input is a valid word acc to dictionary
    if word.strip().lower() in DICTIONARY:
        in_dictionary = True
    else:
        in_dictionary = False

    return (in_draw, in_dictionary)

# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    validated_list = set([x for x in _get_permutations_draw(draw)
                        if _validation(x, draw) == (True, True)])
    return sorted(validated_list)

def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    permutations = []
    for x in range(1,8):
        for l in itertools.permutations(draw, x):
            word = ''
            for x in l:
                word += x
            permutations.append(word)
    return permutations

# board = draw_letters()
# permutations = []
# for x in range(1,8):
#     for l in itertools.permutations(board, x):
#         word = ''
#         for x in l:
#             word += x
#         permutations.append(word)





# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()

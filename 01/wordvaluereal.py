from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open("/Users/daniellibatique/code/github-repos/challenges/01/dictionary.txt") as f:
        raw = f.read()

    dictionary = [x for x in raw.split("\n") if x != ""]

    return dictionary

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    value = 0
    for l in word:
        l = l.upper()
        if l.isalpha():
            value += LETTER_SCORES[l]
    return value

def max_word_value(list):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    values = [(x, calc_word_value(x)) for x in list]
    sorted_by_second = sorted(values, key=lambda tup: tup[1])
    return sorted_by_second[-1][0]


if __name__ == "__main__":
    pass # run unittests to validate

print(max_word_value(load_words()))

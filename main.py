# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string, math

bag_o_words_source = []

with open('words.txt', 'r') as fb:
    for x in fb.readlines():
        if len(x) == 6:
            bag_o_words_source.append((x.strip()))

bag_o_words_source = sorted(bag_o_words_source)

greens = '0RO00'

yellows = {
    'M': [4],
}

greys = [
    'W',
]


def get_freq(greens: str, yellows: dict, bag_o_words):

    frequency = {}

    lettersleft = [x for x in string.ascii_uppercase if x not in greens]

    lettersleft = [x for x in lettersleft if x not in yellows.keys()]

    for letter in [x for x in list(''.join(bag_o_words)) if x in lettersleft]:
        frequency[letter] = frequency.get(letter, 0) + 1

    frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    return frequency


def rate_words(bag_o_words: list, frequency:dict):

    ratings = {}

    for word in bag_o_words:
        score = 0
        for x in frequency.keys():
            if x in word:
                score += frequency.get(x, 0)
        ratings[word] = score

    ratings = dict(sorted(ratings.items(), key=lambda x: x[1], reverse=True))

    return ratings


def guess(greens: str = greens, yellows: dict = yellows, greys: list = greys):

    bag_o_words = bag_o_words_source

    for h in greys:
        bag_o_words = [x for x in bag_o_words if h not in x]

    for i in range(len(greens)):
        if greens[i] != '0':
            bag_o_words = [x for x in bag_o_words if x[i] == greens[i]]

    for j in yellows.keys():
        bag_o_words = [x for x in bag_o_words if j in x]
        for k in yellows[j]:
            bag_o_words = [x for x in bag_o_words if x[k] != j]

    frequency = get_freq(greens, yellows, bag_o_words)

    ratings = rate_words(bag_o_words, frequency)

    print(len(bag_o_words))
    print(bag_o_words)
    print(len(frequency.keys()))
    print(frequency)
    print(ratings)

def get_lens():
    with open('actual_words.txt', 'r') as fa:
        actual_len = len(fa.readlines())

    with open('options_words.txt', 'r') as fb:
        options_len = len(fb.readlines())

    return [options_len, actual_len]

def run_sim():
    # for word in options:
    #     pos_remaining = number_of_possibilities
    #     for i in range(len(word)):
    #         pos_remaining = pos_remaining - len([x for x in options if options[i] == word[i]])
    #     print('')
    pass

def get_remaining_options(guessed_word, actual_word):
    with open("options_words.txt", 'r') as of:
        options = [x.strip() for x in of.readlines()]

    options = [x for x in options ]

    colors = get_colors(guessed_word, actual_word)



def get_colors(guessed_word, actual_word):

    color_grid = []

    for i in range(len(guessed_word)):
        if guessed_word[i] in actual_word:
            color = 'ylo'
        else:
            color = 'gry'
        if guessed_word[i] == actual_word[i]:
            color = 'grn'
        color_grid.append(color)
    print(color_grid)





def validate_guess(word):
    with open("options_words.txt", 'r') as of:
        options = [x.strip() for x in of.readlines()]

    number_of_possibilities = get_lens()[0]

    pos_remaining = number_of_possibilities

    for char in word:
        pass

    for i in range(len(word)):
        options = [x for x in options if word[i] in x]


        count = number_of_possibilities - len([x for x in options if options[i] == word[i]])

        pos_remaining = pos_remaining - count
        print(f'letter "{word[i]}" reduces possibilities by {count}')

    print(f'word {word} reduces space to {pos_remaining} options, with entropy of {get_entropy(pos_remaining)}')



def get_entropy(pos_space):
    return math.log(1/(1/pos_space), 2)

if __name__ == "__main__":
    guess()
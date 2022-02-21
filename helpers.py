import string

def color_format(code, string):
    return f'\033[{code}m{string}\033[0m'

def get_freq(greens, yellows, options):

    frequency = {}

    lettersleft = [x for x in string.ascii_lowercase if x not in greens]

    lettersleft = [x for x in lettersleft if x not in yellows.keys()]

    for letter in [x for x in list(''.join(options)) if x in lettersleft]:
        frequency[letter] = frequency.get(letter, 0) + 1

    frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    return frequency

def rank_words(bag_o_words, frequency):
    ratings = {}

    for word in bag_o_words:
        score = 0
        for x in frequency.keys():
            if x in word:
                score += frequency.get(x, 0)
        ratings[word] = score

    ratings = dict(sorted(ratings.items(), key=lambda x: x[1], reverse=True))

    return ratings
import random

from helpers import *
from entropy import EntropyMagic


class GameState:
    def __init__(self, answer=None, verbose=False, use_entropy=False):
        self.verbose = verbose
        self.solved = False
        self.turns = 0
        self.greens = ['0', '0', '0', '0', '0']
        self.yellows = dict()
        self.greys = []
        with open('options_words.txt', 'r') as fo:
            self.options = [x.strip() for x in fo.readlines()]
        if answer:
            self.actual_word = answer
        else:
            self.actual_word = random.choice(self.options)
        self.freq = get_freq(self.greens, self.yellows, self.options)
        self.rankings = rank_words(self.options, self.freq)
        self.use_entropy = use_entropy
        self.entropy_magic = EntropyMagic()

    def update_frequency(self):
        self.freq = get_freq(self.greens, self.yellows, self.options)

    def update_rankings(self):
        self.rankings = rank_words(self.options, self.freq)

    def words_left(self, last_guess):
        self.options.remove(last_guess)
        for h in self.greys:
            self.options = [x for x in self.options if h not in x]

        for i in range(len(self.greens)):
            if self.greens[i] != '0':
                self.options = [x for x in self.options if x[i] == self.greens[i]]

        for j in self.yellows.keys():
            if j not in self.greens:
                self.options = [x for x in self.options if j in x]
                for k in self.yellows[j]:
                    self.options = [x for x in self.options if x[k] != j]

        if '0' not in self.greens:
            self.solved = True
            if self.verbose:
                print(f'You won in {self.turns} turns!!!')

    def format_output(self, word):
        output = []
        for i in range(len(word)):
            code = 0
            if word[i] == self.greens[i]:
                code = '42;30'
            elif i in self.yellows.get(word[i], []):
                code = '103;30'
            output.append(color_format(code, word[i]))
        return ''.join(output)

    def choose_word(self):
        if self.use_entropy:

            invalid_options = [x for x in self.entropy_magic.entropy_list.keys() if x not in self.options]
            for x in invalid_options:
                self.entropy_magic.entropy_list.pop(x)
            choice = max(self.entropy_magic.entropy_list.items(), key=lambda x: x[1])[0]
        else:
            choice = max(self.rankings.items(), key=lambda x: x[1])[0]
            # return random.choice(self.options)

        return choice

    def guess(self, word=None):
        
        if not word:
            word = self.choose_word()

        for i in range(len(word)):
            if word[i] in self.actual_word:
                self.yellows[word[i]] = self.yellows.get(word[i], []) + [i]
            else:
                self.greys.append(word[i])
            if word[i] == self.actual_word[i]:
                self.greens[i] = word[i]
                self.yellows.pop(word[i], None)
        if self.verbose:
            print(self.format_output(word))
        self.turns += 1
        self.words_left(word)
        self.update_frequency()
        self.update_rankings()

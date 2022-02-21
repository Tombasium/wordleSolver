import math, json


class EntropyMagic:

    def __init__(self, recreate_entropy=False):
        with open('options_words.txt', 'r') as of:
            self.options = [x.strip() for x in of.readlines()]
        self.possible_patterns = self.generate_possible_patterns()
        self.recreate_entropy = recreate_entropy
        if self.recreate_entropy:
            self.entropy_list = self.generate_entropy_list()
        else:
            with open('entropy_list.json', 'r') as elf:
                self.entropy_list = json.load(elf)

    def generate_possible_patterns(self):

        possible_patterns = []

        for x in 'GYB':
            for y in 'GYB':
                for z in 'GYB':
                    for a in 'GYB':
                        for b in 'GYB':
                            possible_patterns.append(''.join([x, y, z, a, b]))

        return possible_patterns

    def calculate_entropy(self, frequency: int):
        total_words = len(self.options)
        if frequency != 0:
            return math.log2(1 / (frequency/total_words))
        return 0

    def get_pattern(self, word_a, word_b):
        letters_used = []
        pattern = ''

        for i in range(len(word_a)):

            letters_used.append(word_a[i])

            if word_a[i] == word_b[i]:
                pattern += 'G'

            elif (word_a[i] != word_b[i]) and (word_a[i] in word_b) and (
                    word_b.count(word_a[i]) >= letters_used.count(word_a[i])):
                pattern += 'Y'

            else:
                pattern += 'B'

        return pattern

    def get_pattern_set(self, word):

        patterns = []

        for option in self.options:
            patterns.append(self.get_pattern(word, option))

        return patterns

    def get_pattern_distribution(self, word) -> dict:

        patterns = self.get_pattern_set(word)

        pattern_distribution = {pattern: patterns.count(pattern) for pattern in set(patterns)}
        pattern_distribution = dict(sorted(pattern_distribution.items(), key=lambda x: x[1], reverse=True))

        return pattern_distribution

    def get_entropy_per_pattern(self, word) -> dict:
        
        pattern_distribution = self.get_pattern_distribution(word)

        patterns_entropy = {x: self.calculate_entropy(pattern_distribution.get(x, 0)) for x in self.possible_patterns}
               
        return dict(sorted(patterns_entropy.items(), key=lambda x: x[1], reverse=True))

    def get_entropy_for_guess(self, word):
        pattern_distribution = self.get_pattern_distribution(word)

        pattern_entropy = self.get_entropy_per_pattern(word)

        return sum([(pattern_distribution.get(x, 0)/len(self.options)) * pattern_entropy.get(x, 0) for x in self.possible_patterns])

    def generate_entropy_list(self):

        entropy_list = {word: self.get_entropy_for_guess(word) for word in self.options}

        return dict(sorted(entropy_list.items(), key=lambda x: x[1], reverse=True))

    def make_entropy_file(self):

        with open('entropy_list.json', 'w') as jf:
            json.dump(self.generate_entropy_list(), jf)

    def update_options(self, invalid_options):
        self.options = [x for x in self.options if x not in invalid_options]

#
# entropy_magic = EntropyMagic()
# entropy_magic.make_entropy_file()

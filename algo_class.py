import random

class Sequence():

    def __init__(self, sequence):
        
        sequences = {
            'cclkwise': ['up','left','down','right'],
            'clkwise': ['up','right','down','left'],
            'weighted_pattern': [random.choices(('up','down','left','right'), weights=(.1,.4,.4,.1))[0] for i in range(50)],
            'contra': ['up','up','down','down','left','right','left','right'],
            'rand_pattern': [random.choices(('up','down','left','right'))[0] for i in range(50)]
        }

        self.sequence = sequences[sequence]
        self.index = 0

    def get_move(self):
        curr_move = self.sequence[self.index]
        if self.index < len(self.sequence) - 1:
            self.index += 1
        else:
            self.index = 0

        return curr_move



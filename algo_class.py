class Sequence():
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def get_move(self):
        curr_move = self.sequence[self.index]
        if self.index < len(self.sequence) - 1:
            self.index += 1
        else:
            self.index = 0

        return curr_move



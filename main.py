from random import randint, choice

def collison(ind01, ind02):
    if abs(ind01.pos[0] - ind02.pos[0]) < 30 and abs(ind01.pos[1] - ind02.pos[1]) < 30:
        return True
    else:
        return False

class Individual:
    def __init__(self, type, boardsize=[500,500]):
        self.type = type
        self.pos = [randint(40, boardsize[0]-40), randint(40, boardsize[1]-40)]
        self.boardsize = boardsize
        self.direction = choice((-1, 1)), choice((-1, 1))

    def move(self):
        self.pos[0] += 3*self.direction[0]
        self.pos[1] += 3*self.direction[1]

        self.pos[0] = 40 if self.pos[0] < 40 else self.pos[0]
        self.pos[0] = self.boardsize[0]-40 if self.pos[0] > self.boardsize[0]-40 else self.pos[0]
        self.pos[1] = 40 if self.pos[1] < 40 else self.pos[1]
        self.pos[1] = self.boardsize[1]-40 if self.pos[1] > self.boardsize[1]-40 else self.pos[1]

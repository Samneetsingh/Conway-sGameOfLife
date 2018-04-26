from enum import Enum


class State(Enum):
    DEAD = 0
    ALIVE = 1


class Cell:

    def __init__(self, position):
        self._position = position
        self._life = State.DEAD
        self._neighbours = list()

    def get_position(self):
        return self._position

    def get_life(self):
        return self._life.value

    def set_life(self, state):
        self._life = state

    def get_neighbours(self):
        return self._neighbours

    def set_neighbours(self, neighbours):
        self._neighbours = neighbours

    def __str__(self):
        return "{}: {}".format(self._position, self._life.value)


if __name__ == '__main__':
    cell = Cell((0, 0))
    print(cell)

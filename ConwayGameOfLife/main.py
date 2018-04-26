from cell import State
from board import Board
import time


class GameHandler:
    def __init__(self, seeds, board):
        self._board = board
        for seed in seeds:
            self._board.get_cells()[seed[0]][seed[1]].set_life(State.ALIVE)

    def display(self):
        self._board.display()

    def generate_next_cell(self, position):
        cell = self._board.get_cell(position)
        condition = [cell.get_life() for cell in cell.get_neighbours()]
        print(condition)
        if condition.count(1) < 2 and cell.get_life == State.DEAD:
            return State.DEAD
        elif (condition.count(1) == 2 or condition.count(1) == 3) and cell.get_life == State.DEAD:
            return State.ALIVE
        elif condition.count(1) > 3 and cell.get_life == State.DEAD:
            return State.DEAD
        elif condition.count(1) == 3 and cell.get_life == State.ALIVE:
            return State.ALIVE

    def run(self):
        while True:
            self.display()
            positions = dict()
            for r in range(self._board.get_rows()):
                for c in range(self._board.get_cols()):
                    positions[(r, c)] = self.generate_next_cell((r, c))
            for pos, state in positions.items():
                self._board.get_cell(pos).set_life(state)
            print("Iteration", end='\n\n\n')
            time.sleep(2)


if __name__ == '__main__':
    # Blinker Pattern
    seed = [(1, 2), (2, 2), (3, 2)]
    board = Board(5, 5)
    gm = GameHandler(seed, board)
    gm.run()

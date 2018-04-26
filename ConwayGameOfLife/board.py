from cell import Cell


class Board:

    def __init__(self, nrows, mcol):
        self._grid_rows = nrows
        self._grid_col = mcol
        self._cells = list()
        self._create_grid()
        [self._map_neighbour((r, c)) for r in range(self._grid_rows) for c in range(self._grid_col)]

    def _map_neighbour(self, position):
        neighbours = list()
        start_row = position[0] - 1
        start_col = position[1] - 1
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if (r, c) != position and r != -1 and c != -1 and r != self._grid_rows and c != self._grid_col:
                    neighbours.append(self._cells[r][c])
        self._cells[position[0]][position[1]].set_neighbours(neighbours)

    def _create_grid(self):
        for r in range(self._grid_rows):
            self._cells.append([Cell((r, c)) for c in range(self._grid_col)])

    def get_rows(self):
        return self._grid_rows

    def get_cols(self):
        return self._grid_col

    def get_cell(self, position):
        return self._cells[position[0]][position[1]]

    def get_cells(self):
        return self._cells

    def display(self):
        top = True
        for row in range(self._grid_rows):
            if top:
                for col in range(self._grid_col):
                    print("-", end='\t-\t')
                print('-\n')
            print('|', end='\t')
            for col in range(self._grid_col):
                print("{}".format(self._cells[row][col].get_life()), end='\t|\t')
            print('\n')
            for col in range(self._grid_col):
                print("-", end='\t-\t')
            print('-\n')
            top = False


if __name__ == '__main__':
    b = Board(3, 3)
    cell = b.get_cells()
    b.display()
    print(b.get_cell((0, 0)).get_neighbours())

import Cell
import SubGrid
import Grid


sg1 = SubGrid.SubGrid(0, [Cell.Cell(1, 0, 1), Cell.Cell(1, 2, 5), Cell.Cell(2, 2, 2)])
sg2 = SubGrid.SubGrid(1, [Cell.Cell(0, 1, 6), Cell.Cell(0, 2, 5), Cell.Cell(1, 1, 2), Cell.Cell(2, 0, 8)])
sg3 = SubGrid.SubGrid(2, [Cell.Cell(0, 0, 9), Cell.Cell(0, 1, 2), Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 7), Cell.Cell(1, 1, 6)])
sg4 = SubGrid.SubGrid(3, [Cell.Cell(0, 0, 5), Cell.Cell(0, 1, 3), Cell.Cell(1, 0, 6), Cell.Cell(1, 1, 4), Cell.Cell(2, 2, 7)])
sg5 = SubGrid.SubGrid(4, [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 8), Cell.Cell(0, 2, 9), Cell.Cell(1, 0, 7), Cell.Cell(2, 1, 1)])
sg6 = SubGrid.SubGrid(5, [Cell.Cell(1, 0, 8), Cell.Cell(1, 1, 3), Cell.Cell(2, 1, 4), Cell.Cell(2, 2, 9)])
sg7 = SubGrid.SubGrid(6, [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 9), Cell.Cell(1, 1, 1), Cell.Cell(1, 2, 8)])
sg8 = SubGrid.SubGrid(7, [Cell.Cell(0, 2, 8), Cell.Cell(2, 1, 9), Cell.Cell(2, 2, 1)])
sg9 = SubGrid.SubGrid(8, [Cell.Cell(0, 0, 1), Cell.Cell(0, 1, 5), Cell.Cell(0, 2, 7), Cell.Cell(1, 0, 3), Cell.Cell(2, 0, 2)])

g = Grid.Grid([sg1, sg2, sg3, sg4, sg5, sg6, sg7, sg8, sg9])
print(g)
g.solve()
print(g)



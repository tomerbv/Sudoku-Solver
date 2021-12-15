import Cell
class SubGrid:

#SubGrids class contains a 3x3 Cell matrix that by defult can are blank and can hold any value. cells field is
#the given cells that have a value and will replace the 'blank' Cell in the same ixj location.
#the last field is collected values that will be used late to eliminate possible values for the cells within the matrix
    
    def __init__(self, i, cells=None):
        self.i = i
        self.cells = cells
        self.collected_values = []
        self.grid = [[Cell.Cell(0,0),Cell.Cell(0,1),Cell.Cell(0,2)],
                     [Cell.Cell(1,0),Cell.Cell(1,1),Cell.Cell(1,2)],
                     [Cell.Cell(2,0),Cell.Cell(2,1),Cell.Cell(2,2)]]
        if cells != None:    
            for a in self.cells:
                self.grid[a.i][a.j] = a
                self.collected_values.append(a.value)
            
#update values method checks every cell in the matrix and if its value is certain (one possible value) it'll add that value
#to the collected values field.
                
    def update_values(self):
        for a in self.grid:
            for b in a:
                if len(b.values) == 1 and b.values[0] not in self.collected_values:
                    self.collected_values.append(b.values[0])
    
#remove_values method does almost the opposite of update_values. it uses collected values field to delete unpossible
#values for a certain cell, values that are in the matrix of that cell and arent possible to apear again.
                    
    def remove_values(self, cell):
        if len(self.grid[cell.i][cell.j].values) == 1:
            return
        for a in self.collected_values:
            if a in self.grid[cell.i][cell.j].values and len(cell.values) != 1:
                self.grid[cell.i][cell.j].values.remove(a)
        self.update_values

#check_cells_possibilities method uses remove values method on the entire matrix instead of a specific cell
        
    def check_cells_possibilities(self):
        for a in self.grid:
            for b in a:
                self.remove_values(b)
        
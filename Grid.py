import SubGrid
class Grid:
    def __init__(self, sub_grids=None):
        self.rows = [[],[],[],[],[],[],[],[],[]]
        self.columns = [[],[],[],[],[],[],[],[],[]]
        self.sub_grids = [SubGrid.SubGrid(0), SubGrid.SubGrid(1), SubGrid.SubGrid(2), SubGrid.SubGrid(3),SubGrid.SubGrid(4), SubGrid.SubGrid(5), SubGrid.SubGrid(6), SubGrid.SubGrid(7), SubGrid.SubGrid(8)]
        if sub_grids != None:
            for a in sub_grids:
                self.sub_grids[a.i] = a
            
#Grid class contains a field of 3x3 matrix of 3x3 cell matrix, othe than that it holds two more fields: rows and columns
#that will later hold values so the same index wouldn't apear in the same row or column
        
    
    def __repr__(self):
        res = ''
        for i in range(9):
            if i % 3 == 0:
                res = res + '\n'
            for j in range(9):
                if j % 3 == 0:
                    res = res + '    '
                res = res + str(self.sub_grids[3 * int(i / 3)+ int(j / 3)].grid[i % 3][j % 3]) + ' '
            res = res + '\n'
        return res

#update values methos will add the values of cells we are certain of their value to the relevent rows and columns. every different 
#sub grid 'i' and 'j' index refers to a different row or column so the method inserts the values accordingly

    def update_values(self):
        for a in self.sub_grids:
            for b in a.grid:
                for c in b:
                    if len(c.values) == 1:
                        if a == self.sub_grids[0] or a == self.sub_grids[3] or a == self.sub_grids[6]:
                            if c.values[0] not in self.columns[c.j]:
                                self.columns[c.j].append(c.values[0])
                        
                        if a == self.sub_grids[1] or a == self.sub_grids[4] or a == self.sub_grids[7]:
                            if c.values[0] not in self.columns[c.j+3]:
                                self.columns[c.j+3].append(c.values[0])
                        
                        if a == self.sub_grids[2] or a == self.sub_grids[5] or a == self.sub_grids[8]:    
                            if c.values[0] not in self.columns[c.j+6]:
                                self.columns[c.j+6].append(c.values[0])
                                
                        if a == self.sub_grids[0] or a == self.sub_grids[1] or a == self.sub_grids[2]:
                            if c.values[0] not in self.rows[c.i]:
                                self.rows[c.i].append(c.values[0])
                                
                        if a == self.sub_grids[3] or a == self.sub_grids[4] or a == self.sub_grids[5]:
                            if c.values[0] not in self.rows[c.i+3]:
                                self.rows[c.i+3].append(c.values[0])
                                
                        if a == self.sub_grids[6] or a == self.sub_grids[7] or a == self.sub_grids[8]:    
                            if c.values[0] not in self.rows[c.i+6]:
                                self.rows[c.i+6].append(c.values[0])
                                
#remove values method checks if a specific cell holds the same possible values that are in the columns, rows and collected values
#fields. if they are it'll remove the cells possible values until its left with ine possible value and that is the definite value
#of that cell

    def remove_values(self, cell, grid_num):
        if len(self.sub_grids[grid_num].grid[cell.i][cell.j].values) == 1:
            return
        self.sub_grids[grid_num].remove_values(cell)

        if grid_num == 0 or grid_num == 1 or grid_num == 2:
            for a in self.rows[cell.i]:
                if a in self.sub_grids[grid_num].grid[cell.i][cell.j].values and len(self.sub_grids[grid_num].grid[cell.i][cell.j].values) != 1:
                    self.sub_grids[grid_num].grid[cell.i][cell.j].values.remove(a)
                    self.update_values()
        if grid_num == 3 or grid_num == 4 or grid_num == 5:
            for a in self.rows[cell.i+3]:
                if a in self.sub_grids[grid_num].grid[cell.i][cell.j].values and len(self.sub_grids[grid_num].grid[cell.i][cell.j].values) != 1:    
                    self.sub_grids[grid_num].grid[cell.i][cell.j].values.remove(a)
                    self.update_values()
        if grid_num == 6 or grid_num == 7 or grid_num == 8:
            for a in self.rows[cell.i+6]:
                if a in self.sub_grids[grid_num].grid[cell.i][cell.j].values and len(self.sub_grids[grid_num].grid[cell.i][cell.j].values) != 1:
                    self.sub_grids[grid_num].grid[cell.i][cell.j].values.remove(a)
                    self.update_values()
                    
        
        if grid_num == 0 or grid_num == 3 or grid_num == 6:
            for a in self.columns[cell.j]:
                if a in self.sub_grids[grid_num].grid[cell.i][cell.j].values and len(self.sub_grids[grid_num].grid[cell.i][cell.j].values) != 1:
                    self.sub_grids[grid_num].grid[cell.i][cell.j].values.remove(a)
                    self.update_values()
        if grid_num == 1 or grid_num == 4 or grid_num == 7:
            for a in self.columns[cell.j+3]:
                if a in self.sub_grids[grid_num].grid[cell.i][cell.j].values and len(self.sub_grids[grid_num].grid[cell.i][cell.j].values) != 1:
                    self.sub_grids[grid_num].grid[cell.i][cell.j].values.remove(a)
                    self.update_values()
        if grid_num == 2 or grid_num == 5 or grid_num == 8:
            for a in self.columns[cell.j+6]:
                if a in self.sub_grids[grid_num].grid[cell.i][cell.j].values and len(self.sub_grids[grid_num].grid[cell.i][cell.j].values) != 1:
                    self.sub_grids[grid_num].grid[cell.i][cell.j].values.remove(a)
                    self.update_values()
                    
#check possibilities method goes over 3 other methods to solve the sudoku. hte first is check cells possibilities that removes possible
#cells values for all of the sub grids (the same number cannot apear more than once in a sub grid). the second is update values to
#update the roes and columns for the cells we found a certain value for(the same number cannot apear more than once in a row or column).
#the third is remove values to remove the cells values for the updated rows and columns indexes.
                    
    def check_possibilities(self):
        for a in self.sub_grids:
            a.check_cells_possibilities()
        self.update_values()
        for a in self.sub_grids:
            for b in a.grid:
                for c in b:
                    self.remove_values(c,a.i)
                
#is solved method goes over every cell in the entire grid and checks if it has only 1 possible value. if all of them do the sudoku
#is solved and the method return True, if not it'll return False
        
    def is_solved(self):
        for a in self.sub_grids:
            for b in a.grid:
                for c in b:
                    if len(c.values) == 1:
                        continue
                    else:
                        return False
        return True

#solve method goes over check possibilities method and every time it does so it goes over is solved method right after. the method
#keeps on doing so until the sudoku is complete and is solved breaks the recurtion
    def solve(self):
        self.check_possibilities()
        if self.is_solved():
            return
        else:
            self.solve()
      
                            

    
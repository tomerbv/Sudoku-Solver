class Cell:

#Cell class simply holds and i and j index for the mmatrix which is the SubGrid later. it alost holds the possible
#valuse for that cell and if we only have 1 possible value we know for sure that is the correct value of the cell
#the class represents itself by a blank '_' if the value isn't known and as the value if it is.
    
    def __init__(self, i, j, value=None):
        self.values = [1,2,3,4,5,6,7,8,9]
        self.i = i 
        self.j = j
        self.value = value
        if self.value != None:
            self.values = [self.value]
        
        
    def __repr__(self):
        if len(self.values) == 1:
            return str(self.values[0])
        return '_'
        
    
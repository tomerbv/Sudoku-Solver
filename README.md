# Sudoku-Solver
Sudoku Solver capable of solving any sudoku that is definite by using elimination for each cell's possible values by 3 levels:
- Row level
- Column level
- Sub-grid level (3x3).

once all possible values for a cell except for 1 are eliminated it is assigend that velue.
and so it goes on every iteration, adding definite values and removing possiblilities for unassigned cells until the sudoku is complete.

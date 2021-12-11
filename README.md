Backtracking Sudoku Solver

Carl Powaza


Objective
This program takes in an incomplete sudoku board from a text file. Then turns it into a list and solves using backtracking.



Implementation Details
The raw String from the read-in text file is split into a list of strings in the createGrid() function and returned to the grid list in the main function.

This grid is then passed to solution() along with zeros for the row and column.I did this because it was necessary to have parameters for row and column to help with passing those values during recursion.
The solution function is where everything happens.At first, the row and column are zeros.Meaning when it is first called, it will drop straight to line 92.

Here the program checks if the index at the current row and column on the grid is a “0”.I had to make sure I tested it as a String since that’s how the list was created.If it doesn’t have a “0” at the current index, it will just add one to the current column and recurse.If this index does have a “0”, the program loops 9 times, generating a number each time.This number is then tested against the grid to see if it will work in the current index.This is done using my safeCheck function.This function checks if this generated value already appears in the row, column or local box.The first two were simple, just loop over and test each value.For checking the box.I created a helper function called squareChecker, which checks for which box the column and row are in.Then it loops over the 9 numbers in that box.If a duplicate is found it returns True.

If the value is found to be safe.It is temporarily added to the grid and we pass that grid in along with the row and column plus one.Then the loop continues, until all 9 numbers are tested.The grid location is reset in between so that checkSafe doesn’t have to test if the val at the current index.

	The solution function will continue to be recursed, resetting the column value to zero once it reaches nine.The row is incremented by one at the same time.Once the recursion causes enough incrementing to where the column and row value are greater than eighth.At that point, the recursion stops.The last value is filled , the grid is printed and the function returns true.


Running the Program
This program must be run by executing py final_project.py example.txt Where example.txt is a text file in the same folder as the python file.The text file should have 9 rows of 9 numbers, separated by a space and a newline between rows.The empty fields should be represented as a “0”.The program assumes all numbers in the text file will be valid as per Sudoku rules.






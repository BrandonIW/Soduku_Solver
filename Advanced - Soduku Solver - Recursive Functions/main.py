# Step 1: Input starting puzzle board as a list of lists
# Step 1a: May want to try a validate the "puzzle" input and format it automatically
# Step 2: Check where on the puzzle we can fill in a spot. I.e. if it's an open space, the computer will assign a number to it - Done
# Step 3: Validate and see if that guessed number is valid

'''
[
[0, 1, 2, 3, 4, 5, 6, 7, 8],
[0, 1, 2, 3, 4, 5, 6, 7, 8],
[0, 1, 2, 3, 4, 5, 6, 7, 8],
[0, 1, 2, 3, 4, 5, 6, 7, 8],
[0, 1, 2, 3, 4, 5, 6, 7, 8],
[0, 1, 2, 3, 4, 5, 6, 7, 8],
[0, 1, 2, 3, 4, 5, 6, 7, 8],
[0, 1, 2, 3, 4, 5, 6, 7, 8],
[0, 1, 2, 3, 4, 5, 6, 7, 8]
]

Our soduku puzzle will look something like the below. So basically just a list of lists with -1 representing a space
that is empty. The rest of the numbers represent valid positions on the board. 

[
[3, 9, -1,  -1, 5, -1,  -1, -1, -1],
[-1, -1, -1,  2, -1, -1,  -1, -1, 5],
[-1, -1, -1,  7, 1, 9,  -1, 8, -1],

[-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
[2, -1, 6,  -1, -1, 3,  -1, -1, -1],
[-1, -1, -1,  -1, -1, -1,  -1, -1, -4],

[5, -1, -1,  -1, -1, -1,  -1, -1, -1],
[6, 7, -1,  1, -1, 5,  -1, 4, -1],
[1, -1, 9,  -1, -1, -1,  2, -1, -1],
]
'''


class Soduko:

    def __init__(self,puzzle):
        self.puzzle = puzzle
        self.solve_soduku(self.puzzle)



## Finds the coordinates in the soduku puzzle that are empty and we can take a guess
## If we get None return from find_next_empty, that means the puzzle is solved
## Then we guess a value between 1-9 and if it's valid we can put in that position in the puzzle

    def solve_soduku(self,puzzle):
        row, column = self.find_next_empty(puzzle)

        if row is None:
            print(self.puzzle)
            return True

        # If the guess we make is valid, then we can continue with the recursion. So if we guess "4" and it's valid in all
        # rows/columns/3x3 that it's in, then we edit the self.puzzle to replace -1 with "4" and call the function again.
        # So we find the next row/column. If it's not None (i.e. if there's still an open spot available) then we guess again
        # Eventually we'll hit the end where row is None, and so we return True. If self.solve_soduku is true, then we've
        # reached the end and we backtrace our steps all the way to the top and we're done

        # If the guess is not valid, then we just reset that spot to -1 and find_next_empty will find that spot and try again

        for guess in range(1,10):
            if self.is_valid(puzzle,guess,row,column):
                self.puzzle[row][column] = guess

                if self.solve_soduku(self.puzzle):
                    return True

            puzzle[row][column] = -1 #Reset the guess

        return False



## Finds the next row,col on the puzzle that's not filled yet. If all spaces are filled, return (None, None).
## Otherwise you'll get stuff like (1,4) or (5,6) etc. etc.

    def find_next_empty(self,puzzle):
        for row in range(9):
            for column in range(9):
                if puzzle[row][column] == -1:
                    return row, column
        return None, None


## Figures out if a certain guess is valid. As in, if that number already exists in the row, column, or 3x3 square, then it's not valid
## For the 3x3, we can do this by getting where that 3x3 square starts based on our given row/column coordinates. Then we iterate.
## So if my row,column is 4,1, then I should be able to find 3,0.
    def is_valid(self,puzzle,guess,row,column):

        row_vals = puzzle[row]
        if guess in row_vals:
            return False

        col_vals = [puzzle[_][column] for _ in range(9)]
        if guess in col_vals:
            return False

        row_start = (row // 3) * 3
        column_start = (column // 3) * 3
        for row in range(row_start, row_start+3):
            for column in range(column_start, column_start+3):
                if puzzle[row][column] == guess:
                    return False

        return True


if __name__ == '__main__':
    board = [
        [-1, -1, 5,  3, -1, -1,  -1, -1, -1],
        [8, -1, -1,  -1, -1, -1,  -1, 2, -1],
        [-1, 7, -1,  -1, 1, -1,  5, -1, -1],

        [4, -1, -1,  -1, -1, 5,  3, -1, -1],
        [-1, 1, -1,  -1, 7, -1,  -1, -1, 6],
        [-1, -1, 3,  2, -1, -1,  -1, 8, -1],

        [-1, 6, -1,  5, -1, -1,  -1, -1, 9],
        [-1, -1, 4,  -1, -1, -1,  -1, 3, -1],
        [-1, -1, -1,  -1, -1, 9,  7, -1, -1],
    ]
    test = Soduko
    test(board)
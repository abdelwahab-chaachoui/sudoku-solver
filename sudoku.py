puzzle = [              # 0 is where we have to add a number 
    [0,0,0,5,0,0,8,0,9],
    [1,8,0,4,0,0,0,6,0],
    [0,0,0,0,7,0,0,1,0],
    [5,0,0,0,0,0,0,7,0],
    [6,4,9,0,0,0,0,0,0],
    [0,2,0,0,1,0,0,0,0],
    [0,9,0,0,3,2,0,0,0],
    [0,1,0,0,0,5,6,0,0],
    [7,0,0,0,0,0,4,8,0]
]

#find the element that equals 0
def findEmpty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return (i,j) # returns col, row of the first 0 found
    return None # return none if no element equals 0

# check if the number that would be added to position is valid or not
def isValidInsert(puzzle, number, position):
    #(x,y) = findEmptySquare(puzzle)
    
    # 1st step : Check rows
    for i in range(len(puzzle[0])):
        if puzzle[position[0]][i] == number and position[1] != i :   # go through each element in the row
                                                                # and check if its equal to the given number
                                                                # and if the position we're checking is
                                                                # the same position where we just inserted something to
                                                                # we ignore it
            return False
        
    # 2nd step : check column
    for i in range(len(puzzle)):
        if puzzle[i][position[1]] == number and position[0] != i :
            return False
        
    # check 3x3 box
    boxX = position[1] // 3 # integer divide by 3 gives 0, 1 or 2
    boxY = position[0] // 3 
    
    #loop into all the elements of the box
    for i in range(boxY * 3, boxY * 3 + 3): # *3 for checking through the elements
        for j in range(boxX * 3, boxX * 3 + 3):
            if puzzle[i][j] == number and (i,j) != position:
                return False
            
    return True
    

# Backtracking Algorithm
def solveAlgorithm(puzzle):
    if not findEmpty(puzzle): # solved | Best Case of recursion
        return True 
    else:
        row, col = findEmpty(puzzle) # not yet solved, returns the (row,column) of 0
    
    for i in range(1,10):
        if isValidInsert(puzzle, i, (row,col)): # check if adding the number is a valid solution
            puzzle[row][col] = i
            if solveAlgorithm(puzzle): # calling the method again on our new board
                return True
            
            puzzle[row][col] = 0
            
    return False
        
# method to print the puzzle
def printPuzzle(puzzle):
    for i in range(len(puzzle)): # go through columns
        if i % 3 == 0 and i != 0: # after each 3 rows new section
            print('- - - - - - - - - - -')   # separate the puzzle
                                                    # into different section
        for j in range(len(puzzle[0])): # go through rows
            if j%3 == 0 and j != 0:
                print('| ', end = '') # end : doesn't print \n
                
            if j == 8 :
                print (puzzle[i][j]) # print last element of the line
                                     # directly without any spaces
            else:
                print(str(puzzle[i][j])+ ' ', end='')   # insert a space after
                                                        # each other element
                                                        # without adding new line
                
            

print('------- Puzzle -------\n')
printPuzzle(puzzle)
solveAlgorithm(puzzle)
print('\n------ Solution ------\n')
printPuzzle(puzzle)

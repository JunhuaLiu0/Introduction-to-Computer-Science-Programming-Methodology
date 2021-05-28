def printQueenPuzzle(): 
    for i in range(8):
        for j in range(8):
            if queen[i][j]==1:
                print('| | '*j+'|Q| '+'| | '*(7-j))
    print("\n")
    
def checkQueen(row,column):
    for k in range(8):
        if queen[k][column]==1:
            return False 
    for i,j in zip(range(row-1,-1,-1),range(column-1,-1,-1)):
        if queen[i][j]==1:
            return False   
    for i,j in zip(range(row-1,-1,-1),range(column+1,8)):
        if queen[i][j]==1:
            return False          
    return True

def findQueen(row):
    if row>7:
        global count
        count+=1
        printQueenPuzzle()
        return
    for column in range(8):
        if checkQueen(row,column):
            queen[row][column]=1
            findQueen(row+1)
            queen[row][column]=0
count = 0
queen = [[0 for i in range(8)] for i in range(8)] 
findQueen(0)
print("The number of solutions:", count)
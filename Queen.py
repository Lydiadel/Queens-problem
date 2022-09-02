
#left diagonal array  
ld = [0] * 100

# right diagonal array 
rd = [0] * 100

#column array where its indices indicates column and 
#used to check whether a queen can be placed in that 
#    row or not
cl = [0] * 100

# Function to print the board
def printBoard(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end= " ")
        print() 
 
def createBoard(n):
   board = [[0 for x in range(n)] for y in range(n)]
   return board
  
#  Function to define problem
def queenProblem(board, col, n):
    
    # if all queens are placed return true, this function
    # makes sure     
    if (col >= n):
        return True
    
    for i in range(n):
        
        # check to see if there is no queen in the col and
        # row to position
        if ((ld[i - col + n - 1] != 1 and 
             rd[i + col] != 1) and cl[i] != 1):
                   
            # Place the queen in this position
            board[i][col] = 1
            ld[i - col + n - 1] = rd[i + col] = cl[i] = 1
              
            # place the queens in the other column
            if (queenProblem(board, col + 1, n)):
                return True
                  
            # If there is a queen and doesn't lead
            # to a solution
            # remove queen from the board 
            # and do backtrack 
            board[i][col] = 0 
            ld[i - col + n - 1] = rd[i + col] = cl[i] = 0
              
    # Queen cannot be placed in any row or column return false
    return False


# n = Number of queens
def Inicio():
    
   n = int(input("Number of queens?: "))
   
   print("\nN - Queens Back-tracking")

   print(f"Number of Queens: {n}")
   board=createBoard(n)
   print("")
   
   if (queenProblem(board,0,n) == False):
       print("Solution does not exist\n")
       return False
   
Inicio()
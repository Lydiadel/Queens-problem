
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
  

def Inicio():
    
   n = int(input("Number of queens?: "))
   
   print("\nN - Queens Back-tracking")

   print(f"Number of Queens: {n}")
   board=createBoard(n)
   print("")
   
Inicio()
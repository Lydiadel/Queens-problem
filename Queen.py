def createBoard(n):
   board = [[0 for x in range(n)] for y in range(n)]
   return board

# n = Number of queens
def Inicio():
    
   n = int(input("Number of queens?: "))
   
   print("\nN - Queens Back-tracking")

   print(f"Number of Queens: {n}")
   board=createBoard(n)
   print("")
   
   
Inicio()
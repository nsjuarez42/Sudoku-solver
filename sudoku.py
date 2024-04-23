#receive boards from https://sudoku-api.vercel.app/api/dosuku
#make own solution and see if it matches
#be able to generate own sudoku boards

#A 9×9 square must be filled in with numbers from 1-9 with no repeated numbers in each line, horizontally or vertically.
#To challenge you more,
#there are 3×3 squares marked out in the grid, and each of these squares can't have any repeat numbers either.
#https://sudoku-api.vercel.app/
#TODO:
#sudoku generator
#sudoku solver
import requests

def print_board(board):
    for row in board:
        print(row)
    
    for i,row in enumerate(board):
        if i == 0 or i == 3 or i == 6:
            print('-'*23)
        for x,val in enumerate(row):
            if x == 2 or x == 5:
                print(val,end="| ")
            elif x == 0 or x == 3 or x == 6:
                print("|",val,"|",sep="",end="")
            else:
                print(val,end="|")
        print()
    
#solution and board
url = "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value,solution,difficulty},results,message}}"
rjson = requests.get(url).json()
board=rjson['newboard']['grids'][0]['value']
solution=rjson['newboard']['grids'][0]['solution']

def is_correct_num(board,position,value):
    return None
    #check if a number is correcly placed
    
def solver(board):
    #9x9
    #horizontal
    for i in range(1):
        #vert
        #dont need to iterate over x
        for x in range(len(board)):
            if board[x][i] == 0:
                #sudoku square to fill
                #board[x][i] actual square to fill
                available_nums = [i for i in range(1,10)]
                #check  horizontal
                y=0
                #from y to i
                while(y < i):
                    if board[x][y] != 0:
                        try:
                            index = available_nums.index(board[x][y])
                            del available_nums[index]
                        except ValueError:
                            #not found
                            print(board[x][y],"Not found")
                    y+=1
                y+=1
                #from i+1 to end
                while(y < len(board)):
                    if board[x][y] != 0:
                        try:
                            index = available_nums.index(board[x][y])
                            del available_nums[index]
                        except ValueError:
                            #not found
                            print(board[x][y],"not found")
                    y+=1

                #vertical
                z=0
                while(z < x):
                    if board[z][i] != 0:
                        try:
                            index = available_nums.index(board[z][i])
                            del available_nums[index]
                        except ValueError:
                            #not found
                            print(board[z][i],"Not found")
                    z+=1
                z+=1
                #from i+1 to end
                while(z < len(board)):
                    if board[z][i] != 0:
                        try:
                            index = available_nums.index(board[z][i])
                            del available_nums[index]
                        except ValueError:
                            #not found
                            print(board[z][i],"not found")
                    z+=1
                
                
                print(available_nums,"for",board[x][i])
                
                    
                
                
            
        
    #returns solved board
    #number cannot be repeated horizontally or vertically
    #find zeroes
    #horizontal and vertical should have 1-9 only twice
    #available numbers based on vertical and horizontal numbers available
    #iterate vertically and check horizontal lines for every column
    return None 

print("Board")
print_board(board)
##print("Solution")
##print_board(solution)

solver(board)


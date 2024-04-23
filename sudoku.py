#receive boards from https://sudoku-api.vercel.app/api/dosuku
#make own solution and see if it matches
#be able to generate own sudoku boards

#A 9×9 square must be filled in with numbers from 1-9 with no repeated numbers in each line, horizontally or vertically.
#To challenge you more,
#there are 3×3 squares marked out in the grid, and each of these squares can't have any repeat numbers either.
#https://sudoku-api.vercel.app/
import requests
solution_url = "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{solution}}}"
board_url = "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}"

r = requests.get(board_url)
board = r.json()['newboard']['grids'][0]['value']

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
#print(board)

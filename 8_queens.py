
class Board:

    # Constructor
    def __init__(self):
        self.board = []

    def addBoard(self, u):
        self.board = u

    def queensPosition(self): # return sort of the postion of queens by column
        position = []
        for row,value in enumerate(self.board): 
            for column, item in enumerate(value): 
                if self.board[int(row)][int(column)] == "Q":
                    position.append((row+1,column+1))
        return (sorted(position, key= lambda k: k[1])) 

    def getHeuristicCost(self):
        queens_postion = self.queensPosition()
        heuristic_board = [] # create a heuristic board
        for x in range(1, 9): 
            heuristic_list = [] # create a heuristic list
            for y in range(1,9):
                temp = queens_postion.copy() # create temp of queens position 
                temp.remove(queens_postion[y-1])
                temp.append((x, y))
                temp = sorted(temp, key= lambda k: k[1])
                h = 0
                for count1, attack_queen in enumerate(temp):
                    for count2 in range(0,8):
                        attacked_queen = temp[count2]
                        (atk_row, atk_column) = attack_queen 
                        (atked_row, atked_column) = attacked_queen 
                        if count1 < count2: 
                            if (atk_row == atked_row or abs(int(atk_row) - int(atked_row)) == abs(int(atk_column) - int(atked_column))):
                                # increment cost if two queens are in same row or in same diagonal
                                h += 1
                heuristic_list.append(h)
            heuristic_board.append(heuristic_list)

            

        for row_index, row in enumerate(heuristic_board): # check positions of queens to fill "Q"
            row_index += 1
            for item_index, column in enumerate(row):
                item_index += 1
                if (row_index, item_index) in queens_postion:
                    heuristic_board[row_index-1][item_index-1] = "Q"

        string = ""
        for i in heuristic_board:
            for j in i:
                string += str(j) + " "
            string += "\n"
        string = string.rstrip("\n")    
        return(string)


g = Board()

matrix = []

# Read from input file
f = open("input.txt", "r")
for i in f:
    j = [it for it in i.strip().split(' ')]
    matrix.append(j)

f.close()

g.addBoard(matrix)

print(g.getHeuristicCost())

f = open("output.txt", "w")
for item in g.getHeuristicCost():
    f.write(str(item))



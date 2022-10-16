import numpy as np
import random
from itertools import product
import copy

class BotPuzzle():


    def __init__(self):
        self.board = []
        self.win_condition = []
        self.possible_moves = []
        self.column_and_row = 0
        self.hole_position = []
        self.visited = []
        self.width_next_step = []
        self.bidirectional_board = 0
        self.bot_clone = 0
        self.flag = False


    def start(self):
        while True:
            self.board_contructor()
            self.shuffler()
            try:
                iniciate = int(input("Select: 1 for Width search, 2 for bidirectional, 3 for random: "))
                if iniciate == 1:
                    self.width_search()
                if iniciate == 2:
                    self.bidirectional_search()
                if iniciate == 3:
                    self.random_search()
            except:
                print("\n\nExiting...")
                exit()


    def board_contructor(self):
        self.column_and_row = int(input("Enter the number of columns and rows: "))
        piece = 1
        for j in range(self.column_and_row):
            aux_list = [piece+i for i in range(self.column_and_row)]
            self.board.append(aux_list)
            piece += self.column_and_row
        self.board[self.column_and_row-1][self.column_and_row-1] = 0
        self.win_condition = copy.deepcopy(self.board)
        print(self.board)


    def check_hole_position(self):
        self.hole_position = []
        for row in range(self.column_and_row):
            try:
                column = self.board[row].index(0)
                self.hole_position.append(row)
                self.hole_position.append(column)
                break
            except:
                continue
        print("position ", self.hole_position)


    def check_moves(self):
        self.possible_moves = []
        aux_board = copy.deepcopy(self.board)
        for column in range(-1, 2, 2):
            try:
                if self.hole_position[0]+column < 0:
                    continue
                aux_board[self.hole_position[0]+column][self.hole_position[1]] = 0
                self.possible_moves.append((self.hole_position[0]+column,self.hole_position[1]))
            except:
                continue

        for row in range(-1, 2, 2):
            try:
                if self.hole_position[1]+row < 0:
                    continue
                aux_board[self.hole_position[0]][self.hole_position[1]+row] = 0
                self.possible_moves.append((self.hole_position[0],self.hole_position[1]+row))
            except:
                continue
        print("possible moves",self.possible_moves)


    def moving(self):
        move = random.randint(0, len(self.possible_moves)-1)
        print("Selected move: ", self.possible_moves[move])
        self.board[self.hole_position[0]][self.hole_position[1]] = self.board[self.possible_moves[move][0]][self.possible_moves[move][1]]
        self.board[self.possible_moves[move][0]][self.possible_moves[move][1]] = 0


    def check_if_visited(self):
        trial_board = []
        for move in range(len(self.possible_moves)-1, -1, -1):
            # if len(self.possible_moves) == 1:
            #     break
            print("Selected trial move: ", self.possible_moves[move])
            trial_board = copy.deepcopy(self.board)
            trial_board[self.hole_position[0]][self.hole_position[1]] = self.board[self.possible_moves[move][0]][self.possible_moves[move][1]]
            trial_board[self.possible_moves[move][0]][self.possible_moves[move][1]] = 0
            print("TRIAL: ", trial_board)
            trial_tuple = self.convert_to_tuple(trial_board)
            self.width_next_step.append(self.convert_to_tuple(trial_board))
            if trial_tuple in self.visited:
                print("DELETING move")
                self.possible_moves.remove((self.possible_moves[move][0], self.possible_moves[move][1]))
        #print("visited ", self.visited)
        print("possible moves remaining", self.possible_moves)


    def shuffler(self):
        shuffling = int(input("Enter the number shuffles: "))
        print("shuffling...")
        for moves in range(shuffling):
            self.check_hole_position()
            self.check_moves()
            self.moving()
        if self.board == self.win_condition:
            self.shuffler()


    def random_search(self):
        print("\n===================================================")
        print("Random search init")
        print("board ", self.board)
        self.visited = []
        self.visited.append(self.convert_to_tuple(self.board))
        step = 0
        while True:
            print("\nboard state", self.board)
            print("{} steps".format(step))
            self.check_hole_position()
            self.check_moves()
            self.moving()
            step += 1
            if self.board == self.win_condition:
                print("Solved in {} steps".format(step))
                break
    
    
    def switch_board(self):
        self.board = []
        partial_board = []
        for piece in self.width_next_step[0]:
            partial_board.append(piece)
            if len(partial_board) == int(self.column_and_row):
                self.board.append(partial_board)
                partial_board = []
        self.width_next_step.pop(0)
    
    
    def width_search(self):
        print("\n===================================================")
        print("Width search init")
        print("board ", self.board)
        self.visited = []
        self.visited.append(self.convert_to_tuple(self.board))
        step = 0
        while True:
            print("\nboard state", self.board)
            print("{} steps".format(step))
            self.check_hole_position()
            self.check_moves()
            self.check_if_visited()
            self.visited.append(self.convert_to_tuple(self.board))
            self.switch_board()
            step += 1
            if self.board == self.win_condition and self.flag == False:
                print("Solved in {} steps".format(step))
                break
            if self.flag == True:
                self.bidirectional_board = self.convert_to_tuple(self.board)
                break


    def convert_to_tuple(self, lista):
        tupleted = ()
        for i, j in product(range(0, self.column_and_row), range(0, self.column_and_row)):
            tupleted = tupleted + (lista[i][j],)
        return tupleted


    def bidirectional_search(self):
        
        self.bot_clone = BotPuzzle()
        self.bot_clone.board = self.win_condition
        self.bot_clone.column_and_row = self.column_and_row
        self.bot_clone.flag = True
        print("\n===================================================")
        print("Bidirectional search init")
        print("board ", self.board)
        self.visited = []
        self.visited.append(self.convert_to_tuple(self.board))
        step = 0
        while True:
            print("\nboard state", self.board)
            print("\nboard bidirectional state", self.bot_clone.board)
            print("{} steps".format(step))
            self.check_hole_position()
            self.check_moves()
            self.check_if_visited()
            self.visited.append(self.convert_to_tuple(self.board))
            self.switch_board()
            self.bot_clone.width_search()
            step += 1
            if self.bot_clone.bidirectional_board in self.visited:
                print("Solved in {} steps".format(step))
                self.bot_clone.close()
                break
            if self.board == self.win_condition:
                print("Solved in {} steps".format(step))
                self.bot_clone.close()
                break



if __name__ == '__main__':
    
    bot = BotPuzzle()
    bot.start()


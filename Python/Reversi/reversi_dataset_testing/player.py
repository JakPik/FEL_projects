MATRIX_SIZE = 8
 
class MyPlayer:
    """Player"""
    def __init__(self, my_color = 0,opponent_color = 0):
        self.name = "Jakub Pikal"
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.row_coord = 0
        self.column_coord = 0
        self.game_matrix = self.create_matrix()
        self.move_matrix = self.create_matrix()
        pass
 
    def create_matrix(self):
        return [[0 for _ in range (MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
 
    def clear_move_matrix(self):
        for r,c in self.matrix_coord_gen():
            self.move_matrix [r][c] = 0
        return 0
 
    def move(self, board):
        self.clear_move_matrix()
        for r,c in self.matrix_coord_gen():
            self.game_matrix [r][c] = board [r][c]
        for r,c in self.matrix_coord_gen():
            if(self.game_matrix [r][c] == self.my_color):
                self.near_check(r,c)
        self.play_move()
        return (self.row_coord, self.column_coord)
     
    def check_bounds(self, row, column):
        if (row < 0 or column < 0 or row > 7 or column > 7):
            skip = True
        else:
            skip = False
        return skip
 
    def near_check(self, row, column):
        for r in range(-1,2):
            for c in range(-1,2):
                if(self.check_bounds(row + r, column + c) == False):
                    if(self.game_matrix[row + r][column + c] == self.opponent_color):
                        self.line_check_set(row + r, column + c, r, c)
        return 0
 
    def line_check_set(self, row, column, row_coef, column_coef):
        count = 1
        keep_checking = True
        while(keep_checking == True):
            if(self.check_bounds(row + row_coef*count, column + column_coef*count) == False):
                if(self.game_matrix[row + row_coef*count][column + column_coef*count] == self.opponent_color):
                    count += 1
                else:
                    break
            else:
                count -= 1
                break
        if(self.game_matrix[row + row_coef*count][column + column_coef*count] != self.my_color):
            if(self.game_matrix[row + row_coef*count][column + column_coef*count] != self.opponent_color):
                self.move_matrix[row + row_coef*count][column + column_coef*count] += count
                print(self.move_matrix[row + row_coef*count][column + column_coef*count])
                print("color: ",self.game_matrix[row + row_coef*count][column + column_coef*count],"coords",row + row_coef*count,column + column_coef*count)
            else:
                pass
        else:
            pass
        return

    def matrix_coord_gen(self):
        for r in range(MATRIX_SIZE):
            for c in range(MATRIX_SIZE):
                yield r, c

    def play_move(self):
        max_value = 0
        row_idx_optimal = -1
        column_idx_optimal = -1
        for r,c in self.matrix_coord_gen():
            print(r,c,"matrix value:",self.move_matrix[r][c])
            if(self.move_matrix [r][c] > max_value):
                max_value = self.move_matrix [r][c]
                row_idx_optimal = r
                column_idx_optimal = c
        self.row_coord = row_idx_optimal
        self.column_coord = column_idx_optimal
        return 0
     
if __name__=="__main__":
    boards = [  
                [0,0,0,0,1,1,1,0],
                [0,0,0,1,1,0,0,0],
                [0,1,0,0,1,1,0,0],
                [0,1,1,0,1,1,0,0],
                [0,1,1,1,0,1,0,1],
                [0,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,0,None],
                [0,0,0,0,0,0,0,None]
            ]
    d = MyPlayer(1, 0)
    print(d.move(boards))
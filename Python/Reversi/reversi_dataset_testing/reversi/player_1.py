MATRIX_SIZE = 8
 
class MyPlayer:
    """Player"""
    def __init__(self, my_color = 0,opponent_color = 0):
        self.name = "Jakub Pikal"
        self.my_color = my_color
        self.opponent_color = opponent_color
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
        row_coord = 0
        column_coord = 0
        self.clear_move_matrix()
        for r,c in self.matrix_coord_gen():
            self.game_matrix [r][c] = board [r][c]
        for r,c in self.matrix_coord_gen():
            if(self.game_matrix [r][c] == self.my_color):
                for row, column, value in self.near_check(r,c):
                    self.move_matrix[row][column] += value
        row_coord, column_coord = self.play_move(self.move_matrix)
        return (row_coord, column_coord)
     
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
                        yield self.line_check_set(row + r, column + c, r, c)
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
                return row + row_coef*count, column + column_coef*count, count
            else:
                keep_checking = False
        else:
            keep_checking = False
        return row + row_coef*count, column + column_coef*count, 0

    def matrix_coord_gen(self):
        for r in range(MATRIX_SIZE):
            for c in range(MATRIX_SIZE):
                yield r, c

    def optima_check(self, r, c):
        if(r == 1 and (0 < c < 7)):
            return False
        if(r == 6 and (0 < c < 7)):
            return False
        if(c == 1 and (0 < r < 7)):
            return False
        if(c == 6 and (0 < r < 7)):
            return False
        return True

    def predict_move(self, row, column):
        total_value = 0
        new_matrix = self.create_matrix()
        for r, c in self.matrix_coord_gen():
            if(r == row and c == column):
                new_matrix[r][c] = self.my_color
            else:
                new_matrix[r][c] = self.game_matrix[r][c]
        for r,c in self.matrix_coord_gen():
            if(self.game_matrix [r][c] == self.my_color):
                for row, column, value in self.near_check(r,c):
                    total_value += value
        return total_value

    def play_move(self, move_matrix):
        number_of_indexes = -1
        predict_value = []
        idx = []
        max_value_optimal = 0
        max_value = 0
        row_idx = []
        column_idx = []
        for r,c in self.matrix_coord_gen():
            if(move_matrix[r][c] > max_value_optimal and self.optima_check(r,c) == True):
                max_value_optimal = move_matrix [r][c]
                predict_value.append(max_value_optimal - self.predict_move(r, c))
                idx.append(1)
                row_idx.append(r)
                column_idx.append(c)
                number_of_indexes += 1
            elif(move_matrix[r][c] > max_value):
                max_value = move_matrix [r][c]
                predict_value.append(max_value - self.predict_move(r, c))
                idx.append(-1)
                row_idx.append(r)
                column_idx.append(c)
                number_of_indexes += 1
        choice = self.pick_strategy(number_of_indexes, predict_value, idx)
        return row_idx[choice], column_idx[choice]
        
    def pick_strategy(self, number_of_indexes, predict_value, idx):
        compare = -64
        compare_optimal = -64
        return_idx = -1
        return_idx_optimal = -1
        for value_idx in range(number_of_indexes):
            if(idx[value_idx] == 1 and predict_value[value_idx] > compare):
                compare = predict_value[value_idx]
                compare_optimal = compare
                return_idx_optimal = value_idx
            elif(idx[value_idx] == -1 and predict_value[value_idx] > compare):
                compare = predict_value[value_idx]
                return_idx = value_idx
            else:
                return_idx = value_idx
        if(compare_optimal >= compare):
            return return_idx_optimal
        else:
            return return_idx


     
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
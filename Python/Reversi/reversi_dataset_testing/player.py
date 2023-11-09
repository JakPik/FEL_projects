MATRIX_SIZE = 8

class MyPlayer:
    """Player"""
    def __init__(self, my_color, opponent_color):
        self.name = 'Jakub Pikal'
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.play_coord = [0 , 0]
        self.game_matrix = [MATRIX_SIZE][MATRIX_SIZE]
        self.move_matrix = [MATRIX_SIZE][MATRIX_SIZE]
        return 0

    def matrix_read_position(self):
        for r in range(MATRIX_SIZE):
            for c in range(MATRIX_SIZE):
                yield r, c

    def clear_move_matrix(self):
        for coord in self.matrix_read_position():
                self.move_matrix [coord] = 0

    def move(self, board):
        for coord in self.matrix_read_position():
            self.game_matrix [coord] = board [coord]
            if(self.game_matrix [coord] == self.my_color):
                self.near_check(coord)
        self.play_move()
        return self.play_coord
    
    def check_bounds(self, row, column, skip):
        if ((row or column) < 0 or (row or column) > 7):
            skip = True
        else:
            skip = False
        return skip

    def near_check(self, row, column):
        self.clear_move_matrix()
        for r in range(-1,1):
            for c in range(-1,1):
                if((r == 0 and c == 0) or self.check_bounds(row + r, column + c) == True):
                    break
                if(self.game_matrix[row + r][column + c] == self.opponent_color):
                    self.line_check_set(row + r, column + c, r, c)
                print(self.move_matrix[r,c])
        return 0

    def line_check_set(self, row, column, row_coef, column_coef):
        count = 1
        while(self.game_matrix[row + row_coef*count][column + column_coef*count] == self.opponent_color):
            count += 1
        if(self.game_matrix[row + row_coef*count][column + column_coef*count] == self.my_color):
            self.move_matrix[row + row_coef*count][column + column_coef*count] = 0
            return 0
        self.move_matrix[row + row_coef*count][column + column_coef*count] += count
        return 0
    
    def play_move(self):
        max_value = 0
        coord_index_optimal = [-1,-1]
        coord_index = [-1,-1]
        for coord in self.matrix_read_position():
            if(self.move_matrix [coord] > max_value and [1,1] < [coord] < [8,8]):
                max_value = self.move_matrix [coord]
                coord_index_optimal = coord
            elif(self.move_matrix [coord] > max_value):
                max_value = self.move_matrix [coord]
                coord_index_optimal = coord
        if(coord_index_optimal == [-1,-1]):
            self.play_coord = coord_index
            print("optimal")
        else:
            self.play_coord = coord_index_optimal
            print("none")
        return 0
    
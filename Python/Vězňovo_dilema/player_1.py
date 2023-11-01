
class MyPlayer:
    COOP = False
    DEFECT = True

    """Player plays first 4 moves to detect itself, than plays safe variant"""
    def __init__(self, payoff_matrix, number_of_iterations = 0):
        self.iteration = 0
        self.optimal_move = False
        self.win_matrix = []
        self.get_value = []

        for x in range(0,2):
            for y in range(0,2):
                self.values = []
                for z in range(0,2):
                    self.values.append(payoff_matrix[x][y][z])
                self.win_matrix.append(self.evaluate_win_probability(self.values))
                self.get_value.append(self.values[0])
        if(self.win_matrix[1] > self.win_matrix[2]):
            self.optimal_move = self.COOP
        else:
            self.optimal_move = self.DEFECT
        pass

    def record_last_moves(self, my_last_move, opponent_last_move):
        self.My_last_move = my_last_move
        self.Other_last_move = opponent_last_move
        pass

    def move(self):
        self.iteration += 1
        self.response = self.Calculate_strategy()
        return self.response
    
    def Calculate_Optimal_Move(self):

    def evaluate_win_probability(self, values):
        output = 0
        if values[0] > values[1]:
            output = 1
        elif values[0] < values[1]:
            output = -1
        else:
            output = 0
        return output
    
    def Calculate_strategy(self):
        pass
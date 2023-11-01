COOP = False
DEFECT = True
code_message1 = [True, True, False, True]
code_message2 = [False, False, True, False]

class MyPlayer:

    """Player plays first 4 moves to detect itself, than analyses other player"""
    def __init__(self, payoff_matrix, number_of_iterations = 0):
        self.same_count = 0
        self.iteration = 0
        self.oponent_coop_count = 0
        self.oponent_defect_count = 0
        self.best_move_switch = 0
        self.oponent_coop_count = 0

        self.best_move = COOP
        self.mirror_play = False
        self.optimal_move = COOP
        self.My_last_move = COOP
        self.Other_last_move = COOP

        self.win_matrix = []
        self.get_value = []

        for r in range(0,2):
            for c in range(0,2):
                self.values = []
                for p_id in range(0,2):
                    self.values.append(payoff_matrix[r][c][p_id])
                self.win_matrix.append(self.evaluate_win_probability(self.values))
                self.get_value.append(self.values[0])
        if(self.win_matrix[1] > self.win_matrix[2]):
            self.optimal_move = COOP
        else:
            self.optimal_move = DEFECT

        self.calculate_best_move()
        pass

    def record_last_moves(self, my_last_move, opponent_last_move):
        self.My_last_move = my_last_move
        self.Other_last_move = opponent_last_move
        pass

    def move(self):
        self.iteration += 1
        self.response = self.calculate_strategy()
        return self.response

    def calculate_best_move(self):  ##Calculates what position brings highest income of points
        in_max = 0
        for x in range(4):
            if in_max < self.get_value[x]:
                in_max = self.get_value[x]
                self.best_move_switch = x
        if (self.best_move_switch == 0 or self.best_move_switch == 1):
            self.best_move = COOP
        else:
            self.best_move = DEFECT
        pass

    def evaluate_win_probability(self, values): ##Takes the matrix and changes is to 0 = draw, 1 = gain points, -1 = gain less points than oponent
        output = 0
        if values[0] > values[1]:
            output = 1
        elif values[0] < values[1]:
            output = -1
        else:
            output = 0
        return output

    def calculate_strategy(self):   ##Calculates strategy. In round 1-4 checks if it plays against it self
        response = COOP
        if self.My_last_move == self.Other_last_move:
            self.same_count += 1
        if self.iteration < 4:
            self.default_switch = 0
            if self.optimal_move == COOP:
                self.default_switch = 1
            response = self.defaul_strategy()
        else:
            response = self.oponent_analysis()
        return response

    def coop_check(self):   ##Counts how many times other plyer plays COOP without interuption
        if(self.Other_last_move == COOP):
            self.oponent_coop_count += 1
            if(self.oponent_defect_count == self. oponent_coop_count):  ##Leaves space to find if he wants to play the switching tactick
                self.oponent_change +=1
            else:
                self.oponent_defect_count = 0
                self.oponent_change = 0
        return 0

    def defect_check(self): ##Counts how many times other plyer plays DEFECT without interuption
        if(self.Other_last_move == DEFECT):
            self.oponent_defect_count += 1
            if(self.oponent_defect_count == self. oponent_coop_count):  ##Leaves space to find if he wants to play the switching tactick
                self.oponent_change +=1
            else:
                self.oponent_coop_count = 0
                self.oponent_change = 0
        return 0

    def response_vs_oponent(self):  ##Based on calculated values determins what he plays
        if(self.oponent_change >= 2):
            response = self.echo()
        elif(self.oponent_coop_count >= 2):
            if(self.best_move == COOP):
                response = COOP
            else:
                response = self.safe_strategy()         
        elif(self.oponent_defect_count >= 2):
            if(self.best_move == DEFECT):
                response = DEFECT
            else:
                response = self.safe_strategy()
        else:
            response = self.safe_strategy()
        return response

    def oponent_analysis(self):
        response = self.optimal_move
        if (self.same_count == 4 and self.mirror_play == True):
            response = self.me_vs_me()
        else:
            self.coop_check()
            self.defect_check()
            response = self.response_vs_oponent()
        return response

    def echo(self): ##Copies Other player move
        response = self.Other_last_move
        return response
   
    def safe_strategy(self): ##Picks the row where it can gain same or more points than other player
        response = self.optimal_move
        self.mirror_play = False
        return response

    def defaul_strategy(self):  ##Based strategy where i play coded mesaage
        if self.default_switch == 0:
            response = code_message1[self.iteration-1]
        else:
            response = code_message2[self.iteration-1]
        return response

    def response_switch(self):
        if self.My_last_move == COOP:
            response = DEFECT
        else:
            response = COOP
        return response

    def me_vs_me(self):
        match self.best_move:
            case 0:
                response = COOP
                if self.My_last_move != self.Other_last_move:
                    self.mirror_play = False
                    response = self.oponent_analysis()
            case 3:
                response = DEFECT
                if self.My_last_move != self.Other_last_move:
                    self.mirror_play = False
                    response = self.oponent_analysis()
            case _:
                response = self.safe_strategy()
        return response
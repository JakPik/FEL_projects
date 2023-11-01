## False == cooperate
## True == defect
import random

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations = 0):
        self.response = False
        self.My_last_move = False
        self.Other_last_move = False
        self.code_message1 = [True, True, False, True]       ##defect = 0
        self.code_message2 = [False, False, True, False]     ##cooperate = 1

        self.default_switch = 0
        self.same_count = 0
        self.same = False
        self.self_stretegy = 1
        self.best_move = False

        self.oponent_false_count = 0
        self.oponent_true_count = 0
        self.oponent_change = 0

        self.iteration = number_of_iterations
        self.iteration = 0

        self.matrix = payoff_matrix
        self.win_probability = []   ## Writes matrix of choice win/draw/lose state
        self.strat_value = []       ## Writes matrix of win points
        self.values = []

        for x in range(0,2):
            for y in range(0,2):
                self.values = []
                for z in range(0,2):
                    self.values.append(payoff_matrix[x][y][z])
                self.win_probability.append(self.evaluate_win_probability(self.values))
                self.strat_value.append(self.values[0])
        if(self.win_probability[1] > self.win_probability[2]):
            self.best_move = False
        else:
            self.best_move =True
        

    def move(self):
        self.iteration += 1
        ##self.response = self.Calculate_strategy()
        x = random.randint(0,10)
        if(x%2 == 0):
            self.response = False
        else:
            self.response = True
        return self.response
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.My_last_move = my_last_move
        self.Other_last_move = opponent_last_move
        pass

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
        response = False
        if self.My_last_move == self.Other_last_move:
            self.same_count += 1
        if self.iteration < 4:
            self.default_switch = 0
            if self.win_probability[1] > self.win_probability[2]:
                self.default_switch = 1
            response = self.Defaul_strategy(self.iteration)
        else:
            response = self.Complex_stretegy()
        return response

    def Defaul_strategy(self, itteration):
        if self.default_switch == 0:
            response = self.code_message1[itteration-1]
        else:
            response = self.code_message2[itteration-1]
        return response

    def Complex_stretegy(self):
        if (self.same_count == 4 or self.same == True):
            self.same = True
            result = self.Me_vs_me()
        else:
            result = self.Oponent_analysis()
        return result

    def Safe_strategy(self, response):
        if self.default_switch == 0:
            response = True
        else:
            response = False
        return response

    def Response_switch(self):
        if self.My_last_move == True:
            response = False
        else:
            response = True
        return response
    
    def Me_vs_me(self):
        in_max = 0
        for x in range(4):
            if in_max < self.strat_value[x]:
                in_max = self.strat_value[x]
                self.self_stretegy = x
        match self.self_stretegy:
            case 0:
                response = False
                if self.My_last_move != self.Other_last_move:
                    self.same = False
                    response = self.Oponent_analysis()
            case 1:
                response = self.Response_switch()
                if (self.My_last_move == self.Other_last_move):
                    response = self.Oponent_analysis()
                    self.same = False
            case 2:
                response = self.Response_switch()
                if (self.My_last_move == self.Other_last_move):
                    response = self.Oponent_analysis()
                    self.same = False
            case 3:
                response = True
                if self.My_last_move != self.Other_last_move:
                    self.same = False
                    response = self.Oponent_analysis()
            case _:
                response = False
        return response
    
    def Oponent_analysis(self):
        response = False
        if(self.Other_last_move == False):
            self.oponent_false_count += 1
            if(self.oponent_true_count == self. oponent_false_count):
                self.oponent_change +=1
            else:
                self.oponent_true_count = 0
                self.oponent_change = 0

        if(self.Other_last_move == True):
            self.oponent_true_count += 1
            if(self.oponent_true_count == self. oponent_false_count):
                self.oponent_change +=1
            else:
                self.oponent_false_count = 0
                self.oponent_change = 0

        if(self.oponent_change >= 2):
            response = self.Echo()
        elif(self.oponent_false_count >= 3):
            if(self.best_move == False):
                response = False
            else:
                response = self.Safe_strategy(response)         
        elif(self.oponent_true_count >= 3):
            if(self.best_move == True):
                response = True
            else:
                response = self.Safe_strategy(response)
        else:
            response = self.Safe_strategy(response)

        return response
    
    def Echo(self):
        return self.Other_last_move



if __name__ == "__main__":
    payoff_matrix = ( ((4,4),(1,6)) , ((6,1),(2,2)) )
    p1 = MyPlayer(payoff_matrix)
    print(p1.win_probability)
    print(p1.strat_value)
    for x in range(20):
        print(p1.move())
import random

class MyPlayer:
    def __init__(self,v, strategy = 1):
        if v is None:
            self.numb = 0
        else:
            self.numb = v
        self.strat = strategy
        self.answer = 'R'

    def play(self):
        self.choice = 0
        self.choice = self.PickStrategy()
        self.answer = self.SelectAnswer()
        return self.answer
  
    def SelectAnswer(self):
        match self.choice:
            case 1:
                return 'R'
            case 2:
                return 'S'
            case 3:
                return 'P'
            case _:
                return 'R'

    def PickStrategy(self):
        self.pick = 0
        match self.strat:
            case 1:
                self.pick = self.StrategyRand()
            case 2:
                self.pick = self.StrategyDoubleRand()
            case _:
                return 0
        return self.pick

    def StrategyRand(self):
       self.name = 'rand'
       return random.randint(1,3)
    
    def StrategyDoubleRand(self):
        self.name = 'doubleRand'
        self.number = random.randint(1,6) + random.randint(1,3)
        return self.number%3 + 1
    

    def __str__(self):
        return 'hrac '+ self.name + ' from module '

if __name__ == "__main__":
    p = MyPlayer(2,2)
    tah = p.play()
    tah2 = MyPlayer.play(p)
    print(tah,tah2)
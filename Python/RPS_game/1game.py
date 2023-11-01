import player

def evaluate(m1, m2):
    if (m1,m2) in [('R','S'), ('P','R'), ('S','P')]:
        return 1,0
    else:
        return 0,1
    
class Game:
    def __init__(self, p1, p2, minwins):
        self.p1 = p1
        self.p2 = p2
        self.minwins = minwins

    def duel(self):
        draw = True
        while draw:
            move1 = self.p1.play()
            move2 = self.p2.play()
            draw = move1 == move2
        return evaluate(move1, move2)

    def run(self):
        total_score = [0,0]
        while max(total_score) < self.minwins:
            score = self.duel()
            total_score[0] = total_score[0] + score[0]
            total_score[1] = total_score[1] + score[1]
        if total_score[0] > total_score[1]:
            return 'p1'
        else:
            return 'p2'

if __name__ == "__main__":
    # create players
    # play a game
    # show the winner
    p1_win = 0
    p2_win = 0
    rounds = 1000
    repeat = 10
    for y in range (repeat):
        p1_Count = 0
        p2_Count = 0
        print('Kolo: ', y + 1)
        for x in range (rounds):
            p1 = player.MyPlayer(1)
            p2 = player.MyPlayer(2)
            g = Game(p1, p2, 3)
            winner = g.run()
            if winner == 'p1':
                p1_Count += 1
            else:
                p2_Count += 1
        print('P1 win rate', p1_Count/rounds)
        print('P2 win rate', p2_Count/rounds)
        if p1_Count>p2_Count:
            p1_win += 1
        else:
            p2_win += 1
    print('p1 wins: ', p1_win)
    print('p2 wins: ', p2_win)
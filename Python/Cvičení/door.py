import random

doors = [1, 2, 3]
strategy = "switch"

def play(strategy):
    car = random.choice(doors)
    selected = random.choice(doors)
    opened = random.choice([d for d in doors if d != car and d != selected])
    if strategy == "switch":
        selected = next(d for d in doors if d != opened and d != selected)
    return selected == car

n = 10000
n_wins = 0
for _ in range(n):
    n_wins += play(strategy)
print(n_wins/n)
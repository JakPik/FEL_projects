payoff_matrix = ( ((4,4),(1,6)) , ((6,1),(2,2)) )
print(type(payoff_matrix))
cc = (payoff_matrix[0][0][0], payoff_matrix[0][0][1])
cd = (payoff_matrix[0][1][0], payoff_matrix[0][1][1])
dc = (payoff_matrix[1][0][0], payoff_matrix[1][0][1])
dd = (payoff_matrix[1][1][0], payoff_matrix[1][1][1])

print(cc, cd)
print(dc, dd)
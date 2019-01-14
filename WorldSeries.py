import numpy as np
import math
def backward(num_games,odds,one,two):
    rows = num_games*3 - 1
    cols = num_games
    temp = []




    computation_matrix = np.array([[1, 1/odds],[1, -1]])
    inv_comp_matrix = np.linalg.inv(computation_matrix)
    for i in range(0,num_games):
        temp.append(one)
    for i in range(0,num_games):
        temp.append(two)


    for _ in range(0,num_games):
        while i < len(temp)-1:
           bet_info = np.matmul(inv_comp_matrix,np.array([[temp[i]], [temp[i + 1]]]))
           temp[i] = float(bet_info[0])
           i += 1
        i =  0
        temp[-1] = -100
        temp.insert(0,100) #add an extra 100 to the left


    return temp[math.floor(len(temp)/2)]



if __name__== "__main__":
    num_games = 7
    odds = 3/2
    odds_otherway = 2/3
    one = 100
    two = -100
    expected_payoff = round(backward(num_games,odds,one,two),2)
    print("Expected payoff is when betting for the first team: {}".format(expected_payoff))
    offset_bet_one =  expected_payoff - one
    offset_bet_two = expected_payoff - two

    expected_payoff_2 = round(backward(num_games, odds, offset_bet_one, offset_bet_two), 1)
    print("Expected payoff is when betting for the second team as an offset: {}".format(expected_payoff_2))

    # print("Expected payoff is when betting for the second team: {}".format(round(backward(num_games, odds_otherway), 2)))
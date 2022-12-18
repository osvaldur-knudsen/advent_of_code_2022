import pandas as pd
import numpy as np

def get_translated_list(moves: list) -> list:
    rps_dict = {'X':'rock', 'Y':'paper', 'Z':'scissors',
                'A':'rock', 'B':'paper', 'C':'scissors'}
    
    opp_move = rps_dict[moves[0]]
    my_move = rps_dict[moves[1]]

    return [opp_move, my_move]

def get_result(moves: list) -> tuple :
    translated_list = get_translated_list(moves) # translate move into rock,paper, scissors
    opp_move = translated_list[0]
    my_move = translated_list[1]

    if opp_move == my_move:
        return (1, translated_list[1])
    elif opp_move == 'rock' and my_move == 'paper':
        return (2, translated_list[1])
    elif opp_move == 'paper' and my_move == 'scissors':
        return (2, translated_list[1])
    elif opp_move == 'scissors' and my_move == 'rock':
        return (2, translated_list[1])
    else:
        return (0, translated_list[1])
        
def get_points(choices: str) -> int:
    '''
    Returns the number of points received in one round of
    "rock, paper, scissors".

    Parameters
    choices: str
    A string containing letter that represent what choices
    both players made.
    '''
    shape_points = {'rock':1, 'paper':2, 'scissors':3}
    result_points = {0:0, 1:3, 2:6}
    choices_list = choices.split()

    # call function to check what the result was
    result, my_shape = get_result(choices_list) 
    return result_points[result] + shape_points[my_shape]

def get_total_points(column: pd.Series) -> int:
    '''
    Returns the total number of points for each round of play.

    Parameters
    column: pandas series
    A series of strings containing the inputs for each round of play.
    '''
    sum = 0

    for row in column:
        result = get_points(row)
        sum = sum + result

    return sum

def main():
    data = 'day_02_input.txt'
    df = pd.read_csv(data, header = None, skip_blank_lines= False)
    
    # test
    df_test = pd.DataFrame({0:['A Y', 'B X', 'C Z']})
    total_points_test = get_total_points(df_test.iloc[:,0])
    assert total_points_test == 15

    total_points = get_total_points(df.iloc[:,0])
    print(f'Your total points are: {total_points}')

if __name__ == '__main__':
    main()

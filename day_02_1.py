import pandas as pd
import numpy as np

def get_translated_list(moves: list) -> list:
    # translate list
    pass

def get_result(moves: list) -> int :
    # translate move into rock,paper, scissors
    opp_move = list[0]
    my_move = list[1]

    # compare moves and return winner

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
    print(choices_list)

    # call function to check what the result was 

    # if you won calculate points based on shape

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
        # sum = sum + result

    return sum

def main():
    # data = 'day_02_input.txt'
    # df = pd.read_csv(data, header = None, skip_blank_lines= False)
    df_test = pd.DataFrame({0:['A Y', 'B X', 'C Y']})
    print(df_test)
    get_total_points(df_test.iloc[:,0])


if __name__ == '__main__':
    main()

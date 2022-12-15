import pandas as pd
import numpy as np


def get_max_cals(col: pd.Series)-> float:
    sum_num = 0
    max_sum = 0
    sum_list = []

    for x in col:
        if pd.isna(x) == False: # check if row has number
            sum_num = sum_num + x       # then add number to running total
        elif pd.isna(x) == True:    # check if row is empty
            if len(sum_list) < 3:       # if empty then check if it's the highest sum_num so far
                sum_list.append(sum_num)
            elif sum_num > min(sum_list):
                sum_list.append(sum_num)
                sum_list.remove(min(sum_list))
            sum_num = 0
    
    if sum_num > min(sum_list):       # check if last group should be included in list
        sum_list.append(sum_num)
        sum_list.remove(min(sum_list))

    print(sum_list)
    assert len(sum_list) < 4
    return sum(sum_list)
    
def main():
    data = 'day_01_input.txt'
    df = pd.read_csv(data, header = None, skip_blank_lines= False)
    df_test = pd.DataFrame({0:[1, 4, np.nan, 4, 5, np.nan, 2, 3, np.nan, 8, 9]})
    print(get_max_cals(df_test.iloc[:,0]))
    max_cals = get_max_cals(df.iloc[:,0])
        
    print(f'This is the number of max_cals: {max_cals}')

if __name__ == '__main__':
    main()



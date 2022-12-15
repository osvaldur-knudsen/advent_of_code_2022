import pandas as pd
import numpy as np

def get_max_cals(col: pd.Series)-> float:
    sum = 0
    max_sum = 0

    for x in col:
        if pd.isna(x) == False: # check if row has number
            sum = sum + x       # then add number to running total
        elif pd.isna(x) == True:    # check if row is empty
            if sum > max_sum:       # if empty then check if it's the highest sum so far
                max_sum = sum
            sum = 0
    
    if sum > max_sum:           # the final sum need to be checked to
        max_sum = sum

    return max_sum
    
def main():
    data = 'day_01_input.txt'
    df = pd.read_csv(data, header = None, skip_blank_lines= False)
    df_test = pd.DataFrame({0:[1, 4, np.nan, 4, 5]})
    print(get_max_cals(df_test.iloc[:,0]))
    max_cals = get_max_cals(df.iloc[:,0])
        
    print(f'This is the number of max_cals: {max_cals}')

if __name__ == '__main__':
    main()



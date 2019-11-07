Nicolas Cardoz python module

Question 1

import pandas as pd

def create_csv():
    url = "pronto.csv"
    df = pd.read_csv(url)
    return(df)
    
df = create_csv()
df


Question 2
def test_create_dataframe(df, column_list):
    list_of_actual_columns = list(df.columns.values)
    
    #C1
    for each_column in column_list:
        if each_column not in list_of_actual_columns:
            return False

    #C2
    type_row0_column_starttime = type(df.iloc[0]['starttime'])
    for index, row in df.iterrows():
        print(index)
        print(row['starttime'])
    
    type_variable = type(row['starttime'])
    print(type_variable)
    
    if type_row0_column_starttime == type_variable:
        print("YAY")
    else:
        print("return False")
    
    #C3
    number_of_rows = df.shape[0]
    print(number_of_rows)
    if number_of_rows < 10:
        return False
        
    return True

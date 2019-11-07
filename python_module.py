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
    if df is < 10: 
        return False 
    
    
#     df = df[[range(11)],['starttime', 'stoptime']]
#     df['trip_duration'] = df['tripduration'] * 2
#     if column_names == column_names
#     return df

test_create_dataframe(df, ['starttime', 'stoptime'])
    
#     if db_columns == list[column]
#     if column_values == same_type
#     if data_frame_size == same_rows
    
#     return True
    
    if rows < 10:
        return False 
    if .....
    if ....
    return True
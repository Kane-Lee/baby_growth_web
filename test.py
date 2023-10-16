import pandas

weight_man_df = pandas.read_csv("weight_man.csv")

def find_column_number(df, row_index, target_value):
    if row_index < 0 or row_index >= len(df.index):
        return -1  # Row index out of range

    row = df.iloc[row_index]
    print(row)
    if target_value >= row.iloc[-1]:
        return df.columns[-1]
    if target_value < row.iloc[1]:
        return df.columns[1]

    for col_num in range(len(row) - 1):
        if row[col_num] <= target_value < row[col_num + 1]:
            return df.columns[col_num]
    
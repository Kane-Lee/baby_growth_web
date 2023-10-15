import pandas

weight_man_df = pandas.read_csv("weight_man.csv")

def find_column_number2(df, row_number, second_number):
    try:
        # Get the specified row as a Series
        row = df.iloc[row_number]

        # Iterate through the columns to find where the second_number is between two values
        for col_num, (col_name, value) in enumerate(row.iteritems()):
            if col_num < len(row) - 1:
                if row[col_num] <= second_number < row[col_num + 1]:
                    return col_num

        # If the second_number is greater than the last value, return the index of the last column
        if second_number >= row.iloc[-1]:
            return len(row) - 1

        # If the second_number is smaller than the first value, return the index of the first column
        if second_number < row.iloc[0]:
            return 0

        # If the second_number doesn't fall between two values, return None
        return None
    except IndexError:
        return None
    
def find_column_number1(df, row_index, target_value):

    row = df.iloc[row_index]

    if (df.iloc[row_index] == target_value).any():
        column_number = row[row == target_value].index.tolist()
    else :
        for col_num, (col_name, value) in enumerate(row.iteritems()):
            if col_num < len(row) - 1:
                if row[col_num] <= second_number < row[col_num + 1]:
                    return col_num
        if target_value >= row.iloc[-1]:
            return 99
        if target_value < row.iloc[0]:
            return 1


    if column_number:
        return int(column_number[0])  # Return the first occurrence
    else:
        return -1  # Value not found in the row
    
print(find_column_number1(weight_man_df, 2, 4.6))
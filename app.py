from flask import Flask, render_template, request
from datetime import datetime
import pandas



weight_man_df = pandas.read_csv("weight_man.csv")
weight_woman_df = pandas.read_csv("weight_woman.csv")
height_man_df = pandas.read_csv("height_man.csv")
height_woman_df = pandas.read_csv("height_woman.csv")


def calculate_month_age(birthday):
    birthdate = datetime.strptime(birthday,'%Y/%m/%d')
    current_date = datetime.now()
    age_in_month = (current_date.year - birthdate.year) * 12 + (current_date.month - birthdate.month)
    return age_in_month

def translate_gender(gender):
    if gender == "boy":
        gender_in_korean = "남자"
    else :
        gender_in_korean = "여자"
    return gender_in_korean


def find_column_number(df, row_index, target_value):
    if row_index < 0 or row_index >= len(df.index):
        return -1  # Row index out of range

    row = df.iloc[row_index]

    if target_value >= row.iloc[-1]:
        return df.columns[-1] # Return 99 if target_value is greater than last value
    elif target_value < row.iloc[1]:
        return df.columns[1] # Return 1 if target_value is smaller than first value
    else:
        for col_num in range(len(row) - 1):
            if row[col_num] <= target_value < row[col_num + 1]:
                return df.columns[col_num]







def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return render_template("home.html")
    
    @app.route('/result', methods=['POST'])
    def result():
        gender = request.form.get('gender')
        gender_in_korean = translate_gender(gender)
        
        birthday = request.form.get('birthdate')
        month_age = calculate_month_age(birthday)
        
        baby_weight = float(request.form.get('weight'))
        baby_height = float(request.form.get('height'))

        if gender == 'boy':
            weight_percentile = find_column_number(weight_man_df, month_age, baby_weight)
            height_percentile = find_column_number(height_man_df, month_age, baby_height)
        else:
            weight_percentile = find_column_number(weight_woman_df, month_age, baby_weight)
            height_percentile = find_column_number(weight_woman_df, month_age, baby_height)

        return render_template("result.html",
                               age=month_age,
                               gender=gender_in_korean,
                               baby_weight=baby_weight,
                               baby_height=baby_height,
                               weight_percentile=weight_percentile,
                               height_percentile=height_percentile
                               )

    return app

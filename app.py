from flask import Flask, render_template, request
from datetime import datetime
import pandas

weight_man_df = pandas.read_csv("weight_man.csv")

def calculate_month_age(birthday):
    birthdate = datetime.strptime(birthday,'%Y-%m-%d')
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
    column_number = row[row == target_value].index.tolist()
    
    if column_number:
        return int(column_number[0])  # Return the first occurrence
    else:
        return -1  # Value not found in the row







def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return render_template("home.html")
    
    @app.route('/result', methods=['POST'])
    def result():
        gender = request.form.get('gender')
        gender_in_korean = translate_gender(gender)
        
        birthday = request.form.get('birthday')
        month_age = calculate_month_age(birthday)
        
        baby_weight = float(request.form.get('weight'))

        weight_percentile = 100-find_column_number(weight_man_df, month_age, baby_weight)
        print(weight_percentile)

        return render_template("result.html",
                               age=month_age,
                               gender=gender_in_korean,
                               baby_weight=baby_weight,
                               weight_percentile=weight_percentile
                               )

    return app

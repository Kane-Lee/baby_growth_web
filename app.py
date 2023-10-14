from flask import Flask, render_template, request
from datetime import datetime

def calculate_month_age(birthday):
    birthdate = datetime.strptime(birthday,'%Y-%m-%d')
    current_date = datetime.now()
    age_in_month = (current_date.year - birthdate.year) * 12 + (current_date.month - birthdate.month)
    return age_in_month

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return render_template("home.html")
    
    @app.route('/result', methods=['POST'])
    def result():
        gender = request.form.get('gender')
        if gender == "boy":
            baby_gender = "남자"
        else :
            baby_gender = "여자"
        birthday = request.form.get('birthday')
        month_age = calculate_month_age(birthday)
        weight = request.form.get('weight')
        return render_template("result.html", age=month_age, gender=baby_gender)

    return app

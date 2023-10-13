from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/result', methods=['POST'])
def result():
    gender = request.form.get('gender')
    birthday = request.form.get('birthday')
    weight = request.form.get('weight')
    return f'gender : {gender} / birthday : {birthday} / weight : {weight}kg'
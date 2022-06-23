from flask import jsonify, render_template
from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("chartjs.html")

@app.route("/data")
def data():
    return jsonify(income=[100, 200, 400, 200, 130], expense=[10, 300, 70, 90, 20], period=[2018, 2019, 2020, 2021, 2022])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")

@app.route("/exercise")
def exercise():
    return render_template("exercise.html")

@app.route("/calculator", methods=["POST", "GET"])
def calculator():
    if request.method == "POST":
        op = request.form['op']
        print(op)
        dic = request.form.to_dict()
        
    return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)

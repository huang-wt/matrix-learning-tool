from flask import Flask, render_template, request
from exercise_generator import ExercisesGenerator
from matrix_operation import Matrix
from data_processor import DataProcessor

app = Flask(__name__)
data_processor = DataProcessor()
exercises_generator = ExercisesGenerator()
exercises_generator.set_exercises(True)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")

@app.route("/exercise", methods=["POST", "GET"])
def exercise():
    exercises = exercises_generator.exercises
    print(exercises)
    is_checked = False
    if request.method == "POST":
        if "import" in request.form.to_dict():
            exercises_generator.set_exercises(False)
            exercises = exercises_generator.exercises
        elif "new" in request.form.to_dict():
            exercises_generator.set_exercises(True)
            exercises = exercises_generator.exercises
        
        user_answers = data_processor.process_user_answers(request.form.to_dict())
        print(user_answers)
        if len(user_answers) != 0:
            is_checked = True
            check = exercises_generator.check_answers(user_answers)
            return render_template("exercise.html", exercises=exercises, is_checked=is_checked, check=check, user_answers=user_answers)

    return render_template("exercise.html", exercises=exercises, is_checked=is_checked)

@app.route("/calculator", methods=["POST", "GET"])
def calculator():
    if request.method == "POST":
        op = request.form['op']
        AB = request.form.to_dict()

        arrA, arrB = data_processor.process_AB_elems(AB)
        is_binary = data_processor.is_binary(op)
        if is_binary:
            matrix_A = Matrix(arrA, op)
            matrix_B = Matrix(arrB, op)
            res = matrix_A.get_bi_result(matrix_B)
            return render_template("calculator.html", is_binary=is_binary, A=arrA, op=op, B=arrB, res=res)
        else:
            is_unary = True
            is_on_A = data_processor.is_on_matrix_A(op)
            if is_on_A:
                matrix_A = Matrix(arrA, op)
                res = matrix_A.get_result()
                return render_template("calculator.html", is_unary=is_unary, op=op[1:], is_on_A=is_on_A, A=arrA, res=res)
            else:
                matrix_B = Matrix(arrB, op)
                res = matrix_B.get_result()
                return render_template("calculator.html", is_unary=is_unary, op=op[1:], is_on_A=is_on_A, B=arrB, res=res)
            
    else:
        return render_template("calculator.html")



if __name__ == "__main__":
    app.run(debug=True)

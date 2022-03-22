from flask import Flask, render_template, request
from exercise_generator import ExercisesGenerator
from matrix_operation import Matrix
from data_processor import DataProcessor

app = Flask(__name__)
data_processor = DataProcessor()
exercises_generator = ExercisesGenerator()
# exercises_generator.set_exercises(True, 3)
MARKER = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")

@app.route("/choose")
def choose():
        return render_template("choose.html")
    
@app.route("/chooseEX")
def chooseEX():
    global MARKER
    MARKER = True
    return render_template("chooseEX.html")

@app.route("/exercise", methods=["POST", "GET"])
def exercise():
    global MARKER
    if MARKER:
        exercises_generator.set_exercises(True, 3)
        MARKER = False
    exercises = exercises_generator.exercises
    print(exercises)
    is_checked = False
    if request.method == "POST":
        if "import" in request.form.to_dict():
            exercises_generator.set_exercises(False, 3)
            exercises = exercises_generator.exercises
        elif "new" in request.form.to_dict():
            exercises_generator.set_exercises(True, 3)
            exercises = exercises_generator.exercises
        
        user_answers = data_processor.process_user_answers(request.form.to_dict())
        print(user_answers)
        if len(user_answers) != 0:
            is_checked = True
            check = exercises_generator.check_answers(user_answers)
            return render_template("exercise.html", exercises=exercises, is_checked=is_checked, check=check, user_answers=user_answers)

    return render_template("exercise.html", exercises=exercises, is_checked=is_checked)

@app.route("/exercise2x2", methods=["POST", "GET"])
def exercise2x2():
    global MARKER
    if MARKER:
        exercises_generator.set_exercises(True, 2)
        MARKER = False
    exercises = exercises_generator.exercises
    print(exercises)
    is_checked = False
    if request.method == "POST":
        if "import" in request.form.to_dict():
            exercises_generator.set_exercises(False, 2) ##
            exercises = exercises_generator.exercises
        elif "new" in request.form.to_dict():
            exercises_generator.set_exercises(True, 2) ##
            exercises = exercises_generator.exercises
        
        user_answers = data_processor.process_user_answers(request.form.to_dict())
        print(user_answers)
        if len(user_answers) != 0:
            is_checked = True
            check = exercises_generator.check_answers(user_answers)
            return render_template("exercise2x2.html", exercises=exercises, is_checked=is_checked, check=check, user_answers=user_answers)

    return render_template("exercise2x2.html", exercises=exercises, is_checked=is_checked)

@app.route("/calculator", methods=["POST", "GET"])
def calculator():
    if request.method == "POST":
        op = request.form['op']
        AB = request.form.to_dict()

        arrA, arrB = data_processor.process_AB_elems(AB)
        is_binary = data_processor.is_binary(op)
        if is_binary:
            matrix_A = Matrix(arrA, op, 3)
            matrix_B = Matrix(arrB, op, 3)
            res = matrix_A.get_bi_result(matrix_B)
            return render_template("calculator.html", is_binary=is_binary, A=arrA, op=op, B=arrB, res=res)
        else:
            is_unary = True
            is_on_A = data_processor.is_on_matrix_A(op)
            if is_on_A:
                matrix_A = Matrix(arrA, op, 3)
                res = matrix_A.get_result()
                return render_template("calculator.html", is_unary=is_unary, op=op[1:], is_on_A=is_on_A, A=arrA, res=res)
            else:
                matrix_B = Matrix(arrB, op, 3)
                res = matrix_B.get_result()
                return render_template("calculator.html", is_unary=is_unary, op=op[1:], is_on_A=is_on_A, B=arrB, res=res)
            
    else:
        return render_template("calculator.html")
    
@app.route("/calculator2x2", methods=["POST", "GET"])
def calculator2x2():
    if request.method == "POST":
        op = request.form['op']
        AB = request.form.to_dict()

        arrA, arrB = data_processor.process_AB_elems(AB)
        is_binary = data_processor.is_binary(op)
        if is_binary:
            matrix_A = Matrix(arrA, op, 2)
            matrix_B = Matrix(arrB, op, 2)
            res = matrix_A.get_bi_result(matrix_B)
            return render_template("calculator2x2.html", is_binary=is_binary, A=arrA, op=op, B=arrB, res=res)
        else:
            is_unary = True
            is_on_A = data_processor.is_on_matrix_A(op)
            if is_on_A:
                matrix_A = Matrix(arrA, op, 2)
                res = matrix_A.get_result()
                return render_template("calculator2x2.html", is_unary=is_unary, op=op[1:], is_on_A=is_on_A, A=arrA, res=res)
            else:
                matrix_B = Matrix(arrB, op, 2)
                res = matrix_B.get_result()
                return render_template("calculator2x2.html", is_unary=is_unary, op=op[1:], is_on_A=is_on_A, B=arrB, res=res)
            
    else:
        return render_template("calculator2x2.html")



if __name__ == "__main__":
    app.run(debug=True)

import random
from matrix_operation import Matrix

class ExercisesGenerator:
    EXERCISE_TYPES = {0:"add", 1:"sub", 2:"mult", 3:" determinant", 4:" inverse", 5:" eigenvalue(s)", 6:" eigenvector(s)"}
    EXERCISES_NUMBER = 5

    def __init__(self) -> None:
        self.exercises = []

    def set_exercises(self, is_auto):
        self.exercises = []
        if is_auto:
            self.set_exercises_type()
            self.set_exercises_data()
        else:
            self.import_exercises()

    def set_exercises_type(self):
        for i in range(self.EXERCISES_NUMBER):
            num = random.randint(0, 6)
            self.exercises.append([])
            self.exercises[i].append(num <= 2)
            self.exercises[i].append(self.EXERCISE_TYPES[num])

    def set_exercises_data(self):
        
        for i in range(self.EXERCISES_NUMBER):
            if self.exercises[i][0]:
                A = [random.randint(-20, 20) for _ in range(9)]
                matrix_A = Matrix(A, self.exercises[i][1])
                B = [random.randint(-20, 20) for _ in range(9)]
                matrix_B = Matrix(B, self.exercises[i][1])
                res = str(matrix_A.get_bi_result(matrix_B))
                self.exercises[i].append(A)
                self.exercises[i].append(B)
                self.exercises[i].append(res)
            else:
                A = [random.randint(-20, 20) for _ in range(9)]
                matrix_A = Matrix(A, self.exercises[i][1])
                res = str(matrix_A.get_result())
                self.exercises[i].append(A)
                self.exercises[i].append(res)

    #import exercises from data/input(.txt)
    #format e.g. is_binary|True
    #            exer_type|add
    #               A_data|1,1,1,1,1,1,1,1,1
    #               B_data|1,1,1,1,1,1,1,1,1
    def import_exercises(self):
        with open("data/input", "rt") as file: 
            lines = file.readlines()
            lines  = [l.strip('\n') for l in lines]
            j = 0
            for i in range(self.EXERCISES_NUMBER):
                self.exercises.append([])
                is_binray = lines[j] == "True"
                j += 1
                type = lines[j]
                j += 1
                self.exercises[i].append(is_binray)
                self.exercises[i].append(type)
                if is_binray:
                    A = list(map(int, lines[j].split(',')))
                    matrix_A = Matrix(A, self.exercises[i][1])
                    j += 1
                    B = list(map(int, lines[j].split(',')))
                    matrix_B = Matrix(B, self.exercises[i][1])
                    j += 1
                    res = str(matrix_A.get_bi_result(matrix_B))
                    self.exercises[i].append(A)
                    self.exercises[i].append(B)
                    self.exercises[i].append(res)
                else:
                    A = list(map(int, lines[j].split(',')))
                    matrix_A = Matrix(A, self.exercises[i][1])
                    j += 1
                    res = str(matrix_A.get_result())
                    self.exercises[i].append(A)
                    self.exercises[i].append(res)

    def check_answers(self, user_answers):
        check = []
        for i in range(self.EXERCISES_NUMBER):
            check.append(user_answers[i] == self.exercises[i][-1])
        return check



# Imformal Test
# eg = ExercisesGenerator()
# eg.set_exercises(True)
# print(eg.exercises)
# print(eg.check_answers(["", "", "", "", '[[10, 20, 0], [5, 25, -2], [-21, 4, 4]]']))

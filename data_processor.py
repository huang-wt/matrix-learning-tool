class DataProcessor:
    def __init__(self) -> None:
        pass

    def process_AB_elems(self, AB):
        A = []
        B = []
        for k, v in AB.items():
            if k[0] == "A":
                A.append(v)
            elif k[0] == "B":
                B.append(v)
        return A, B

    def is_binary(self, op):
        if op in "addsubmult":
            return True
        else:
            return False

    def is_on_matrix_A(self, op):
        if op[0] == "A":
            return True
        else:  # elif op[0] == "B"
            return False

    def process_user_answers(self, ua):
        user_answers = []
        for k, v in ua.items():
            if k != "submit" and k != "import" and k != "new":
                user_answers.append(v)

        return user_answers
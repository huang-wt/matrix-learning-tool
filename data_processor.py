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
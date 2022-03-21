import numpy as np

MATRIXSIZE = 3

class Matrix:

    def __init__(self, M, op) -> None:
        self.op = op
        self.arrM = np.empty(MATRIXSIZE * MATRIXSIZE, dtype=int)
        
        for i in range(MATRIXSIZE * MATRIXSIZE):
            self.arrM[i] = M[i]
        
        self.arrM = self.arrM.reshape(MATRIXSIZE, MATRIXSIZE)

    def get_bi_result(self, N):
        if self.op == "add":
            return self + N
        elif self.op == "sub":
            return self - N
        elif self.op == "mult":
            return self * N
    
    def get_result(self):
        if self.op[1:] == "determinant":
            return self.det()
        elif self.op[1:] == "inverse":
            return self.inv()
        elif self.op[1:] == "eigenvalue(s)":
            return self.eigval()
        elif self.op[1:] == "eigenvector(s)":
            return self.eigvect()

    def __add__(self, N):
        return (self.arrM + N.arrM).tolist()

    def __sub__(self, N):
        return (self.arrM - N.arrM).tolist()

    def __mul__(self, N):
        return self.arrM.dot(N.arrM).tolist()

    def det(self):
        return round(np.linalg.det(self.arrM).real, 2)

    def inv(self):
        try:
            return np.linalg.inv(self.arrM).tolist()
        except:
            return "This matrix is a singular matrix"
    
    def eig(self):
        return np.linalg.eig(self.arrM)
    
    def eigval(self):
        res = self.eig()[0].tolist()
        for i in range(len(res)):
            res[i] = round(res[i].real, 2)
        return res
    
    def eigvect(self):
        res = self.eig()[1].tolist()
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = round(res[i][j].real, 2)
        return res



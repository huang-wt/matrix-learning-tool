import numpy as np

print("A matrix must be a squre form")

row_number = input("Enter your number of the row and column")
A = int(row_number)

arrA = np.empty(A * A, dtype=int)

for i in range(A * A):
    arrA[i] = input("Enter your elemet from a00 to ann")

flag = True
while flag:
    flag1 = input("if you want arithmetic operation with another matrix, enter yes. Otherwise, Just press enter")

    if flag1 == 'yes':
        arrB = np.empty(A * A, dtype=int)

        for i in range(A * A):
            arrB[i] = input("Enter your elemet from a00 to ann")

        arr2 = arrB.reshape(A, A)
        flag = False
    elif flag1 == '':
        flag = False
    else:
        print("you entered wrong characters. please enter yes or nothing")

arr1 = arrA.reshape(A, A)

if flag1:
    print(arr1)

    print(arr1 + arr2)
    print(arr1 - arr2)

    print(arr1.dot(arr2))

determinant = np.linalg.det(arr1)
print(determinant)
print()
try:
    inverse = np.linalg.inv(arr1)
    print(inverse)
except:
    print("This matrix is a singular matrix")
print()
eigenvalue, eigenvector = np.linalg.eig(arr1)

print(eigenvalue)
print()
print(eigenvector)


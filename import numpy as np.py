import numpy as np
import time

start_time = time.time()
# Клас для операцій з бінарними відношеннями
class BinaryRelationOperationsRenamed:
    def __init__(self, relation1, relation2):
        self.relation1 = relation1
        self.relation2 = relation2

    def print_relation(self, relation):
        for row in relation:
            print(' '.join(map(str, row)))

    def perform_operation(self, operation, operation_name):
        result = operation(self.relation1, self.relation2)
        print(f"\n{operation_name}:")
        self.print_relation(result)

    def intersection(self):
        self.perform_operation(self.binary_intersection, "Intersection")

    def union(self):
        self.perform_operation(self.binary_union, "Union")

    def difference(self):
        self.perform_operation(self.binary_difference, "Difference (P - Q)")

    def composition(self):
        self.perform_operation(self.binary_composition, "Composition (P o Q)")

    def inverse(self, relation):
        result = [[relation[j][i] for j in range(len(relation))] for i in range(len(relation[0]))]
        print("\nInverse of P:")
        self.print_relation(result)

    def symmetric_difference(self):
        self.perform_operation(self.binary_symmetric_difference, "Symmetric Difference")

    @staticmethod
    def binary_intersection(relation1, relation2):
        return [[1 if relation1[i][j] and relation2[i][j] else 0 for j in range(len(relation1[0]))] for i in range(len(relation1))]

    @staticmethod
    def binary_union(relation1, relation2):
        return [[1 if relation1[i][j] or relation2[i][j] else 0 for j in range(len(relation1[0]))] for i in range(len(relation1))]

    @staticmethod
    def binary_difference(relation1, relation2):
        return [[1 if relation1[i][j] and not relation2[i][j] else 0 for j in range(len(relation1[0]))] for i in range(len(relation1))]

    @staticmethod
    def binary_composition(relation1, relation2):
        composition_result = [[0] * len(relation2[0]) for _ in range(len(relation1))]
        for i in range(len(relation1)):
            for j in range(len(relation2[0])):
                for k in range(len(relation1[0])):
                    composition_result[i][j] |= relation1[i][k] and relation2[k][j]
        return composition_result

    @staticmethod
    def binary_symmetric_difference(relation1, relation2):
        return [[1 if (relation1[i][j] and not relation2[i][j]) or (not relation1[i][j] and relation2[i][j]) else 0 for j in range(len(relation1[0]))] for i in range(len(relation1))]

# Занесення даних
A = {1, 2, 3, 4, 5}

P = [[1,0,0,0,0],
     [1,1,0,1,1],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,1,1,0,1]]

Q = [[0,0,0,0,0],
     [0,1,0,1,0],
     [0,0,0,0,0],
     [1,1,0,0,0],
     [0,0,0,0,0]]

R = [[0,1,1,0,0],
     [0,0,1,0,1],
     [0,1,0,0,0],
     [1,1,1,1,1],
     [1,0,1,1,0]]

# Виведення кожної матриці
def print_matrix(matrix, matrix_name):
    print(f"\nMatrix {matrix_name}:")
    for row in matrix:
        print(' '.join(map(str, row)))

print_matrix(P, "P")
print_matrix(Q, "Q")
print_matrix(R, "R")

# Функція для перетворення відношення в бінарну матрицю
def relation_to_binary_matrix(relation):
    return [[1 if elem != 0 else 0 for elem in row] for row in relation]

# Перетворення відношень у бінарні матриці
B_P = relation_to_binary_matrix(P)
B_Q = relation_to_binary_matrix(Q)
B_R = relation_to_binary_matrix(R)

# Функція для знаходження верхнього перетину множини з рядком матриці
def find_upper_intersection(matrix_row, set_A):
    return [elem for elem in matrix_row if elem in set_A]

# Знаходження верхнього перетину для кожної матриці
upper_intersection_P = [find_upper_intersection(row, A) for row in P]
upper_intersection_Q = [find_upper_intersection(row, A) for row in Q]
upper_intersection_R = [find_upper_intersection(row, A) for row in R]

print("\nUpper intersection of P")
for row in upper_intersection_P:
    print(row)

print("\nUpper intersection of Q")
for row in upper_intersection_Q:
    print(row)

print("\nUpper intersection of R")
for row in upper_intersection_R:
    print(row)

# Конструктори створення елементарних бінарних відношень

def create_empty_relation():
    return {}

# Створення пустого бінарного відношення
empty_relation = create_empty_relation()
print("\nEmpty binary relation:", empty_relation)

def create_full_relation(matrix):
    relation = {}
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                relation[(i, j)] = True
    return relation

# Приклад використання для матриці P
matrix_P = [[1,0,0,0,0],
            [1,1,0,1,1],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,1,1,0,1]]
full_relation_P = create_full_relation(matrix_P)
print("\nFull binary relation:",full_relation_P)

def create_diagonal_relation(matrix):
    relation = {}
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 1:
            relation[(i, i)] = True
    return relation

# Приклад використання для матриці Q
matrix_Q = [[0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
            [1,1,0,0,0],
            [0,0,0,0,0]]
diagonal_relation_Q = create_diagonal_relation(matrix_Q)
print("\nDiagonal binary relation:",diagonal_relation_Q)

def create_antidiagonal_relation(matrix):
    relation = {}
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != 0:
                relation[(i, j)] = True
    return relation

# Приклад використання для матриці R
matrix_R = [[0,1,1,0,0],
            [0,0,1,0,1],
            [0,1,0,0,0],
            [1,1,1,1,1],
            [1,0,1,1,0]]
antidiagonal_relation_R = create_antidiagonal_relation(matrix_R)
print(antidiagonal_relation_R)

# Виведення результатів дій над відношеннями
relation_operations = BinaryRelationOperationsRenamed(P, Q)
relation_operations.intersection()
relation_operations.union()
relation_operations.difference()
relation_operations.composition()
relation_operations.inverse(P)
relation_operations.symmetric_difference()

# Функція-член перевірки умови включення одного відношення в інше

def matrix_to_relation(matrix):
    relation = {}
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                relation[(i, j)] = True
    return relation

def is_relation_included(R, S):
    return all(pair in S.items() for pair in R.items())

# Перетворення матриць у відношення
relation_P = matrix_to_relation(P)
relation_Q = matrix_to_relation(Q)
relation_R = matrix_to_relation(R)

# Перевірка умови включення
print("\nIs P included in Q:", is_relation_included(relation_P, relation_Q))
print("Is Q included in P:", is_relation_included(relation_Q, relation_P))
print("Is P included in R:", is_relation_included(relation_P, relation_R))

# Функція для обчислення двоїстого відношення
def dual_relation(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dual_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            dual_matrix[i][j] = 1 - matrix[i][j]
    return dual_matrix

# Знаходження двоїстого відношення R^dual
R_dual = dual_relation(R)

# Обчислення матриці K
K = [[P[i][j] * Q[i][j] // R_dual[i][j] if R_dual[i][j] != 0 else 0 for j in range(len(P[0]))] for i in range(len(P))]

# Виведення результатів
print("\nMatrix K:")
for row in K:
    print(row)

end_time = time.time()
execution_time = end_time - start_time

print("\nExecution time:", execution_time)






















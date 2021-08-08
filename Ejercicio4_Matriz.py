import l as l
import numpy as np
'''
4. Read a 4X3 Integer matrix and determine in what exact position the prime numbers are
'''

matrix = np.array([[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [9, 10, 11]])

matrix_order = matrix.shape[0]
prime_number = matrix[0, 0]
not_prime_number = matrix[0, 0]
position_prime_number = []

print(matrix)

for i in range(matrix_order):
    for j in range(matrix_order - 1):

        if matrix[i, j] == 2:
            prime_number = matrix[i, j]
            position_prime_number = [(i, j)]
            print(f'The number {prime_number} is prime and is in the position {position_prime_number}')

        elif matrix[i, j] > 2:
            n = matrix[i, j]
            for k in (2, n):
                if n % k != 0:
                    prime_number = matrix[i, j]
                    position_prime_number = [(i, j)]
                    print(f'The number {prime_number} is prime and is in the position {position_prime_number}')



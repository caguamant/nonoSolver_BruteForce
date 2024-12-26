import time
import random

def solve():
    start_time = time.time() # Start timer

    matrix_length = 5
    tries = 0
    a_matrix = [] # Matrix to solve

    for i in range(matrix_length):
        for j in range(matrix_length):
            random_int = random.randint(0, 1)
            a_matrix.append(random_int)

    while True:
        b_matrix = []

        for i in range(matrix_length):
            for j in range(matrix_length):
                random_int = random.randint(0, 1)
                b_matrix.append(random_int)

        if b_matrix != a_matrix:
            tries += 1
        else:
            break

    end_time = time.time()  # End timer
    final_time = end_time - start_time  # Check the difference between the start and end time
    print(f"Solution found in {final_time} seconds and {tries} tries")

if __name__ == '__main__':
    solve()
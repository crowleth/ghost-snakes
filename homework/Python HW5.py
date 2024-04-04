import numpy as np

# 1

def find_rows(arr):
    
    row_equal = np.all(arr[:, 1:] == arr[:, :-1], axis=1)
    
    a = np.where(row_equal)[0]
    return a

arr = np.array([[4, 4, 4],
                [5, 5, 5],
                [6, 7, 8],
                [9, 9, 9]])

result = find_rows(arr)
print(result)


# 2

checkers = np.zeros((8, 8), dtype=int)

checkers[::2, ::2] = 1 
checkers[1::2, 1::2] = 1  

print(checkers)

# 3

def separate(arr):
    return [' '.join(thing) for thing in arr]

arr = ["pythons", "eat", "snakes"]

result = separate(arr)
print(result)

# 4 


def sort(matrix):
    sorted_matrix = np.sort(matrix, axis=0)
    return sorted_matrix


matrix = np.array([[3, 2, 5],
                   [1, 4, 6],
                   [7, 0, 2]])


sorted_matrix = sort(matrix)
print(sorted_matrix)

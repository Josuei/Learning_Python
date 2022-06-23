from itertools import combinations
import numpy as np

students = [
    'Alex C', 'Benny D', 'Esmeralda R', 'Helena L', 'Karina M', 'Marisol R', 'Matthew Q', 'Sandy P', 'Trudy B', 'Yori K'
]

groups_of_two = list(combinations(students, 2))
print(groups_of_two)

# Extracting the unique elements.
combinations = np.unique(groups_of_two)
print(combinations)

# Shuffling the elements.
combinations = np.random.permutation(combinations)
print(combinations)

# Reshaping the unique elements in groups of three.
combinations = combinations.reshape((-1, 2))
print()
print(combinations)

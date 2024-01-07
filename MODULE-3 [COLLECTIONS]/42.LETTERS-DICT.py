from itertools import product

# Sample data
my_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

# Generate all combinations of letters
combinations = list(product(*my_dict.values()))

# Convert each combination to a string
# result = [''.join(combination) for combination in combinations
# ]

for i in combinations:
  result = "".join(i)
  print(' '.join(result))
    




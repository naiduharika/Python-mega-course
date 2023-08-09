import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

print(random.randrange(lower_bound, upper_bound + 1))

# The following program creates a dice simulator using a function.
import random


def random_number(max_int):
    print("Rolling the Dice!")
    rand_num = random.randint(1, max_int)
    return rand_num


a_number = random_number(12)
print(a_number)
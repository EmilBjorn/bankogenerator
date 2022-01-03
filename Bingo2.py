#%%
from random import randrange
from dataclasses import dataclass

#%%
# @dataclass
# class Bankoplade():


def bingo_num():
    """Randomly generates 15 unique numbers between 1 and 90"""

    numbers = {}
    n_numbers = 0
    for i in range(9):
        numbers[i] = [1 + randrange(10) + i * 10]
        n_numbers += 1

    while n_numbers < 15:
        new_number = randrange(1, 91)
        dict_key = (new_number - 1) // 10
        if len(numbers[dict_key]) < 3 and (new_number) not in numbers[dict_key]:
            numbers[dict_key].append(new_number)
            n_numbers += 1

    for values in numbers.values():
        values.sort()

    return numbers


def render_plate():
    numbers = list(bingo_num().values())
    plate = [["", "", ""] for i in range(9)]

    def check_row_numbers(plate):
        row_counts = {0: 0, 1: 0, 2: 0}
        for plate_column in plate:
            for row, number in enumerate(plate_column):
                if number != "":
                    row_counts[row] += 1
        return row_counts

    for index, value in enumerate(numbers):
        if len(value) == 3:
            plate[index] = value

    return plate


if __name__ == "__main__":
    tal = bingo_num()
    for val in tal.values():
        print(val)
    plade = render_plate()
    for i in plade:

        print(i)

# %%

# %%

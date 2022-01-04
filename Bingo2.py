#%%
from random import randrange
from dataclasses import dataclass


# TODO: Hele ti'ere kommer i den forkerte kategori. De ligger sammen med de foregående tal, så 50 er sammen med 46, fx.
#%%
# @dataclass
# class Bankoplade():


def bingo_num():
    """Randomly generates 15 unique numbers between 1 and 90"""

    numbers_dict = {}
    n_numbers = 0

    # Generates 9 random digits from each band of 10
    for i in range(9):
        numbers_dict[i] = [1 + randrange(10) + i * 10]
        n_numbers += 1

    # Generates the remaining 6 digits making sure to add no dublicates
    while n_numbers < 15:
        new_number = randrange(1, 91)
        key = (new_number - 1) // 10
        if len(numbers_dict[key]) < 3 and (new_number) not in numbers_dict[key]:
            numbers_dict[key].append(new_number)
            n_numbers += 1

    for values in numbers_dict.values():
        values.sort()

    return numbers_dict


def render_plate(number_dict):
    number_list_nested = list(number_dict.values())
    plate = [["", "", ""] for i in range(9)]

    def check_rows(plate):
        row_counts = {0: 0, 1: 0, 2: 0}
        for plate_column in plate:
            for row, number in enumerate(plate_column):
                if number != "":
                    row_counts[row] += 1

        for row_count in row_counts.values():
            if row_count > 5:
                valid = False
                break
            else:
                valid = True

        return valid

    # Firstly, columns with all three numbers in are added to the plate. These will have no row-conflicts
    for index, number_list in enumerate(number_list_nested):
        if len(number_list) == 3:
            plate[index] = number_list

    # Secondly, columns with two numbers are placed. These can potentially have conflicts and
    # will need to be verified with the check_row_numbers() method.
    prev_places = ["", "", ""]
    for ten, number_list in enumerate(number_list_nested):
        if len(number_list) == 2:
            while True:
                places = list(range(3))
                places.remove(randrange(3))
                print(places, "vs", prev_places)
                if places != prev_places:
                    prev_places = places
                    break

            for index, number in enumerate(number_list):
                plate[ten][places[index]] = number

    # todo Lastly, the singular numbers will need to be placed to make the all the rows have exactly 5 numbers in them.

    return plate


if __name__ == "__main__":
    tal = bingo_num()
    for val in tal.values():
        print(val)
    plade = render_plate(tal)
    for i in plade:

        print(i)

# %%

# %%

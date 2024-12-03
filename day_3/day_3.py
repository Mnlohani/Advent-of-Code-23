import numpy as np
from utils import (
    extract_part_number_and_indices,
    get_neighbours_indices_all_symbols,
    calculate_total_gear_ratios,
)

# Read the data file
try:
    with open("day_3.txt", "r") as file:
        file_content = file.read()
except FileNotFoundError:
    print("File not found at provided path location")

# Part 1: sum of all of the part numbers adjacent to a symbol except '.')
# -----------------------------------------------------------------------

data = np.array([list(line) for line in file_content.splitlines()])

# Extract_part_number_and_indices in the file
part_numbers_with_indices = extract_part_number_and_indices(file_content)

# Get the set of neighbours' indices of all symbols except '.'
all_symbol_neighbours_indices, symbol_with_neighbor_indices = (
    get_neighbours_indices_all_symbols(data)
)

# Initalise a list to store part numbers whose indices overlap with any symbol's neighbor indices
eligible_part_numbers = []

# Check for overlap for each part number by set difference between the positional indices of a number
# and set of neighbours' indices of all symbols
for number in part_numbers_with_indices:
    part_indices = number[1]
    overlapping_indices = part_indices.intersection(all_symbol_neighbours_indices)

    # if overlap, add part number to the eligible list
    if len(overlapping_indices) > 0:
        eligible_part_numbers.append(number[0])

print(
    f"The sum of all eligible part numbers in the engine schematic is {sum(eligible_part_numbers)}."
)


# Part 2: Sum of all of the gear ratios in the engine schematic
# --------------------------------------------------------------

total_gear_ratios = calculate_total_gear_ratios(
    symbol_with_neighbor_indices, part_numbers_with_indices
)

print(
    f"The sum of all of the gear ratios in the engine schematic is {total_gear_ratios}."
)

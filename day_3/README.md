## Part 1: Sum of all of the part numbers that are adjacent to a symbol except '.'

### Approach:

1. Get the set of neighbours' indices of all symbols except '.' as `all_symbol_neighbours_indices`
2. Get positional indices of all part numbers number as `part_numbers_with_indices`
3. Check for each part number. If there is an overlap between the positional indices of part number and all_symbol_neighbours_indices, include it into list and calculuate sum of all such part numbers.

## Part 2:

### Approach: Sum of all of the gear ratios in the engine schematic

1. Loop through an outer loop for symbols to identify the gears ('\*' symbols with exactly 2 neighbors)
2. Loop through an inner each part number to find overlap between the indices of part number and neighbors of symbol '\*'
3. Validate if the number of overlapping part number is two.
4. Compute the product of such two part numbers as gear ratio
5. Add all such gear ratios

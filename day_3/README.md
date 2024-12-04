## Part 1: Sum of all of the part numbers that are adjacent to a symbol except '.'

The engine schematic (puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..  
..._......  
..35..633.  
......#...  
617_......  
.....+.58.  
..592.....  
......755.  
...$.\*....  
.664.598..  
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

For input data file, what is the sum of all of the part numbers in the engine schematic?

### Approach:

1. Get the set of neighbours' indices of all symbols except '.' as `all_symbol_neighbours_indices`
2. Get positional indices of all part numbers number as `part_numbers_with_indices`
3. Check for each part number. If there is an overlap between the positional indices of part number and all_symbol_neighbours_indices, include it into list and calculuate sum of all such part numbers.

## Part 2: Sum of all of the gear ratios in the engine schematic

A gear is any \* symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together. This time, we need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..  
..._......  
..35..633.  
......#...  
617_......  
.....+.58.  
..592.....  
......755.  
...$.\_....  
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The \_ adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in the engine schematic?

### Approach:

1. Loop through an outer loop for symbols to identify the gears ('\*' symbols with exactly 2 neighbors)
2. Loop through an inner each part number to find overlap between the indices of part number and neighbors of symbol '\*'
3. Validate if the number of overlapping part number is two.
4. Compute the product of such two part numbers as gear ratio
5. Add all such gear ratios

## Part 1:

### Approach:

1. Read the input file
2. Substitute characters except [0-9] with "" e.g, ['Zone1c2d4', 'dhs2c3gh2, 'dd'] --> ['124', '232', ''] with regular expression.
3. Convert to list of 2-digit numbers (1st and last) e.g, ['124', '232', ''] --> [12, 22]
4. Calculate Sum of calibrated 2-digit numbers.

## Part 2:

### Approach:

1. Read the input file,
2. Clean the text by replaceing the overlapping substrings. e.g, '4twone9' --> '4twoone9' via creating a dictionary for overlaping strings such as
   dict_str_overlap = {
   "oneight": "oneeight",
   "twone": "twoone",...}
3. Loop over each line of i/p file and find matches for each digit strings using regular expression and convert to numbers.
4. Calculate Sum of 2-digit numbers created with first and last digit

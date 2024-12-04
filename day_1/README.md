## Part 1:

Given input sample:

1abc2  
pqr3stu8vwx  
a1b2c3d4e5f  
treb7uchet  
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

For the input data file, what is the sum of all of the calibration values?

### Approach:

1. Read the input file
2. Substitute characters except [0-9] with "" e.g, ['Zone1c2d4', 'dhs2c3gh2, 'dd'] --> ['124', '232', ''] with regular expression.
3. Convert to list of 2-digit numbers (1st and last) e.g, ['124', '232', ''] --> [12, 22]
4. Calculate Sum of calibrated 2-digit numbers.

## Part 2:

Some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

two1nine  
eightwothree  
abcone2threexyz  
xtwone3four  
4nineeightseven2  
zoneight234  
7pqrstsixteen  
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
What is the sum of all of the calibration values?

### Approach:

1. Read the input file,
2. Clean the text by replaceing the overlapping substrings. e.g, '4twone9' --> '4twoone9' via creating a dictionary for overlaping strings such as
   dict_str_overlap = {
   "oneight": "oneeight",
   "twone": "twoone",...}
3. Loop over each line of i/p file and find matches for each digit strings using regular expression and convert to numbers.
4. Calculate Sum of 2-digit numbers created with first and last digit

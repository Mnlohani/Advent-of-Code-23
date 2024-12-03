import re


def calculate_calibrated_sum(input_file_path: str) -> int:
    """Read the input file, replace the overlapping strings,
    find matches for each digit-strings and convert into digits,
    extract first and last digit from each line of the input file,
    make 2-digit calibrated numbers from them and
    return summation of calibrated numbers

    Args:
        input_file (str): Path of the input data file

    Returns:
        int: Sum of all calibrated 2-digit numbers (first digit and last digit)

    Example:
    --------
    Input file content:

    "4twoone9
    eightninesix
    2eightwo
    abc"

    Generated 2-digit numbers: [49, 86, 22]
    Calculated Sum = 157
    """

    dict_str_overlap = {
        "oneight": "oneeight",
        "twone": "twoone",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "sevenine": "sevennine",
        "eightwo": "eighttwo",
        "eighthree": "eightthree",
        "nineight": "nineeight",
    }
    dict_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    pattern = re.compile(
        r"(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)"
    )
    calibrated_lines = []
    calibrated_numbers = []

    # Read input file
    try:
        with open(input_file_path, "r") as f:
            contents = f.read()
    except FileNotFoundError:
        print("File not found at provided path location")

    # Clean the text by replaceing the overlapping substrings. e.g, '4twone9' --> '4twoone9'
    for key in dict_str_overlap.keys():
        contents = contents.replace(key, dict_str_overlap[key])

    # loop over each line of i/p file and find matches for each digit strings
    for each_line in contents.splitlines():
        matches = pattern.finditer(each_line)
        matched_digits = [
            dict_digits[match.group()] for match in matches
        ]  # 4twoone9 --> ['4', '2', '1', '9']
        calibrated_line = "".join(matched_digits)  # ['4', '2', '1', '9'] --> '4219'
        calibrated_lines.append(calibrated_line)  # append into list ['4219', '124', '']

    # convert to list of 2-digit numbers (1st and last) e.g, ['4219', '124', '']  --> [49, 14]
    calibrated_numbers = [
        int(line[0] + line[-1]) for line in calibrated_lines if len(line) > 0
    ]
    return sum(calibrated_numbers)


if __name__ == "__main__":
    total = calculate_calibrated_sum("day_1.txt")
    print(f"The sum of calibrated numbers is {total}.")

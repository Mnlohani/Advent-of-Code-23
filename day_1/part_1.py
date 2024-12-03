import re


def cal_calibrated_sum(input_file_path: str) -> int:
    """Reads input file, extract first and last digit from each line of the input file,
    make 2-digit calibrated numbers from them and return summation of calibrated numbers

    Args:
        input_file_path (str): path of the data file

    Returns:
        sum_calibrated (int): sum of all such 2-digit numbers


    Example:
    -------
    Input file:

    "1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    tt"

    Generated 2-digit numbers: [12, 38, 15, 77]
    Calculated sum = 142
    """

    # Read the input data file
    try:
        with open(input_file_path, "r") as f:
            contents = f.readlines()
    except FileNotFoundError:
        print("File not found at provided path location")

    # substitute characters except [0-9] e.g, ['Zone1c2d4', 'dhs2c3gh2, 'dd'] --> ['124', '232', '']
    numbers = [re.sub(r"\D", "", each_line) for each_line in contents]

    # convert to list of 2-digit numbers (1st and last) e.g, ['124', '232', '']  --> [12, 22]
    calibrated_numbers = [
        int(number[0] + number[-1]) for number in numbers if len(number) > 0
    ]

    sum_caliberated = sum(calibrated_numbers)
    return sum_caliberated


if __name__ == "__main__":
    total = cal_calibrated_sum("day_1.txt")
    print(f"The sum of calibrated numbers is {total}.")

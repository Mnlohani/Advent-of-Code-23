import pandas as pd
from utils import get_valid_game_ids, calculate_power_of_minimum_set

# Read the data file
try:
    with open("day_2.txt", "r") as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found at provided path location")


# Part 1: Possible game ids and their sum
# ---------------------------------------

games = contents.splitlines()
full_game = []  # variable to store info of all game trials

for game in games:
    # Split the line into 2 parts e.g, Game id, sets of game
    game_id, game_sets_str = game.split(": ")
    game_number = int(
        game_id.split(" ")[1]
    )  # Game 1: 3 blue, 4 red; 1 red, 2 green => game_number = 1
    game_sets = game_sets_str.split(
        "; "
    )  # ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']

    # iteration for each set of the game
    for i, each_set in enumerate(game_sets):
        game_set_dict = {
            "game number": game_number,
            "set number": i + 1,
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        # Extract the color of cubes and their counts in each set e.g, ['3 blue', '4 red']
        for cube in each_set.split(", "):
            color_count = int(cube.split(" ")[0])
            color = cube.split(" ")[1]
            game_set_dict[color] = color_count

        full_game.append(game_set_dict)

# Dataframe of all game trials
df = pd.DataFrame(full_game)

# Sum of valid game ids
valid_game_ids = get_valid_game_ids(df)
sum_valid_game_ids = sum(valid_game_ids)

print(f"The sum of valid game ids is {sum_valid_game_ids}.")


# Part 1: Power of sets containing the minimum number of cubes that must be present for a game
# ---------------------------------------------------------------------------------------------

sum_power_of_sets = calculate_power_of_minimum_set(df)

print(
    f"The sum of the power of sets which contain the minimum number of cubes that must have been present is {sum_power_of_sets}."
)

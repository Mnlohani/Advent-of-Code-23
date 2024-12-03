import pandas as pd


def is_valid_game(row: pd.Series) -> bool:
    """check if no set exceeds the maximum allowed number of cubes for each color.
        e.g, A game set Game 1: (3 blue, 4 red; (1 red, 20 green, 6 blue); (2 green)
        In set 2, green cubes exceeds the maximum allowed 13 green cubes. So, Game 1 is invalid.

    Args:
        row (pd.Series): pandas Series with info of game trials

    Returns:
        bool: True/False if valid game or not
    """
    return row["red"] <= 12 and row["green"] <= 13 and row["blue"] <= 14


def get_valid_game_ids(df: pd.DataFrame) -> set:
    """get the game ids in which no individual set of each game exceeds the maximum allowed
    number of cubes for each color.

    Args:
        df (pd.DataFrame): Dataframe of all game ids with columns
                           ('game number', 'set number', 'red', 'green', 'blue')

    Returns:
        valid_games_id(set): the set of valid game ids
    """

    # add a column indicating if row is valid or not
    df["is_valid"] = df.apply(is_valid_game, axis=1)

    # unique game Id's
    all_game_ids = set(df["game number"].unique())

    # create set for invalid games
    df_invalid_games = df[df["is_valid"] == False]

    # invalid games ids
    invalid_game_ids = set(df_invalid_games["game number"])

    # set difference between set with all game numbers and set of invalid games numbers
    valid_game_ids = all_game_ids - invalid_game_ids
    return valid_game_ids


def calculate_power_of_minimum_set(df: pd.DataFrame) -> int:
    """
    Find the minimum set of cubes that must have been present for each game and
    calculate the sum of the power of these sets.
    The power of set is the product of the element of a set.
    Args:
        df (pd.DataFrame): Dataframe of all game ids with columns
                           ('game number', 'set number', 'red', 'green', 'blue')
    Returns:
        int: The sum of the power of the minimum sets of cubes across all games.
    """
    df_max_cubes = df.groupby("game number")[["red", "blue", "green"]].max()
    df_max_cubes["power set"] = (
        df_max_cubes["red"] * df_max_cubes["green"] * df_max_cubes["blue"]
    )
    return df_max_cubes["power set"].sum()

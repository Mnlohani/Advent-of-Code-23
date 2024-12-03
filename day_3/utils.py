import numpy as np
import re


def get_neighbours_indices_2D(row_id, col_id, w, h):
    """generate neighbours' 2D indices of an element in a 2D matrix

    Args:
        row_id (int): row index of the element
        col_id (int): column index of the element
        w (int): width of matrix
        h (int): height of matrix

    Returns:
        valid_neighbour_indices(list): list of neighbours' indices


    Example:
    --------
    >> get_neighbours_indices_2D(0, 0, 10, 10)
    Output:
    [(0, 1), (1, 0), (1, 1)]

    >>
    get_neighbours_indices_2D(1, 1, 10, 10)
    Output:
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    """

    # List of possible neighbours in 2D (right, left, down, up, and digonals)
    possible_neighbour_indices = [
        (row_id - 1, col_id - 1),
        (row_id - 1, col_id),
        (row_id - 1, col_id + 1),
        (row_id, col_id - 1),
        (row_id, col_id + 1),
        (row_id + 1, col_id - 1),
        (row_id + 1, col_id),
        (row_id + 1, col_id + 1),
    ]

    # List of valid neighbours which are in bound of matrix
    valid_neighbour_indices = []

    # Check if the neighbours are in bounds and add to list
    for neighbour_ind in possible_neighbour_indices:
        if 0 <= neighbour_ind[0] < w and 0 <= neighbour_ind[1] < h:
            valid_neighbour_indices.append(neighbour_ind)

    return valid_neighbour_indices


def get_neighbours_indices_1D(row_id: int, col_id: int, w: int, h: int) -> list:
    """Get the neighbours' 2D indices of an element in a matrix
    and convert the 2D indices to 1D indices

    Args:
        row_id (int): row index of the element
        col_id (int): column index of the element
        w (int): width of matrix
        h (int): height of matrix

    Returns:
        set: _description_


    Example:
    -------
    >> get_neighbours_indices_1D(0, 0, 10, 10)
    Output:
    {1, 10, 11}

    >> get_neighbours_indices_1D(1, 1, 10, 10)
    output:
    {0, 1, 2, 10, 12, 20, 21, 22}
    """

    # Get the neighbours' 2D indices
    neighbours = get_neighbours_indices_2D(row_id, col_id, w, h)
    # Convert the 2D indices to 1D indices and add to the list
    neighbours_indices_1D = []
    for neighbour in neighbours:
        index_1d = neighbour[0] * w + neighbour[1]
        neighbours_indices_1D.append(index_1d)
    return neighbours_indices_1D


def extract_part_number_and_indices(input_file_content: str) -> list:
    """Extract part numbers(consecutive digits) from the input file text
    and calculate their positional indices (start to end)

    Args:
        input_file_content (str): raw text from the file as a string

    Returns:
        part_numbers_with_indices(list): A List of list [part_number, part_number_indices]
                                    part_number(int) : The numeric value of number
                                    part_number_indices(set): set of indices of part number's position

    Example:
    --------

    Input file content:
    467..114..\n...*......\n..35..633.

    Output:
    [[467, {0, 1, 2}],
    [114, {5, 6, 7}],
    [35, {22, 23}]]

    """
    # Remove '\n' from the raw text from the file
    content = input_file_content.replace("\n", "")

    # Define regular expression pattern for part numbers
    pattern = re.compile(r"\d+")

    # Find all matches in the file content using pattern
    matches = re.finditer(pattern, content)

    # Initialize a list to store part numbers and their indices
    part_numbers_with_indices = []
    for match in matches:
        part_number = int(match.group())
        part_number_indices = set(range(match.start(), match.end(), 1))
        part_numbers_with_indices.append([part_number, part_number_indices])

    return part_numbers_with_indices


def get_neighbours_indices_all_symbols(data: np.array) -> set:
    """Find and return the indices of the neighbours of all symbols (excluding '.') in the matrix

    Args:
        data (np.array): 2D Numpy array where each symbol can be a digit or a symbol

    Returns:
        set, list:  A set containg indices of the neighbours of all symbols (excluding '.')
                    A list of symbol with its neighbours [ symbol, list of neigbours]
                    eg. [['*', [2, 3, 4, 12, 14, 22, 23, 24]], ['#', [25, 26, 27, 35, 37, 45, 46, 47]]]
    """

    # Initialise list to store indices of the neighbors of all symbols
    all_symbol_neighbours_indices = []
    # Initialise list of lists containing symbols with their indices
    symbols_with_neighbours_indices = []

    # Dimension of the matrix
    w, h = data.shape

    # Iterate through each element and store the neighbors indices
    for row_id in range(w):
        for col_id in range(h):
            element = data[row_id, col_id]

            if not element.isdigit() and element != ".":
                symb_neighbors = get_neighbours_indices_1D(row_id, col_id, w, h)
                symbols_with_neighbours_indices.append([element, symb_neighbors])
                all_symbol_neighbours_indices.extend(symb_neighbors)

    return set(all_symbol_neighbours_indices), symbols_with_neighbours_indices


def calculate_total_gear_ratios(
    symbol_with_neighbor_indices: list, part_numbers_with_indices: list
) -> int:
    """Calculate sum of all of the gear ratios in the engine schematic
        Gear is the '*' symbol having exactly two neighbours in the engine schematic

    Args:
        symbol_with_neighbor_indices (list): List of symbol with its neighbours [ symbol, list of neigbours]
                                            eg. [['*', [2, 3, 4, 12, 14, 22, 23, 24]], ['#', [25, 26, 27, 35, 37, 45, 46, 47]]]
        part_numbers_with_indices(list): A List of list [part_number, part_number_indices]
                                    part_number(int) : The numeric value of number
                                    part_number_indices(set): set of indices of part number's position
    Returns:
        int: Summation of all gear ratios in the engine schematic

    """

    # Initialise a list of all gear ratios
    gear_ratios = []

    # Iterate over symbols to see overlap between symbol indices and parts indices
    for item_symbol in symbol_with_neighbor_indices:
        symbol, symbol_neighbours = item_symbol
        if symbol != "*":
            continue
        # Initialise a list of neighbors of symbol '*'
        neighbour_part_list = []
        neigbours_index = set(symbol_neighbours)
        for part in part_numbers_with_indices:
            part_no, part_idx = part
            overlaps = part_idx.intersection(neigbours_index)
            if overlaps:
                neighbour_part_list.append(part_no)

        # Append to the list if the '*' is a gear i.e, '*' symbol with two neighbours
        if len(neighbour_part_list) == 2:
            gear_ratios.append(neighbour_part_list[0] * neighbour_part_list[1])

    return sum(gear_ratios)

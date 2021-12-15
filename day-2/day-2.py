def get_puzzle_input(input_file):
    """Takes in puzzle input as text file and returns list of directions"""

    day_2_input = open(input_file)

    directions = []

    for line in day_2_input:
        directions.append(line.rstrip())

    return directions
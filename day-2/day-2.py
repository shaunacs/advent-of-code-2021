def get_puzzle_input(input_file):
    """Takes in puzzle input as text file and returns list of directions"""

    day_2_input = open(input_file)

    directions = []

    for line in day_2_input:
        directions.append(line.rstrip())

    return directions


def split_command(command):
    """Takes in a command (Ex. 'up 3') and splits on space"""

    return command.split()





directions_lst = get_puzzle_input('day-2-input.txt')

for direction in directions_lst:
    print(split_command(direction))
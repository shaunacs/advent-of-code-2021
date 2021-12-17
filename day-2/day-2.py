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


def execute_commands(command, location):
    """Takes in a list command (Ex. ['up', 3]) and location, and updates location accordingly"""

    movement_num = int(command[1])

    if command[0] == 'forward':
        location['horizontal'] += movement_num
    elif command[0] == 'down':
        location['depth'] += movement_num
    elif command[0] == 'up':
        location['depth'] -= movement_num
    
    return location

def solve_day2_1():
    starting_location = {'horizontal': 0,
                        'depth': 0}

    directions_lst = get_puzzle_input('day-2-input.txt')

    for direction in directions_lst:
        execute_commands(split_command(direction), starting_location)

    final_answer = starting_location['horizontal'] * starting_location['depth']

    return final_answer


def execute_commands2(command, location):

    movement_num = int(command[1])

    if command[0] == 'forward':
        location['horizontal'] += movement_num
        location['depth'] += (location.get('aim') * movement_num)
    elif command[0] == 'down':
        location['aim'] += movement_num
    elif command[0] == 'up':
        location['aim'] -= movement_num
    
    return location


def solve_day2_2():

    starting_location = {'horizontal': 0,
                        'depth': 0,
                        'aim': 0}

    directions_lst = get_puzzle_input('day-2-input.txt')

    for direction in directions_lst:
        execute_commands2(split_command(direction), starting_location)

    final_answer = starting_location['horizontal'] * starting_location['depth']

    return final_answer
def find_num_increases(input_file):
    day_1_input = open(input_file)

    increased = 0

    prev_num = None

    for line in day_1_input:
        if prev_num is not None:
            current_num = int(line)
            if current_num > prev_num:
                increased += 1
            prev_num = current_num
        else:
            prev_num = int(line)
    
    return increased


def make_windows_of_three(input_file):
    measurements = open(input_file)

    windows_of_three = []

    for line in measurements:
        if windows_of_three == []:
            windows_of_three.append([int(line)])
        elif len(windows_of_three[-1]) < 3:
            windows_of_three[-1].append(int(line))
        else:
            windows_of_three.append([int(line)])
    
    increased = 0

    prev_num = None

    for window in windows_of_three:
        if prev_num is not None and len(window) == 3:
            sum_of_window = sum(window)
            if sum_of_window > prev_num:
                increased += 1
            prev_num = sum_of_window
        else:
            prev_num = sum(window)
            
    print(increased)


def check_every_three(input_file):
    measurements = open(input_file)

    measurements_lst = []
    for line in measurements:
        measurements_lst.append(int(line.strip()))

    increased = 0
    prev_num = None

    for num in range(len(measurements_lst) - 2):
        if prev_num is not None:
            window_range = [measurements_lst[num], measurements_lst[num + 1], measurements_lst[num + 2]]
            sum_of_window = sum(window_range)
            if sum_of_window > prev_num:
                increased += 1
            prev_num = sum_of_window
        else:
            window_range = [measurements_lst[num], measurements_lst[num + 1], measurements_lst[num + 2]]
            prev_num = sum(window_range)
        
    return increased
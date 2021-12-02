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



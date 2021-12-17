# PSEUDOCODE
# create empty dict for bit count
# open file
# iterate over each line of file
# strip each line of whitespace
# for idx, char in enumerate(each line)
    # convert char to int
    # bit count dict[idx] += 1
# return bit count

def count_bits(input_file):
    
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
    day_3_input = open(input_file)

    bit_count = {}

    for bin_num in day_3_input:
        bin_num = bin_num.rstrip()
        
        for idx, char in enumerate(bin_num):
            if idx in bit_count:
                if int(char) in bit_count[idx]:
                    bit_count[idx][int(char)] += 1
                else:
                    bit_count[idx][int(char)] = 1
            else:
                bit_count[idx] = {int(char): 1}
    
    return bit_count

print(count_bits('test-input.txt'))
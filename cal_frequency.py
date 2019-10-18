def cal_frequency():

    # initialise variables
    allowed_chars = list(map(chr, range(97, 123)))  # creates list of characters a to z
    chars_freq = {}

    # prompt for string and lower()
    input_string = str(input('Please provide input string: ')).lower()
    for char in input_string:
        if char not in allowed_chars:
            continue  # skip this prohibited char
        if char in chars_freq:
            chars_freq[char] += 1  # increment character counter
        else:
            chars_freq[char] = 1  # add character as a key and initialise counter in value

    # order array by value
    # loop through array and print key and value
    print(sorted(chars_freq.items(), key=lambda x: x[1], reverse=True))

cal_frequency()
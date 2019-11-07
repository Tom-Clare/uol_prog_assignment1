def cal_frequency():

    # initialise variables
    chars_freq = {}  # new dictionary for characters and frequencies

    input_string = str(input('Please provide input string: ')).lower()  # prompt for string and make lowercase
    for char in input_string:
        if char.isalpha():  # check against whitelist
            if char in chars_freq:  # we've seen this character before
                chars_freq[char] += 1  # increment character counter
            else:  # we haven't seen this character so far
                chars_freq[char] = 1  # add character as key and initialise counter in value

    if not chars_freq:  # if chars_freq is empty
        print("Analysis failed. Invalid input.")
        return

    # sorted() will take dictionary, and sort by value in reverse (desc) order because of our reverse=True flag. The
    # `lambda x: x[1]` will, for every element x, pass x[1] to sorted(), which is the value in the dictionary
    # (as x[0] is the character and x[1] is it's frequency). This means we end up sorting by value instead of key.
    chars_freq_sorted = sorted(chars_freq.items(), key=lambda x: x[1], reverse=True)

    # after sorting, we can loop through the tuple and format nicely.
    for char_freq in chars_freq_sorted:
        print(char_freq[0] + ": " + str(char_freq[1]))

def pig_latin():
    input_string = str(input('What would you like to translate? '))
    input_array = input_string.split()  # split the string into an array of separate words

    for index, word in enumerate(input_array):
        word = word[1:] + word[:1] + 'ay'  # all but the first letter + first letter + 'ay'
        input_array[index] = word.lower()  # replace original word with lowercase modified word

    print((" ".join(input_array)))  # join array values together with " " as separator

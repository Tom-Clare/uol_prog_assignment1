def pig_latin():
    input_string = str(input('What would you like to translate? '))
    input_array = input_string.split()  # split the string into an array of separate words

    pig_latin = []  # initialise array

    for word in input_array:
        word = word[1:] + word[:1] + 'ay'  # all but the first letter + first letter + 'ay'
        pig_latin.append(word.lower())  # append modified string

    print((" ".join(pig_latin)))  # join array values together with " " as separator

def compare_ages():
    editor_age = 20
    # ask for user age and cast to integer
    user_age = int(input('What is your age? '))
    if user_age > editor_age:
        age_difference = user_age - editor_age
        # display age_difference with message
        print('You are older than me by', age_difference, 'year(s)')
    elif user_age < editor_age:
        age_difference = editor_age - user_age
        # display age_difference with message
        print('You are younger than me by', age_difference, 'year(s)')
    else:
        # display message
        print('You are the same age as me')

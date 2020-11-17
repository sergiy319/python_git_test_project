def greeting(name, surname, age, language):
    print(f'Hi, {name} {surname}!')
    print(f"Are you only {age} years old?! It's time to start learning {language}!")


if __name__ == '__main__':
    the_name = str(input('Please, enter your name: '))
    the_surname = str(input('Please, enter your surname: '))
    the_age = int(input('How old are you?: '))
    programming_language = str(input('What is your favorite programming language?: '))
    greeting(the_name, the_surname, the_age, programming_language)

def greeting(name, surname, age):
    print(f'Hi, {name} {surname}!')
    print(f"Are you only {age} years old?! It's time to start learning Python!")


if __name__ == '__main__':
    the_name = str(input('Please, enter your name: '))
    the_surname = str(input('Please, enter your surname: '))
    the_age = int(input('How old are you?: '))
    greeting(the_name, the_surname, the_age)

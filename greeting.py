def greeting(name, surname):
    print(f'Hi, {name} {surname}! How are you?')


if __name__ == '__main__':
    the_name = str(input('Please, enter your name: '))
    the_surname = str(input('Please, enter your surname: '))
    greeting(the_name, the_surname)

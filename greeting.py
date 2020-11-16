def greeting(name):
    print(f'Hi, {name}! How are you?')


if __name__ == '__main__':
    the_name = str(input('Please, enter your name: '))
    greeting(the_name)

name = input()

while name != 'Welcome!':
    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    if len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    if len(name) > 6:
        print(f'{name} goes to Hufflepuff.')

    name = input()
    if name == 'Welcome!':
        print('Welcome to Hogwarts.')
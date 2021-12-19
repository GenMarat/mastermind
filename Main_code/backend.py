import random

colors = ['r', 'g', 'b', 'y', 'o', 'w', 'p', 'v']

def random_colors(count: int, list_value: list) -> list:
    new_list_value = []
    for i in range(count):
        temp_value = random.choice(list_value)
        new_list_value.append(temp_value)
    return new_list_value

def choice_user(count: int) -> int:
    print('red (r)')
    print('green (g)')
    print('blue (b)')
    print('yellow (y)')
    print('orange (o)')
    print('white (w)')
    print('pink (p)')
    print('violet (v)')
    print()
    list_choice = []
    for i in range(count):
        while True:
            choice = input('Choice color: ')
            if choice in ['r', 'g', 'b', 'y', 'o', 'w', 'p', 'v']:
                list_choice.append(choice)
                break
            else:
                print('Incorrect choice')
    return list_choice

#def compare_index(list_1: list, list_2: list) -> list:

#print(random_colors(8, colors))

x = choice_user(2)
print(x)
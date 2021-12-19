import random

colors = ['r', 'g', 'b', 'y', 'o', 'w', 'p', 'v']

def random_colors(list_value: list) -> list:
    new_list_value = []
    for i in range(4):
        temp_value = random.choice(list_value)
        new_list_value.append(temp_value)
    return new_list_value

print(random_colors(colors))
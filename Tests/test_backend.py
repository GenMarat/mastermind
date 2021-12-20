from Main_code import backend as bc

colors = ['r', 'g', 'b', 'y', 'o', 'w', 'p', 'v']

ran = bc.random_colors(4, colors)
ch_user = bc.random_colors(4, colors)
print(ran, 'Random colors')
print(ch_user, 'Simulation choice user')

comp = bc.compare_index(ran, ch_user)
overlap = bc.inside_the_list(ch_user, ran)
print(comp, 'Comparison of indexes')
print(overlap, 'Overlap')
print((overlap - comp), 'True overlap')









"""
2 boyutlu bir eksende var olan bir robotu verilen string'deki talimatlara uyarak koordinat ekseni üzerinde hareket
ettireceğiz.
 Mesela; string 'URR' ise robot 1br yukarı 2br sağa hareket edecek.
U = up, increase in Y axis
D = down, decrease in Y axis
R = right, increase in X axis
L = left, decrease in X axis
"""

def robot_to_origin(moves):
    possible_moves = set(moves)
    my_dict = {}
    for move in possible_moves:
        my_dict[move] = moves.count(move)
    x = my_dict['R'] - my_dict['L']
    y = my_dict['U'] - my_dict['D']
    print("x:", x, "y:", y)
    print("Your distance to origin is: ", ((abs(x) ** 2) + (abs(y) ** 2)) ** 1 / 2)
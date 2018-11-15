import random
from game2048.grid_2048 import create_grid

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def get_all_tiles(grid):
    tiles=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==' ':
                tiles.append(0)
            else:
                tiles.append(grid[i][j])
    return tiles

def get_value_new_tile():
    return random.choices([2,4],[0.9,0.1])[0]

def get_empty_tiles_positions(grid):
    empty_tiles=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==' ' or grid[i][j]==0:
                empty_tiles.append((i,j))
    return empty_tiles

def get_new_position(grid):
    empty_tiles=get_empty_tiles_positions(grid)
    n=len(empty_tiles)
    list1=[k for k in range(n)]
    list2=[1/n for k in range(n)]
    num=random.choices(list1,list2)[0]
    (x,y)=empty_tiles[num]
    return x,y

def grid_get_value(grid,x,y):
    if grid[x][y]==' ':
        return 0
    else:
        return grid[x][y]

def grid_add_new_tile(grid):
    x,y=get_new_position(grid)
    grid[x][y]=get_value_new_tile()
    return grid

def init_game(n):
    grid=create_grid(4)
    grid=grid_add_new_tile(grid)
    grid=grid_add_new_tile(grid)
    return grid

def grid_to_string(grid,n):
    a=""""""
    for i in range(n):
        a+=" ==="
    a+=" /n"
    for j in range(n):
        for i in range(n):
            a+="| " + str(grid[j][i]) + " "
        a+="|/n"
        for i in range(n):
            a+=" ==="
        a+=" /n"
    return a

def grid_to_string_with_size(grid,n):
    m=longvalue(grid)
    a=""""""
    for i in range(n):
        a+=" " +(m)*"="
    a+=" /n"
    for j in range(n):
        for i in range(n):
            a+="|" + (m-len(str(grid[j][i]))//2 + m-len(str(grid[j][i]))%2)*" "+ str(grid[j][i]) +(m-len(str(grid[j][i]))//2)* " "
        a+="|/n"
        for i in range(n):
            a+=" "+ (m)*"="
        a+=" /n"
    return a

def longvalue(grid):
    n=len(grid)
    longueur=0
    for i in range(n):
        for j in range(n):
            if len(str(grid[i][j]))>longueur:
                longueur=len(str(grid[i][j]))
    return longueur

def long_value_with_theme(grid,theme):
    n=len(grid)
    longueur=0
    for i in range(n):
        for j in range(n):
            if len(theme[grid[i][j]])>longueur:
                longueur=len(theme[grid[i][j]])
    return longueur

def grid_to_string_with_size_and_theme(grid,theme,n):
    m=long_value_with_theme(grid,theme)
    a=""""""
    for i in range(n):
        a+=" " +(m)*"="
    a+=" /n"
    for j in range(n):
        for i in range(n):
            a+="|" + ((m-len(str(grid[j][i])))//2 )*" "+ theme[grid[j][i]] +((m-len(str(grid[j][i])))//2+ (m-len(str(grid[j][i])))%2)* " "
        a+="|/n"
        for i in range(n):
            a+=" "+ (m)*"="
        a+=" /n"
    return a

def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    if move in ['g','d','h','b']:
        return move
    else:
        print('commande incorrecte')
        read_player_command()

def read_size_grid():
    size = input("choisissez la taille de la grille :")
    return size

def read_theme_grid():
    theme = input("choisissez le theme (Defaut : 0, chemistry : 1, alphabet : 2):")
    return theme

def test_is_full_grid(grid):
    return get_empty_tiles_positions(grid)==[]

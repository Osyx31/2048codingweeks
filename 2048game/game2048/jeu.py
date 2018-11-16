from game2048.tile import *
from game2048.grid_2048 import *
import random

def random_play():
    grid=init_game(4)
    print(grid_to_string_with_size_and_theme(grid,THEMES['1'],4))
    nb=0                                    #nombre de mouvements
    while not is_game_over(grid):
        x=random.choice([0,1,2,3])
        mv=move_possible(grid)
        while not mv[x]:
            x=random.choice([0,1,2,3])
        if x==0:
            grid=move_grid(grid,"right")
        else:
            if x==1:
                grid=move_grid(grid,"left")
            else:
                if x==2:
                    grid=move_grid(grid,"down")
                else:
                    grid=move_grid(grid,"up")
        grid=grid_add_new_tile(grid)
        nb+=1
        print(grid_to_string_with_size_and_theme(grid,THEMES['1'],4))
    print(nb)
    if get_grid_tile_max(grid)>=2048:
        print("c'est gagné")
    else:
        print("c'est perdu")

def game_play():
    taille=int(read_size_grid())
    theme=read_theme_grid()

    grid=init_game(taille)
    print(grid_to_string_with_size_and_theme(grid,theme,taille))
    nb=0                                    #nombre de mouvements
    while not is_game_over(grid):
        x=read_player_command()
        mv=move_possible(grid)
        if x=='d':
            x=0
        elif x=='g':
            x=1
        elif x=='b':
            x=2
        elif x=='h':
            x=3

        while not mv[x]:
            x=read_player_command()
            if x=='d':
                x=0
            elif x=='g':
                x=1
            elif x=='b':
                x=2
            elif x=='h':
                x=3
        if x==0:
            grid=move_grid(grid,"right")
        else:
            if x==1:
                grid=move_grid(grid,"left")
            else:
                if x==2:
                    grid=move_grid(grid,"down")
                else:
                    grid=move_grid(grid,"up")
        grid=grid_add_new_tile(grid)
        nb+=1
        print(grid_to_string_with_size_and_theme(grid,theme,taille))
    print(nb)
    if get_grid_tile_max(grid)>=2048:
        print("c'est gagné")
    else:
        print("c'est perdu")

game_play()








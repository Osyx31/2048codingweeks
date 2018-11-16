def create_grid(taille):
    game_grid=[]
    for i in range(0,taille):
        game_grid.append([' ',' ',' ',' '])
    return game_grid

def move_row_left(grid):
    n=len(grid)
    limite=0
    for j in range(1,n):
        i=1
        while grid[j-i] in [0,' '] and j-i>=0:
            grid[j-i]=grid[j-i+1]
            grid[j-i+1]=0
            i+=1
        if j-i>=0 and grid[j-i]==grid[j-i+1] and j-i+1>limite:
            grid[j-i]=2*grid[j-i]
            grid[j-i+1]=0
            limite=j-i+1
    return grid

def move_row_right(grid):
    n=len(grid)
    limite=n-1
    for j in range(n-2,-1,-1):
        i=1
        while j+i<=n-1 and grid[j+i] in [0,' ']:
            grid[j+i]=grid[j+i-1]
            grid[j+i-1]=0
            i+=1

        if j+i<=n-1 and grid[j+i]==grid[j+i-1] and j+i-1<limite:
            grid[j+i]=2*grid[j+i]
            grid[j+i-1]=0
            limite=j+i-1
    return grid

def rota(grid):
    n=len(grid)
    rot=[[0 for k in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            rot[i][j]=grid[j][i]

    return(rot)



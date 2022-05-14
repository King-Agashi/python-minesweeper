WIDTH = 1080
HEIGHT = 720
GRID_SIZE = 6
MINES_COUNT=(GRID_SIZE ** 2) // 4


def ContainerHeightByPct(x):
    return (HEIGHT * x)//100


def ContainerWidthByPct(x):
    return (HEIGHT * x)//100

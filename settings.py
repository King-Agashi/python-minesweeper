WIDTH = 1440
HEIGHT = 720
GRID_SIZE = 6
CELL_COUNT = GRID_SIZE ** 2
MINES_COUNT = (GRID_SIZE ** 2) // 4


def ContainerHeightByPct(x):
    return (HEIGHT * x)//100


def ContainerWidthByPct(x):
    return (HEIGHT * x)//100

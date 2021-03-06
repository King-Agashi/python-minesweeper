from tkinter import *
import settings
from cell import Cell

root = Tk()
# Settings
root.configure(bg="white")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

# Containers
title_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=settings.ContainerHeightByPct(25)
)
title_frame.place(x=0, y=0)

score_frame = Frame(
    root,
    bg='black',
    width=settings.ContainerWidthByPct(30),
    height=settings.ContainerHeightByPct(75)
)
score_frame.place(
    x=0,
    y=settings.ContainerHeightByPct(25)
)

body_frame = Frame(
    root,
    bg='black',
    width=settings.ContainerWidthByPct(70),
    height=settings.ContainerHeightByPct(75)
)
body_frame.place(
    x=settings.ContainerWidthByPct(30),
    y=settings.ContainerHeightByPct(25)
)

# Grid
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(body_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.create_cell_count_label(score_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()  # Assign mine cells

# Run loop
root.mainloop()

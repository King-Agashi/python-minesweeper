from tkinter import *
import settings
from cell import Cell

root = Tk()
# Settings
root.configure(bg="white")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

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

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(body_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Run loop
root.mainloop()

"""Testing making square buttons in tkinter."""

import tkinter as tk

def button_grid(window, image, b_per_side=5, b_width=60):
    """Make a grid of square buttons (b_per_side*b_per_side) for console tk.

    Return a b_per_side*b_per_side list of buttons.
    """
    buttons = {(i*j, make_button(window, image, b_width, i, j))
               for i in range(b_per_side)
               for j in range(b_per_side)}
    return buttons


def make_button(window, image, b_width, i, j):
    """Make an individual button."""
    b = tk.Button(window, image=image, text='', compound=tk.CENTER)
    b.config(width=b_width, height=b_width)
    b.grid(row=i, column=j, sticky="NSWE")


def main():
    """Run main loop controlling game window."""
    window = tk.Tk()
    image = tk.PhotoImage()
    light_grid = button_grid(window, image)
    window.mainloop()


if __name__ == "__main__":
    main()

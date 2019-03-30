"""A basic gui of squares that change colors when clicked."""
import tkinter as tk


class Game(tk.Frame):
    """GUI application for a simple button based game."""

    # I don't understand why I need this.

    btn_width = 75
    btn_per_side = 5
    lcolors = ['White', 'red']

    def __init__(self, parent=None):
        """Initialize the GUI."""
        super(Game, self).__init__(parent)
        self.btn_img = tk.PhotoImage()
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the game."""
        self.make_button_grid()

    def make_button_grid(self):
        """Create the button grid."""
        total_btns = self.btn_per_side*self.btn_per_side
        self.lbtns = {(i, j): self.make_light_btn(i, j)
                      for i in range(self.btn_per_side)
                      for j in range(self.btn_per_side)}

        self.lstatus = {(i, j): 0
                        for i in range(total_btns)
                        for j in range(total_btns)}

    def make_light_btn(self, i, j):
        """Make the individual light buttons."""
        btn = tk.Button(self.parent, image=self.btn_img, text='',
                        compound=tk.CENTER,
                        command=lambda: self.press_light((i, j)))
        btn.config(width=self.btn_width, height=self.btn_width)
        btn.grid(row=i, column=j, sticky='NSWE')
        return btn

    def change_color(self, i_j):
        """Change color of a button."""
        self.lstatus[i_j] = (self.lstatus[i_j] + 1) % len(self.lcolors)
        new_color = self.lcolors[self.lstatus[i_j]]
        self.lbtns[i_j].configure(highlightbackground=new_color)

    def press_light(self, i_j):
        """Identify buttons whose colors change with click."""
        btn_i, btn_j = i_j
        [self.change_color((i, btn_j))
         for i in [btn_i - 1, btn_i, btn_i + 1]
         if i >= 0 and i < self.btn_per_side]
        [self.change_color((btn_i, j))
         for j in [btn_j - 1,  btn_j + 1]
         if j >= 0 and j < self.btn_per_side]


root = tk.Tk()
root.title('Click Squares')
game = Game(parent=root)
root.mainloop()

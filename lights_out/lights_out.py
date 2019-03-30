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
        self.lbtns = {index: self.make_light_btn(index)
                      for index in range(total_btns)}
        self.lstatus = {index: 0 for index in range(total_btns)}

    def make_light_btn(self, index):
        """Make the individual light buttons."""
        btn = tk.Button(self.parent, image=self.btn_img, text='',
                        compound=tk.CENTER,
                        command=lambda: self.press_light(index))
        btn.config(width=self.btn_width, height=self.btn_width)
        btn.grid(row=index//self.btn_per_side,
                 column=index % self.btn_per_side, sticky='NSWE')
        return btn

    def change_color(self, index):
        """Change color of a button."""
        self.lstatus[index] = (self.lstatus[index] + 1) % len(self.lcolors)
        new_color = self.lcolors[self.lstatus[index]]
        self.lbtns[index].configure(highlightbackground=new_color)

    def press_light(self, index):
        """Identify buttons whose colors change with click."""
        btn_i = index//self.btn_per_side
        btn_j = index % self.btn_per_side

        # write function to return buttons to change
        [self.change_color(i*self.btn_per_side + btn_j)
         for i in [btn_i - 1, btn_i, btn_i + 1]
         if i >= 0 and i < self.btn_per_side]
        [self.change_color(btn_i*self.btn_per_side + j)
         for j in [btn_j - 1,  btn_j + 1]
         if j >= 0 and j < self.btn_per_side]


root = tk.Tk()
root.title('Click Squares')
game = Game(parent=root)
root.mainloop()

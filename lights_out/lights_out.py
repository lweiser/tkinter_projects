"""A basic gui of squares that change colors when clicked."""
import tkinter as tk
import random


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
        self._init_starting_confs()
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the game."""
        self.make_button_grid()
        self.make_control_buttons()

    def make_control_buttons(self):
        """Make the buttons that control gameplay."""
        self.cbtns = {}
        self.cbtns['new'] = tk.Button(self.parent, text="New Game",
                                      command=self.press_new)
        self.cbtns['restart'] = tk.Button(self.parent, text="Restart")
        self.cbtns['custom'] = tk.Button(self.parent, text="Custom")
        self.cbtns['choose'] = tk.Button(self.parent, text="Choose\n Game")
        self.choose_txt = tk.Entry(self.parent, width=self.btn_width//10,
                                   state="disabled")
        self.cbtns['quit'] = tk.Button(self.parent, text="Quit",
                                       command=root.destroy)
        self.cbtns['new'].grid(column=0, row=self.btn_per_side + 1)
        #self.cbtns['restart'].grid(column=1, row=crow)
        #self.cbtns['custom'].grid(column=2, row=crow)
        #self.cbtns['choose'].grid(column=3, row=crow)
        #self.choose_txt.grid(column=3, row=crow+1)
        self.cbtns['quit'].grid(column=self.btn_per_side - 1,
                                row=self.btn_per_side + 1)

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
        self.lbtns[i_j].configure(highlightbackground=new_color, bg=new_color)

    def press_light(self, i_j):
        """Identify buttons whose colors change with click."""
        btn_i, btn_j = i_j
        [self.change_color((i, btn_j))
         for i in [btn_i - 1, btn_i, btn_i + 1]
         if i >= 0 and i < self.btn_per_side]
        [self.change_color((btn_i, j))
         for j in [btn_j - 1,  btn_j + 1]
         if j >= 0 and j < self.btn_per_side]

    def press_new(self):
        """Generate a random starting conf and set lights."""
        self.get_start_layout()
        for i_j, value in self.lstatus_start.items():
            new_color = self.lcolors[value]
            self.lbtns[i_j].configure(highlightbackground=new_color,
                                      bg=new_color)
            self.lstatus[i_j] = value

    def get_start_layout(self, game_number=None):
        """Return the starting light layout.

        If game_number = None, return a random game.
        If game_number = #, return a generator for that game number.
        Todo: If game_number out of range, pop up an error.
        """
        available_confs = len(self._start_confs) * 2
        if game_number is None:
            game_number = random.randint(0, available_confs)
        if game_number < len(self._start_confs):
            start_conf = self._start_confs[game_number]
            self.lstatus_start = {i_j: 0 for i_j in self.lbtns.keys()}
            for i_j in start_conf:
                self.lstatus_start[i_j] = 1
        else:  # should cover all cases for now... will want to throw an error
            start_conf = self._start_confs[game_number % (available_confs/2)]
            self.lstatus_start = {i_j: 1 for i_j in self.lbtns.keys()}
            for i_j in start_conf:
                self.lstatus_start[i_j] = 0
        return None

    def _init_starting_confs(self):
        """Return a generator for the start of a game.

        If game_number = None, return a random game.
        If game_number = #, return a generator for that game number.

        Return: a tuple generator for use making starting confs.
        """
        btns = self.btn_per_side
        self._start_confs = {}
        self._start_confs[0] = [(i, j)
                                for i in range(btns)
                                for j in range(btns)]
        self._start_confs[1] = [(i, j)
                                for i in range(btns)
                                for j in range(0, btns, 2)]
        self._start_confs[2] = [(i, j)
                                for i in range(0, btns, 2)
                                for j in range(btns)]
        self._start_confs[3] = [(i, j)
                                for i in range(0, btns, 2)
                                for j in range(0, btns, 2)]
        self._start_confs[4] = [(i, j)
                                for i in range(btns)
                                for j in range(1, btns, 2)]
        self._start_confs[5] = [(i, j)
                                for i in range(1, btns, 2)
                                for j in range(btns)]
        self._start_confs[6] = [(i, j)
                                for i in range(1, btns, 2)
                                for j in range(1, btns, 2)]
        # four corners
        self._start_confs[7] = [(i, j)
                                for i in [0, btns - 1]
                                for j in [0, btns - 1]]
        self._start_confs[8] = [(i, j)
                                for i in [1, btns - 2]
                                for j in [1, btns - 2]]
        # boxes
        self._start_confs[9] = [(i, j)
                                for i in range(btns)
                                for j in range(btns)
                                if i == 0 or j == 0
                                or i == (btns - 1) or j == (btns - 1)]
        self._start_confs[10] = [(i, j)
                                 for i in range(1, btns - 1)
                                 for j in range(1, btns - 1)
                                 if i == 1 or j == 1
                                 or i == btns - 2 or j == btns - 2]
        # diagonals
        self._start_confs[11] = [(i, j)
                                 for i in range(btns)
                                 for j in range(btns)
                                 if i == j]
        self._start_confs[12] = [(i, j)
                                 for i in range(1, btns - 1)
                                 for j in range(1, btns - 1)
                                 if i == j]
        self._start_confs[13] = [(i, btns - j - 1)
                                 for i in range(btns)
                                 for j in range(btns)
                                 if i == j]
        self._start_confs[14] = [(i, btns - j - 1)
                                 for i in range(1, btns - 1)
                                 for j in range(1, btns - 1)
                                 if i == j]
        return None


root = tk.Tk()
root.title('Lights Out')
game = Game(parent=root)
root.mainloop()

"""Learn tab."""

import Tkinter as gui

from config.config import CONFIG
from tools.colorlog import log
from tools.localize import _


class Learn(object):

    """Learn tab."""

    def __init__(self, master):
        """Draw Learn tab."""
        self.frame = gui.Frame(master, bd=1)
        self.title = gui.Label(
            self.frame,
            text=_("Learn chords"),
            font=CONFIG.h1_font)
        self.title.grid(row=1, column=5, sticky=gui.W, columnspan=10)

        # Make frame visible
        self.frame.grid(row=2, column=1, rowspan=15, columnspan=9)

    def destroy(self):
        """Remove frame."""
        # No idea what the difference between grid_remove and
        # grid_forget is, but we'll call them both to be sure.
        self.frame.grid_remove()
        self.frame.grid_forget()
        self.frame.destroy()

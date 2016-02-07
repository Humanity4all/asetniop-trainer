"""Display which fingers to use."""

import Tkinter as gui


# pylint: disable=invalid-name
# x and y are perfectly good names!
class Hands(object):

    """Display two hands - mark which fingers to use."""

    def __init__(self, master, x, y):
        """Store where to display the hands and show them."""
        self._master = master
        self._x = x
        self._y = y
        self.fingers = {}

        self.fingers["l5"] = gui.Frame(
            master,
            bg="white",
            height=200,
            width=50)
        self.fingers["l4"] = gui.Frame(
            master,
            bg="white",
            height=200,
            width=50)
        self.fingers["l3"] = gui.Frame(
            master,
            bg="white",
            height=200,
            width=50)
        self.fingers["l2"] = gui.Frame(
            master,
            bg="white",
            height=200,
            width=50)
        self.fingers["l1"] = gui.Frame(
            master,
            bg="white",
            height=50,
            width=100)
        self.fingers["r1"] = gui.Frame(
            master,
            bg="white",
            height=50,
            width=100)
        self.fingers["r2"] = gui.Frame(
            master,
            bg="white",
            height=200,
            width=50)
        self.fingers["r3"] = gui.Frame(
            master,
            bg="white",
            height=200,
            width=50)
        self.fingers["r4"] = gui.Frame(
            master,
            bg="white",
            height=200,
            width=50)
        self.fingers["r5"] = gui.Frame(
            master,
            bg="white",
            height=200,
            width=50)
        self.fingers["lp"] = gui.Frame(
            master,
            bg="white",
            height=150,
            width=275)
        self.fingers["rp"] = gui.Frame(
            master,
            bg="white",
            height=150,
            width=275)

        # place the fields on the grid
        # left hand
        self.fingers["l5"].grid(row=y, column=x)
        self.fingers["l4"].grid(row=y, column=x+2)
        self.fingers["l3"].grid(row=y, column=x+4)
        self.fingers["l2"].grid(row=y, column=x+6)
        self.fingers["lp"].grid(row=y+1, column=x, rowspan=2, columnspan=7)
        self.fingers["l1"].grid(row=y+2, column=x+8)

        # right hand
        self.fingers["r1"].grid(row=y+2, column=x+10)
        self.fingers["rp"].grid(row=y+1, column=x+11, rowspan=2, columnspan=7)
        self.fingers["r2"].grid(row=y, column=x+11)
        self.fingers["r3"].grid(row=y, column=x+13)
        self.fingers["r4"].grid(row=y, column=x+15)
        self.fingers["r5"].grid(row=y, column=x+17)

    def show_chord(self, chord):
        """
        Display a chord.

        chord is a dict.
        Layer indicates which layer this key is on - display
        what color the light should be.
        Finger1 (str) indicates first finger to be active.
        Finger2 (str) indicates second finger to be actite.
        Finger 1 & 2 can have the same value if it's a single-fingered
        chord.
        """
        # TODO: implement layer indication
        self.show_finger(chord["Finger1"])
        self.show_finger(chord["Finger2"])

    def reset(self):
        """Reset hands."""
        for finger in self.fingers:
            self.fingers[finger]["bg"] = "white"

    def show_finger(self, finger):
        """Color a finger red."""
        self.fingers[finger]["bg"] = "red"

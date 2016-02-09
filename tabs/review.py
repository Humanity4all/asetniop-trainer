"""Review tab."""

import Tkinter as gui

from config.config import CONFIG
from tools.colorlog import log
from tools.localize import _
from trainingelements.hands import Hands
from trainingelements.assignmentselection import AssignmentSelection


class Review(object):

    """Review tab."""

    def __init__(self, master):
        """Draw Review tab."""
        self.frame = gui.Frame(master, bd=1)
        self.title = gui.Label(
            self.frame,
            text=_("Review"),
            font=CONFIG.h1_font)
        self.title.grid(row=1, column=5, sticky=gui.W, columnspan=10)

        # show hands to help out with errors
        self.hands = Hands(self.frame, 2, 2)

        self.assignment_list = []
        # Show what to type (relic from old version)
        # self.assignment = gui.Label(
        #    self.frame,
        #    text="A",
        #    bg="white",
        #    font=CONFIG.very_large_font)
        # self.assignment.grid(row=7, column=11)

        # Select assignment
        self.assignment_selection = gui.Frame(self.frame)
        self.assignment_selection.grid(row=2, column=25, rowspan=30)

        self.assignment_window = AssignmentSelection(
            self.assignment_selection,
            self.set_assignment)

        # Make frame visible
        self.frame.grid(row=2, column=1, rowspan=15, columnspan=9)

    def set_assignment(self, assignment_list):
        """Receive the assignment_list and start exercise."""
        self.assignment_list = assignment_list
        # TODO: start the actual assignment

    def destroy(self):
        """Remove frame."""
        log("info", "Destroying review frame")
        self.frame.grid_remove()
        self.frame.grid_forget()
        self.frame.destroy()

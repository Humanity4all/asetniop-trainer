"""Frame that allows user to select an assignment."""

import Tkinter as gui

from config.config import CONFIG
from tools.localize import _
from tools.colorlog import log


class AssignmentSelection(object):

    """Frame that allows user to select an assignment."""

    def __init__(self, frame, return_assignment):
        """Build assignment selection frame."""
        self.frame = frame
        # this is a pointer to the method we have to call if an
        # assignment is picked.
        self.return_assignment = return_assignment

        # hack to get a scrollbar
        self.canvas = gui.Canvas(self.frame)
        self.inner_frame = gui.Frame(self.canvas)
        self.scrollbar = gui.Scrollbar(
            self.frame,
            orient="vertical",
            command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", self.scroll)

        self.title = gui.Label(
            self.inner_frame,
            text=_("Pick an assignment"),
            font=CONFIG.h2_font)
        self.title.grid(row=1, column=1, columnspan=4)

        self.buttons = {}

        # wordlist exercises
        self.buttons['wl-english'] = gui.Button(
            self.inner_frame,
            text=_("Random words (english)"),
            command=lambda: self.set_assignment("wl-english"))
        self.buttons['wl-english'].grid(row=2, column=1)

        self.buttons['wl-dutch'] = gui.Button(
            self.inner_frame,
            text=_("Random words (dutch)"),
            command=lambda: self.set_assignment("wl-dutch"))
        self.buttons['wl-dutch'].grid(row=3, column=1)

        # exercises from exercises directory
        # TODO: fetch exercises from file

    def set_assignment(self, assignment):
        """Fetch the actual assignment data."""
        assignment_list = []
        if assignment == "wl-english":
            # make assignment out of english wordlist
            pass
        elif assignment == "wl-dutch":
            # make assignment out of dutch wordlist
            pass
        elif assignment.startswith("file-"):
            # fetch assignment from file
            pass
        else:
            # unknown assignment
            log("error", "AssignmentSelection: unknown assignment.")
        self.return_assignment(assignment_list)

    def scroll(self, _):
        """Scroll the assignment selection frame."""
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all"),
            width=250,
            height=800)

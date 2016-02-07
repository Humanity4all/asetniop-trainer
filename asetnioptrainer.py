"""Train chord typing."""

import Tkinter as gui
import tkFont
import os

from config.config import CONFIG
from tools.colorlog import LOGLEVEL, log
from tools.localize import _

from tabs.home import Home
from tabs.learn import Learn
from tabs.review import Review
from tabs.stats import Stats
from tabs.settings import Settings
from tabs.help import Help

# pylint: disable=invalid-name
LOGLEVEL.set_level(CONFIG.log_level)
localepath = os.path.join(os.getcwd(), "locale")


class AsetniopTrainer(object):

    """Train chord typing."""

    def __init__(self, master):
        """Draw main window."""
        self.master = master

        # current tab
        self.active_tab = Home(master)

        # menu frame + buttons
        self.menu = gui.Frame(master, bd=1)
        self.menu.grid(row=1, column=1, columnspan=30, sticky=gui.W)
        self.buttons = {}
        self.buttons['home'] = gui.Button(
            self.menu,
            text=_("Home"),
            command=self.home)
        self.buttons['home'].grid(row=1, column=1)
        self.buttons['learn'] = gui.Button(
            self.menu,
            text=_("Learn"),
            command=self.learn)
        self.buttons['learn'].grid(row=1, column=2)
        self.buttons['review'] = gui.Button(
            self.menu,
            text=_("Review"),
            command=self.review)
        self.buttons['review'].grid(row=1, column=3)
        self.buttons['stats'] = gui.Button(
            self.menu,
            text=_("Statistics"),
            command=self.stats)
        self.buttons['stats'].grid(row=1, column=4)
        self.buttons['settings'] = gui.Button(
            self.menu,
            text=_("Settings"),
            command=self.settings)
        self.buttons['settings'].grid(row=1, column=5)
        self.buttons['help'] = gui.Button(
            self.menu,
            text=_("Help"),
            command=self.help_)
        self.buttons['help'].grid(row=1, column=6)
        self.buttons['quit'] = gui.Button(
            self.menu,
            text=_("Quit"),
            command=self.quit)
        self.buttons['quit'].grid(row=1, column=7)

    def home(self):
        """Switch to home tab."""
        log("info", "Switch to home tab.")
        self.active_tab = Home(self.master)

    def learn(self):
        """Switch to learn tab."""
        log("info", "Switch to learn tab.")
        self.active_tab = Learn(self.master)

    def review(self):
        """Switch to review tab."""
        log("info", "Switch to review tab.")
        self.active_tab = Review(self.master)

    def stats(self):
        """Switch to stats tab."""
        log("info", "Switch to stats tab.")
        self.active_tab = Stats(self.master)

    def settings(self):
        """Switch to settings tab."""
        log("info", "Switch to settings tab.")
        self.active_tab = Settings(self.master)

    def help_(self):
        """Switch to help tab."""
        log("info", "Switch to help tab.")
        self.active_tab = Help(self.master)

    def quit(self):
        """Exit application."""
        log("info", "Exit application.")
        del self.active_tab
        self.master.quit()

if __name__ == "__main__":
    root = gui.Tk()

    # Fonts can't be created prior to the root object,
    # so we do so here.
    CONFIG.large_font = tkFont.Font(family="Arial", size=30)
    CONFIG.very_large_font = tkFont.Font(family="Arial", size=100)
    asetniop_trainer = AsetniopTrainer(root)

    root.mainloop()
    root.destroy()

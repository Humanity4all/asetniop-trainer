"""Global configuration."""
import configparser
import os


class Config(object):

    """Manage global configuration."""

    def __init__(self):
        """Fetch config from config file."""
        # TODO: fetch config from config file
        self.log_level = "verbose"
        self.locale_path = os.path.join(os.getcwd(), "locale")
        self.language = "nl"
        # Fonts can't be created prior to the tk root object,
        # so there are just stubs that asetnioptrainer.py will fill.
        self.large_font = None
        self.very_large_font = None

CONFIG = Config()

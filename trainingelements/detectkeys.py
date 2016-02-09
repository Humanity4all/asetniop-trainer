"""Bind keys and hanle key events."""
import string


class DetectKeys(object):

    """Bind keys and handle key events."""

    def __init__(self, element, callback):
        """Bind keys."""
        # TODO: use key_t enum instead of charstring
        self.callback = callback
        self.bindings = {}
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        chars += "0123456789"
        chars += "!@#$%^&*()"
        chars += "+=\\/|?-_`~[{]}'\";:,<.>"

        for char in chars:
            if char == "<":
                self.bindings[char] = element.bind(
                    '<less>',
                    lambda e: self.key("<"))
            elif char in string.whitespace:
                self.bindings[char] = element.bind(
                    '<space>',
                    lambda e: self.key(" "))
            elif char.isupper():
                self.bindings[char] = element.bind(
                    '<Shift-'+char.tolower()+'>',
                    lambda e, q=char: self.key(q))
            else:
                self.bindings[char] = element.bind(
                    char,
                    lambda e, q=char: self.key(q))

    def key(self, char):
        """Call callback."""
        self.callback(char)

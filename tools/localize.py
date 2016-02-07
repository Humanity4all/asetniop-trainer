"""Provide localization."""

import gettext

from config.config import CONFIG

TRANSLATOR = gettext.translation(
    CONFIG.language,
    CONFIG.locale_path,
    fallback=True)

_ = TRANSLATOR.ugettext

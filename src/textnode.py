#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# =========================================

# ---- dependencies {{{
from enum import Enum
#}}}

# --- support methods --- {{{
class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not self.text == other.text: return False
        if not self.text_type == other.text_type: return False
        if not self.url == other.url: return False
        return True

    def __repr__(self):
        text = self.text
        text_type = self.text_type
        url = self.url
        return f"TextNode({text}, {text_type}, {url})"


# }}}

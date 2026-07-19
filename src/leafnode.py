#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# =========================================

# ---- dependencies {{{
from htmlnode import HTMLNode
#}}}

# --- support methods --- {{{
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super(LeafNode, self).__init__(tag, value, None, props)

    def __eq__(self, other):
        if not self.tag == other.tag: return False
        if not self.value == other.value: return False
        if not self.props == other.props: return False
        return True

    def to_html(self):
        if not self.value: raise ValueError
        if not self.tag: return self.value
        if self.tag == "p":
            return f"<p>{self.value}</p>"
        if self.tag == "h1":
            return f"# {self.value}\n"
        if self.tag == "a":
            link = self.props["href"]
            return f'<a href="{link}">{self.value}</a>'

    def __repr__(self):
        if self.tag: return self.tag
        if self.value: self.value
        if self.props: self.props
        return "Empty HTMLNode object"

# }}}

#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# =========================================

# ---- dependencies {{{
import unittest
from textnode import TextNode, TextType
#}}}

# --- support methods --- {{{
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def assertEqual(self, a, b):
        assert a.text == b.text
        assert a.text_type == b.text_type
        assert a.url == b.url

    def assertNotEqual(self, a, b):
        assert a.text != b.text
        assert a.text_type != b.text_type
        assert a.url != b.url
# }}}

# --- main --- {{{
if __name__ == "__main__":
    unittest.main()
# }}}

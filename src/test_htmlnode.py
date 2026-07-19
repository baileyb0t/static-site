#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# =========================================

# ---- dependencies {{{
import unittest
from htmlnode import HTMLNode
#}}}

# --- support methods --- {{{
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="h1", value="Howdy, ma'am.")
        node2 = HTMLNode(tag="h1", value="Howdy, ma'am.")
        self.assertEqual(node, node2)

    def assertEqual(self, a, b):
        assert a.tag == b.tag
        assert a.value == b.value
        if a.children:
            assert set(a.children).equals(b.children)
        if a.props:
            assert len(a.props.keys()) == len(b.props.keys())
            for k,v in a.props.items():
                assert k in b.props.keys()
                assert props[k] == v

    def assertNotEqual(self, a, b):
        assert a.tag != b.tag
        assert a.value != b.value
        if a.children:
            assert not set(a.children).equals(b.children)
        if a.props:
            assert len(a.props.keys()) != len(b.props.keys())
            for k,v in a.props.items():
                assert k not in b.props.keys()
                assert props[k] != v
# }}}

# --- main --- {{{
if __name__ == "__main__":
    unittest.main()
# }}}

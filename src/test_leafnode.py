#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# =========================================

# ---- dependencies {{{
import unittest
from leafnode import LeafNode
#}}}

# --- support methods --- {{{
class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="h1", value="Howdy, ma'am.")
        node2 = LeafNode(tag="h1", value="Howdy, ma'am.")
        self.assertEqual(node, node2)
        print(node)
        print(node2)

    def assertEqual(self, a, b):
        assert a == b
        #assert a.tag == b.tag
        #assert a.value == b.value
        #if a.props:
        #    assert len(a.props.keys()) == len(b.props.keys())
        #    for k,v in a.props.items():
        #        assert k in b.props.keys()
        #        assert props[k] == v

    def assertNotEqual(self, a, b):
        assert a.tag != b.tag
        assert a.value != b.value
        if a.props:
            assert len(a.props.keys()) != len(b.props.keys())
            for k,v in a.props.items():
                assert k not in b.props.keys()
                assert props[k] != v

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
# }}}

# --- main --- {{{
if __name__ == "__main__":
    unittest.main()
# }}}

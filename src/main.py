#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# =========================================

# ---- dependencies {{{
import sys

sys.path.append("src")
from textnode import TextNode
#}}}

# --- support methods --- {{{
def main():
    dummy = TextNode(
        text="OOOOOhhhhh who lives in a pineapple under the sea",
        text_type="bold"
    )
    print(dummy)
# }}}

# --- main --- {{{
if __name__ == '__main__':
    main()
# }}}

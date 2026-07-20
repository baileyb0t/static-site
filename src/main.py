#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# =========================================

# ---- dependencies {{{
from os.path import exists

from copystatic import copycontents
from pages import generate_pages_recursive

# }}}


# --- support methods --- {{{
def main():
    if exists("static"):
        copycontents("static", "public")

    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="public",
    )


# }}}

# --- main --- {{{
if __name__ == "__main__":
    main()
# }}}

#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# =========================================


from multiprocessing import Value


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if not self.tag == other.tag:
            return False
        if not self.value == other.value:
            return False
        if not self.children:
            if other.children:
                return False
        if not len(self.children) == len(other.children):
            return False
        if not all([sc in other.children for sc in self.children]):
            return False
        if not self.props == other.props:
            return False
        return True

    def to_html(self):
        if self.tag is None:
            return self.value if self.value is not None else ""

        html_parts = []
        html_parts.append(f"<{self.tag}")
        for prop, value in self.props.items():
            html_parts.append(f' {prop}="{value}"')
        html_parts.append(">")

        if self.value is not None:
            html_parts.append(self.value)
        else:
            for child in self.children:
                html_parts.append(child.to_html())
        html_parts.append(f"</{self.tag}>")

        return "".join(html_parts)

    def props_to_html(self):
        out = ""
        for k, v in props.items():
            out += f' {k}="{v}"'
        return out

    def __repr__(self):
        if self.tag:
            print(self.tag)
        if self.value:
            print(self.value)
        if self.children:
            print(self.children)
        if self.props:
            print(self.props)
        print("Empty HTMLNode object")


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children, props: None):
        self.tag = tag
        self.children = children

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag found")
        if not self.children:
            raise ValueError("No children found")
        return super().to_html()

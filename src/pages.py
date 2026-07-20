import os
from pathlib import Path
from tempfile import template

from htmlnode import HTMLNode
from inline_markdown import extract_title
from markdown_blocks import markdown_to_html_node


def readtextlike(path) -> str:
    with open(path, "r") as f:
        lines = f.readlines()
    return "\n".join(lines)


def writehtml(path, data) -> str:
    with open(path, "w") as f:
        f.write(data)
    return 1


def getfiles(arg, fext="*"):
    assert os.path.isdir(arg)
    return [path for path in Path(arg).rglob(f"*.{fext}")]


def generate_page(from_path, template_path, dest_path):
    print("\n\n", readtextlike(from_path)[:100])
    md = readtextlike(from_path)
    print("\n\n", markdown_to_html_node(md))
    print("\n\n", extract_title(md), "\n\n")
    template = readtextlike(template_path)
    node = markdown_to_html_node(md)
    html = node.to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    writehtml(dest_path, template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    found = getfiles(dir_path_content)
    for file in found:
        newstub = file.name.replace("md", "html")
        destpath = f"{dest_dir_path}/"
        destpath += "/".join([part for part in Path(file).parts[1:] if "." not in part])
        os.makedirs(destpath, exist_ok=True)
        destpath += "/" + newstub
        msg = f"Generating page from {file} to {destpath} using {template_path}"
        print(msg)
        generate_page(from_path=file, template_path=template_path, dest_path=destpath)

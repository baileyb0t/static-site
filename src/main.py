#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# Maintainers: BP
# =========================================

import os
import shutil
import sys

from loguru import logger

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def setuplogging(logfile):
    logger.add(
        logfile,
        colorize=True,
        format="<green>{time:YYYY-MM-DD⋅at⋅HH:mm:ss}</green>⋅<level>{message}</level>",
        level="INFO",
    )
    return 1


def main() -> None:
    setuplogging("logs/main.log")
    logger.info("--- START ----")

    logger.info(f"processing arguments `{sys.argv}`")
    args = sys.argv
    if len(args) == 1:
        basepath = "/"
    else:
        basepath = args[1]
    logger.info(f"Identified base directory {basepath}")

    logger.info(f"Deleting public directory {dir_path_public}")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    logger.info(
        f"Copying static files from {dir_path_static} to destination {dir_path_public}"
    )
    copy_files_recursive(dir_path_static, dir_path_public)

    logger.info(
        f"Generating content from {dir_path_content} to destination {dir_path_public}"
    )
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

    logger.info("--- DONE ----")


main()

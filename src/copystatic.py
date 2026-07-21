import os
import shutil

from loguru import logger


def setuplogging(logfile):
    logger.add(
        logfile,
        colorize=True,
        format="<green>{time:YYYY-MM-DD⋅at⋅HH:mm:ss}</green>⋅<level>{message}</level>",
        level="INFO",
    )
    return 1


def copy_files_recursive(source_dir_path: str, dest_dir_path: str) -> None:
    setuplogging("logs/copystatic.log")
    logger.info(f"checking for existing destination {dest_dir_path}")
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    logger.info(f"checking for files from source {source_dir_path}")
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        logger.info(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

import os
import shutil
import subprocess
from pathlib import Path


def getfiles(arg, fext="*"):
    return [path for path in Path(arg).rglob(f"*.{fext}")]


def copycontents(srcdir, destdir):
    # if not os.path.exists(srcdir):
    #    print(f"Source directory path does not exist: {srcdir}")
    #    return
    found = getfiles(srcdir)
    if os.path.exists(destdir):
        if any(getfiles(destdir)):
            subprocess.call(["rm", "-r", f"{destdir}/*"])
    else:
        os.mkdir(destdir)
    for file in found:
        nested = file.parts[1:-1]
        newpath = f"{destdir}/"
        newpath += "/".join(nested)
        os.makedirs(newpath, exist_ok=True)
        newpath += "/" + file.name
        shutil.copy(file, newpath)
    shutil.rmtree(srcdir)

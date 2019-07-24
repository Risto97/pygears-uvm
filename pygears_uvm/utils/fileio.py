from pygears.util.fileio import save_file
from pathlib import Path
import os

def save_if_nexist(fn, outdir, content):
    file_path = os.path.join(outdir, fn)
    if os.path.exists(file_path):
        pass
    else:
        save_file(fn, outdir, content)
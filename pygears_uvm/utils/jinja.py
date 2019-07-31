import jinja2
import os
from pygears.util.fileio import save_file
from pygears_uvm.utils.fileio import save_if_nexist
from pathlib import Path
import importlib

def gen_file(template_fn, out_fn, outdir, context, overwrite=True):
    template_dir = importlib.machinery.PathFinder().find_spec("pygears_uvm")
    template_dir = template_dir.submodule_search_locations[0]
    template_dir = os.path.join(template_dir, "templates")

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True)

    res = env.get_template(template_fn).render(context)

    if overwrite:
        save_file(out_fn, outdir, res)
    else:
        save_if_nexist(out_fn, outdir, res)

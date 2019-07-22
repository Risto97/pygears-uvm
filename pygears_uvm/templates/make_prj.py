import jinja2
from pygears.util.fileio import save_file
import os
from pathlib import Path

class Make_Prj:
    def __init__(self, dut, prjdir):
        self.dut = dut
        self.prjdir = prjdir
        self.fn = "Makefile"

    @property
    def rtldir(self):
        return os.path.join(self.prjdir, "rtl")

    @property
    def outdir(self):
        return self.prjdir

    def create_files(self):
        template_dir = Path(__file__).resolve().parent.__str__()
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)

        context = {'dut': self.dut}
        res = env.get_template('make_prj.j2').render(context)
        save_file(f"Makefile", self.outdir, res)

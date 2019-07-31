import jinja2
from pygears.util.fileio import save_file
from pygears_uvm.utils.jinja import gen_file
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
        context = {}
        gen_file("make_prj.j2", "Makefile", self.outdir, context)

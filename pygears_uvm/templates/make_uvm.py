import jinja2
from pygears.util.fileio import save_file
from pygears_uvm.utils.jinja import gen_file
import os
from pathlib import Path

import importlib


class Make_UVM:
    def __init__(self, dut, prjdir):
        self.dut = dut
        self.prjdir = prjdir
        self.fn = "Makefile"

    @property
    def rtldir(self):
        return os.path.join("..", "rtl")

    @property
    def outdir(self):
        return os.path.join(self.prjdir, "uvm")

    def create_files(self):
        pygears_uvm_dir = importlib.machinery.PathFinder().find_spec(
            "pygears_uvm")
        pygears_uvm_dir = pygears_uvm_dir.submodule_search_locations[0]

        context = {
            'dut': self.dut,
            'rtldir': self.rtldir,
            'pygears_uvm_dir': pygears_uvm_dir
        }

        try:
            os.environ['SYSTEMC']
            os.environ['SYSTEMC_UVM']
        except:
            raise EnvironmentError("Please set your environment variables")

        gen_file("make_uvm.j2", "Makefile", self.outdir, context)

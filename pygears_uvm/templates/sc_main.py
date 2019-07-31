from pygears_uvm.templates.dut import DUT
from pygears.util.fileio import save_file
from pygears_uvm.utils.jinja import gen_file
import jinja2
import os
from pathlib import Path

from pygears_uvm.templates.env import Env


class SC_Main:
    def __init__(self, prjdir, dut):
        self.dut = DUT(dut.basename, dut)
        self.outdir = os.path.join(prjdir, "uvm")

    def create_files(self):
        context = {'dut': self.dut}

        gen_file("sc_main.j2", "sc_main.cpp", self.outdir, context)

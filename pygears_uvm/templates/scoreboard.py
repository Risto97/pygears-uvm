import jinja2
from pygears.util.fileio import save_file
from pygears_uvm.utils.jinja import gen_file
from pathlib import Path
import os
from pygears_uvm.utils.fileio import save_if_nexist

from pygears.typing.queue import QueueMeta
from pygears.typing.uint import UintType, IntType
from pygears_uvm.templates.dut import DUT
from pygears.typing.queue import QueueMeta
from pygears.typing.uint import UintType, IntType


class Scoreboard:
    def __init__(self, intfs=None, prjdir=None, dut=None, name="scoreboard"):
        self.name = name
        self.prjdir = prjdir
        self.dut = DUT(dut=dut)
        self.fn = self.name + ".hpp"

        if intfs is None:
            self.intfs = self.dut.intfs
        else:
            self.intfs = intfs

    @property
    def outdir(self):
        return os.path.join(self.prjdir, "uvm")

    def create_files(self):
        context = {"sb": self}

        gen_file("scoreboard.j2", "scoreboard.hpp", self.outdir, context)

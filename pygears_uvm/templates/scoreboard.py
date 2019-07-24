import jinja2
from pygears.util.fileio import save_file
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
        template_dir = Path(__file__).resolve().parent.__str__()
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True)

        context = {"sb": self}
        res_hpp = env.get_template('scoreboard.j2').render(context)
        # res_cpp = env.get_template('sequence_cpp.j2').render(context)
        save_file(f"{self.name}.hpp", self.outdir, res_hpp)
        # save_file(f"{self.name}.cpp", self.outdir, res_cpp)
        # save_if_nexist(f"{self.name}.cpp", self.outdir, res_cpp)

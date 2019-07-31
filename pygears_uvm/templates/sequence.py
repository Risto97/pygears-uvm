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


class Sequence:
    def __init__(self, intf=None, prjdir=None, dut=None):
        self.intf = intf
        self.name = self.intf.basename + "_sequence"
        self.prjdir = prjdir
        self.dut = DUT(dut=dut)
        self.fn = self.name + ".hpp"

    def seq_var_type(self):
        seq_t = ""
        data_t = "unsigned int"

        if self.is_queue:
            for i in range(self.intf.dtype.lvl):
                seq_t += "std::vector<"
            seq_t += data_t
            seq_t += (i + 1) * "> "
        elif self.is_uint:
            seq_t = "std::vector<unsigned int>"
        elif self.is_int:
            seq_t = "std::vector<int>"

        return seq_t

    @property
    def is_queue(self):
        return isinstance(self.intf.dtype, QueueMeta)

    @property
    def queue_lvl(self):
        if self.is_queue:
            return self.intf.dtype.lvl
        else:
            return 0

    @property
    def is_integer(self):
        return self.is_uint or self.is_int

    @property
    def is_uint(self):
        return isinstance(self.intf.dtype, UintType)

    @property
    def is_int(self):
        return isinstance(self.intf.dtype, IntType)

    @property
    def outdir(self):
        return os.path.join(self.prjdir, "uvm")

    def create_files(self):
        context = {"seq": self}

        gen_file("sequence.j2", f"{self.name}.hpp", self.outdir, context)
        gen_file("sequence_cpp.j2",
                 f"{self.name}.cpp",
                 self.outdir,
                 context,
                 overwrite=False)

import jinja2
from pygears.util.fileio import save_file
from pygears_uvm.utils.jinja import gen_file
from pathlib import Path
import os

from pygears_uvm.templates.dut import DUT
from pygears_uvm.templates.sequence import Sequence

from pygears.typing.queue import QueueMeta
from pygears.typing.uint import UintType, IntType


class Env:
    def __init__(self, prjdir, dut=None):
        self.dut = DUT(dut.basename, dut)
        self.hdr_files = [
            "dti_vif.hpp", "dti_packet.hpp", "dti_agent.hpp", "data_types.hpp"
        ]
        self.outdir = os.path.join(prjdir, "uvm")
        self.din_seq = Sequence(intf=self.dut.in_ports[0],
                                prjdir=None,
                                dut=dut)

    def create_files(self):
        context = {
            'hdr_files': self.hdr_files,
            'ports': self.dut.intfs,
            'dut': self.dut,
            'env': self
        }
        gen_file("env.j2", "env.hpp", self.outdir, context)

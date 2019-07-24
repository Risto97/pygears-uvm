import jinja2
from pygears.util.fileio import save_file
from pathlib import Path

from pygears_uvm.templates.dut import DUT
from pygears_uvm.templates.sequence import Sequence

from pygears.typing.queue import QueueMeta
from pygears.typing.uint import UintType, IntType

class Env:
    def __init__(self, name='env', dut=None):
        self.name = name
        self.dut = DUT(dut.basename, dut)

        self.hdr_files = ["dti_vif.hpp", "dti_packet.hpp", "dti_agent.hpp", "data_types.hpp"]
        self.fn = "env.hpp"

        self.din_seq = Sequence(intf=self.dut.in_ports[0], prjdir=None, dut=dut)

    def create_files(self, outdir):
        template_dir = Path(__file__).resolve().parent.__str__()
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)

        context = {'hdr_files': self.hdr_files, 'ports': self.dut.intfs, 'dut': self.dut, 'env': self}
        res = env.get_template('env.j2').render(context)
        save_file(f"{self.fn}", outdir, res)

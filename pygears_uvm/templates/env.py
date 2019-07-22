import jinja2
from pygears.util.fileio import save_file
from pathlib import Path

from pygears.typing.queue import QueueMeta
from pygears.typing.uint import UintType, IntType

class DUT:
    def __init__(self, name='dflt', dut=None):
        self.dut = dut
        self.name = self.dut.basename

    @property
    def intfs(self):
        ports = []
        for p in self.in_ports:
            ports.append(p)
        for p in self.out_ports:
            ports.append(p)
        return ports

    @property
    def out_ports(self):
        ports = []
        for port in self.dut.out_ports:
            ports.append(port)
        return ports

    @property
    def in_ports(self):
        ports = []
        for port in self.dut.in_ports:
            ports.append(port)
        # print(ports)
        return ports

    def agent_type(self, intf):
        if intf.direction == "in":
            return "producer"
        elif intf.direction == "out":
            return "consumer"

    def packet_type_str(self, intf):
        if isinstance(intf.dtype, QueueMeta):
            if isinstance(intf.dtype.data, UintType):
                data_type = "sc_uint"
            elif isinstance(intf.dtype.data, IntType):
                data_type = "sc_int"

            return f"dti_packet<queue_type<sc_dt::{data_type}<{self.intf_data_w(intf)}>, {self.intf_eot_lvl(intf)}> >"

    def intf_eot_lvl(self, intf):
        if isinstance(intf.dtype, QueueMeta):
            eot_lvl = intf.dtype.lvl
            return eot_lvl

    def intf_data_w(self, intf):
        if isinstance(intf.dtype, QueueMeta):
            data_w = len(intf.dtype.data)
            return data_w

    def intf_w(self, intf):
        if isinstance(intf.dtype, QueueMeta):
            data_w = len(intf.dtype.data)
            eot_lvl = intf.dtype.lvl
            return data_w+eot_lvl

class Env:
    def __init__(self, name='env', dut=None):
        self.name = name
        self.dut = DUT(dut.basename, dut)

        self.hdr_files = ["dti_vif.hpp", "dti_packet.hpp", "dti_agent.hpp", "dti_sequence.hpp", "data_types.hpp"]
        self.fn = "env.hpp"

    def create_files(self, outdir):
        template_dir = Path(__file__).resolve().parent.__str__()
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)

        context = {'hdr_files': self.hdr_files, 'ports': self.dut.intfs, 'dut': self.dut}
        res = env.get_template('env.j2').render(context)
        save_file(f"{self.fn}", outdir, res)


# din = Intf(Queue[Uint[8], 2])

# din | ii_gen(frame_size=(5, 5))

# root = registry('gear/hier_root')
# top = root.child[0]

# env = Env('env', top)
# print(env.dut.intfs)

# env.create_files("../build")

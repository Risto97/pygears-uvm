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

        elif isinstance(intf.dtype, UintType) or isinstance(intf.dtype, IntType):
            if isinstance(intf.dtype, UintType):
                data_type = "sc_uint"
            elif isinstance(intf.dtype, IntType):
                data_type = "sc_int"

            return f"dti_packet<integer_type<sc_dt::{data_type}<{self.intf_w(intf)}> > >"





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
            return data_w + eot_lvl
        elif isinstance(intf.dtype, UintType) or isinstance(intf.dtype, IntType):
            return len(intf.dtype)

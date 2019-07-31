from pygears_uvm.core.dut import DUT
from pygears_uvm.utils.jinja import gen_file
from pygears_uvm.utils.hdlgen import hdlgen_wspy, delete_tracing_off
from pygears_uvm.templates.sequence import Sequence
import importlib
import os


class UVM:
    def __init__(self, prjdir, dut):
        self.dut = DUT(dut)
        self.prjdir = prjdir
        self.rtldir = os.path.join(self.prjdir, "rtl")
        self.uvmdir = os.path.join(self.prjdir, "uvm")
        self.language = "sv"

        self.sequences = []
        for intf in dut.in_ports:
            self.sequences.append(Sequence(intf=intf))

        self.hdr_files = [
            "dti_vif.hpp", "dti_packet.hpp", "dti_agent.hpp", "data_types.hpp"
        ]

        try:
            os.environ['SYSTEMC']
            os.environ['SYSTEMC_UVM']
        except:
            raise EnvironmentError("Please set your environment variables")

    @property
    def pygears_uvm_dir(self):
        pygears_uvm_dir = importlib.machinery.PathFinder().find_spec(
            "pygears_uvm")
        return pygears_uvm_dir.submodule_search_locations[0]

    def hdlgen(self):
        v_dir = os.path.join(self.rtldir, "src")
        hdlgen_wspy(v_dir, self.dut)
        delete_tracing_off(v_dir, self.dut)

    def create_files(self):
        context = {'uvm': self, 'ports': self.dut.intfs}

        gen_file("sc_main.j2", "sc_main.cpp", self.uvmdir, context)

        gen_file("make_prj.j2", "Makefile", self.prjdir, context)
        gen_file("make_rtl.j2", "Makefile", self.rtldir, context)
        gen_file("make_uvm.j2", "Makefile", self.uvmdir, context)
        gen_file("scoreboard.j2", "scoreboard.hpp", self.uvmdir, context)

        for sequence in self.sequences:
            ctxt = {"seq": sequence, "uvm": self}
            gen_file("sequence.j2", f"{sequence.name}.hpp", self.uvmdir, ctxt)
            gen_file("sequence_cpp.j2",
                     f"{sequence.name}.cpp",
                     self.uvmdir,
                     ctxt,
                     overwrite=False)

        gen_file("env.j2", "env.hpp", self.uvmdir, context)

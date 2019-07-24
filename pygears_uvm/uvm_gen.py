from pygears_uvm.templates.make_prj import Make_Prj
from pygears_uvm.templates.make_uvm import Make_UVM
from pygears_uvm.templates.make_rtl import Make_RTL
from pygears_uvm.templates.sc_main import SC_Main
from pygears_uvm.templates.sequence import Sequence

from pygears.conf.registry import registry

import subprocess
import os


def clang_format(dir):
    dir = os.path.abspath(dir)
    for root, dirs, files in os.walk(dir):
        for file in files:
            file = os.path.join(root, file)
            if file.endswith(".hpp") or file.endswith(".cpp"):
                subprocess.check_call(['clang-format', '-i', file])


def uvm_gen(prjdir):
    root = registry('gear/hier_root')
    top = root.child[0]

    rtl = Make_RTL(top, prjdir=prjdir, language='sv')
    rtl.hdlgen()
    rtl.create_files()
    rtl.delete_tracing_off()

    din_seq = Sequence(intf=top.in_ports[0], prjdir=prjdir, dut=top)
    din_seq.create_files()


    uvm = Make_UVM(top, prjdir=prjdir)
    uvm.create_files()

    prj = Make_Prj(top, prjdir=prjdir)
    prj.create_files()

    sc_main = SC_Main(prjdir=prjdir, dut=top)
    sc_main.create_files()

    try:
        clang_format(os.path.join(prjdir, "uvm"))
    except:
        print("Install clang-format for c++ formatting")

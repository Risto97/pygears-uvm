from pygears_uvm.templates.make_prj import Make_Prj
from pygears_uvm.templates.make_uvm import Make_UVM
from pygears_uvm.templates.make_rtl import Make_RTL
from pygears_uvm.templates.sc_main import SC_Main
from pygears_uvm.templates.env import Env
from pygears_uvm.templates.sequence import Sequence
from pygears_uvm.templates.scoreboard import Scoreboard

from pygears.conf.registry import registry

import subprocess
import os

from pygears_uvm.templates.uvm import UVM

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

    uvm = UVM(prjdir=prjdir, dut=top)
    uvm.hdlgen()
    uvm.create_files()

from pygears_uvm.core.uvm import UVM

from pygears.conf.registry import registry

from pygears_uvm.utils.clang_format import clang_format


def uvm_gen(prjdir):
    root = registry('gear/hier_root')
    top = root.child[0]

    uvm = UVM(prjdir=prjdir, dut=top)
    uvm.hdlgen()
    uvm.create_files()

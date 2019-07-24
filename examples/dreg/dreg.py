from pygears_uvm.uvm_gen import uvm_gen

from pygears.lib import dreg
from pygears import Intf
from pygears.typing import Queue, Uint


din = Intf(Queue[Uint[8], 2])

din | dreg()

uvm_gen("uvm")

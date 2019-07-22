from pygears_uvm.uvm_gen import uvm_gen

from cascade_classifier.pygears_impl.design import ii_gen
from pygears import Intf
from pygears.typing import Queue, Uint


din = Intf(Queue[Uint[8], 2])

din | ii_gen(frame_size=(5, 5))

uvm_gen("uvm")

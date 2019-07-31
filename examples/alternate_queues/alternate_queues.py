from pygears_uvm.uvm_gen import uvm_gen

from pygears.lib import alternate_queues
from pygears import Intf
from pygears.typing import Queue, Uint


din1 = Intf(Queue[Uint[8], 1])
din2 = Intf(Queue[Uint[8], 1])

alternate_queues(din1, din2)

uvm_gen("uvm")

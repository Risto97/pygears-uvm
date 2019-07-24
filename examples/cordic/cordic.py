from pygears_uvm.uvm_gen import uvm_gen

from pygears.lib import cordic_sin_cos
from pygears import Intf
from pygears.typing import Queue, Uint

pw = 16
iw = 12
ow = 12

din = Intf(Uint[pw])

din | cordic_sin_cos(ow=ow, iw=iw, norm_gain_sin=True, norm_gain_cos=True)

uvm_gen("uvm")

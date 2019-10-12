from pygears.hdl import hdlgen
from pygears.conf.registry import bind
import os

from string import Template
signal_spy_connect_t = Template("""
/*verilator tracing_on*/
${intf_name}_t ${intf_name}_data;
logic ${intf_name}_valid;
logic ${intf_name}_ready;
/*verilator tracing_off*/

assign ${intf_name}_data = ${conn_name}.data;
assign ${intf_name}_valid = ${conn_name}.valid;
assign ${intf_name}_ready = ${conn_name}.ready;
""")

def hdlgen_wspy(rtldir, dut):
    bind('debug/trace', [''])
    bind('svgen/spy_connection_template', signal_spy_connect_t)

    hdlgen(
        f"/{dut.name}",
        outdir=rtldir,
        wrapper=True,
        copy_files=True)

def delete_tracing_off(rtldir, dut):
    wrap_name = os.path.join(rtldir, f"wrap_{dut.name}.sv")

    with open(wrap_name, "r") as f:
        lines = f.readlines()
    with open(wrap_name, "w") as f:
        for line in lines[1:]:
            f.write(line)

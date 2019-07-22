import jinja2
from pygears.util.fileio import save_file
import os
from pathlib import Path

from pygears.hdl import hdlgen
from pygears.conf.registry import bind

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


class Make_RTL:
    def __init__(self, dut, prjdir, language='sv'):
        self.dut = dut
        self.language = language
        self.prjdir = prjdir
        self.fn = "Makefile"

    @property
    def outdir(self):
        return os.path.join(self.prjdir, "rtl")

    @property
    def rtldir(self):
        return os.path.join(self.outdir, "src")

    def create_files(self):
        template_dir = Path(__file__).resolve().parent.__str__()
        print(template_dir)
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True)

        context = {'dut': self.dut}
        res = env.get_template('make_rtl.j2').render(context)
        save_file(f"Makefile", self.outdir, res)

    def hdlgen(self):
        bind('hdl/debug_intfs', [''])
        bind('hdl/spy_connection_template', signal_spy_connect_t)

        hdlgen(
            f"/{self.dut.basename}",
            outdir=self.rtldir,
            wrapper=True,
            copy_files=True)

    def delete_tracing_off(self):
        wrap_name = os.path.join(self.rtldir, f"wrap_{self.dut.basename}.sv")

        with open(wrap_name, "r") as f:
            lines = f.readlines()
        with open(wrap_name, "w") as f:
            for line in lines[1:]:
                f.write(line)

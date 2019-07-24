import jinja2
from pygears.util.fileio import save_file
import os
from pathlib import Path


class Make_UVM:
    def __init__(self, dut, prjdir):
        self.dut = dut
        self.prjdir = prjdir
        self.fn = "Makefile"

    @property
    def rtldir(self):
        return os.path.join("..", "rtl")

    @property
    def outdir(self):
        return os.path.join(self.prjdir, "uvm")

    def create_files(self):
        template_dir = Path(__file__).resolve().parent.__str__()
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True)

        try:
            os.environ['SYSTEMC']
            os.environ['SYSTEMC_UVM']
            os.environ['PYGEARS_UVM']
        except:
            raise EnvironmentError("Please set your environment variables")

        context = {'dut': self.dut, 'rtldir': self.rtldir}
        res = env.get_template('make_uvm.j2').render(context)
        save_file(f"Makefile", self.outdir, res)

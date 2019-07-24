from pygears.util.fileio import save_file
import jinja2
import os
from pathlib import Path

from pygears_uvm.templates.env import Env


class SC_Main:
    def __init__(self, dut, prjdir, name='main'):
        self.env = Env('env', dut)
        self.fn = "sc_main.cpp"
        self.prjdir = prjdir

    def create_files(self):
        template_dir = Path(__file__).resolve().parent.__str__()
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True)

        outdir = os.path.join(self.prjdir, "uvm")

        context = {'dut': self.env.dut}
        res_main = env.get_template('sc_main.j2').render(context)
        save_file(self.fn, outdir, res_main)
        res_params = env.get_template('sim_params.j2').render(context)
        save_file("sim_params.hpp", outdir, res_params)

        self.env.create_files(outdir)

SystemC-UVM generator for PyGears components
============================================

Install
---------

Dependencies
~~~~~~~~~~~~
* [SystemC] Tested on version 2.3.3. You need to set **SYSTEMC** variable pointing to SystemC installation directory.
  And **LD\_LIBRARY\_PATH** poitnitg to **$SYSTEMC/lib-linux64**.
* [SystemC-UVM] Using public review beta version *UVM-SystemC Library 1.0-beta2*. Export **SYSTEMC\_UVM** variable to installed directory.
* [Verilator] Verilator should be present in system path. Version 4.016 is recommended. (4.012 not working)
* [PyGears] develop branch.

Install
~~~~~~~
* Clone `git clone https://github.com/Risto97/pygears_uvm.git`
* cd into cloned repository.
* `python setup.py develop`

Run example
~~~~~~~~~~~
* cd into example/cordic.
* `python cordic.py`
* `cd uvm`
* `make test`
* `gtkwave uvm/trace.vcd`

[SystemC]: https://www.accellera.org/downloads/standards/systemc
[SystemC-UVM]: https://www.accellera.org/downloads/drafts-review
[Verilator]: https://www.veripool.org/
[PyGears]: https://github.com/bogdanvuk/pygears/tree/develop

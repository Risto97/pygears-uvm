<a href="https://www.pygears.org/"><img src="https://www.pygears.org/_static/logo.png" title="FVCproductions" alt="PyGears"></a>

# PyGears-UVM

> SystemC-UVM generator for PyGears components.

---

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)

---


## Dependencies

- <a href="https://www.accellera.org/downloads/standards/systemc" target="_blank">**SystemC**</a> Tested on version 2.3.3. You need to set **SYSTEMC** variable pointing to SystemC installation directory.
  And **LD\_LIBRARY\_PATH** pointing to **$SYSTEMC/lib-linux64**.

- <a href="https://www.accellera.org/downloads/drafts-review" target="_blank">**SystemC-UVM**</a> Using public review beta version *UVM-SystemC Library 1.0-beta2*. Export **SYSTEMC\_UVM** variable to installed directory.

- <a href="https://www.veripool.org/" target="_blank">**Verilator**</a> Verilator should be present in system path. Version 4.016 is recommended. (4.012 is not working**.

- <a href="https://github.com/bogdanvuk/pygears/tree/develop" target="_blank">**PyGears**</a> develop branch.

- <a href="https://www.accellera.org/downloads/standards/systemc" target="_blank">**SystemC Verification**</a> for constraint randomization, export **SCV** variable to installed dir.

- <a href="https://github.com/amiq-consulting/fc4sc" target="_blank">**FC4SC**</a> Functional Coverage for SystemC from Amiq Consulting, export FC4SC variable to installed dir.

---

## Installation

- All the `code` required to get started
- Images of what it should look like

### Clone

- `git clone https://github.com/Risto97/pygears_uvm.git`

### Setup

- `python setup.py develop`

---

## Example

- cd into example/cordic
- `python cordic.py`
- `cd uvm`
- `make test`
- `gtkwave uvm/trace.vcd`

---

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/top.sv

TOPLEVEL := top
MODULE   := test_top

include $(shell cocotb-config --makefiles)/Makefile.sim

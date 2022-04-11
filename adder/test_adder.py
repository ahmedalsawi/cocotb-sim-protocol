# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer,Edge,Join
#from adder_model import adder_model
from cocotb.utils import get_sim_time
import random


#@cocotb.test()
#async def adder_basic_test(dut):
#    """Test for 5 + 10"""
#
#    A = 5
#    B = 10
#
#    dut.A.value = A
#    dut.B.value = B
#
#    await Timer(2, units='ns')
#
#    assert dut.X.value == adder_model(A, B), f"Adder result is incorrect: {dut.X.value} != 15"
#
#
#@cocotb.test()
#async def adder_randomised_test(dut):
#    """Test for adding 2 random numbers multiple times"""
#
#    for i in range(10):
#
#        A = random.randint(0, 15)
#        B = random.randint(0, 15)
#
#        dut.A.value = A
#        dut.B.value = B
#
#        await Timer(2, units='ns')
#
#        assert dut.X.value == adder_model(A, B), "Randomised test failed with: {A} + {B} = {X}".format(
#            A=dut.A.value, B=dut.B.value, X=dut.X.value)
#
async def task(dut):
    print(f"task:{get_sim_time()}")
    await Timer(10, units='ns')
    print(f"task:{get_sim_time()}")

async def task1(dut):
    print(f"task1:{get_sim_time()}")
    await Timer(40, units='ns')
    print(f"task1:{get_sim_time()}")
    return "yo"

async def task2(dut):
    print(f"task2:{get_sim_time()}")
    await  Edge(dut.x)
    await  Edge(dut.x)
    print(f"task2:{get_sim_time()}")

@cocotb.test()
async def read_signal(dut):
    task_coro  = await cocotb.start(task(dut))
    task1_coro = await cocotb.start(task1(dut))
    task2_coro = await cocotb.start(task2(dut))

    print(f"main1:{get_sim_time()}, {dut.x.value}")

    await Timer(10, units='ns')
    print(f"main2:{get_sim_time()}, {dut.x.value}")

    result = await Join(task1_coro)
    print(f"main3:{get_sim_time()}, {dut.x.value}")


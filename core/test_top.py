import cocotb
from cocotb.triggers import Timer,Edge,Join
from cocotb.utils import get_sim_time
import random

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
async def tb_top(dut):
    task_coro  = await cocotb.start(task(dut))
    task1_coro = await cocotb.start(task1(dut))
    task2_coro = await cocotb.start(task2(dut))

    print(f"main1:{get_sim_time()}, {dut.x.value}")

    await Timer(10, units='ns')
    print(f"main2:{get_sim_time()}, {dut.x.value}")

    result = await Join(task1_coro)
    print(f"main3:{get_sim_time()}, {result} {dut.x.value}")


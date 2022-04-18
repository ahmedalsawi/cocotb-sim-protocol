import random
import socket
import asyncio

import cocotb
from cocotb.triggers import Timer,Edge,Join
from cocotb.utils import get_sim_time

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


async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        response = str(eval(request)) + '\n'
        await loop.sock_sendall(client, response.encode('utf8'))
    client.close()

@cocotb.coroutine
async def start_server(dut):
    server = socket.socket()
    port = 12345
    server.bind(('', port))
    server.listen(5)
    server.setblocking(False)

    print("starting server")

    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(server)
        print("========================")
        print("accept")
        print(type(client))
        print("========================")
    #    loop.create_task(handle_client(client))

@cocotb.test()
async def tb_top(dut):
    task_coro  = await cocotb.start(task(dut))
    task1_coro = await cocotb.start(task1(dut))
    task2_coro = await cocotb.start(task2(dut))
    wait_for_socket_coro = await cocotb.start(start_server(dut))

    print(f"main1:{get_sim_time()}, {dut.x.value}")

    await Timer(10, units='ns')
    print(f"main2:{get_sim_time()}, {dut.x.value}")

    result = await Join(task1_coro)
    print(f"main3:{get_sim_time()}, {result} {dut.x.value}")

    result = await Join(wait_for_socket_coro)
    print(f"End:{get_sim_time()}, {result} {dut.x.value}")


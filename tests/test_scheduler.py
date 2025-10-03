from datetime import datetime
from schedulerx.interfaces import Order, Resource
from schedulerx.heuristics import GreedyScheduler

def test_parallel_capacity():
    orders = [
        Order('A',1,3,datetime(2025,1,10,12,0),'print',datetime(2025,1,10,6,0)),
        Order('B',1,3,datetime(2025,1,10,12,0),'print',datetime(2025,1,10,6,0)),
        Order('C',1,3,datetime(2025,1,10,12,0),'print',datetime(2025,1,10,6,0)),
    ]
    resources = [Resource('P1','print',2)]
    sched = GreedyScheduler(datetime(2025,1,10,6,0)).build(orders, resources).solve()
    starts = sorted([a.start for a in sched])
    assert starts[0] == starts[1]

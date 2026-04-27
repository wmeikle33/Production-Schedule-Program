from datetime import datetime


def test_parallel_capacity():
    orders = [
        Order('A',1,3,datetime(2025,1,10,12,0),'print',datetime(2025,1,10,6,0)),
        Order('B',1,3,datetime(2025,1,10,12,0),'print',datetime(2025,1,10,6,0)),
        Order('C',1,3,datetime(2025,1,10,12,0),'print',datetime(2025,1,10,6,0)),
    ]
    starts = sorted([a.start for a in sched])
    assert starts[0] == starts[1]

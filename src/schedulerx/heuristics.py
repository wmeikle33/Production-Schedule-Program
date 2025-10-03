from collections import defaultdict
from datetime import datetime, timedelta
from typing import List, Dict
from .interfaces import Order, Resource, Assignment, Scheduler

class GreedyScheduler:
    def __init__(self, start: datetime | None = None): self.start = start
    def build(self, orders: List[Order], resources: List[Resource]):
        self.orders = orders; self.resources = resources; return self
    def solve(self) -> List[Assignment]:
        if not getattr(self, 'orders', None): return []
        start0 = self.start or min((o.release or datetime.now()) for o in self.orders)
        by_skill: Dict[str, List[Order]] = defaultdict(list)
        for o in self.orders: by_skill[o.required_skill].append(o)
        lanes = {}
        res_by_skill: Dict[str, List[Resource]] = defaultdict(list)
        for r in self.resources:
            res_by_skill[r.skill].append(r); lanes[r.id] = [start0 for _ in range(max(1, r.parallel))]
        out: List[Assignment] = []
        for skill, orders in by_skill.items():
            orders.sort(key=lambda o: (o.due, -o.priority, o.release or start0))
            for o in orders:
                cands = []
                for r in res_by_skill.get(skill, []):
                    for i, t in enumerate(lanes[r.id]):
                        est = max(t, o.release or start0)
                        cands.append((est, r.id, i))
                if not cands: continue
                est, rid, idx = min(cands, key=lambda x: x[0])
                dur = timedelta(hours=o.proc_time_hours)
                st, en = est, est + dur
                out.append(Assignment(order_id=o.id, resource_id=rid, start=st, end=en))
                lanes[rid][idx] = en
        return out

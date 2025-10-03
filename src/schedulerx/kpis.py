from typing import List, Dict
from .interfaces import Assignment, Order

def lateness(assignments: List[Assignment], orders: List[Order]) -> Dict[str, float]:
    due = {o.id: o.due for o in orders}
    last = {}
    for a in assignments:
        last[a.order_id] = max(last.get(a.order_id, a.end), a.end)
    return {oid: (end - due.get(oid, end)).total_seconds()/3600.0 for oid, end in last.items()}

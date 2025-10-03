import csv
from datetime import datetime
from typing import List
from .interfaces import Order, Resource, Assignment, Writer

FMTS = ["%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y/%m/%d %H:%M", "%Y/%m/%d"]
def parse_dt(s: str):
    s = (s or '').strip()
    if not s: return None
    for f in FMTS:
        try: return datetime.strptime(s, f)
        except ValueError: pass
    raise ValueError(f'Bad datetime: {s}')

class CSVOrdersLoader:
    def __init__(self, path: str): self.path = path
    def load_orders(self) -> List[Order]:
        out = []
        with open(self.path, newline='', encoding='utf-8') as f:
            r = csv.DictReader(f)
            for row in r:
                out.append(Order(
                    id=row['id'],
                    qty=float(row.get('qty',1)),
                    proc_time_hours=float(row.get('proc_time_hours',1)),
                    due=parse_dt(row['due']),
                    required_skill=row.get('required_skill','default'),
                    release=parse_dt(row.get('release','')),
                    priority=int(row.get('priority',0))
                ))
        return out

class CSVResourcesLoader:
    def __init__(self, path: str): self.path = path
    def load_resources(self) -> List[Resource]:
        out = []
        with open(self.path, newline='', encoding='utf-8') as f:
            r = csv.DictReader(f)
            for row in r:
                out.append(Resource(
                    id=row['id'],
                    skill=row.get('skill','default'),
                    parallel=int(row.get('parallel',1))
                ))
        return out

class CSVWriter(Writer):
    def __init__(self, path: str): self.path = path
    def write(self, assignments):
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f); w.writerow(['order_id','resource_id','start','end'])
            for a in assignments:
                w.writerow([a.order_id, a.resource_id, a.start.isoformat(' '), a.end.isoformat(' ')])

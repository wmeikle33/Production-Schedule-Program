from dataclasses import dataclass
from typing import Protocol, Optional, Iterable, List
from datetime import datetime

@dataclass
class Order:
    id: str
    qty: float
    proc_time_hours: float
    due: datetime
    required_skill: str
    release: Optional[datetime] = None
    priority: int = 0

@dataclass
class Resource:
    id: str
    skill: str
    parallel: int = 1

@dataclass
class Assignment:
    order_id: str
    resource_id: str
    start: datetime
    end: datetime

class OrdersLoader(Protocol):
    def load_orders(self) -> List[Order]: ...

class ResourcesLoader(Protocol):
    def load_resources(self) -> List[Resource]: ...

class Scheduler(Protocol):
    def build(self, orders: List[Order], resources: List[Resource]): ...
    def solve(self) -> List[Assignment]: ...

class Writer(Protocol):
    def write(self, assignments: Iterable[Assignment]) -> None: ...

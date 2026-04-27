from dataclasses import dataclass
from typing import List

@dataclass
class ProgramConfig:
    date: str
    value_list: List
    new_values: List
    marker:str
    
    

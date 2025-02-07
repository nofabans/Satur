from dataclasses import dataclass
@dataclass
class InsLineObject:
    ins:str
    args:list[str|int]
    label:str
@dataclass
class HinsLineObject:
    hins:str
    args:list[str|int]
u = {'ins':[''],
    'hins':[''],
    'registers':[''],
    'symbols':['']}
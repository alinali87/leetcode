from dataclasses import dataclass
from typing import List


@dataclass
class Test:
    args: List[int]
    expected: int

@dataclass
class Case:
    name: str
    test: Test


CASES = [
    Case('1', Test([2,3,-2,4], 6)),
    Case('2', Test([-2,0,-1], 0)),
]
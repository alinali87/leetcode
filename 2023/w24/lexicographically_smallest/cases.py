from dataclasses import dataclass
import typing as tp

@dataclass
class Test:
    args: tuple
    expected: tp.Any

@dataclass
class Case:
    name: str
    test: Test


CASES = [
    Case('bbb', Test(('leetcode',), 'kddsbncd')),
    Case('Abb', Test(('acbbc',), 'abaab')),
    Case('bAbb', Test(('cbabc',), 'baabc')),
    Case('AbbAbb', Test(('abcabc',), 'aababc')),
    Case('bbAbbA', Test(('bcabca',), 'ababca')),
    Case('1 A', Test(('a', ), 'z')),
    Case('2 A', Test(('aa',), 'az')),
    Case('3 A', Test(('aaa',), 'aaz')),
    Case('4 A', Test(('aaaa',), 'aaaz'))
]

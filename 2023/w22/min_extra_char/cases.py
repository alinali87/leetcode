from dataclasses import dataclass


@dataclass
class Test:
    data: tuple
    expected: int

@dataclass
class Case:
    name: str
    test: Test


CASES = [
    Case('no_matches', Test(('asdf', ['q', 'r', 't']), 4)),
    Case('simple', Test(('asdf', ['a', 'df', 'y']), 1)),
    Case('leetcode', Test(('leetscode', ["leet", "code", "leetcode"]), 1)),
    Case('eglglxa', Test(('eglglxa',
                          ["rs","j","h","g","fy","l","fc","s","zf","i","k","x","gl","qr","qj","b","m","cm","pe","y","ei","wg","e","c","ll","u","lb","kc","r","gs","p","ga","pq","o","wq","mp","ms","vp","kg","cu"]),
                         1)
         )
]

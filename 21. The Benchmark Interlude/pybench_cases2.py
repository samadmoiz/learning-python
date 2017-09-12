"""
pybench_cases.py: Run pybench on a set of pythons and statements.

Select modes by editing this script or command line arguments (in
sys.argv) e.g. "python pybench.py" to test specific version on
stmts, "python pybench.py -a" to test all python listed, or a
"python pybench.py -a -t" to trace command line too
"""

import pybench
import sys

pythons = [
    (1, 'python3'),
    (0, 'python2'),
    (0, '~/Downloads/pypy/pypy-c-jit-92150-9ac0b00b959a-linux64/bin/pypy')
]

stmts = [  # num, rep,stmt
    # use function call: map wins
    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
    (0, 0, "$listif3(map(ord, 'spam' * 2501))"),
    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
    # set and dict
    (0, 0, "{x ** 2 for x in range(1000)}"),
    (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
    (0, 0, "{x: x ** 2 for x in range(1000)}"),
    (0, 0, "d=dict()\nfor x in range(1000): d[x] = x ** 2"),
    # Pathlogical: 300k digits
    (1, 1, "len(str(2**1000000))")  # Pypy loses on this today
]

tracecmd = '-t' in sys.argv                      # -t trace command line
pythons = pythons if '-a' in sys.argv else None  # -a: all in list, else one?
pybench.runner(stmts, pythons, tracecmd)

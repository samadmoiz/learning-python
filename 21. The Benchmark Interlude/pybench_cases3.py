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
    (0, 0, """f=open('/usr/lib/python3.5/pdb.py')\nfor line in f: x=line\nf.close()""")
]

tracecmd = '-t' in sys.argv                      # -t trace command line
pythons = pythons if '-a' in sys.argv else None  # -a: all in list, else one?
pybench.runner(stmts, pythons, tracecmd)

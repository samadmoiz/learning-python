# M.py has func
# N.py has func

# fails
from M import func
from N import func

func()  # call N func()


import M
import N

M.func()
N.func()


# introduce as extension
from M import func as mfunc
from N import func as nfunc

mfunc()
nfunc()

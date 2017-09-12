# Bad choice

from small import x, y  # copy two names out
x = 42  # changes my x only
y[0] = 42

import small  # get module name
small.x = 42  # changes x in other module

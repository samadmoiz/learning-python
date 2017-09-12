from small import x, y

# changes y mutable here also change it to small module

import small
x = small.x
y = small.y
del small

print(x, y)

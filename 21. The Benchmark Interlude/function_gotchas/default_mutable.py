def saver(L=[]):
    L.append(1)
    print(L)

L([2]) # default not used
L() # default used
L() # default used

def saver(L=None):
    L = L or []
    L.append(1)
    print(L)

# another way state retention
# function mutable attribute
def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []

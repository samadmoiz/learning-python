# thismod.py

var = 99


def local():
    var = 0                       # Change local variable


def glob1():
    global var                    # Declare global (normal)
    var += 1                      # Change global var


def glob2():
    var = 0                       # Change local var
    import thismod                # import myself
    thismod.var += 1              # Change global var


def glob3():
    var = 0                       # Change local var
    import sys                    # Import system table
    glob = sys.modules['thismod']  # Get module object (or use __name__)
    glob.var += 1


def test():
    print(var)
    local()
    glob1()
    glob2()
    glob3()
    print(var)

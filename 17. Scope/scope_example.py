# Global scope
X = 99  # X and func assigned in module: global


def func(Y):  # Y and Z assigned in function: local
    # Local scope
    Z = Y + X  # X is global

    return Z

print(func(1))

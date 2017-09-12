def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)
f(3)  # 3 ** 2

g = maker(3)
g(3)  # 3 ** 3


def maker1(N):
    return lambda X: X ** N

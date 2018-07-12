def marker(n):
    def action(x):
        return n**x
    return action
f=marker(9)
print(f(5))
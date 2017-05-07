
def make_incrementor(n):
    return lambda x: x + n

increment2 = make_incrementor(2)
print increment2(5)

increment3 = make_incrementor(3)
print increment3(5)


def power(p):
    return lambda base: pow(base, p)

power2 = power(2)
print power2(3)
print power2(4)


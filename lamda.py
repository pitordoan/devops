
def increment(n):
    return lambda x: x + n

increment2 = increment(2)
print increment2(5)

increment3 = increment(3)
print increment3(5)


def power(p):
    return lambda base: pow(base, p)

power2 = power(2)
print power2(3)
print power2(4)


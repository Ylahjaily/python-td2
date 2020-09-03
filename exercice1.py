def functionA(n):
    for i in n:
        yield i * 2


def functionB(n):
    for i in n:
        yield i**2


def functionC(n):
    for i in n:

        yield i/5


def set_pipeline(*functions):
    return reduce(lambda x, y: y(x), list(functions))


results = set_pipeline(range(1000), functionA, functionB, functionC)
for result in results:
    print(result)

# 1===
def count_decorator(funk):
    i = 0

    def wrapped(obj):
        nonlocal i
        funk(obj)
        i += 1
        print(f'вызвана {i} раз')

    return wrapped


@count_decorator
def trulyla(obj):
    pass


trulyla(123)
trulyla(123)
trulyla(123)

# 2====
def debug(funk):
    def wrapper(arg):
        print(funk.__name__, arg)
        res = funk(arg)
        print(res)
        return res
    return wrapper

@debug
def pprint(f):
    return f + 100


pprint(123)
pprint(12)
pprint(67)
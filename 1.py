import itertools
test = [[-1, -3], [50, 60], [15, 25]]
print(list(itertools.chain.from_iterable(test)))
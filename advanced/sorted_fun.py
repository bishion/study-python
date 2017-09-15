print(sorted([1, 3, 2, 4, 5, 6, 5, 2, 0]))

print(sorted(['Bob', 'guo', 'Fang', 'bi'], key=str.lower))
print(sorted(['Bob', 'guo', 'Fang', 'bi'], key=str.lower, reverse=True))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


print(lazy_sum(1, 3, 5, 6, 7)())

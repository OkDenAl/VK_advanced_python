import cProfile
import pstats
import io


def profile_deco(func):
    stats = cProfile.Profile()

    def inner(*args, **kwargs):
        stats.enable()
        result = func(*args, **kwargs)
        stats.disable()
        return result

    def print_stat():
        stm = io.StringIO()
        pstats.Stats(stats, stream=stm).sort_stats("cumulative").print_stats()
        print(stm.getvalue())

    inner.print_stat = print_stat
    return inner


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


if __name__=="__main__":
    add(1, 2)
    add(4, 5)
    sub(4, 5)

    add.print_stat()
    sub.print_stat()

import weakref
import time
import cProfile
import pstats
import io
from memory_profiler import profile


class HelpClass:
    def __init__(self, x_lc):
        self.value = x_lc


class DefaultClass:

    def __init__(self, x_n: HelpClass, y_n: HelpClass, smth):
        self.link_1 = x_n
        self.link_2 = y_n
        self.smth = smth


class SlotsClass:
    __slots__ = ('link_1', 'link_2', 'smth')

    def __init__(self, x_s: HelpClass, y_s: HelpClass, smth):
        self.link_1 = x_s
        self.link_2 = y_s
        self.smth = smth


class WeakRefClass:

    def __init__(self, link_1: HelpClass, link_2: HelpClass, smth):
        self.link_1 = weakref.ref(link_1)
        self.link_2 = weakref.ref(link_2)
        self.smth = smth


def creating_list(variant, count):
    time_start = time.time()
    new_list = [variant(HelpClass(1), HelpClass('abc'), "smth") for _ in range(count)]
    time_finish = time.time() - time_start
    return time_finish, new_list


def change_list(mass):
    time_start = time.time()
    for item in mass:
        item.link_2 = HelpClass('dsa')
        item.link_1 = HelpClass(123)
        item.smth = [1, 2]
    time_finish = time.time() - time_start
    return time_finish


@profile
def default(t_norm):
    norm = []
    for item in range(M):
        t_n, norm = creating_list(DefaultClass, N)
        t_norm[item] = t_n

    for item in range(M):
        t_norm[item] = change_list(norm)


@profile
def slots(t_slots):
    slot = []
    for item in range(M):
        t_s, slot = creating_list(SlotsClass, N)
        t_slots[item] = t_s

    for item in range(M):
        t_slots[item] = change_list(slot)


@profile
def weak(t_weak):
    w_list = []
    for item in range(M):
        t_w, w_list = creating_list(WeakRefClass, N)
        t_weak[item] = t_w

    for item in range(M):
        t_weak[item] = change_list(w_list)


if __name__ == '__main__':
    N, M = 1_000_000, 10
    SORT_BY = 'cumulative'
    time_norm, time_slots, time_weak = [0.0] * M, [0.0] * M, [0.0] * M
    list_norm, list_slots, list_weak = [], [], []

    pr = cProfile.Profile()
    pr.enable()
    for i in range(M):
        time_n, list_norm = creating_list(DefaultClass, N)
        time_norm[i] = time_n
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('class with default attributes')
    print(s.getvalue())

    pr = cProfile.Profile()
    pr.enable()
    for i in range(M):
        time_s, list_slots = creating_list(SlotsClass, N)
        time_slots[i] = time_s
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('class with slot attributes')
    print(s.getvalue())


    pr = cProfile.Profile()
    pr.enable()
    for i in range(M):
        time_w, list_weak = creating_list(WeakRefClass, N)
        time_weak[i] = time_w
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('class with weak ref attributes')
    print(s.getvalue())

    print(f'average time for {M} attempts to create list with {N} values')
    print(f'with default attributes {sum(time_norm) / M} sec')
    print(f'with slots {sum(time_slots) / M} sec')
    print(f'with weak ref {sum(time_weak) / M} sec')
    print('-----------------------------------')

    time_norm, time_slots, time_weak = [0.0] * M, [0.0] * M, [0.0] * M
    pr = cProfile.Profile()
    pr.enable()
    for i in range(M):
        time_n = change_list(list_norm)
        time_norm[i] = time_n
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('class with default attributes')
    print(s.getvalue())

    pr = cProfile.Profile()
    pr.enable()
    for i in range(M):
        time_s = change_list(list_slots)
        time_slots[i] = time_s
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('class with slots attributes')
    print(s.getvalue())

    pr = cProfile.Profile()
    pr.enable()
    for i in range(M):
        time_w = change_list(list_weak)
        time_weak[i] = time_w
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('class with weak ref attributes')
    print(s.getvalue())

    print(f'average time for {M} attempts to change list with {N} values')
    print(f'class with default attributes {sum(time_norm) / M} seconds')
    print(f'class with slots {sum(time_slots) / M} seconds')
    print(f'class with weak ref {sum(time_weak) / M} seconds')

    time_norm, time_slots, time_weak = [0.0] * M, [0.0] * M, [0.0] * M
    default(time_norm)
    slots(time_slots)
    weak(time_weak)

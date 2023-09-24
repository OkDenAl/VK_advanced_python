import time


class InvalidParamError(Exception):
    pass


def mean(k):
    if k <= 0:
        raise InvalidParamError("invalid k param value")
    counter = 0
    buffer = [0] * k
    mean_val = 0

    def mean_inner(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            nonlocal counter
            nonlocal mean_val
            if counter < k:
                buffer[counter] = end_time - start_time
                mean_val = mean_val * counter + buffer[counter]
                mean_val /= (counter + 1)
            else:
                mean_val = mean_val * k - buffer[counter % k]
                buffer[counter % k] = end_time - start_time
                mean_val += buffer[counter % k]
                mean_val /= k

            counter += 1
            if counter % k == 0:
                last_calls = k
            else:
                last_calls = counter % k
            print(f"Среднее время выполнения последних {last_calls}"
                  f" вызовов функции {func.__name__}: {mean_val}", buffer)

        return inner

    return mean_inner


@mean(10)
def foo(arg1):
    pass


@mean(2)
def boo(arg1):
    pass


if __name__ == "__main__":
    for _ in range(100):
        boo("Walter")

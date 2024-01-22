import time
from multiprocessing import Process
import logging

logging.basicConfig(level=logging.DEBUG)
start = time.perf_counter()


def is_divisible(number, divisor):
    return (number % divisor) == 0


def mul_factorize(number):
    factorize_list = []
    for div in range(1, int(number) + 1):
        if is_divisible(number, div):
            factorize_list.append(div)
    logging.debug(f'{number}:= {factorize_list}')
    return None


if __name__ == '__main__':
    processes = []

    for num in [128, 255, 99999, 10651060]:
        pr = Process(target=mul_factorize, args=(num,))
        processes.append(pr)
        pr.start()

    for pr in processes:
        pr.join()

    logging.debug(
        f'Concurrent code execution: {time.perf_counter() - start}')

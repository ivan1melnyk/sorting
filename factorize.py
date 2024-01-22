import time
import logging

logging.basicConfig(level=logging.DEBUG)
start = time.process_time()
# your code here


def is_divisible(number, divisor):
    return (number % divisor) == 0


def factorize(*numbers):
    # YOUR CODE HERE
    factorizes = []
    for number in numbers:
        factorize_list = []
        for div in range(1, number+1):
            if is_divisible(number, div):
                factorize_list.append(div)
        factorizes.append(factorize_list)
    return factorizes
    raise NotImplementedError()  # Remove after implementation


a, b, c, d = factorize(128, 255, 99999, 10651060)

logging.debug(a)
logging.debug(b)
logging.debug(c)
logging.debug(d)

logging.debug(f'Synchronous code execution: {time.process_time() - start}')


assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
             380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

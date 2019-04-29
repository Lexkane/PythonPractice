import random


def main():
    pass


def myranger(begin, end, step):
    current = begin
    while current < end:
        yield current
        current += step


def random_length_repeat(obj, prob):
    while True:
        if random.random() < prob:
            break
        yield obj


[2*x+1 for x in range(5)]
list(2*x+1 for x in range(5))

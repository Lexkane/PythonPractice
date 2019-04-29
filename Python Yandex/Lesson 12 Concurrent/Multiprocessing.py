from multiprocessing import Process
from multiprocessing import Pool


def main():
    pass


def f(name):
    print("hello", name)


p = Process(target=f, args=('world',))
p.start()
p.join()


def calc(value):
    return value**2


p = Pool(process=4)
results = p.map(calc, range(10))
print(results)


def calc_parallel(values):
    def calc(value):
        return(value**2)
    p = Pool(processes=2)
    return p.map(calc, values)

calc_parrallel(range(10))    

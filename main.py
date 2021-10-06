import multiprocessing
import time

start_time = time.time()
def counter(number, number2):
    for i in range(number, number2):
        print(i)


if __name__ == '__main__':
    for i in range(1):
        p = multiprocessing.Process(target=counter, args=(1400000000, 1700000000))
        p.start()

print(time.time() - start_time)


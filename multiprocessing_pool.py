import time
import multiprocessing as mp

def f(n):
    sum = 0
    for x in range(100000):
        sum += x*x

if __name__ == "__main__":

    print("In main")
    pl = mp.Pool()
    t1 = time.time()
    result = pl.map(f,range(100000))
    pl.close()
    pl.join()
    print("Pool took this much time: " + str(time.time()-t1))

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(range(100000)))
    print("Serial took this much time: " + str(time.time() - t2))

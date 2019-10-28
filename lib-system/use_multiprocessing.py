import multiprocessing
import time


def func(msg):
    for i in range(3):
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    p = multiprocessing.Process(target=func,
                                args=('hello', ))
    p.start()
    p.join()
    print('Sub-process done.')

    pool = multiprocessing.Pool(processes=4)
    for i in range(10):
        msg = f"hello {i}"
        pool.apply_async(func, (msg, ))
    pool.close()
    pool.join()
    print("Sub-process(es) done.")

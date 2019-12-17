import multiprocessing as mp
import os
import time
import random


def task(q, l, task_id):
    print('start run task %s ...' % (os.getpid()))
    temp = 0
    time.sleep(5)
    print("task %s is running" % (os.getpid()))
    time.sleep(5)
    # file_name = str(random.random()) + ".txt"
    # a = open(file_name, "w")
    # a.close()
    # l.acquire()
    if random.random() > 0.8:
        q.put("%2d: fail" % task_id)
    else:
        q.put("%2d: pass" % task_id)
    # l.release()
    print("task %s finish " % (os.getpid()))


if __name__ == '__main__':
    print(mp.cpu_count())
    number_per_board = 24        # 一批数量
    pool = mp.Pool(number_per_board)       # 同时运行的进程数量
    manager = mp.Manager()
    result_queue = manager.Queue()      # 与父进程通信用
    lock = manager.Lock()
    start = time.time()
    for i in range(1, number_per_board + 1):
        pool.apply_async(task, args=([result_queue, lock, i, ]))
    print('Waiting for all subprocesses done...')
    pool.close()
    pool.join()
    end = time.time()
    for i in range(number_per_board):
        print(result_queue.get())
    print('All subprocesses done.', round(end-start, 2))

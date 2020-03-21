from multiprocessing import Process
import os
import time
import random
# 子进程要执行的代码
def run_proc(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p1 = Process(target=run_proc, args=('test1',))
    p2 = Process(target=run_proc, args=('test2',))
    p3 = Process(target=run_proc, args=('test3',))
    p4 = Process(target=run_proc, args=('test4',))
    p5 = Process(target=run_proc, args=('test5',))
    print('Child process will start.')
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    print('Child process end.')
# coding: utf-8
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()  # 默认进程池大小为4，这里可以指定同时运行的进程数量，如：p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  # 执行apply_async，子进程就会立即启动
    print 'Waiting for all subprocesses done...'
    p.close()  # 调用close()之后就不能继续添加新的Process
    p.join()  # 调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()
    print 'All subprocesses done.'

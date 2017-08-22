# coding=utf8

from multiprocessing import Pool
import os, time, random
import re

def long_time_task(filenamepath):
    p_filename = re.compile(".*(boss.log.*)$")
    m_filename = p_filename.match(filenamepath)
    filename = m_filename.group(1)
    print 'Run task %s, process file %s ...' % (os.getpid(), filename)

    ffrom = open(filenamepath)
    fto = open(filename, "w+")
    
    # 提取奇数行
    num = 1
    for line in ffrom:
        if num % 2 == 1:
            fto.write(line) 
        num = num + 1

    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Process file %s runs %0.2f seconds.' % (filename, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    fileobj = os.popen('find $PWD | grep boss.log')

    p = Pool()
    for filenamepath in fileobj:
        filenamepath = filenamepath.strip()
        p.apply_async(long_time_task, args=(filenamepath,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()

    print 'All subprocesses done.'

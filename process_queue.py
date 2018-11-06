#coding:utf-8
#在父进程中创建三个子进程。两个子进程向queue中写入数据，一个子进程从Queue中读取数据
from multiprocessing import Process, Queue
import os, time, random

#写数据进程代码
def proc_write(q,urls):
	print('Process(%s) is Writing...' % os.getpid())
	for url in urls:
		q.put(url)
		print('Put %s to queue...' % url)
		time.sleep(random.random())


#读取数据进程代码
def proc_read(q):
	print('Process(%s) is reading...' % os.getpid())
	while True:
		url = q.get(True)
		print('Get %s from Queue.' % url)


if __name__ == '__main__':
	q = Queue()
	proc_writer1 = Process(target=proc_write, args=(q, ['url_1','url_2','url_3']))
	proc_writer2 = Process(target=proc_write, args=(q, ['url_4','url_5','url_6']))
	proc_reader = Process(target=proc_read, args=(q,))
	#启动子进程proc_writer,写入
	proc_writer1.start()
	proc_writer2.start()
	#启动子进程proc_reader，读取
	proc_reader.start()
	#等待proc_writer结束
	proc_writer1.join()
	proc_writer2.join()
	#proc_reader进程是死循环，无法等待其结束，只能强行终止
	proc_reader.terminate()

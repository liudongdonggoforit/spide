#coding:utf-8
import os
from multiprocessing import Process
#子进程要执行的代码
#使用multiprocessing模块创建多进程
#multiprocessing 模块提供了一个Process类来描述一个进程对象，创建子进程时，只需要
#传入一个执行函数和函数的参数，即可完成一个Process实例的创建，用start()方法启动进程，
#用join()方法实现进程间的同步。
def run_proc(name):
	print('Child process %s (%s) Running...' % (name,os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	for i in range(5):
		p = Process(target=run_proc, args=(str(i),))
		print('Process will start')
		p.start()
	p.join()
	print('Process end')
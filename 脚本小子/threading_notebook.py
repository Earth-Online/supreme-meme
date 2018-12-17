import threading
import time
from queue import Queue

lock = threading.Lock()

def job_foo():
	time.sleep(1)
	print("t1")

def job(l, q):
	lock.acquire() # 锁保护
	print(threading.current_thread())
	for i in range(len(l)):
		l[i] = l[i]**3
	q.put(l) # 结果放入队列池
	lock.release()

def Simple_Thread():
	new_job = threading.Thread(target=job_foo, args=())
	new_job.start()
	new_job.join() # 主线程阻塞
	print("done")

def thread_pool():
	q = Queue()
	t = []
	ans = []
	data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 5, 5]]
	for i in range(4):
		t_o = threading.Thread(name="t"+str(i), target=job, args=(data[i], q))
		t_o.start()
		t.append(t_o)
	for thread in t:
		thread.join()
	for _ in range(4):
		ans.append(q.get())
	print(ans)

thread_pool()
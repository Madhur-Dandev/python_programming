from threading import Thread
from time import sleep

def thread_body(num):
	""" Synchronization is not guaranteed """
	sleep(1.0)
	print(num)

	#sleep(1.0)
	#print("Done")

def run():
	threads = []
	for i in range(1, 11):
		t = Thread(target=thread_body, args=(i,))
		threads.append(t)
		t.start()

	for thrd in threads:
		thrd.join()

if __name__ == "__main__":
	run()

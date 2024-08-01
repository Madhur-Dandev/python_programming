from threading import Thread, Lock

num = 0
lock = Lock()

def first_body():
	global num
	with lock:
		num += 1
		print(num)

def second_body():
	global num
	with lock:
		num += 2
		print(num)

def run():
	t1 = Thread(target=first_body)
	t2 = Thread(target=second_body)

	t1.start()
	t2.start()

	t1.join()
	t1.join()


if __name__ == "__main__":
	run()

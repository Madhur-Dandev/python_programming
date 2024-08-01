from threading import Thread, Lock, Condition

lock = Lock()
done = True
cv = Condition(lock)

def first_body():
	global done

	with cv:
		print("A")
		done = True
		cv.notify()

def second_body():
	global done

	with cv:
		while not done:
			cv.wait()
		print("B")

def run():
	t1 = Thread(target=first_body)
	t2 = Thread(target=second_body)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__ == "__main__":
	run()

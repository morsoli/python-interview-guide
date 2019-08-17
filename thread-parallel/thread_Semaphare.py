import threading
import time
import random
semaphare=threading.Semaphore(0)
def producer():
    global item
    time.sleep(2)
    item=random.randint(0,1000)
    print('Producer notify: produced item number %s'%item)
    semaphare.release()
def consumer():
    print('comsumer is waiting')
    semaphare.acquire()
    print('Consumer notify: consumed item number %s'%item)

if __name__ == "__main__":
    for i in range(5):
        t1=threading.Thread(target=producer)
        t2=threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print('end!!!')
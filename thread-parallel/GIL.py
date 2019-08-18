import threading
lock=threading.Lock()
n=[0]
def demo():
    with lock:
        n[0]=n[0]+1
threads=[]
for i in range(5000):
    t=threading.Thread(target=demo)
    threads.append(t)
for t in threads:
    t.start()
print(n)
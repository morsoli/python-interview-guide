import threading
import time
# 简单程序的多线程编程
""" def get_html():
    print('get html start')
    time.sleep(2)
    print('get html end')
def get_url():
    print('get url start')
    time.sleep(4)
    print('get url end') """

# 复杂程序的多线程编程
class GetHtml(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)
    def run(self):
        print('get html start')
        time.sleep(2)
        print('get html end')
class GetUrl(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)
    def run(self):
        print('get url start')
        time.sleep(4)
        print('get url end')
if __name__ == "__main__":
#    thread1=threading.Thread(target=get_html)
#    thread2=threading.Thread(target=get_url)
    thread1=GetHtml(name='html')
    thread2=GetUrl(name='url')
    start_time=time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time=time.time()
    total_time=end_time-start_time
    print('total running tim:{}'.format(total_time))
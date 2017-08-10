##################################### 并发 ############################################
#启动和停止线程
import time
def countdown(n):
    while n > 0:
        print('T-minus',n)
        n -= 1
        time.sleep(5)
from threading import Thread
t = Thread(target=countdown, args=(10,))
#t.start()

#t = Thread(target=countdown, args=(10,), daemon=True) #daemon=True 守护线程 无法被连接，主线程结束 会自动销毁
t.start()
if t.is_alive():
    print('Still running')
else:
    print('Complteted')


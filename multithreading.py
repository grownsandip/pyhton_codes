import time
import threading
from concurrent.futures import ThreadPoolExecutor
def func1(seconds):
    print(f"sleeping for {seconds}seconds")
    time.sleep(seconds)
    return seconds
    
# time_start=time.perf_counter()
# func1(4)
# func1(3)
# func1(1)
# time_end=time.perf_counter()
# print(f"time taken for run:{time_end-time_start}")

# time_start=time.perf_counter()
# t1=threading.Thread(target=func1,args=[4]) #basically starts all at same time and throws in back for execution
# t2=threading.Thread(target=func1,args=[3])
# t3=threading.Thread(target=func1,args=[1])
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

# time_end=time.perf_counter()
# print(f"time taken for run:{time_end-time_start}")

def poolingDemo(): #this process comes handy when we want to submit functions and values
    with ThreadPoolExecutor() as executor:
        # future1=executor.submit(func1,4)
        # future2=executor.submit(func1,3)
        # future3=executor.submit(func1,2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l=[5,3,1,7]
        results=executor.map(func1,l) #lets suppose we have list of urls and we want to downlod
        for res in results:
            print(res)
    
poolingDemo()
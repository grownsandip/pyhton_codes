import requests
import multiprocessing
def downloadFile(url,name):
    print(f"process {name} started")
    respose=requests.get(url)
    open(f"extras/mul/file{name}.jpg","wb").write(respose.content)
    print(f"process {name} ended")
    
url="https://picsum.photos/2000/3000"
pros=[]
for i in range(5):
    #downloadFile(url,i) #normal way of downloading files
    p=multiprocessing.Process(target=downloadFile,args=[url,i])
    p.start()
    pros.append(p)
for p in pros:
    p.join()
    
    
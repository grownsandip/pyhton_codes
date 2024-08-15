import os
ls=os.listdir("/home/sandip/Documents/python_programmes")
#print(ls)
for folder in ls:
    #print(folder)
    print(os.listdir(folder))
#for i in range(0,3):
    #os.mkdir(f"data{i+1}")
   # os.rename(f"data{i+1}",f"tutorial{i+1}")
    #os.listdir()
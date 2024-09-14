#asyncio is used the run asynchronous tasks parallely
import asyncio
import requests
async def func1():
    # await asyncio.sleep(2)
    print("func1")
    URL="https://media.istockphoto.com/id/1602458519/photo/colorful-powder-explosion-on-white-background.webp?a=1&b=1&s=612x612&w=0&k=20&c=NBmXVaTxcq0Bw-0jXMlA3_A6cbG4r_WbNMGEECWglmk="
    response=requests.get(URL)
    open("extras/pic1.jpg","wb").write(response.content)
async def func2():
    print("func2")
    URL="https://images.unsplash.com/photo-1530631673369-bc20fdb32288?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3BsYXNofGVufDB8fDB8fHww"
    response=requests.get(URL)
    open("extras/pic2.jpg","wb").write(response.content)
    #await asyncio.sleep(3)
async def func3():
    print("func3")
    URL="https://media.istockphoto.com/id/2018463641/photo/water-fight-in-our-backyard.webp?a=1&b=1&s=612x612&w=0&k=20&c=rTyiilttJ-4Y5HD3ecHah8fl3ZLilPwB9w5U_-nMKps="
    response=requests.get(URL)
    open("extras/pic3.jpg","wb").write(response.content)
    #await asyncio.sleep(4)
    
async def main(): 
    # await func1()
    # await func2()   #this traditional method takes longer time to download images 
    # await func3()
    L=await asyncio.gather(
     func1(),
     func2(),
     func3(),   #this begins all downloads together
    ) 
    print(L)
asyncio.run(main())
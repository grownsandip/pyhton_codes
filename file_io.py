#creating  a file in write mode if file odoesnot exits than it creates a file

# f=open("file.txt",'w')
# f.write("Hello world")
# f.close()

#reading a existing file

# try:
#     f=open("file.txt",'r')
#     text=f.read()
#     print(text)
#     f.close()
# except:
#     print("The file doesnot exist")
#APPEND MODE append mode doesnot clear prexeisting data but write mode does
# try:
#     f=open("file.txt",'a')
#     text=input("Enter a text:")
#     f.write( text)
#     # updated=f.read()
#     # print(f"the updated text in the file is:{updated}")
#     f.close()
# except:
#     print("The file doesnot exist")
# finally:
#     print("The text is altered")
#with this syntax we dont need to specifically close the file this automatically closes the file.
# with open("file.txt",'a') as f:
#     f.write("Hello i am inside an open file")
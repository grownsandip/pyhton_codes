# a=input("Enter a number:")
# try:
#     for i in range (1,11):
#         print(f"{int(a)}x{i}={int(a)*i}")
# except Exception as e:
#     print(e)
# print("some important lines of codes")
# print("End of program")
try:
  num=int(input("Enter a number:"))
  p=[9,10]
  print(p[6])
except ValueError:
    print("There is a value error")
except IndexError:
    print("Invalid index")
    
print("end of program")
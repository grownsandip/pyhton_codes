def fibo(n):
    if(n<0):
        raise ValueError("Negative numbers are not allowed")
    series=[0,1]
    #print(a,b)
    for i in range(2,n):
        series.append(series[-1]+series[-2])
    return series
n=int(input("Enter number of terms:"))
print(fibo(n))
list1=[]
def fib(a,b,n):
    if(n==0):
        return
    else:
        temp=a+b
        list1.append(temp)
        fib(b,temp,n-1)
n=int(input("enter the number to geneterate the Fibonacci series\t"))
a=0
b=1
list1.append(a)
list1.append(b)

fib(a,b,n-2)
print("Fibonnaci numbers are ")
for x in list1:
    print(x)

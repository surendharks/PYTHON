#Write a Python program to print all positive numbers in a range
list1 = [12, -7, 5, 64, -14]  
list2 = [12, 14, -95, 3] 
def make(lis):
    for x in lis:
        if x<0:
            lis.remove(x)
make(list2)
make(list1)
print(list1)
print(list2)

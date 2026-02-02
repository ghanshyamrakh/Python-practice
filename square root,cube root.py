import math
num=int(input("enter a number:"))
if 0<num<10:
        print(num**2)
elif 10<num<100:
    print(math.sqrt(num))
else:
    print(math.cbrt(num))
        
        

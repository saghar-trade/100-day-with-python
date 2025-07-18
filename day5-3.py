total=0
for n in range(0,101,2):
    total+=n
print(f"sum of even number between 0 and 100 equals : {total}")    
#--------------------------------------
for n in range(1,101):
    if n %15 ==0:
        print("fizzbuzz")
    elif n % 3 ==0:
        print("fizz")
    elif n % 5==0:
        print("Buzz")
    else:
        print(n)
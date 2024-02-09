# in progress


#list with num div/3 
num_div3 = []

#list with num div/3
num_div5 = []
for num in range(3,101,3):
    num_div3.append(num) 

for num in range(5,101,5):
    num_div5.append(num) 


    
print(num_div5, "\n")


def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


n = int(input().strip())
fizzBuzz(n)
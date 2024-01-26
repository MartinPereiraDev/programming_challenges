# lambda function example 


def add(num1, num2):
    return num1+num2

add_lambda = lambda num1,num2: num1+num2

print("Here function add :",add(5,2))
print("Here lambda function :",add_lambda(5,2))


twice = lambda x: x*2

print("lambda twice : ", twice(5))
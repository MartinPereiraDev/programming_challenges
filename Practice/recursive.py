def function_a(n):
    if n == 0:
        return 1
    else:
        return n * function_b(n - 1)

def function_b(n):
    if n == 0:
        return 1
    else:
        return n * function_a(n - 1)

print(function_a(4))

def example(val):
    val = val + '4'
    val = val * 2
    return val 

print(example('jump'))
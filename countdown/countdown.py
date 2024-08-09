""" two numbers countdown
    import time for seconds 
    modify time.sleep(seconds)
    args:
        num1 (int) : start count 
"""
import time

def countdown(start, end):
    a = 0
    countdown = end - start
    
    print("The account begins :", start, " -- ends : ", end , "seconds")
    print ("I have ", countdown, "seconds :")

    for a in range(countdown):
        print(countdown, " ...")
        countdown = countdown -1
        time.sleep(1)
    return ("end countdown")    
            
countdown(20,45)    
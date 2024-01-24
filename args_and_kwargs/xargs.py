#xargs use *args when function receive many data
# Get many numbers return sum
def get_sum(*nums):
    result = 0
    for num in nums:
        result += num
    print('The sum of get_num is : ',result)

get_sum(6,7)
get_sum(6,5,8,152)
get_sum(90,25,21,14,89) 


# get many numbers and return max 
def get_num_max(*nums):
    max = 0
    for num in nums:
        if max < num:
            max = num
    print('The maximun of function is :', max)

get_num_max(25,10,12,120)
get_num_max(0,1000,-10,51,0)
get_num_max(15,2,56,78,580,451)






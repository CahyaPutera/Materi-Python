# def prime_num(num):
#     prime_tab = []
#     for i in range(2, num+1):
#         if num % i == 0 :
#             prime_tab.append(True)
    
#     if sum(prime_tab) == 1:
#         return True
#     else :
#         return False

# def fizzBuzz(num) :
#     for i in range(1, num + 1):
#         if prime_num(i) :
#             print('FizzPrime')
#         elif (i % 15 == 0) :
#             print('FizzBuzz')
#         elif (i % 3 == 0):
#             print('Fizz')
#         elif (i % 5 == 0):
#             print('Buzz')
#         else :
#             print(i)
# fizzBuzz(20)

# Mean

from math import floor

x = [ 1,2,3,2,5,2,7,2 ]
def getMean(list) :
    sum = 0
    for item in list :
        sum += item

    mean = sum / len(list)
    return mean
print(getMean(x))

# Median

x = [ 1,2,3,2,5,2,7,2 ]
def getMedian(list) :
    list.sort()
    median = 0 
    if (len(list) % 2 != 0) :
	median = list[floor(len(list) / 2)]
    else :
        mid1 = list[(int(len(list) / 2)) - 1]
        mid2 = list[int(len(list) / 2)]
        median = (mid1 + mid2) / 2
    return median
print(getMedian(x))

# Mode

x = [ 1,2,3,2,5,2,7,2 ]
def getMode(list) :
    countList = []
    # create countList
    for num in list :
        check = False
        for list1 in countList :
            if(list1[0] == num) :
                list1[1] += 1
                check = True
        if(check == False) :
            countList.append([num, 0])
    # create list of mode/s
    maxFrequency = 0
    modes = []
    for list1 in countList :
        if (list1[1] > maxFrequency) :
            modes = [list1[0]]
            maxFrequency = list1[1]
        elif (list1[1] == maxFrequency) :
            modes.append(list1[0])
    # if every value appears same amount of times
    if (len(modes) == len(countList)) :
        modes = []
    return modes
print(getMode(x))


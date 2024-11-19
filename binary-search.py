
#O(Log n)
def binary_search(list, item):
    #low and high keep track of which part of the list you'll search in
    low = 0
    high = len(list)-1

    while low <= high: #while you haven't narrowed it down to the one element...
        mid = (low + high) #check the niddle element
        guess = list[mid]
        if guess == item: #found the item 
            return mid
        if guess > item: #guess was too high
            high = mid - 1
        else:            #guess was too low
            low = mid + 1
    return None #the item does not exist

my_list = [1, 3, 5, 7, 9]

print (binary_search(my_list, 3)) # answer is 1
print (binary_search(my_list, -1)) # answer is None



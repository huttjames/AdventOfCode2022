
with open('input.txt') as f:
    string = f.readlines() #f.read() reads it as a single string saving this step

string = string[0]

# Loop through string looking back 4 

for i in range(3,len(string)+1):
    list4 = [string[i-3], string[i-2], string[i-1], string[i]]

    # There are lots of ways of checking if a list is equal. This is a fast implementation. 
    # Creates a dictionary from a list of keys, which is the list. 
    # If the keys are all the same then the dictionary has only 1 key. If all keys are different it has 4 keys. 

    if len(dict.fromkeys(list4)) == 4:
        print(i+1)
        print(list4)
        break


# Part 2 

# Cumbersome to define the list elements 1 by 1 as above, so using the unpack method to convert a string into a list of elements
# Note character 14 is now first included when i=14, because list 14 is created as characters 0 to 13 inclusive, which is the first
# 14 characters. This means no need to report i+1. 
# In part 1 then i=3 gave the first 4 characters, as i-3, i-2, i-1 and i. So the 4th character was i=1. 
# The difference is whether the right hand boundary of the range is included. 

for i in range(14, len(string)+1):
    list14 = [*string[i-14:i]]

    if len(dict.fromkeys(list14)) == 14:
        print(i)
        print(list14)
        break


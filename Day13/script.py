import ast as ast
import functools as functools

with open('input.txt') as f:
    pairs = f.read().splitlines()

for i in range(len(pairs)):
    if pairs[i] == '':
        pairs[i] = "space" #So that is visible and not confused with newlines in the console
    else:
        pairs[i] = ast.literal_eval(pairs[i])

# Create a copy of pairs for use later as by running the function some elements are converted to lists 
pairs_copy = pairs.copy()

# At the pair level, both are lists 
def compare_two_lists(left, right):
    left_len = len(left)
    right_len = len(right)
    x = "unch"
    
    for i in range(min(left_len, right_len)):
        if x == "correct" or x == "incorrect": #Then a difference has already been spotted and we don't want to carry on looking elementwise
            break
        else:
            if type(left[i]) == int and type(right[i]) == int: #If both ints then compare them
                if left[i] < right[i]:
                    x = "correct"
                    break
                
                elif right[i] < left[i]:
                    x = "incorrect"
                    break
                else: #They are equal
                    continue
            elif type(left[i]) == int and type(right[i]) == list: #One is a list and one is an int. Convert to 2 lists.
                left[i] = [left[i]].copy()
                x = compare_two_lists(left[i], right[i]) #Then run the function on the 2 lists
            elif type(left[i]) == list and type(right[i]) == int: # As above
                right[i] = [right[i]].copy()
                x = compare_two_lists(left[i], right[i])
            else:
                x = compare_two_lists(left[i], right[i]) #Run the function on the 2 lists

    if x == "correct" or x == "incorrect": #If this has found a difference then return it
        return(x)
    elif x == None: #If x is none then one of the lists was empty
        if left_len < right_len:
            x = "correct"
            return(x)
        elif right_len < left_len:
            x = "incorrect"
            return(x)
    elif x == "unch": #If x is unch then it means the short list is equal to the start of the longer list
        #In both cases the discriminator is list length
        if left_len < right_len:
            x = "correct"
            return(x)
        elif right_len < left_len:
            x = "incorrect"
            return(x)

#Part 1 
correct_pairs = []
for i in range(0, len(pairs), 3): #Steps 3 at a time because haven't removed blank lines between pairs
    y = compare_two_lists(pairs[i], pairs[i+1])
    #print("Item 1", pairs[i])
    #print("Item 2", pairs[i+1])
    #print(y, "\n")
    if y == "correct":
        index = int((i / 3) + 1)
        correct_pairs.append(index)

print("Part 1:")
print(correct_pairs)
print(sum(correct_pairs))
print()


# Part 2 

# Translate the correct & incorrect return functions to a boolean so it can be used as a key 
def compare_as_bool(left, right):
    x = compare_two_lists(left, right)
    if x == "correct":
        return -1
    if x == "incorrect":
        return 1
    else:
        return 0

# Filter out the blank rows between pairs
pairs = [i for i in pairs if i != "space"]
pairs.append([[2]])
pairs.append([[6]])

# Sort using the custom function
sorted_list = sorted(pairs, key=functools.cmp_to_key(compare_as_bool)) 
#Note - because the function wraps integers into a list the original values of [[2]] and [[6]] are wrapped in an extra 2 layers of list
#The fix would be to go back and make the wrapping temporary rather than changing the original list
#print(*sorted_list, sep="\n")

index1, index2 = sorted_list.index([[[[2]]]]) + 1, sorted_list.index([[[[6]]]]) + 1

print("Part 2:")
print(index1, index2)
print(index1 * index2)

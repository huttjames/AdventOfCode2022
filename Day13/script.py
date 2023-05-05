import ast as ast
import functools as functools

with open('input.txt') as f:
    pairs = f.read().splitlines()

for i in range(len(pairs)):
    if pairs[i] == '':
        pairs[i] = "space"
    else:
        pairs[i] = ast.literal_eval(pairs[i])

# At the pair level, both are lists 
def compare_two_lists(left, right):
    left_len = len(left)
    right_len = len(right)
    x = "unch"
    #print("x is currently: ",x)

    if x == "unch":
        for i in range(min(left_len, right_len)):
            if x == "correct" or x == "incorrect":
                break
            else:
                #print(left[i],right[i])
                if type(left[i]) == int and type(right[i]) == int:
                    if left[i] < right[i]:
                        #print("correct")
                        x = "correct"
                        break
                
                    elif right[i] < left[i]:
                        #print("incorrect")
                        x = "incorrect"
                        break
                
                    else:
                        #print("equal")
                        #print("x is currently: ",x)
                        continue

                elif type(left[i]) == int and type(right[i]) == list:
                    left[i] = [left[i]].copy()
                    #print(left[i],right[i], type(left[i]), type(right[i]))
                    x = compare_two_lists(left[i], right[i])

                elif type(left[i]) == list and type(right[i]) == int:
                    right[i] = [right[i]].copy()
                    #print(left[i],right[i], type(left[i]), type(right[i]))
                    x = compare_two_lists(left[i], right[i])

                else:
                    #print(left[i],right[i], type(left[i]), type(right[i]))
                    x = compare_two_lists(left[i], right[i])

    #print("down here x is currently: ",x)
    if x == "correct" or x == "incorrect":
        #print("I spotted a changed X")
        return(x)
    elif x == None:
        if left_len < right_len:
            x = "correct"
            return(x)
        elif right_len < left_len:
            x = "incorrect"
            return(x)
    elif x == "unch":
        if left_len < right_len:
            x = "correct"
            return(x)
        elif right_len < left_len:
            x = "incorrect"
            return(x)

    #return(x)
        
correct_pairs = []
for i in range(0, len(pairs), 3):
    #print(i)
    y = compare_two_lists(pairs[i], pairs[i+1])
    print("Item 1", pairs[i])
    print("Item 2", pairs[i+1])
    print(y, "\n")
    if y == "correct":
        index = int((i / 3) + 1)
        correct_pairs.append(index)

#print(correct_pairs)
#print(sum(correct_pairs))

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

#print(pairs)
pairs = [i for i in pairs if i != "space"]
pairs.append([[2]])
pairs.append([[6]])
#print(pairs)

sorted_list = sorted(pairs, key=functools.cmp_to_key(compare_as_bool))

print(*sorted_list, sep="\n")


index1, index2 = sorted_list.index([[[[2]]]]) + 1, sorted_list.index([[[[6]]]]) + 1
print(index1, index2)

'''
def check_two_ints(left, right):
        if left < right:
            return "correct"
        elif right > left:
            return "incorrect"
        else: # They must be equal
            return "equal"

def confirm_both_lists(left,right):
    if type(left) == int and type(right) == int:
        return [False, left, right]
    elif type(left) == list and type(right) == list:
        return [True, left, right]
    elif type(left) == list and type(right) == int:
        return [True, left, [right]]
    elif type(left) == int and type(right) == list:
        return [True, [left], right]
    else:
        print("Flawed logic in confirm_both_lists")
        return

def check_two_lists(left, right):
    left_len = len(left)
    right_len = len(right)

    if left_len == 0:
        return "correct"
    elif right_len == 0:
        return "incorrect"
    else:
        for i in range(min(left_len, right_len)):
            if type(left[i]) == int and type(right[i]) == int:
                x = check_two_ints(left[i], right[i])
                if x != "equal":
                    return x


def check_values(left, right):

    x = confirm_both_lists(left, right)
    if not x[0]: # both are integers
        check_two_ints(x[1],x[2])
    else:
        print(x[1],[x[2]])
        check_values(x[1],x[2])

    

def compare_two_lists(list1, list2):
    if list1 == list2:
        return "equal"
    else:
        for i in range(min(len(list1), len(list2))):
            x = check_two_ints(list1[i], list2[i])
            if x == "equal":
                continue
            else:
                return x

    # if we reach here then then 1 list must be longer than the other, but the short list equals the first N elements of the long list

    if len(list1) < len(list2):
        return "correct"
    else:
        return "incorrect"



'''
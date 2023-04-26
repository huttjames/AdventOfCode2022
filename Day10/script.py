
with open('input.txt') as f:
    register = [0,1]
    
    for line in f:

        currentVal = register[-1]
        if line == "noop\n" or line == "noop":
            register.append(currentVal)

        else:
            instruction = line.split()
            additive = int(instruction[1])
            register.append(currentVal)
            register.append(currentVal + additive)

# Part 1 
signal = 0
for i in range(20, 240, 40):
    signal += i * register[i]

print(signal)

# Part 2 
for k in range(0,6):
    for i in range(0 + 40 * k,40 + 40 * k):
        registerVal = register[i+1]
        lst = list(range(i-1 - 40 * k, i+2 - 40 * k))

        if registerVal in lst:
            print("#", end="")
        else:
            print(" ", end="")
    print("")

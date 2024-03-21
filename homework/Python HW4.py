# List Slicing and Striding

# 2.1

main = [0]
i = 1

while i < 51:
    main.insert(i, i)
    i += 1

print(main)
# When I first tried to do this I did not use the .insert command, which had the list assignment index out of range. 

# 2.2

def square(list):

    i = 0

    for i in list:
        num_squared = list[i]
        squared = num_squared**2
        list[i] = squared
        i+=1

    return list

print(square(main))

# I forgot to reset the list to squared so the list did not change at all.

# 2.3

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def odd(list):

    listN = []

    for j in range(len(list)):

        check = list[j]
        double_check = check % 2

        if double_check != 0:
            listN.append(check)

    return listN

A = odd(listA)
B = odd(listB)
C = A + B

print(C)

# My first error was that I was iterating over the elements instead of the indexes which I fixed by turning the list into an int range. Then .insert was not working, so I switched to append to fix that error.

# 3.1

def five_by_five():
    fivexfive = []

    num = 1

    for i in range(5):
        row = []

        for j in range(5):
            row.append(num)
            num += 1
        fivexfive.append(row)

    for row in fivexfive:
        print(row)

five_by_five()

# Got this one first try!!

# 3.2

def five_by_five_nothree():
    fivexfive = []

    num = 1

    for i in range(5):
        row = []

        for j in range(5):
            if num % 3 != 0:
                row.append(num)
            else:
                row.append("?")
            num += 1
        fivexfive.append(row)

    for row in fivexfive:
        print(row)

five_by_five_nothree()

# Forgot a colon.

# 4 More list practice

lis = [ 1 , 1 , 2 , 3 , 4 , 4 ]

def duplicates(input):

    no_dupe = []

    for item in input:
        if item not in no_dupe:
            no_dupe.append(item)
    
    return no_dupe

print(duplicates(lis))

# Could not get it to iterrate properly then looked for if statements to help. Saw the not in and decided to use it.

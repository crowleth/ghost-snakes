# 1 Power of a Number

x = 5
y = 2

def exp(x,y):
    n_x = 1
    for _ in range(y):
        # The range function allows y to become iterable
        n_x = x*x
    return n_x

print(exp(x, y))

# 2 Minimum and Maximum

def min_max(lst):

    min = 1
    max = 1

    n1 = lst[0]
    n2 = lst[-1]

    for n in range(n1,n2):

        if lst[n] >= max:
            max = lst[n]
        
        if lst[n] <= min:
            min = lst[n]
    
    all = (min, max)

    print(all)

lst = [1,2,7,4,5]

min_max(lst)

# 3 Check Leap Year

def leap(year):

    checker = year % 4

    if checker == 0:
        
        return True
    
    else: 
        return False
    
year = 2001

print(leap(year))

# 4 Calculate BMI

def bmi(w,h):
    real = w/h**2
    return real
w = 100
h = 5
print(bmi(w,h))

# 5 Rotating Digits

def rotate(num):
    
    gibbus = num % 10
    doobus = num // 10
    reebus = str(gibbus) + str(doobus)
    return reebus

num = 223
print(rotate(num))

# 6 Max Min pt2

def min_for(list):

    min = list[0]

    for num in list:
        if num < min:
            min = num
    return min

def max_for(list):
    
    max = list[0]

    for num in list:
        if num > max:
            max = num
    return max

def min_while(list):
    
    min = list[0]
    i = 1

    while i < len(list):

        if list[i] < min:
            min = list[i]
        i += 1
    return min

def max_while(list):
   
    max = list[0]
    i = 1

    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max

list = [1,2,3,4,5,6,7,8,9,0]

print(min_for(list))
print(max_for(list))
print(min_while(list))
print(max_while(list))

# 7 Vowels

def num_vowels(word):

    vowels = ['a','e','i','o','u','A','E','I','O','U']
    the_vowels = 0

    for a in range(0, len(word)):

        for b in range(0, len(vowels)):

            if(word[a]==vowels[b]):
                the_vowels += 1

    return the_vowels

word = "the bad guy"
print(num_vowels(word))

# 8 Digital Root

def digital_root(z):
    
    into_string = str(z)
    len_string = len(into_string)
    sum = 0
    
    for i in range(0, len_string):
        sum+=(ord(into_string[i])-ord('0'))
    
    return sum

z = 12345
print(digital_root(z))

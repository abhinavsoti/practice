# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    v1 = a%2
    v2 = b%2
    v_remainder = v1+v2
    l_list = [a,b]
    l_list.sort()
    if v_remainder == 0:
        return l_list[0]
    elif v_remainder > 0:
        return l_list[1]

result = lesser_of_two_evens(2,4)
print (result)

result = lesser_of_two_evens(2,5)
print (result)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# Another way of implementing the same can be by splitting the string and loop through it function name -- string.split()

def animal_crackers(text):
    first_char = text[0]
    init_value = 0
    for char in text:
        if char == ' ':
            init_value = init_value + 1
        elif init_value == 1:
            second_char = char
            init_value = 0

    if first_char == second_char:
        return True
    else:
        return False
result = animal_crackers('Levelheaded Llama')
print (result)

result = animal_crackers('Crazy Kangaroo')
print (result)

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or n1+n2 == 20:
        return True
    else:
        return False

result = makes_twenty(20,10)
print (result)

result = makes_twenty(2,3)
print (result)

# LEVEL 1 PROBLEMS¶
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    count = 0
    new_name = ''
    for string in name:
        if count == 0 or count == 3:
            new_name = new_name + string.upper()
            count = count + 1
        else:
            new_name = new_name + string
            count = count + 1
    return new_name

# Check
result = old_macdonald('macdonald')
print (result)

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    l_list = text.split()
    reverse_list = []
    for item in l_list[::-1]:
        reverse_list.append(item)

    reversed_string = ' '.join(reverse_list)
    return reversed_string

# Check
print (master_yoda('I am home'))


# Check
print (master_yoda('We are ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if (abs(n) >= 90 and abs(n) <= 110) or (abs(n) >= 190 and abs(n) <= 210):
        return True
    else:
        return False

# Check
print (almost_there(104))

# Check
print (almost_there(150))

# Check
print (almost_there(209))

# Level 2 Problems

# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    init_count = 0
    for value in nums:
        if value == 3 and init_count == 1:
            return True
        elif value == 3 and init_count == 0:
            init_count = 1
        elif init_count == 1 and value <> 3:
            init_count = 0
    return False

# Check
print (has_33([1, 3, 3]))

# Check
print (has_33([1, 3, 1, 3]))

# Check
print (has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    new_string = ''
    for i in text:
        value = i*3
        new_string = new_string + value
    return new_string

# Check
print (paper_doll('Hello'))

# Check
print (paper_doll('Mississippi'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a, b, c):
    sum_value = a + b + c
    if sum_value > 21 and (a == 11 or b == 11 or c == 11):
        sum_value = sum_value - 10
        if sum_value <= 21:
            return sum_value
        else:
            return 'BUST'
    elif sum_value > 21:
        return 'BUST'
    else:
        return sum_value

# Check
blackjack(5,6,7)

# Check
blackjack(9,9,9)

# Check
blackjack(9,9,11)

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    init_cnt = 0
    sum_value = 0
    for num in arr:
        if num <> 6 and init_cnt == 0:
            sum_value = sum_value + num
        elif num == 6:
            init_cnt = 1
        elif num == 9 and init_cnt == 1:
            init_cnt = 0
    return sum_value

# Check
print (summer_69([1, 3, 5]))

# Check
print (summer_69([4, 5, 6, 7, 8, 9]))

# Check
print (summer_69([2, 1, 6, 9, 11]))

# CHALLENGING PROBLEMS
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    init_count = 0
    for agent in nums:
        if agent == 7 and init_count == 2:
            return True
        elif agent == 0 and (init_count == 0 or init_count == 1):
            init_count = init_count + 1
    return False

# Check
spy_game([1,2,4,0,0,7,5])

# Check
spy_game([1,0,2,4,0,5,7])

# Check
spy_game([1,7,2,0,4,5,0])

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.


def count_primes(num):
    init_count = 0
    i = 2
    while i <= num:
        if i == 2 or i == 3:
            init_count = init_count + 1
            i = i+1
        elif i > 3:
            j = 2
            prime_flag = 1
            while j <= i/2:
                if i%j == 0:
                    prime_flag = 0
                    break
                elif i%j != 0:
                    j=j+1
            if prime_flag == 1:
                init_count = init_count + 1
            i=i+1
    return init_count

print (count_primes(100))


# Just for fun:
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')
#
# out:   *
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".

def print_big(letter):
    letterDict = {"A": ['  *  ', ' * * ', '*****', '*   *', '*   *'],
                  "a": ['  *  ', ' * * ', '*****', '*   *', '*   *'],
                  "B": ['**** ', '*   *', '**** ', '*   *', '**** '],
                  "b": ['**** ', '*   *', '**** ', '*   *', '**** ']}
    letter_print = letterDict[letter]

    for val in letter_print:
        print(val)

print_big('a')
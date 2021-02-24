# Problem 1 Handle the exception thrown for below code by try and except block
# for i in ['a', 'b', 'c']:
#     print (i**2)

try:
    for i in ['a', 'b', 'c']:
        print (i**2)
except TypeError:
    print("Please pass numbers instead of characters")

# Problem 2 Handle the exception thrown for below code by try and except block. Then use a finally block to print 'All Done.'

try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print ('The denominator cannot be zero')
finally:
    print ('All Done.')

# Problem 3 - Write a function that asks for an integer and print the square of it. Use a while loop with a try. except, else block
# to account for incorrect inputs

def ask_for_int():
    while True:
        try:
            val = int(input('Please provide a number as input:'))
            print(val**2)
            break
        except:
            print ('Please provide a number')
            continue
        finally:
            print ('I am going to ask you again')

ask_for_int()
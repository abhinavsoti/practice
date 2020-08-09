# Dictionary example to store stock price for a given stock over a perriod of time

dict_stock_price_YesBank = {'YES':{'NSE': {'07302020': 11.90,'07292020': 12.35, '07282020': 12.20}, 'BSE': {'07302020': 11.80,'07292020': 12.15, '07282020': 12.00}}}

print (dict_stock_price_YesBank ['YES'] ['NSE'])

print (dict_stock_price_YesBank ['YES'] ['BSE'])

# Time to Start reading & writing text files

print ('\n***************** Reading test.txt Files *****************')

myfile = open('test.txt',mode = 'r')
contents = myfile.read()
myfile.seek(0)
contents2 = myfile.readlines()

print (contents)
print (contents2)

myfile.close()

print ('\n***************** Finished Reading test.txt Files *****************')

print ('\n***************** Another way of Reading/writing Files *****************')

with open('test.txt', mode = 'r') as my_newfile:
    content = my_newfile.read()

print ('Content of test.txt file is \n' + content)

with open('test_copy.txt', mode = 'w') as write_newfile:
    write_newfile.write('**************Creating copy of test.txt file**************\n')
    write_newfile.write(content)

with open('test_copy.txt', mode = 'r') as my_writtenfile:
    content_read = my_writtenfile.read()

print('Content of test_copy.txt file is \n' + content_read)

# Basic Practice: http://codingbat.com/python

# More Mathematical (and Harder) Practice:  https://projecteuler.net/archives

# List of Practice Problems: http://www.codeabbey.com/index/task_list


mystring = 'Hello World'
print(mystring)
print('Hello World')

for letter in mystring:
    print(letter)

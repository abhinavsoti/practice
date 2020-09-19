import datetime

def myfunc(strin):
    j=0
    str_out = ''
    for i in strin:
       if j%2 == 0:
           str_out = str_out + str(i).upper()
       else:
           str_out = str_out + str(i).lower()
       j = j+1
    return str_out


v_start = datetime.datetime.now()
print (v_start)
result = myfunc('today is the most important day of my life. i might end up inventing something new. Hopefully, I will pull this through and ensure that I am contributing something good to the society. Repeating again, today is the most important day of my life. i might end up inventing something new. Hopefully, I will pull this through and ensure that I am contributing something good to the society. This is hilarious, the program should take more than 1 second atleast')
v_stop = datetime.datetime.now()
print (v_stop)
print (result)
v_execution_time = (v_stop - v_start).total_seconds()
print ('The program got executed in ' + str(v_execution_time) + ' seconds')


text = 'Levelheader Llama'
first_char = text[0]
print (first_char)

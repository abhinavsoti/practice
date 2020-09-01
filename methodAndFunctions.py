######################################################################################
# Script Name: methodAndFunctions                                 #
# Description: This script will print the user executing the program and will also   #
#              keep checking the current system processes running at the moment.     #
# Version    : 1.0                                                                   #
######################################################################################

def check_even_list(inp_list):
    out_list = []
    for item in inp_list:
        if type(item) == int:
            if item % 2 == 0:
                out_list.append(item)
        else:
            print ('This value is not an integer: ' + item)
    return out_list



l = [1,2,3,4,6,5,7,9,8,10,'a','b',12,'c',20,'d','22']

result = check_even_list(l)
print ('Following are the even numbers in the list: ' + str(result))

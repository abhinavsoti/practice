######################################################################################
# Script Name: GetUserDetails_checkAllrunningProcess                                 #
# Description: This script will print the user executing the program and will also   #
#              keep checking the current system processes running at the moment.     #
# Version    : 1.0                                                                   #
######################################################################################

import datetime
import getpass
import psutil
import time

username = getpass.getuser()
print('execution starts now at ' + str(datetime.datetime.now()) + ' by ' + username)

print ('Following process are running at the moment at ' + str(datetime.datetime.now()))

i=0

while i < 20:
    process_list = [p.name() for p in psutil.process_iter() if p.name() == 'notepad.exe']
    for running_process in process_list:
        print(running_process)
    print ('Going to sleep for 3 seconds')
    time.sleep(3)
    i = i+1
    print (i)

print ('execution completed at ' + str(datetime.datetime.now()) + ' by ' + username)
#!/usr/bin/env python

import os 
import subprocess 

#String Resources
cmd = ['gem','query','-i','calabash-android']
success_str = '\nHooray feature folder found ! confirming contents ........\n'
sucess_str_two = '\nHooray! You have Calabash Android installed on your system  \n' 
fail_str = '\nfeature folder not found!!! \n Please Run script  from folder where the feature folder lives \n Else do you want to initialize calabash at the current location ?? y/n  ' 
#Checking if calabash is installed 
shell_obj = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
shell_output , shell_error = shell_obj.communicate()
if shell_output == 'true' or  shell_output == 'True' :
	print (sucess_str_two)

#Checking current directory 
loc = os.getcwd()
filecont=os.listdir(loc)
flag = 0 
for  n in filecont :
	#print(n)	
        if n == 'features' :
        	print(sucess_str)
         	flag = 1 	
 
if flag == 0 :
	print (fail_str)
	        	



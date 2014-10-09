#!/usr/bin/env python

import os 

loc = os.getcwd()
filecont=os.listdir(loc)
flag = 0 
for  n in filecont :
	print(n)	
        if n == 'features' :
        	print('\nHooray feature file found ! confirming contents ........\n' )
         	flag = 1 	
 
if flag == 0 :
	print("hi")        	




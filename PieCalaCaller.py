#!/usr/bin/env python

import os 
import subprocess 

#String Resources
gem_cmd = ['gem','query','-i','-n','calabash-android']
cala_cmd = ['gem','install','calabash-android','--verbose']
success_str = '\nHooray feature folder found ! confirming contents ........\n'


sucess_str_two = '\nHooray! You have Calabash Android installed on your system  \n' 

fail_str = '\nfeature folder not found!!! \n Please Run script  from folder where the feature folder lives \n Else do you want to initialize calabash at the current location ?? y/n  ' 

install_prompt = '\nDo you want to install calabash-android via the internet ? y/n?\n'
#Checking if calabash is installed

 
def CalaChecker () :

        shell_obj = subprocess.Popen(gem_cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        shell_output , shell_error = shell_obj.communicate()

        shell_output=str(shell_output)
        
        #subprocess.call("gem query -i -n calabash",shell=True)
        if shell_output == 'true\n' or  shell_output == 'True\n' :
            print(sucess_str_two)
        else: 
            print(install_prompt)
            CalaInstaller()
            

#install calabash to current system

def CalaInstaller():  
        
        subprocess.call("gem install calabash-android --verbose",shell=True)

           
        
       
 
#Checking current directory 

def CalaDirChecker():

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





print("\nWELCOME\n!")
CalaDirChecker()
CalaChecker()
        


        





                        

	        	







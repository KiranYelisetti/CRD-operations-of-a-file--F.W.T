#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import code1 as x 
#importing the main file("code" is the name of the file I have used) as a library 


x.create("Ravi",22)
#to create a key with key_name,value given and with no time-to-live property


x.create("src",85,4800) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("Ravi")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("Ravi",22)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


x.modify("Ravi",25)
#it replaces the initial value of the respective key with new value 

 
x.delete("Ravi")
#it deletes the respective key and its value from the database(memory is also freed)



#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB


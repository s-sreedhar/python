# import the time module 
import time 

# define the countdown func. 
def countdown(t): 
	
#Use divmod() to calculate the number of minutes and seconds.
	
#Using end = ‘\r’ we force the cursor to go back to the start of the screen (carriage return) so that the next line printed will overwrite the previous one.

	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1) 
		t -= 1
	
	print('Fire in the hole!!') 


# input time in seconds 
t = input("Enter the time in seconds: ") 

# function call 
countdown(int(200)) 

import time

print("Epoch to GMT Conversion")
#epoch_time = time.time() #To test it with the second amount from January 1, 1970 till now.
epoch_time = 86399 # The amount of seconds in a single day

# Dividing epoch_time by 86400 to get the days
days = epoch_time // 86400
# Dividing epoch_time by 3600 to get the hours
hours = (epoch_time % 86400) // 3600
# Dividing the remainder of the above division by 60 to get the minutes
minutes = (epoch_time % 3600) // 60

# Dividing the remainder of the above division by 60 to get the seconds
seconds = (epoch_time % 3600) % 60

print("The Time is: %d:%d:%d:%d" % (days, hours, minutes, seconds))

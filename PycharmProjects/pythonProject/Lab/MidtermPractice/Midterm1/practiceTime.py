import time

time = time.time()

print(time) # Unix Epoch Time, counting seconds from 1970-01-01 till the present time
print(type(time))
# convert seconds to hours, minutes, and seconds
total_seconds = int(time)
print(total_seconds)
current_second = total_seconds % 60

total_minutes = total_seconds // 60
current_minute = total_minutes % 60

total_hours = total_minutes // 60
current_hour = total_hours % 24

#beirut time zone is GMT+2
print("Current time is", current_hour + 2, ":", current_minute, ":", current_second, "GMT")
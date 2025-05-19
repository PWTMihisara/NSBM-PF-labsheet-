def time_to_seconds(hours,minites,seconds):
    total_second = (hours%2) * 3600 + minites * 60 + seconds
    return total_second

def seconds_between_time(hours1, minutes1, seconds1, hours2, minutes2, seconds2):
    time1_seconds = time_to_seconds(hours1, minutes1, seconds1)
    time2_seconds = time_to_seconds(hours2, minutes2, seconds2)
    return(time1_seconds - time2_seconds)

hours1, minutes1, seconds1 = 3, 20, 40
hours2, minutes2, seconds2 = 2, 30, 10

result = seconds_between_time(hours1, minutes1, seconds1, hours2, minutes2, seconds2)
print(f"the soconds between two times is: {result}") 
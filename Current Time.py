import time
#we imported the time module
currentTime = time.time()
print(currentTime)
#Here we printed the current time which starts from 01-01-1970 (00:00) till date/time
totalseconds = int(currentTime)
print(totalseconds)
#here we took the integar value of the current time which was in seconds
currentsecond = totalseconds%60
print(currentsecond)
#Here we divided the value calculated above and divided it by 60 then because we were
#concerned about getting the remainder we got (How we got it - we took the remainder in
#points and multiplied it with 60
#to get the integar value of the remainder
totalminutes = totalseconds // 60
print(totalminutes)
#Here we divided the seconds with 60 to get the minutes - the integar value of minutes
currentMinute = totalminutes % 60
print(currentMinute)
#Here we divided the total minutes by 60 to get he hours and since we want to get to
# the current minutes so we apply this formula (what this formula does is that
#it takes the value after points and multiplies it by 60 to get the integar
#value of the remainder
totalHours = totalminutes // 60
print(totalHours)
#Here simply we apply // to get the integar value of the hours
currentHour = totalHours % 24
#This fomula tell us the current hour by dividing he total hours by 24 and then
#picking up the reminder (what the formula does is that it takes the remainder in points
#and multiplies it with)
print(totalseconds)
print(totalminutes)
print(totalHours)


print("Current time is", currentHour, ":", currentMinute, ":", currentsecond, "GMT")




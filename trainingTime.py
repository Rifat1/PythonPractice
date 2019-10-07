

startTime=str(input("Please enter the start time: "))

endTime=str(input("Please enter the end time: "))

startHour=int(startTime[0:2])
startMins=int(startTime[2:])

endHour=int(endTime[0:2])
endMins=int(endTime[2:])

if(endMins>startMins) or (endMins==startMins):
    totalMins=(endMins-startMins)
    totalHour=(endHour-startHour)
else:
    totalMins=(startMins-endMins)
    totalHour=(endHour-startHour)-1

# print(startTime)
# print(endTime)
print("The total training time is {} hours {} minutes".format(totalHour,totalMins))


# vi ~/.bash_profile  
# alias python='/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'  
# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
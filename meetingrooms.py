def canAttendMeetings( intervals):
    #[[0,30],[5,10],[15,20]]
    intervals.sort(key=lambda x:x[0])
    print(intervals)
    flag=True
    for i in range(1,len(intervals)):
        if intervals[i][0]>=intervals[i-1][0] and intervals[i][0]<intervals[i-1][1]:
            #print(intervals[i][0],intervals[i-1][0],intervals[i][0],intervals[i-1][1])
            return False
        else:
            flag=True
    return flag


    print(intervals)
print(canAttendMeetings([[13,15],[1,13]]))
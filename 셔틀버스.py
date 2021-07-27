from collections import deque

n, t, m, timetable = 		1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]

for i in range(len(timetable)):
    temp = timetable[i].split(':')
    time = int(temp[0]) * 60 + int(temp[1])
    timetable[i] = time

print(timetable)
timetable = sorted(timetable)
last_time = (60*9) + (n-1)*t


for i in range(n):
    #print(i, timetable, 'start')
    if len(timetable) < m:
        print( '%02d:%02d'%(last_time//60,last_time%60) )
        break
    if i == n - 1:
        if timetable[0] <= last_time: last_time = timetable[m-1] - 1
        print( '%02d:%02d'%(last_time//60,last_time%60))
        break

    for j in range(m-1, -1, -1):
        bus_arrive = 540 + (i * t)
        if timetable[j] <= bus_arrive:
                del timetable[j]
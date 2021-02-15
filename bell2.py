from playsound import playsound
import time

#timetable = {(19,25):1, (19,50):1, (20,11):1, (20,45):1}
timetable = {(8,0):1,(8,45):1,(9,0):1,(9,45):1,(10,0):1,(10,45):1,(11,0):1,(11,45):1,
            (12,0):1,(12,45):1,(13,0):1,(13,45):1,(14,0):1,(14,45):1,(15,0):1,(15,45):1,
            (16,0):1,(16,45):1,(17,0):1,(17,45):1,(18,0):1,(18,45):1,(19,0):1,(19,45):1,
            (20,0):1,(20,45):1,(21,0):1,(21,45):1,(22,0):1,(22,45):1}
 
def ring():
    print("ring",time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
    playsound('school_bell.mp3')
 
def itemcheck(_time):
    if _time[0] == time.localtime().tm_hour and _time[1] == time.localtime().tm_min:
        ring()
        timetable[_time] = 0
    #before
    elif _time[0] > time.localtime().tm_hour or ( _time[0] == time.localtime().tm_hour and _time[1] > time.localtime().tm_min ): #before ring
        gaptime=(_time[0]-time.localtime().tm_hour)*60+ (_time[1] - time.localtime().tm_min)
#        global breakflag
        print("before ring", gaptime)
        time.sleep(gaptime*60 - time.localtime().tm_sec)
        if gaptime < 40:
            ring()
        else:
            playsound('start.mp3')
        timetable[_time] = 0
    #after
    elif timetable[_time] :
        timetable[_time] = 0

print("start",time.localtime().tm_hour, time.localtime().tm_min)
for _time in sorted (timetable.keys()) :
        #print(_time[0], _time[1])
    itemcheck(_time)
print("end")

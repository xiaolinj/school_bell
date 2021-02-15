from playsound import playsound
import time

timetable = {(19,25):1, (19,50):1, (20,00):1, (20,45):1}
#timetable = {(8,0):1,(8,45):0,(8,50):1,(9,35):0,
#             (9,50):1,(10,35):0,(10,40):1,(11,25):0,
#             (11,30):1,(12,15):0,(13,30):1,(14,15):0,
#             (14,20):1,(15,5):0,(15,20):0,(16,5):0,
#             (16,10):1,(16,55):0,(18,30):1,(19,15):0,
#             (19,20):1,(20,5):0,(20,10):1,(20,55):0}
 
def ring():
    print("ring",time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
    playsound('bells.mp3')
 
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
        ring()
        timetable[_time] = 0
    #after
    elif timetable[_time] :
        print("pass")
        #ring()
        timetable[_time] = 0

print("start",time.localtime().tm_hour, time.localtime().tm_min)
for _time in sorted (timetable.keys()) :
        #print(_time[0], _time[1])
    itemcheck(_time)
print("end")

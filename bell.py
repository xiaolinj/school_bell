import time
from playsound import playsound
import csv
import sys

def get_timetable():
    with open('timetable.csv', 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    return rows


def bell(list_timetable):
    class_begin = []
    class_end = []
    for line in list_timetable[1:]:
        class_begin.append(line[1]) 
        class_end.append(line[2])
    length = len(list_timetable) - 1
    class_index = 0
    while class_index < length:
        now_localtime = time.strftime('%H:%M:%S', time.localtime())
        if now_localtime in class_begin:
            playsound('bells.mp3')
        if now_localtime in class_end:
            playsound('bells.mp3')
        class_index = class_begin.index(now_localtime) + 1
            

if __name__ == "__main__":
    print('running')
    bell(get_timetable())
    print('exit')
    sys.exit()

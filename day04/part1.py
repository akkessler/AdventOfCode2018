import numpy as np
import re
from datetime import datetime

time_format = '[%Y-%m-%d %H:%M]'
guard_regex = r"Guard #(\d+) begins shift"

event_offset = 19
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

events = []
for line in lines:
    ts = datetime.strptime(line[:event_offset].strip(), time_format)
    events.append((ts, line[event_offset:].strip()))
events.sort()

guards = {}
curr_guard = None
sleep_start = None
for ts, text in events:
    if text == 'falls asleep':
        sleep_start = ts
    elif text == 'wakes up':
        minute_start = sleep_start.minute
        minute_end = ts.minute
        minutes_asleep = minute_end - minute_start
        guards[curr_guard]['minutesAsleep'] += minutes_asleep
        guards[curr_guard]['minuteFrequency'][minute_start:minute_end] += 1
        sleep_start = None
    else:
        m = re.match(guard_regex, text)
        curr_guard = int(m[1])
        if curr_guard not in guards:
            guards[curr_guard] = {
                'minutesAsleep': 0,
                'minuteFrequency': np.zeros(60)
            }

best_guard = None
max_asleep = -1
for key, value in guards.items():
    if value['minutesAsleep'] > max_asleep:
        max_asleep = value['minutesAsleep']
        best_guard = key

best_minute = None
max_freq = -1
freqs = guards[best_guard]['minuteFrequency']
for i in range(60):
    m = freqs[i]
    if m > max_freq:
        max_freq = m
        best_minute = i

print(best_guard)
print(best_minute)
print(best_guard * best_minute)
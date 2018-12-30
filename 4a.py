from collections import defaultdict
from datetime import datetime
import fileinput
from operator import itemgetter
import re

INPUT_RE = re.compile(r'\[([^\]]+)\] (.+)')
ID_RE = re.compile(r'Guard #(\d+) begins shift')

class GuardHour:
  def __init__(self, date, id_):
    self.date = date
    self.id_ = id_
    self._minutes = [0] * 60
    self._prev_minute = None

  def start_sleep(self, minute):
    self._prev_minute = minute

  def end_sleep(self, minute):
    if (self._prev_minute is None):
      raise ValueError('Attempt to set end minute for guard without start %s' %
                      (self.date, self.id_))
    for i in range(self._prev_minute,
                   self._prev_minute + (minute - self._prev_minute)):
      self._minutes[i] = 1
    self._prev_minute = None

  def total_sleep_minutes(self):
    return sum(self._minutes)

  def is_asleep(self, minute):
    return self._minutes[minute] == 1

def most_slept_minute(guard_hours):
  minute_tallies = defaultdict(int)
  for hour in guard_hours:
    for i in range(60):
      if hour.is_asleep(i):
        minute_tallies[i] += 1
  sort_ = sorted(list(minute_tallies.items()), key=itemgetter(1), reverse=True)
  return sort_[0][0]

data = []
for line in fileinput.input():
  md = INPUT_RE.match(line.strip())
  if not md:
    raise ValueError('Line (%s) did not match regex' % line)
  data.append((md.group(1), md.group(2)))

timed_data = [(datetime.strptime(d[0], '%Y-%m-%d %H:%M'), d[1]) for d in data]
sorted_time_data = sorted(timed_data, key=itemgetter(0))

guard_hours = defaultdict(list)
hour = None
for td in sorted_time_data:
  md = ID_RE.match(td[1])
  if md:
    # Store the previously completed hour.
    if hour is not None:
      guard_hours[hour.id_].append(hour)

    # Create a new hour for this guard.
    id_ = md.group(1)
    hour = GuardHour(td[0].date, id_)
  else:
    if td[1] == 'falls asleep':
      hour.start_sleep(td[0].minute)
    elif td[1] == 'wakes up':
      hour.end_sleep(td[0].minute)
    else:
      raise ValueError('Unrecognized input: %s' % td[1])

total_minutes = []
for id_, gh in guard_hours.items():
  total = 0
  for hour in gh:
    total += hour.total_sleep_minutes()
  total_minutes.append((id_, total))

sorted_minutes = sorted(total_minutes, key=itemgetter(1), reverse=True)
most_minutes = sorted_minutes[0]

guard_id = most_minutes[0]
hours = guard_hours[guard_id]
print(int(guard_id) * most_slept_minute(hours))

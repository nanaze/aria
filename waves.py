import math

def sine(time):
  return math.sin(2 * math.pi * time)

def square(time):
  assert time >= 0

  time, _ = math.modf(time)

  if time < 0:
    time = 1 + time

  if time < 0.5:
    return 1

  return -1

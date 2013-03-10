def map_amplitude(wave_func, map_func):
  return lambda t: map_func(wave_func(t))    

def scale_amplitude(func, multiplier):
  mult_func = lambda amp: amp * multiplier    
  return lambda s: mult_func(func(s))

def map_rate(wave_func, map_func):
  return lambda t: wave_func(map_func(t))

def scale_rate(func, multiplier):
  return map_rate(func, lambda t: t * multiplier)



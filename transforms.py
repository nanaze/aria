def map_amplitude(wave_func, map_func):
  return lambda t: map_func(wave_func(t))    

def scale_amplitude(func, multiplier):
  mult_func = lambda amp: amp * multiplier    
  return lambda s: mult_func(func(s))



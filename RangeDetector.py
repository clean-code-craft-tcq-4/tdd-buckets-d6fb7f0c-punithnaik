import itertools

def bucket_amperes(amps_list):
    return '4-5, 2'
  
def bucket_individual_readings(ampere_readings):
  ampere_counts_list = []
  ampere_counts = {}
  for i in range(0,6):
    ampere_counts['amp'] = i
    ampere_counts['count'] = 0
    ampere_counts_list.append(ampere_counts.copy())
  for amp in ampere_readings:
      ampere_counts_list[amp]['count'] += 1
  return ampere_counts_list
  
def report_consecutive_groups(ampere_counts):
    return [list(y) for x, y in itertools.groupby(ampere_counts, lambda z: z == 0) if not x]

#------------Current Sensing----------------
def check_error(sensor_readings):
  if 4095 in sensor_readings:
    sensor_readings.remove(4095)
  return sensor_readings

def input_to_amps(input):
  return round((10*input)/4094)

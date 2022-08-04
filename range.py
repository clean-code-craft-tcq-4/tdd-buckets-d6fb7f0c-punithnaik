
def check_range(value_list):
  count = 1
  for i in range(len(value_list)-1):
    if value_list[i] == value_list[i+1]-1:
      count = count+1
  return str(value_list[0]) + '-' + str(value_list[-1]) + ',' + str(count)

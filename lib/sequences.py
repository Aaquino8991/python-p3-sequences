def print_fibonacci(length):
  list = []
  
  if length == 0:
    print(list)
  elif length == 1:
    list.append(0)
    print(list)
  elif length > 1:
    count = 2
    list.append(0)
    list.append(1)
    while count < length:
      last_num = list[-1]
      second_to_last = list[-2]
      next_number = last_num + second_to_last
      list.append(next_number)
      count += 1
      
    print(list)
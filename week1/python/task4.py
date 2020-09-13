def is_leap(year):
  pass
  if year % 400 ==0:
    return True
  else:
    if year % 100!=0 and year %4==0:
      return True
    else:
      return False
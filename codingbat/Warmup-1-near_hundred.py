def near_hundred(n):
  near = 0
  if n < 100:
    near = 100 - n
  elif n>100:
    if (n-100) > 10:
      near = 200 - n
    else:
      near = n-100
  elif n > 200:
    near = n - 200
  
  if abs(near) <= 10:
    return True
  else:
    return False

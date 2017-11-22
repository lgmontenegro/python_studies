def front_times(str, n):
  if len(str) > 3:
    return str[:3]*abs(n)
  else:
    return str*abs(n)

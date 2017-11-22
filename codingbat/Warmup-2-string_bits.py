def string_bits(str):
  x=1
  ret=""
  while x<=len(str):
    ret = ret + str[x-1:x]
    x = x+2
  return ret


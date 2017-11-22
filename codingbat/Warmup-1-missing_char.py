def missing_char(str, n):
  lengthStr = len(str)
  if n == 0:
    return str[1:]
  if n <= (lengthStr-1):
    str1 = str[0:n]
    str2 = str[n+1:lengthStr]
    return str1+str2
  else:
    return false

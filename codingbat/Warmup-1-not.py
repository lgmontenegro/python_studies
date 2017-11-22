def not_string(str):
  find = str.find('not')
  if find == 0:
    return str
  else:
    return 'not ' + str

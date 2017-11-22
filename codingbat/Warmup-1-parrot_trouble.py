def parrot_trouble(talking, hour):
  if (hour<7) or (hour>20):
    if(talking):
      return True
    else:
      return False
  else:
    return False
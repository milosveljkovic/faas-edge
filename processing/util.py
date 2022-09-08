def removeNaNs(sd):
  for i,x in enumerate(sd):
    if not sd[i]:
      sd[i] = "-1"
  return sd

def formatAll(sd):
  for i,x in enumerate(sd):
    if i>0 and i<10:
      x=float(sd[i])
      sd[i] = format(x,'.8f')
  return sd
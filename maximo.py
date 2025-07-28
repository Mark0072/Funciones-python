def maximo(a,b,c):
  if a > b and a > c:
    return f"{a} es el mayor numero"
  
  elif b > a and a > c:
    return f"{b} es el numero mayor" 
  
  else:
      return f"{c} es el numero mayor" 
  
print(maximo(1,5,7))
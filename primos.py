def primos(n):
  
  if n <= 1:
    return False

  
  if n == 2:
    return True



  
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False  

  return True  


print(primos(7))   
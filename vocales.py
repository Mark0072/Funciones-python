def vocales(s):
  
  vocal = "aeiou"
  contado = 0
  for i in s:
    if i in vocal:
      contado += 1
  
  return contado


print(vocales("Hola bro"))

    
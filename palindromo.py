def palindromo(s):
  reverse = "".join(reversed(s))
  

  if s == reverse:
    return "Yes"
  else:
    return "No"
  

print(palindromo("333"))

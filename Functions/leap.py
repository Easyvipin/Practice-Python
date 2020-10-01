def leap_year(year):
  if year < 1900:
    return "Please Enter a year after 1900 ONLY"
  leap = False
  if year % 4 == 0:
    leap = True 
    if year % 100 == 0:
    leap = False
      if year % 400 ==0:
      leap = True 
  return leap 

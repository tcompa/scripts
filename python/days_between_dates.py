from datetime import date

today = date.today()
deadline = date(2016, 7, 15)
print (deadline - today).days

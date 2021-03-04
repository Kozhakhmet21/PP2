from datetime import datetime
now=datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.year)
print(now.strftime("%d:%m:%Y %H:%M"))
print(now.strftime("%A"))
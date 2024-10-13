from datetime import datetime,time,timedelta,date


print(datetime.now())
print(datetime.utcnow())
print(date.today())

x=datetime.now()
print(x.strftime('%Y:%m:%d %H-%M-%S'))

print(x+timedelta(days=1))
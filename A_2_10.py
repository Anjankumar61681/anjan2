from datetime import datetime
dt=datetime.today();
print(dt)
d1=dt.strftime("%d-%M-%Y and %h:%M:%p")
print(d1)

d1=dt.strftime("%d %B %Y")
print(d1)
d1=dt.strftime("%I:%M %p")
print(d1)

d1=dt.strftime("%d/%b/%y")
print(d1)

from datetime import datetime,timedelta

now = datetime.now()
mcrsec=now.replace(microsecond=0)
print("today:",mcrsec)
from datetime import datetime,timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow= today + timedelta(days=1)
print("yesterday:", yesterday.strftime("%Y-%B-%d"))
print("today:", today.strftime("%Y-%B-%d"))
print("tomorrow:", tomorrow.strftime("%Y-%B-%d"))
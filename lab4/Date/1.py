from datetime import datetime,timedelta

current = datetime.now()
another_date = current - timedelta(days=5)

print("current date",another_date.strftime("%Y-%B-%d"))

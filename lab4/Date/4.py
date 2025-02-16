from datetime import datetime,timedelta

today = datetime.now()
tomorrow= today + timedelta(days=1)
difference = abs((tomorrow - today).total_seconds())

print("Difference in sec: ",difference) 


#or
# date1_s = input("Enter first date (YYYY-MM-DD): ")
# date2_s = input("Enter second date (YYYY-MM-DD): ")

# date1 = datetime.strptime(date1_str, "%Y-%m-%d")
# date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# difference = abs((date2 - date1).total_seconds())

# print("Difference in seconds:", difference)
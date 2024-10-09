from datetime import datetime, timedelta

current_date = datetime.now()
date_five_days_ago = current_date - timedelta(days=5)
print("Date five days ago:", date_five_days_ago)

yesterday = current_date - timedelta(days=1)
today = current_date
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

datetime_without_microseconds = current_date.replace(microsecond=0)
print("Datetime without microseconds:", datetime_without_microseconds)

date1 = datetime(2024, 10, 1)
date2 = datetime(2024, 10, 9)
difference_in_seconds = (date2 - date1).total_seconds()
print("Difference in seconds:", difference_in_seconds)

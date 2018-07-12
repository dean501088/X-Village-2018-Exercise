import datetime

def print_next_day():
    a=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    return a
print(print_next_day())


#alternative
import datetime
(datetime.date.today() + datetime.timedelta(days=1)).isoformat()
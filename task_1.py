from datetime import datetime


def get_days_from_today(your_date):
    datetime_date = datetime.strptime(your_date, "%Y-%m-%d")
    today = datetime.today()
    days_from_today = (datetime_date - today).days

    return days_from_today

while True:
    your_date = input("Enter data in format 'РРРР-ММ-ДД': ")
    try:
        datetime_date = datetime.strptime(your_date, "%Y-%m-%d")
        if datetime_date:
            break
    except:
        print(f"{your_date} has invalid format, please enter date in format 'РРРР-ММ-ДД': ")

print(get_days_from_today(your_date), " DAYS") 




 
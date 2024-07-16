from datetime import datetime


def get_days_from_today(your_date):
    while True:
        try:
            datetime_date = datetime.strptime(your_date, "%Y-%m-%d")
            if datetime_date:
                break
        except:
            print(f"{your_date} has invalid format, please enter date in format 'РРРР-ММ-ДД': ")
            your_date = input("Enter data in format 'РРРР-ММ-ДД': ")
    datetime_date = datetime.strptime(your_date, "%Y-%m-%d").date()
    today = datetime.today().date()
    days_from_today = (datetime_date - today).days

    return days_from_today


your_date = input("Enter data in format 'РРРР-ММ-ДД': ")
print(get_days_from_today(your_date), " DAYS") 
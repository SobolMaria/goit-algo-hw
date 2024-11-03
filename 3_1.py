from datetime import datetime


def get_days_from_today(your_date):
    today = datetime.today().date()
    try:
        datetime_date = datetime.strptime(your_date, "%Y-%m-%d").date()
    except:
        return print(f"{your_date} has invalid format")
    
    days_from_today = (datetime_date - today).days
    
    print(f"{days_from_today} days")
    
    return days_from_today
        



your_date = input("Enter data in format 'РРРР-ММ-ДД': ")
get_days_from_today(your_date)

from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        difference = (today - target_date).days
        return difference
    except ValueError:
        return "неправильний формат дати"

result = get_days_from_today("2024-10-02")
print(result)

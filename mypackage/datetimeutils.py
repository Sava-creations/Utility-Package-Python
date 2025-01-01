from datetime import datetime, timedelta

def get_current_date():
    return datetime.now().date()                            # Returns only the date part (e.g., 2024-12-31)

def get_current_time():
    return datetime.now().time()                            # Returns only the time part (e.g., 23:59:59.123456)

def get_current_datetime():
    return datetime.now()                                   # Returns full date and time (e.g., 2024-12-31 23:59:59.123456)



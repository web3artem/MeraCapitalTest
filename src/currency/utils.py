from datetime import datetime

def convert_datetime_to_unix(date: str) -> int:
    try:
        dt = datetime.strptime(date, "%d-%m-%Y")
        print(dt)
        return int(dt.timestamp())

    except ValueError as e:
        return None

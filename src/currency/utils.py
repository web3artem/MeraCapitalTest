from datetime import datetime

from fastapi import HTTPException


def convert_datetime_to_unix(date: str) -> int:
    try:
        dt = datetime.strptime(date, "%d-%m-%Y")
        print(dt)
        return int(dt.timestamp())

    except ValueError as e:
        raise HTTPException(status_code=404, detail="Дата должна быть в UNIX формате либо DD-MM-YY")

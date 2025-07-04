import pytz # type: ignore

def convert_to_timezone(dt, tz_str="Asia/Kolkata"):
    tz = pytz.timezone(tz_str)
    return dt.astimezone(tz)

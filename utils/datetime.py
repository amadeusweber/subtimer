# Imports
import datetime

# Functions
def time_total_seconds(time:datetime.time) -> float:
    return (
        time.hour * 3600 +
        time.minute * 60 +
        time.second +
        time.microsecond / 1e6
    )

def time_from_seconds(sec:float) -> datetime.time:
    return (datetime.datetime.min + datetime.timedelta(seconds=sec)).time()

def strftime_hmsmilli(time:datetime.time) -> str:
    return time.strftime("%H:%M:%S") + f".{time.microsecond // 1000:03d}"

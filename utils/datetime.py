# Imports
import datetime

# Logging
import logging
logger = logging.getLogger(__name__)

# Functions
def time_total_seconds(time:datetime.time) -> float:
    seconds = (
        time.hour * 3600 +
        time.minute * 60 +
        time.second +
        time.microsecond / 1e6
    )
    logger.debug(f"{time} -> {seconds}")
    return seconds

def time_from_seconds(sec:float) -> datetime.time:
    time = (datetime.datetime.min + datetime.timedelta(seconds=sec)).time()
    logger.debug(f"{sec} -> {time}")
    return time

def strftime_hmsmilli(time:datetime.time) -> str:
    result = time.strftime("%H:%M:%S") + f".{time.microsecond // 1000:03d}"
    logger.debug(f"{time} -> {result}")
    return result

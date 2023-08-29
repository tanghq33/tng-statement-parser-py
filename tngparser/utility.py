from typing import List
import re
import logging
import sys
from datetime import datetime

def extract_convert_date_range(value: str) -> List['str']:
    date_pattern = r"\d{2}-\d{2}-\d{4}"
    dates = re.findall(date_pattern, value)

    formatted_dates = []
    for date_str in dates:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        formatted_dates.append(formatted_date)

    return formatted_dates

def init_logger():    #Create a logger named ‘app’
    logger = logging.getLogger('app')
    #Set the threshold logging level of the logger to INFO
    logger.setLevel(logging.DEBUG)
    #Create a stream-based handler that writes the log entries    #into the standard output stream
    handler = logging.StreamHandler(sys.stdout)
    #Create a formatter for the logs
    formatter = logging.Formatter('%(created)f %(levelname)s %(name)s %(module)s %(message)s')
        #Set the created formatter as the formatter of the handler    handler.setFormatter(formatter)
    #Add the created handler to this logger
    logger.addHandler(handler)
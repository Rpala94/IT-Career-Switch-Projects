import logging
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
        
def division():
  try:
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
  except ValueError:
    return None
  if divisor == 0:
    return None
  else:
    return dividend/divisor
result = division()
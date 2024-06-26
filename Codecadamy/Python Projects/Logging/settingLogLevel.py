import logging
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)
        
def division():
  logger.debug("Starting Division!")
  try:
    dividend = float(input("Enter the dividend: " ))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
  except SyntaxError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return None
  if divisor == 0:
    logger.error("Attempting to divide by 0!")
    return None
  else:
    return dividend/divisor
result = division()
if result == None:
 logger.warning("The result value is None!")
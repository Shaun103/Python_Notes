import logging
import time 

# Create logger

logging.basicConfig(filename = "/Users/User/Desktop/Python/Python_Socratica/Exceptions/problems.txt", level = logging.DEBUG)

logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""

    start_time = time.time()  # record the time when used
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data 
    except FileNotFoundError as err:
        logger.error(err)
        raise 
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time  # subtracts the start and stop time
        logger.info("Time required for {file} = {time}".format(file=path, time = dt))

path = '/Users/User/Desktop/Python/Python_Socratica/TextFiles/oceans.txt'

data = read_file_timed(path)

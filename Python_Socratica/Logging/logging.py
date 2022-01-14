# ______________________________________________
#               Helpful Links
# https://docs.python.org/3/howto/logging.html
# ______________________________________________

# Logging - allows you to write status messages 
# which parts of the code has executed 
# levels - 
    # Notset(0), 
    # Debug(10), 
    # Info(20), 
    # Warning(30), 
    # Error(40), 
    # Critical(50)

# All capitals are CONSTANTS
# Capitalized items are Classes
# Start with a lowercase letter are methods 

import logging
import math

print(dir(logging))

# Create and configure logger
LOG_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "/Users/User/Desktop/Python/PythonLOG/lumberjack.log", 
                            level = logging.DEBUG,  # Set to ERROR, will only display the Error/critical warning
                            format = LOG_format,
                            filemode = 'w')
logger = logging.getLogger()

# # Test the logger
# logger.info("Our first message.")
# logger.info("Our Second message.")
# # print(logger. level)

# logger.debug("This is a harmless debug message.")
# logger.info("Just some useful info.")
# logger.warning("I'm sorry, but I can't do that, Dave.")
# logger.error("Did you just try to divide by zero?")
# logger.critical("The entire internet is down!!")


# ________________________________________________________
def quadratic_formula(a, b, c):
    """ 
    Returns the solutions 
    to the equation ax^2 + bx + c = 0 
    """
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # compute the discriminant - 
    logger.debug("# compute the discriminant")
    disc = b**2 - 4*a*c

    # compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)  # change -4 to 1, compute problem
print(roots)

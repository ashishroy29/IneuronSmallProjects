import logging

# Initializing Logger
logging.basicConfig(filename="Newfile.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')
logger = logging.getLogger()

# Setting Logger level
logger.setLevel(logging.DEBUG)


# Calling GUI Module Logging
logging.info("Calling GUICode file")
# Calling GUI Module
from GUI import GUIcode

logging.info("Returned From File")
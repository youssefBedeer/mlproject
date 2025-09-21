import logging 
import os 
from datetime import datetime 

# CREATE LOGS FOLDER if not exists
log_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(log_folder, exist_ok=True)

# IDENTIFY LOG FILE PATH 
log_file_name = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S_')}.log"
log_file_path = os.path.join(log_folder, log_file_name)

# LOGGING CONFIGURATION 
logging.basicConfig(
    filename=log_file_path,
    level= logging.INFO,
    format = "[ %(asctime)s ] %(lineno)s %(name)s - %(levelname)s - %(message)s"
)

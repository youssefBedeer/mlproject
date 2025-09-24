import logging 
import os 
from datetime import datetime 

# CREATE DAILY LOG FOLDER (based on date)
base_log_folder = os.path.join(os.getcwd(), "logs")
today_folder = datetime.now().strftime("%Y_%m_%d")
log_folder = os.path.join(base_log_folder, today_folder)
os.makedirs(log_folder, exist_ok=True)

# IDENTIFY LOG FILE PATH 
log_file_name = f"{datetime.now().strftime('%H_%M_%S')}.log"
log_file_path = os.path.join(log_folder, log_file_name)

# LOGGING CONFIGURATION 
logging.basicConfig(
    filename=log_file_path,
    level= logging.INFO,
    format = "[%(asctime)s] [%(levelname)s] [%(name)s:%(funcName)s:%(lineno)d] - %(message)s"
)

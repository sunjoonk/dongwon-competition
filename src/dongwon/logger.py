import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger with a specified name and log file."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a file handler
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)

    return logger

# Set up the logger for the application
log_filename = os.path.join(os.path.dirname(__file__), 'application.log')
logger = setup_logger('dongwon_sales_simulator', log_filename)

logger.info("Logging setup complete.")
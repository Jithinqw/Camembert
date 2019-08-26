"""Module for maintaing logs for server."""
import falcon
import sys, os, logging, uuid
from datetime import datetime


def setup_logging(log):
    file_path = sys.modules[__name__].__file__
    project_path = os.path.dirname(os.path.dirname(file_path))
    log_location = project_path + "/logs/"
    if not os.path.exists(log_location):
        os.makedirs(log_location)
    current_time = datetime.now()
    current_date = current_time.strftime("%Y-%m-%d")
    file_name = current_date + ".log"
    file_location = log_location + file_name

    logging.basicConfig(filename=file_location, level=logging.DEBUG)
    with open(file_location, "a+"):
        pass

    logger = logging.getLogger(__name__)
    logger.info(log)
    return None


class ServerLoggingManager:

    """
        This module is responsible for maintaing 
        logs in a .log file. These are the currently
        implemented details for each log entry.
        1. IP
        2. Method
        3. Resource
        4. Host
        5. Forwared host
        6. URL
        7. Date
        8. UUID for each request
        9. Server Response code
    """

    def process_response(self, req, resp, resource, req_succeeded):
        construct_logger_info = "{0} {1} {2} {3} {4}".format(
            uuid.uuid4(), datetime.now(), req.method, req.uri, resp.status
        )
        setup_logging(construct_logger_info)
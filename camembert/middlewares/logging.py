"""Module for maintaing logs for server."""
import os
import logging
import uuid
from datetime import datetime


def setup_logging(log):
    """
        setup_logging - A server logging setting up resource.

        Args:
            log(object): A log object from process_request

        Returns:
            None

        Raises:
            None
    """
    file_path = os.getcwd()
    log_location = file_path + "/logs/"
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
        1. UUID for each request.
        2. datetime
        3. Method
        4. URI
        5. Status
    """

    def process_response(self, req, resp, resource, req_succeeded):
        """
            process_response - Process response from Falcon server.

        Args:
            req (object): Request object
            resp (object): Response object
            resource (object): Resources targetted.
            req_succeeded (bool): True if succeded

        Returns:
            None

        Raises:
            None
        """
        construct_logger_info = "{0} {1} {2} {3} {4}".format(
            uuid.uuid4(), datetime.now(), req.method, req.uri, resp.status
        )
        setup_logging(construct_logger_info)
        return

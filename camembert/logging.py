import falcon
import logging
from os.path import join, dirname, realpath

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("test.log"))
logger.setLevel(logging.INFO)


class ResponseLoggerMiddleware(object):
    def process_response(self, req, resp, resource, req_succeeded):
        """process_response is a middleware for logging response.
        Args:
            self (object): class instance
            req (object): request object 
            res (object): response object
        
        Raises:
            None
        """
        logger.info("{0} {1} {2}".format(req.method, req.relative_uri, resp.status[:3]))

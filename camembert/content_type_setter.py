import falcon


class ContentTypeManager:
    """Class for content type Manager"""

    def __init__(self):
        pass

    def process_request(self, req, resp):
        """process_request is a middleware for checking the application/json request.
        Args:
            self (object): class instance
            req (object): request object 
            res (object): response object
        
        Raises:
            falconHTTPBadRequest: request object does not have a application/json in req.content_type
        """
        if req.content_type is None or "application/json" not in req.content_type:
            raise falcon.HTTPBadRequest("Invalid Request")

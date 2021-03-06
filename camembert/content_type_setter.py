import falcon


class ContentTypeManager(object):
    """Class for content type Manager"""

    def process_request(self, req, resp):
        """process_request is a middleware for
        checking the application/json request.
        Args:
            req (object): request object
            resp (object): response object

        Status:
            Stable

        Raises:
            HTTPBadRequest:
                request object does not have a application/json
                in req.content_type
        """
        if req.content_type is None or "application/json" not in req.content_type:
            raise falcon.HTTPBadRequest(
                title="Invalid Request",
                description="All requests must have a application/json header",
            )
        else:
            return

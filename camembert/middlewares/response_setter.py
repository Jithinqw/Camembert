import datetime
import falcon

class SuccessResponseManager(object):
    """
       A manager middleware for changing the security headers in success response.
    """

    def __init__(self, response_headers):
        """
            Initialization method for SucessResponseManager

            Args:
                response_headers(object): Response headers for setting response header.

            Returns:
                None

            Raises:
                falcon.HTTPBadRequest
        """
        self.headers = response_headers
        if self.headers is None:
            falcon.HTTPBadRequest(
                title="Bad Request",
                description="Response header not set."
            )

    def process_response(self, req, resp, resource, req_succeeded):
        """
        process_response - It can process successful responses and
        set headers to every header.
        This middlware does not deletes headers which are vernerable.
        Please use use another middleware in deleting unwanted response headers.
        Please refer https://www.owasp.org for more details.

        Args:
            req (object): request object
            resp (object): response object
            resporce (object): Target respource
            req_succeeded (bool): Does this response instance succedded

        Raises:
            None

        Status:
            Stable

        Returns:
            None
        """
        for key, value in self.headers.items():
            resp.set_header(key, value)
        return

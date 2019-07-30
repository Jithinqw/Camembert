import datetime


class SuccessResponseManager:
    """A manager middleware for changing the security
        headers in success response"""

    def process_response(self, req, resp, resource, req_succeeded):
        """process_response, It can process successful response and 
        set headers to every header and deletes any headers which are vernerable. 
        Please refer https://www.owasp.org for more details.

        Args:
            req (object): request object
            resp (object): response object
            resporce (object): Target respource
            req_succeeded (bool): Does this response instance succedded

        Raises:
            None

        Returns:
            None
        """
        resp.set_header("X-Powered-By", "JBoss/7.1.2")
        resp.set_header("X-Download-Options", "noopen")
        resp.set_header("X-Content-Type-Options", "nosniff")
        resp.set_header("X-XSS-Protection", "1; mode=block")
        resp.set_header("Referrer-Policy", "same-origin")
        resp.set_header("X-Frame-Options", "same-origin")
        resp.set_header(
            "Expires", (datetime.datetime.now() + datetime.timedelta(days=60))
        )

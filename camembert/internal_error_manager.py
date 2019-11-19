"""
Middleware for managing internal server errors,
and response with a apt error message
"""
import falcon


class InternalServerErrorManager(object):
    """Middleware for managing internal server errors"""

    def process_response(self, request, resp, resource, req_succeeded):
        """
            Manages response if the server encounters any internal server errors.
            For 500 status

            Args:
                req (object): request object
                resp (object): response object
                resource (object): Target respource
                req_succeeded (bool): Does this response succedded

            Returns:
                None

            Raises:
                falcon.HTTPInternalServerError: Raises Falcon internal server error.
        """
        if resp.status == falcon.HTTP_500:
            raise falcon.HTTPInternalServerError(
                title="Internal Server Error",
                description="Something went wrong on our side. Please try again later.",
            )
        else:
            return

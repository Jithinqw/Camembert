"""
    Middleware for limiting user access to the server globally.
    Inspired from https://pypi.org/project/ratelimiter/
"""
import collections
import time
import falcon


class RateLimiterManager(object):
    """
        A middlware manager for limiting API calls.
        It raises a falcon error if hit with too much requests.

    """

    def __init__(self, max_calls, time_period=1.0):
        """
            Initialization method for RateLimiterManager.

            Args:
                max_calls (int): Maximum number of calls for the server.
                time_period (float): Time limit for the API. This time is set to 1.0.

            Returns:
                None

            Status:
                Expiremental

            Raises:
                falcon.HTTPPreconditionFailed
        """
        if time_period <= 0:
            raise falcon.HTTPPreconditionFailed(
                title="Server HTTP Pre-Condition Failed",
                description="Time period cannot be less than 0.",
            )
        if max_calls <= 0:
            raise falcon.HTTPPreconditionFailed(
                title="Server HTTP Pre-Condition Failed",
                description="Maximum number of calls should be more than 0.",
            )
        self.calls = collections.deque()
        self.max_calls = max_calls
        self.time_period = time_period
        self._timespan = 0

    def process_request(self, req, resp):
        """
            process_request - Processing incoming falcon request.

            Args:
                req (object): Request object
                resp (object): Response object

            Returns:
                None

            Status:
                Expiremental

            Raises:
                falcon.HTTPLocked: Falcon HTTP error informing user of resource is been locked.
                falcon.HTTPPreconditionFailed: Falcon HTTP error is raised when the user is
                    passing values less than the threshold time or response limit.
        """
        self.calls.append(time.time())
        if len(self.calls) > self.max_calls:
            raise falcon.HTTPLocked(
                title="Resource locked.",
                description="The resource you requested is currently locked.",
            )
        else:
            return

    def process_response(self, req, resp, resource, req_succeeded):
        """
            process_response - Process response from falcon.

            Args:
                req (object): Request object.
                resp (object): Response object
                Resource (object): Resource object
                req_succeeded (bool): is request succeeded or not.

            Status:
                Expiremental

            Returns:
                None

            Raises:
                None
        """
        self._timespan = self.calls[-1] - self.calls[0]
        while self._timespan >= self.time_period:
            if len(self.calls) == 0:
                break
            else:
                self.calls.popleft()
        return

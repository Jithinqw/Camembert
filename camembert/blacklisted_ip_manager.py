import falcon


class BlacklistedIpManager(object):
    """
        Middleware for managing blacklisted ip addresss
        for a server.

        Usage:

        >>> from camembert.middlewares import BlacklistedIpManager
        >>> app = falcon.api(
            middlewares=[
                BlacklistedIpManager(IPAddress_list)
            ]
        )

        A list of ip address string must be passed to the middleware.
    """

    def __init__(self, black_ip_address):
        if black_ip_address is None:
            raise falcon.HTTPPreconditionFailed(
                title="Server precondition failed",
                description="list of black listed IPs cannot be empty.",
            )
        if isinstance(black_ip_address, list) is not True:
            raise falcon.HTTPBadRequest(
                title="Bad Request",
                description="Black listed IP must be passed as a list.",
            )
        else:
            self.black_ip = black_ip_address

    def process_request(self, req, resp):
        """
            process_request

            Args:
                req (object)
                resp (object)

            Returns:
                None

            Raises:
                falcon.HTTPUnauthorized
        """
        if req.remote_addr in self.black_ip:
            raise falcon.HTTPUnauthorized(
                title="Unauthorized",
                description="You are unauthorized to view this route.",
            )
        else:
            return

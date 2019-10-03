import falcon


class ServerMaintainceManager(object):

    """
        Server maintance manager, for checking if the server is under maintance.
        Useage:
            >>> from camembert.middlewares import ServerMaintainceManager
            >>> api = falcon.api(middlware=[ServerMaintainceManager(True)])
        
        You can configure the bool value to come from anywhere
        1. A configuration file.
        2. DB 
        3. or hard code it. :(
    """

    def __init__(self, server_state):

        """
            Initialization method

            Args:
                server_state (bool): True if server is under maintance.

            Raises:
                falcon.HTTPInvalidParam
            
            Returns:
                None
        """
        if server_state is None:
            raise falcon.HTTPInvalidParam(
                title="Invalid Param", description="Server State should be passed."
            )
        if type(server_state) is not bool:
            raise falcon.HTTPInvalidParam(
                title="Invalid Param",
                description="Invalid datatype. Server Maintaince manager accepts bool.",
            )
        else:
            self.server_state = server_state

    def process_request(self, req, resp):
        """
            process_request, processing the incoming request.

            Args:
                req (object)
                resp (object)
            
            Returns: 
                None
            
            Raises:
                falcon.HTTPInvalidParam
        """
        if self.server_state is True:
            raise falcon.HTTPServiceUnavailable(
                title="Service unavailable.",
                description="Service is currently unavailable. Please try again later.",
            )
        else:
            return

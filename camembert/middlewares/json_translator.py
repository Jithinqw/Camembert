import falcon
import json


class JSONTranslatorManager(object):
    """JSONTranslatorManager for translating JSON"""

    def process_request(self, req, resp):
        """
            process_request, translates json

            Args:
                req (object): request object
                resp (object): response object

            Returns:
                object: sets data as a req param
            
            Status:
                Stable
            Raises:
                falconHTTPBadRequest
        """
        if req.method == "GET":
            pass
        else:
            try:
                req.data = json.loads(req.stream.read().decode("utf-8"))
            except:
                raise falcon.HTTPBadRequest(
                    title="Bad request",
                    description="Invalid body. Unable to parse the given content",
                )
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
            return
        else:
            try:
                if req.content_length:
                    req.data = json.loads(req.bounded_stream.read().decode("utf-8"))
                    return
                else:
                    raise falcon.HTTPBadRequest(
                        "Bad request", "Cannot accept content lenght null."
                    )
            except Exception:
                raise falcon.HTTPBadRequest(
                    title="Bad request",
                    description="Invalid body. \
                        Unable to parse the given content",
                )

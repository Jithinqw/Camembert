import falcon
from camembert.internal_error_manager import InternalServerErrorManager
import falcon, json
from camembert.internal_error_manager import InternalServerErrorManager
from camembert.https_required import RequireHTTPSManager
from camembert.content_type_setter import ContentTypeManager
from camembert.server_manataince_manager import ServerMaintainceManager

TEST_ROUTE = "/test"
TEST_RESPONSE = {"status": "ok"}


class InterServerErrorTestResource(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_500
        resp.body = json.dumps(TEST_RESPONSE)

def non_secure_server():
    api = falcon.API(
        middleware=[InternalServerErrorManager()]
    )
    api.add_route(TEST_ROUTE, InterServerErrorTestResource())
    return api

def secure_server():
    api = falcon.API(
        middleware=RequireHTTPSManager()
    )
    api.add_route(TEST_ROUTE, InterServerErrorTestResource())
    return api

def under_maintaince_server():
    api = falcon.API(middleware=ServerMaintainceManager(True))
    api.add_route(TEST_ROUTE, InternalServerErrorManager())
    return api
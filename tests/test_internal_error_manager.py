from camembert.internal_error_manager import InternalServerErrorManager
import falcon, json
from falcon.testing import testing

TEST_ROUTE = "/test"
TEST_RESPONSE = {"status": "ok"}


class TestResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(TEST_RESPONSE)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(TEST_RESPONSE)

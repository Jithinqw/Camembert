from .test_mock_server import non_secure_server
from falcon import testing
import falcon

class TestServer(testing.TestCase):
    def setUp(self):
        super(TestServer, self).setUp()
        self.app = non_secure_server()
    
    def tearDown(self):
        super(TestServer, self).tearDown()
    
    def test_server_exist(self):
        result = self.simulate_get('/test')
        self.assertIsNotNone(result, None)
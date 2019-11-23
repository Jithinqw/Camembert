from .test_mock_server import secure_server
from falcon import testing
import falcon

class RequireHTTPSTest(testing.TestCase):
    def setUp(self):
        super(RequireHTTPSTest, self).setUp()
        self.app = secure_server()
    
    def tearDown(self):
        super(RequireHTTPSTest, self).tearDown()
    
    def test_https_status(self):
        result = self.simulate_get('/test')
        self.assertEqual(result.status, falcon.HTTP_400)
    
    def test_https_description(self):
        result = self.simulate_get('/test')
        self.assertEqual(result.json['title'], 'HTTPS Required')
        self.assertEqual(result.json['description'], 'All requests must be performed via the HTTPS protocol. Please switch to HTTPS and try again.')
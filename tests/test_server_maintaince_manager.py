from .test_mock_server import under_maintaince_server
from falcon import testing
import falcon

class MaintainceTest(testing.TestCase):
    def setUp(self):
        super(MaintainceTest, self).setUp()
        self.app = under_maintaince_server()
    
    def tearDown(self):
        super(MaintainceTest, self).tearDown()
    
    def test_server_under_maintaince(self):
        result = self.simulate_get('/test')
        self.assertEqual(result.status, falcon.HTTP_503)
        self.assertEqual(result.json['title'], 'Service unavailable.')
        self.assertEqual(result.json['description'], 'Service is currently unavailable. Please try again later.')
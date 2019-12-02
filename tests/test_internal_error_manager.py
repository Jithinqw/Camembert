from .test_mock_server import non_secure_server
from falcon import testing
import falcon

class InternalServerErrorTest(testing.TestCase):
    def setUp(self):
        super(InternalServerErrorTest, self).setUp()
        self.app = non_secure_server()
    
    def tearDown(self):
        super(InternalServerErrorTest, self).tearDown()
    
    def test_route_exist(self):
        result = self.simulate_get('/test')
        self.assertIsNotNone(result.status)
    
    def test_route_status(self):
        result = self.simulate_get('/test')
        self.assertEqual(result.status, falcon.HTTP_500)
    
    def test_route_response(self):
        result = self.simulate_get('/test')
        self.assertEqual(result.json['title'], 'Internal Server Error')
        self.assertEqual(result.json['description'], 'Something went wrong on our side. Please try again later.')
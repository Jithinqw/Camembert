from .test_mock_server import non_secure_server
from falcon import testing
import falcon

class ContentHeaderSetterTest(testing.TestCase):
    def setUp(self):
        super(ContentHeaderSetterTest, self).setUp()
        self.app = non_secure_server()
    
    def tearDown(self):
        super(ContentHeaderSetterTest, self).tearDown()
    
    def test_set_header(self):
        result = self.simulate_get('/test')
        

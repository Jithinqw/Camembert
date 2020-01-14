import falcon
from secure import SecureHeaders

secure_headers = SecureHeaders()

class SecureHeaderManager(object):
    """Middleware for setting secure headers to a header"""
    
    def __init__(self, server=False, hsts=True, xfo=True, xxp=True, content=True, csp=False, referrer=True, cache=True, feature=False):
        """
            Initialization method

            Args:
                server (bool): True if server is under maintance.
                hsts
                xfo
                xxp
                content
                csp
                referrer
                cache
                feature
                
            Raises:
                Exception
            
            Returns:
                None
        """
        self.server = server
        self.hsts = hsts
        self.xfo = xfo
        self.xxp = xxp
        self.content = content
        self.csp = csp
        self.referrer = referrer
        self.cache = cache
        self.feature = feature
    
    def process_request(self, req, resp):
        try:
            secure_headers = SecureHeaders(server=self.server, hsts=self.hsts, xfo=self.hsts, xxp=self.xxp, content=self.content, csp=self.csp, referrer=self.referrer, cache=self.cache, feature=self.cache)
            return secure_headers.falcon(resp)
        except Exception as err:
            raise err
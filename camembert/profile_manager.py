"""Middleware for profiling requests to a user """

import falcon
from werkzeug.contrib.profiler import ProfilerMiddleware

class AppProfilerMiddleware(object):

    def demo():
        pass
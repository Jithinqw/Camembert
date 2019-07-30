import falcon


class DBSesssionManager(object):
    """Middleware for manager for managing db sessions 
    for each request. 
    Each request requires a session object from SQLAlchemy 
    session creator method
        >>> from sqlalchemy.orm import sessionmaker
        >>> from sqlalchemy import create_engine
        >>> session = Sessionmaker()
        >>> engine = create_engine('mysql://user@password')
        >>> Session.configure(bind=engine)
        >>> session = Session()
    Which is passed to this middleware
    """

    def __init__(self, db_session):
        self.db_session = db_session
    
    def process_request(self, req, resp, resource, params):
        try:
            resource.db_session = self.db_session()
        except:
            raise ConnectionError("Unable to create sessions with database")
    
    def process_response(self, req, resp, resource, req_succeeded):
        try:
            if hasattr(response, "session"):
                if not req_succeeded:
                    resource.db_session.rollback()
                db_session.remove()
        except:
            raise EnvironmentError("Unable to remove sessions from request")
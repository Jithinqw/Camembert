import falcon

class DBSesssionManager(object):
    """
        Middleware for manager for managing db sessions 
        for each request. 
        Each request requires a session object from SQLAlchemy 
        session creator method
            >>> from sqlalchemy.orm import sessionmaker
            >>> from sqlalchemy import create_engine
            >>> session = Sessionmaker()
            >>> engine = create_engine('mysql://user@password')
            >>> Session.configure(bind=engine)
            >>> session = Session()
        Which is passed to this middleware.

        Todo:
            Make the session manager more sexy.
    """

    def __init__(self, db_session):
        """
            __init__ method for database session manager.

            Args:
                db_session (object): SQLAlchemy object
            
            Raises:
                falcon.HTTPBadRequest
        """
        self.db_session = db_session
        if db_session is None:
            raise falcon.HTTPBadRequest(
                title="Bad Request",
                description="Database gone away."
            )

    def process_request(self, req, resp, resource, params):
        """process_request is a middleware for
        checking the application/json request.
        Args:
            req (object): request object 
            res (object): response object
        
        Status:
            Stable
            
        Raises:
            falcon.HTTPBadRequest
        """
        try:
            resource.db_session = self.db_session()
            return
        except:
            raise ConnectionError("Unable to create sessions with database")

    def process_response(self, req, resp, resource, req_succeeded):
        """
            process_request

            Args:
                req (object): request object
                resp (object): response object

            Returns:
                object: sets data as a req param
            
            Status:
                Stable
            Raises:
                falconHTTPBadRequest
        """
        try:
            if hasattr(resource, "session"):
                if not req_succeeded:
                    resource.db_session.rollback()
                resource.db_session.remove()
                return
        except:
            raise EnvironmentError("Unable to remove sessions from request")

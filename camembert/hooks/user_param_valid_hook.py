import falcon


def is_user_parameter_valid(req, resp, resource, params, req_params):
    """
        is_user_parameter_valid, falcon hook for checking if the
        parameters passed by user is valid or not.
        Args:
            req (object): request object
            resp (object): response object
            resource (object): resource
            params (object): params
            req.params (object): Required parameter list
        Returns:
            None
        Raises:
            falcon.HTTPBadRequest
    """
    if req_params is None:
        raise falcon.HTTPUnprocessableEntity(
            title="Unprocessable Entity",
            description="Invalid number of parameters. Please send all the required parameters.",
        )
    else:
        valid = set(req_params).issubset(req.data)
        if valid:
            return
        else:
            raise falcon.HTTPUnprocessableEntity(
                title="Unprocessable Entity",
                description="Invalid number of parameters. Please send all the required parameters.",
            )

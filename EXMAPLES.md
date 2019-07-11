You can use Camembert by installing `pip install camembert`

## Content Type Setter

This middleware is used to strict `application/json` for every request other than the `GET` method.

```python
    import falcon
    from .images import Resource
    from camembert.content_type_setter import ContentTypeManager
    api = falcon.API(middleware=[
        ContentTypeManager()
        ]
    )
    images = Resource()
    api.add_route('/images', images)
```

This raises a `falcon.HTTPBadRequest` if found otherwise.

## HTTPS Required

This middleware is for strictly accepting `HTTPS` requests.

```python
    import falcon
    from .images import Resource
    from camembert.https_required import RequireHTTPS
    api = falcon.API(middleware=[
        RequireHTTPS()
        ]
    )
    images = Resource()
    api.add_route('/images', images)
```
This raises a `falcon.HTTPBadRequest` if found otherwise.

## JSON Translator

This middleware is for decoding JSON

```python
    import falcon
    from .images import Resource
    from camembert.json_translator import JSONTranslatorManager
    api = falcon.API(middleware=[
        JSONTranslatorManager()
        ]
    )
    images = Resource()
    api.add_route('/images', images)
```

## Logging

This middleware is for enabling logging.

```python
    import falcon
    from .images import Resource
    from camembert.logging import ResponseLoggerMiddleware
    api = falcon.API(middleware=[
        ResponseLoggerMiddleware()
        ]
    )
    images = Resource()
    api.add_route('/images', images)
```

## Response Setter

This middleware is for setting response headers.

```python
    import falcon
    from .images import Resource
    from camembert.response_setter import SuccessResponseManager
    api = falcon.API(middleware=[
        SuccessResponseManager()
        ]
    )
    images = Resource()
    api.add_route('/images', images)
```

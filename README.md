# Camembert

[![Total alerts](https://img.shields.io/lgtm/alerts/g/Jithinqw/Camembert.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Jithinqw/Camembert/alerts/)

This is a library for configuring and setting up middleware and using programming hooks for the Falcon framework.

## Requirements

Please refer to `requirements.txt` for list of requirements.

## List of middleware functions

- Converting request to JSON
- Requests Logging
- Response headers
- Content Type
- Require HTTPS
- SQLAlchemy session management
- Internal Server Error
- RateLimiting
- Blacklisted IP

## Installing Camembert

### Local installation

Clone this repository to your workspace and change directory to it.

Run dependencies using `python3 -m pip install -r requirements.txt`

If you are need to use a proxy certificate run `python3 -m pip install -r requirements.txt --cert <proxy-cert>`

Then run `python3 setup.py install`

### Installation as a PIP module

`pip install camembert`

Pypi page - [Camembert](https://pypi.org/project/camembert/)

## Examples

Please see `Examples.md` for examples.

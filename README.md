# Camembert
[![Total alerts](https://img.shields.io/lgtm/alerts/g/Jithinqw/Camembert.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Jithinqw/Camembert/alerts/)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<p>
<a href="https://github.com/psf/black/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
</p>
Configure middlewares and hooks for the Falcon framework easily.

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

If you are in need to use a proxy certificate run `python3 -m pip install -r requirements.txt --cert <proxy-cert>`

Then run `python3 setup.py install`

### Installation as a PIP module

`pip install camembert`

Pypi page - [Camembert](https://pypi.org/project/camembert/)

## Examples

Please see `Examples.md` for examples.

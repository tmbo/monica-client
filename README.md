# Monica Python Client
[![Build Status](https://travis-ci.com/tmbo/monica-client.svg?token=dD3o9yxyCw5PCTNpznf4&branch=master)](https://travis-ci.com/tmbo/monica-client)
[![PyPI version](https://badge.fury.io/py/monica-client.svg)](https://badge.fury.io/py/monica-client)

Connects to the Monica API and provides an easy to use python API.

## Installation
```
pip install monica-client
```

## Usage example

```python
from monica import MonicaClient

client = MonicaClient(access_token="ACCESS_TOKEN")
```

You can find the value for the `ACCESS_TOKEN` on your 
[Monica Profile page](https://app.monicahq.com/settings/api). Create a 
new token and use the returned key as your access token. 

### me()
Get the profile of the authenticated user.

```python
client.me()
```
Example:
```python
In [4]: client.me()
Out[4]:
{'id': 14109, 'object': 'user', 'first_name': 'Peter', 'last_name': 'Pan', 'email': 'peter.pan@example.com', 'timezone': 'UTC', 'currency': {'id': 2, 'object': 'currency', 'iso': 'USD', 'name': 'US Dollar', 'symbol': '$'}, 'locale': 'en', 'is_policy_compliant': True, 'account': {'id': 13}, 'created_at': '2018-10-28T09:51:19Z', 'updated_at': '2018-10-28T14:09:17Z'}
```

## Advanced Usage

### Specifying your own Monica API server
If you happen to run your own monica API server, there
is a way to specify its url:

```python
from monica import MonicaClient

client = MonicaClient(access_token="ACCESS_TOKEN",
                      api_url="http://yourapi.com/api")
```

## Changelog

### 1.0.0 - 14.05.18

*added*:
- initial version released
- feature complete with respect to node js client library

## License

Licensed under the Apache License, Version 2.0. Copyright 2018 Tom Bocklisch. [Copy of the license](LICENSE).

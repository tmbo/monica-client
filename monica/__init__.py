from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import logging

import requests

logger = logging.getLogger(__name__)

API_URL = "https://app.monicahq.com/api"

API_VERSION = "1.0"


class MonicaClient(object):

    def __init__(self,
                 access_token,
                 api_url=API_URL,
                 api_version=API_VERSION
                 ):
        self.access_token = access_token
        self.api_url = api_url
        self.api_version = api_version

    def _call_api(self, sub_url):
        url = "{}/{}".format(self.api_url, sub_url)

        logger.debug("Calling Monica API '{}'".format(url))

        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(self.access_token)
        }

        result = requests.get(url, headers=headers)

        result.raise_for_status()

        logger.debug("Monica API Response Code: {} Content: '{}'".format(
                result.status_code, result.json))

        return result.json()

    def me(self):
        return self._call_api("me").get("data")

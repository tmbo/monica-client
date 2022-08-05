import logging
from typing import Any, Dict, List, Text

import requests

from monica.constants import API_URL, API_VERSION

logger = logging.getLogger(__name__)


class MonicaClient(object):

    def __init__(self,
                 access_token: Text,
                 api_url: Text = API_URL,
                 api_version: Text = API_VERSION
                 ):
        self.access_token = access_token
        self.api_url = api_url
        self.api_version = api_version

    def _call_api(self,
                  sub_url: Text,
                  method: Text = "get",
                  **kwargs) -> Any:
        url = "{}/{}".format(self.api_url, sub_url)

        logger.debug("Calling Monica API '{}'".format(url))

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': "Bearer {}".format(self.access_token)
        }

        result = requests.request(method, url, headers=headers, **kwargs)

        logger.debug("Monica API Response Code: {} Content: '{}'".format(
            result.status_code, result.json()))

        result.raise_for_status()

        return result.json()

    def me(self) -> Dict[Text, Any]:
        return self._call_api("me").get("data")

    def genders(self):
        return self._call_api("genders").get("data")

    def lifeevents(self) -> List[Dict[Text, Any]]:
        return self._call_api("lifeevents").get("data")

    def find_contact(self, query):
        return self._call_api("contacts", params={"query": query}).get("data")

    def contacts(self):
        return self._call_api("contacts").get("data")

    def notes_of(self, contact_id):
        return self._call_api(f"contacts/{contact_id}/notes").get("data")

    def create_note(self, body, contact_id, is_favorited=False):
        body = {
          "body": body,
          "contact_id": contact_id,
          "is_favorited": 1 if is_favorited else 0
        }
        response = self._call_api("notes", json=body, method="post")
        return response.get("data")

    def create_contact(self,
                       first_name,
                       gender_id,
                       is_birthdate_known=False,
                       is_deceased=False,
                       is_deceased_date_known=False,
                       nickname=None,
                       last_name=None,
                       birthdate_day=None,
                       birthdate_month=None,
                       birthdate_year=None,
                       birthdate_is_age_based=True,
                       is_partial=False,
                       birthdate_age=None,
                       deceased_date_day=None,
                       deceased_date_month=None,
                       deceased_date_year=None,
                       deceased_date_is_age_based=None
                       ):
        contact_defaults = {
            "first_name": first_name,
            "last_name": last_name,
            "nickname": nickname,
            "gender_id": gender_id,
            "birthdate_day": birthdate_day,
            "birthdate_month": birthdate_month,
            "birthdate_year": birthdate_year,
            "is_birthdate_known": is_birthdate_known,
            "birthdate_is_age_based": birthdate_is_age_based,
            "birthdate_age": birthdate_age,
            "is_partial": is_partial,
            "is_deceased": is_deceased,
            "deceased_date_day": deceased_date_day,
            "deceased_date_month": deceased_date_month,
            "deceased_date_year": deceased_date_year,
            "deceased_date_is_age_based": deceased_date_is_age_based,
            "is_deceased_date_known": is_deceased_date_known,
        }

        r = self._call_api("contacts",
                           json=contact_defaults,
                           method="post")

        return r.get("data")

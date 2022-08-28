from abc import ABC
from typing import List

import requests
import msal


def response_has_json(response: requests.Response):
    return response.headers.get("Content-Type", "").startswith("application/json")


def api_call_factory(
    scopes: List[str], app: msal.ClientApplication, session: requests.Session = None
):
    def api_call(*, url: str, body=None, extra_headers=None, method: str = "get"):

        if not extra_headers:
            extra_headers = {}
        result = app.acquire_token_silent(scopes, account=None)

        if not result:
            result = app.acquire_token_for_client(scopes=scopes)

        try:
            api_response = session.request(
                method=method,
                url=url,
                headers={
                    "Authorization": f'Bearer {result["access_token"]}',
                    **extra_headers,
                },
                data=body,
            )
            api_response.raise_for_status()

            if response_has_json(api_response):
                acc = []

                data = api_response.json()
                acc+=data['value']

                while '@odata.nextLink' in data:
                    response = session.request(method=method, url=data['@odata.nextLink'],headers={
                        "Authorization": f'Bearer {result["access_token"]}',
                        **extra_headers,
                    },
                    data=body,)
                    response.raise_for_status()
                    data = response.json()
                    acc+=data['value']

                return acc

        except Exception as e:
            reason = (
                f"Request failed! Reason [{e}] with code {api_response.status_code}"
            )
            if response_has_json(api_response):
                reason += f"\n{api_response.json()}"
            raise Exception(reason)

    return api_call


class BaseClient(ABC):

    scopes = []

    def __init__(self, app: msal.ClientApplication) -> None:
        self.app = app
        self.session = requests.Session()
        self.api_call = api_call_factory(self.scopes, self.app, self.session)
        super().__init__()

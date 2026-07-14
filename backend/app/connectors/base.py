from abc import ABC
from typing import Any

import requests


class BaseConnector(ABC):
    """Base connector for external systems."""

    def __init__(
        self,
        base_url: str,
        headers: dict[str, str],
        timeout: int = 30,
    ):
        self.base_url = base_url.rstrip("/")
        self.headers = headers
        self.timeout = timeout

    def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any,
    ) -> dict[str, Any]:

        response = requests.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            headers=self.headers,
            timeout=self.timeout,
            **kwargs,
        )

        response.raise_for_status()

        if response.content:
            return response.json()

        return {}

    def get(self, endpoint: str, params=None):
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, data=None):
        return self._request("POST", endpoint, json=data)

    def put(self, endpoint: str, data=None):
        return self._request("PUT", endpoint, json=data)

    def delete(self, endpoint: str):
        return self._request("DELETE", endpoint)

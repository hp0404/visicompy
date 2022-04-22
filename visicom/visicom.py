# -*- coding: utf-8 -*-
"""This module contains Visicom class."""
from dataclasses import dataclass
from time import sleep
from typing import Any, ClassVar, Dict, List, Optional, Union

import httpx

from .logger import log

JSON = Dict[str, Any]
Params = Dict[str, Union[str, float]]
Geometry = List[float]

TIMEOUT = 1.2


def log_request(request: httpx.Request) -> None:
    """Request event hook"""
    text = request.url.params["text"]
    log(f"Request event hook: {request.method} {text} - Waiting for response")


def log_response(response: httpx.Response) -> None:
    """Response event hook"""
    request = response.request
    text = request.url.params["text"]
    log(f"Response event hook: {request.method} {text} - Status {response.status_code}")


def process_response(response: JSON) -> Geometry:
    """Extracts coordinates from geocode response."""
    if "features" in response:
        # first response - the highest relevance
        return response["features"][0]["geo_centroid"]["coordinates"]
    if "geo_centroid" in response:
        return response["geo_centroid"]["coordinates"]
    raise ValueError


@dataclass
class Visicom:
    """Visicom wrapper base class

    Examples
    --------
    >>> api = Visicom(token="414eb149c5b857fb898dbaf80bcb1def")
    >>> api.geocode(address="м. Київ, вул. Хрещатик, 26", limit=True)
    [30.521626, 50.448847]
    >>> api.geocode(address="м. Київ, вул. Полярна, 5", limit=True)
    [30.453879, 50.521189]
    """

    BASE_URL: ClassVar[str] = "https://api.visicom.ua"
    token: str  # token length 32
    client: Optional[httpx.Client] = None

    def fetch(self, endpoint: str, params: Optional[Params] = None) -> httpx.Response:
        """Requests data making sure the client is up & timeouts are set."""
        if self.client is None or self.client.is_closed:
            self.client: httpx.Client = httpx.Client(
                base_url=Visicom.BASE_URL,
                params={"key": self.token},
                event_hooks={"request": [log_request], "response": [log_response]},
            )
        return self.client.get(endpoint, params=params)

    def geocode(self, address: str, limit: bool = True) -> Union[JSON, Geometry, List]:
        """Extracts features/coordinates by calling geocode endpoint."""
        geocode_endpoint = "/data-api/5.0/uk/geocode.json"
        response = self.fetch(geocode_endpoint, params={"text": address})
        sleep(TIMEOUT)

        data = response.json()
        if not data:
            return []
        return process_response(data) if limit else data

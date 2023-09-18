from .waypoint import *
import pytest
from lib.openatms import OpenATMS
from .test_waypoint_data import *


class TestWaypointTopstar:
    airport = "WSSS"
    waypoint_top_sid_url = (
        f"{OpenATMS().base_url}/{OpenATMS.url_get_sid_by_airport_icao}/{airport}"
    )

    @pytest.mark.asyncio
    async def test_waypoint_top_sid_should_return_response_when_valid_response(
        self, requests_mock
    ):
        mock_response = mock_response_valid
        requests_mock.get(
            self.waypoint_top_sid_url,
            json=mock_response,
        )

        response = await waypoint_top_sid(self.airport)
        assert response == [
            {"count": 2, "name": "HOSBA"},
            {"count": 2, "name": "TOMAN"},
        ]

    @pytest.mark.asyncio
    async def test_waypoint_top_sid_should_return_empty_array_when_invalid_response(
        self, requests_mock
    ):
        mock_response = [{"mock": "response"}]
        requests_mock.get(
            self.waypoint_top_sid_url,
            json=mock_response,
        )

        response = await waypoint_top_sid(self.airport)
        assert response == []

    @pytest.mark.asyncio
    async def test_waypoint_top_sid_should_return_empty_array_when_null(
        self, requests_mock
    ):
        mock_response = None
        requests_mock.get(
            self.waypoint_top_sid_url,
            text=mock_response,
        )

        response = await waypoint_top_sid(self.airport)
        assert response == []



class TestWaypointTopStar:
    airport = "WSSS"
    waypoint_top_star_url = (
        f"{OpenATMS().base_url}/{OpenATMS.url_get_star_by_airport_icao}/{airport}"
    )

    @pytest.mark.asyncio
    async def test_waypoint_top_star_should_return_response_when_valid_response(
        self, requests_mock
    ):
        mock_response = mock_response_valid
        requests_mock.get(
            self.waypoint_top_star_url,
            json=mock_response,
        )

        response = await waypoint_top_star(self.airport)
        assert response == [
            {"count": 2, "name": "HOSBA"},
            {"count": 2, "name": "TOMAN"},
        ]

    @pytest.mark.asyncio
    async def test_waypoint_top_star_should_return_empty_array_when_invalid_response(
        self, requests_mock
    ):
        mock_response = [{"mock": "response"}]
        requests_mock.get(
            self.waypoint_top_star_url,
            json=mock_response,
        )

        response = await waypoint_top_star(self.airport)
        assert response == []

    @pytest.mark.asyncio
    async def test_waypoint_top_star_should_return_empty_array_when_null(
        self, requests_mock
    ):
        mock_response = None
        requests_mock.get(
            self.waypoint_top_star_url,
            text=mock_response,
        )

        response = await waypoint_top_star(self.airport)
        assert response == []

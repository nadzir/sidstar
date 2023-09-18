from .waypoint import WaypointService
from lib.openatms import OpenATMS
from .test_waypoint_data import *

class TestWaypointServiceGetTopSID:
    airport = "WSSS"
    url = f"{OpenATMS().base_url}/{OpenATMS.url_get_sid_by_airport_icao}/{airport}"

    def test_get_top_waypoints_sid_should_return_response_when_valid_input(self, requests_mock):
        mock_response = mock_response_valid_sid
        requests_mock.get(
            self.url,
            json=mock_response,
        )
        response = WaypointService().get_top_waypoints_sid(self.airport)
        assert response == [{'count': 2, 'name': 'HOSBA'}, {'count': 2, 'name': 'TOMAN'}]


    def test_get_top_waypoints_sid_should_return_empty_json_when_invalid_input(self, requests_mock):
        mock_response = [{"mock": "response"}]
        requests_mock.get(
            self.url,
            json=mock_response,
        )
        response = WaypointService().get_top_waypoints_sid(self.airport)
        assert response == []


class TestWaypointServiceGetTopSTAR:
    airport = "WSSS"
    url = f"{OpenATMS().base_url}/{OpenATMS.url_get_star_by_airport_icao}/{airport}"

    def test_get_top_waypoints_star_should_return_response_when_valid_input(self, requests_mock):
        mock_response = mock_response_valid_star
        requests_mock.get(
            self.url,
            json=mock_response,
        )
        response = WaypointService().get_top_waypoints_star(self.airport)
        assert response == [{'count': 6, 'name': 'SAMKO'}, {'count': 6, 'name': 'DOVAN'}]


    def test_get_top_waypoints_star_should_return_empty_json_when_invalid_input(self, requests_mock):
        mock_response = [{"mock": "response"}]
        requests_mock.get(
            self.url,
            json=mock_response,
        )
        response = WaypointService().get_top_waypoints_star(self.airport)
        assert response == []


class TestWaypointServiceGetToWaypoint:

    def test_get_top_waypoints_should_return_response_when_valid_input(self):
        data = mock_response_valid_sid
        response = WaypointService()._get_top_waypoints(data)
        assert response == [{'count': 2, 'name': 'HOSBA'}, {'count': 2, 'name': 'TOMAN'}]

    def test_get_top_waypoints_should_return_empty_array_when_invalid_input(self):
        data = None
        response = WaypointService()._get_top_waypoints(data)
        assert response == []

        data = "a"
        response = WaypointService()._get_top_waypoints(data)
        assert response == []

from lib.listutil import get_top_occurences_from_list
from lib.openatms import OpenATMS


class WaypointService:
    def __init__(self):
        self.openATMS = OpenATMS()

    def get_top_waypoints_sid(self,airport):
        sids = self.openATMS.get_sid_by_airport_icao(airport)
        return self._get_top_waypoints(sids)

    def get_top_waypoints_star(self,airport):
        stars = self.openATMS.get_star_by_airport_icao(airport)
        return self._get_top_waypoints(stars)

    def _get_top_waypoints(self, data):
        if data is None:
            return []

        total_waypoints = []
        for item in data:
            if "waypoints" in item:
                for waypoint in item["waypoints"]:
                    total_waypoints.append(waypoint["name"])

        result = get_top_occurences_from_list(total_waypoints, num_of_elements=2)
        format_result = [{"name": item[0], "count": item[1]} for item in result]

        return format_result
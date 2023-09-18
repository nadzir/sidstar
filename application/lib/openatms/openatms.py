import requests
import os


class OpenATMS:
    api_key = os.environ.get("OPEN_ATM_API_KEY")
    base_url = "https://open-atms.airlab.aero/api/v1"

    url_get_sid_by_airport_icao = "airac/sids/airport"

    def get_sid_by_airport_icao(self,airport):
        if airport is None:
            return {}
            
        headers = {"api-key": self.api_key}
        url = f"{self.base_url}/{self.url_get_sid_by_airport_icao}/{airport}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        try:
            return response.json()
        except:
            return {}
    
    url_get_star_by_airport_icao = "airac/stars/airport"

    def get_star_by_airport_icao(self,airport):
        if airport is None:
            return {}
            j
        headers = {"api-key": self.api_key}
        url = f"{self.base_url}/{self.url_get_star_by_airport_icao}/{airport}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        try:
            return response.json()
        except:
            return {}

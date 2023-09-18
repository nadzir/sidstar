from .openatms import OpenATMS
import pytest
from requests import HTTPError

class TestOpenATMSID:
   airport = "WSSS"
   url = f"{OpenATMS().base_url}/{OpenATMS.url_get_sid_by_airport_icao}/{airport}"

   def test_get_sid_by_airport_icao_shouuld_return_response_when_success(self,requests_mock):
       mock_response = [{"mock": "response"}]
       requests_mock.get(
           self.url,
           json=mock_response,
       )
       sids = OpenATMS().get_sid_by_airport_icao(self.airport)
       assert sids == mock_response
   
   
   def test_get_sid_by_airport_icao_shouuld_raise_error_when_invalid_status_code(self,requests_mock):
       requests_mock.get(
           self.url, status_code=500
       )
       with pytest.raises(HTTPError):
           OpenATMS().get_sid_by_airport_icao(self.airport)
    
   def test_get_sid_by_airport_icao_shouuld_return_empty_json_when_input_is_null(self,requests_mock):
       requests_mock.get(
           self.url, status_code=500
       )
       sids = OpenATMS().get_sid_by_airport_icao(None)
       assert sids == {}

class TestOpenATMStar:
   airport = "WSSS"
   url = f"{OpenATMS().base_url}/{OpenATMS.url_get_star_by_airport_icao}/{airport}"

   def test_get_star_by_airport_icao_shouuld_return_response_when_success(self,requests_mock):
       mock_response = [{"mock": "response"}]
       requests_mock.get(
           self.url,
           json=mock_response,
       )
       stars = OpenATMS().get_star_by_airport_icao(self.airport)
       assert stars == mock_response
   
   
   def test_get_star_by_airport_icao_shouuld_raise_error_when_invalid_status_code(self,requests_mock):
       requests_mock.get(
           self.url, status_code=500
       )
       with pytest.raises(HTTPError):
           OpenATMS().get_star_by_airport_icao(self.airport)
    
   def test_get_star_by_airport_icao_shouuld_return_empty_json_when_input_is_null(self,requests_mock):
       requests_mock.get(
           self.url, status_code=500
       )
       stars = OpenATMS().get_star_by_airport_icao(None)
       assert stars == {}

#importing request module that gets the timezones in the airport

import requests

request=request.get("https://airport.api.aero/timezone.json")
if (response.status_code) == 401:

    print("Please check your information such as the api key")

elif response.status_code == 200:
	
	print (request.text)

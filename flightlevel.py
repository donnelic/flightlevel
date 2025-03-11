import requests

# API endpoint
qs = 1013.2
fieldElevation = 80
maxFL = 55
aboveQs = maxFL * 30.48

icao_code = "EHDL"  # Replace with the ICAO code of the airport you're interested in
url = f"https://api.checkwx.com/metar/{icao_code}/decoded"

# Your API key (passed in the X-API-Key header)
headers = {
    "X-API-Key": "b6a84a3e31a94080a28c87abf6d4f02a"
}

# Send GET request
response = requests.get(url, headers=headers)

# Check if the response is OK
if response.status_code == 200:
    data = response.json()
    # Extract QNH pressure from the barometer field
    qnhPressure = data['data'][0].get('barometer', {}).get('hpa', None)
   
    correction = (qnhPressure - qs) * 8
    maxHeight = aboveQs + correction - fieldElevation
    maxHeight = round(maxHeight, 2)
    print(maxHeight)

else:
    print(f"Failed to retrieve data: {response.status_code}")
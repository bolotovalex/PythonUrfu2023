import requests


def get_request_params() -> dict:
    user_requests = {'format': 'geojson'}
    questions = {
        'starttime': 'Enter the start time: ',
        # Без этого не работает. Можно было с помощью datetime сделать период, но решил так.
        'endtime': 'Enter the end time: ',
        'latitude': 'Enter the latitude: ',
        'longitude': 'Enter the longitude: ',
        'maxradiuskm': 'Enter the max radius in km: ',
        'minmagnitude': 'Enter the min magnitude: '}
    for question in questions.keys():
        user_requests[question] = input(questions[question])
    return user_requests


def get_json_response(user_params: dict):
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
    response = requests.get(url, headers={'Accept': 'aplication/json'}, params=user_params)
    return response.json()


def print_event_from_json(json_response):
    i = 1
    for index in json_response['features']:
        print(f"{i}. "
              f"Place: {index['properties']['place']}. "
              f"Magnitude: {index['properties']['mag']}")
        i += 1


request_params = get_request_params()
response = get_json_response(request_params)
print_event_from_json(response)

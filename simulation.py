import requests
import random


BACK_URL = 'https://covid--back.herokuapp.com'

def send_new_cases(lat_range=(51.024901, 51.227157), lon_range=(71.297808, 71.592204), count=10, endpoint='data-api/new-case') -> requests.Response:

    responses = []
    
    for _ in range(count):
        lat_offset = random.random() / 10
        lon_offset = random.random() / 10
        
        new_lat = round(lat_range[0], 1) + lat_offset
        
        if new_lat > lat_range[1] or new_lat < lat_range[0]:
            continue
        
        new_lon = round(lon_range[0], 1) + lon_offset
        
        if new_lon > lon_range[1] or new_lon < lon_range[0]:
            continue
        
        print(f'Generated latitude: {new_lat}, longtitude: {new_lon}')
        
        response = requests.api.post(
            f'{BACK_URL}/{endpoint}',
            json={
                'latitude': new_lat,
                'longitude': new_lon,
            },
            headers={
                'Authorization': 'Bearer IdfxFirDkNcJ19EQPgY8hgZcSgs',
            },
        )
        responses.append(response)
    
    return responses

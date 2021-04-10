import requests
import random
import typing
import json
import logging

back_url = None

def set_api_host(host):
    global back_url

    if back_url is None:
        back_url = host


def fetch_authoriztion_token(
    basic_auth: typing.Tuple[float, float],
    oauth: typing.Dict[str, str],
    endpoint: str,
    ):

    response = requests.post(
        f'{back_url}/{endpoint}',
        data=oauth,
        auth=basic_auth,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )

    if response.status_code != 200:
        return None, None

    body = response.json()    

    return body['access_token'], body['token_type']


def send_new_cases(
    auth_token: str,
    token_type: str,
    lat_range: typing.Tuple[float, float], 
    lon_range: typing.Tuple[float, float], 
    count: int, 
    endpoint: str,
    ) -> typing.List[requests.Response]:

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

        print(f'Generated new hotspot with latitude: {new_lat}, longitude: {new_lon}')
                
        response = requests.api.post(
            f'{back_url}/{endpoint}',
            json={
                'latitude': new_lat,
                'longitude': new_lon,
            },
            headers={
                'Authorization': f'{token_type} {auth_token}',
            },
        )
        responses.append(response)
    
    return responses

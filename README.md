# SimulationCovidApp- simulation of contact cases

### Make sure, you created config yaml with the format as presented below:

* server:
  * host: test_host
  * basic_auth: !!python/tuple [test_client, test_secret]
  * oauth:
    ** endpoint: 'oauth/token'
    ** grant_type: 'password'
    ** username: 'test_username'
    ** password: 'test_password'
* simulation:
  * endpoint: 'data-api/new-case'
  * lat_range: !!python/tuple [51.024901, 51.227157]
  * lon_range: !!python/tuple [71.297808, 71.592204]
  * count: 10

### When you will be running simulation, don't forget to use valid server host and point valid oauth credenticals in config yaml

### To start simulation, simply type: 

python main.py

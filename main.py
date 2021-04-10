import simulation
import requests
import pydantic
import typing
import yaml

CONFIG_YAML = 'config.yaml'

class SimulationConfig(pydantic.BaseModel):
    endpoint: str
    lat_range: typing.Tuple[float, float]
    lon_range: typing.Tuple[float, float]
    count: int

class OauthConfig(pydantic.BaseModel):
    endpoint: str
    grant_type: str
    username: str
    password: str

class ServerConfig(pydantic.BaseModel):
    host: str
    basic_auth: typing.Tuple[str, str]
    oauth: OauthConfig

class AppConfig(pydantic.BaseModel):
    server: ServerConfig
    simulation: SimulationConfig


def app():
    with open(CONFIG_YAML) as f:
        raw_conf = yaml.load(f)

    conf = AppConfig(**raw_conf)
    simulation.set_api_host(conf.server.host)

    auth_token, token_type = simulation.fetch_authoriztion_token(
        basic_auth=conf.server.basic_auth,
        oauth=conf.server.oauth.dict(exclude={'endpoint'}),
        endpoint=conf.server.oauth.endpoint,
    )

    responses = simulation.send_new_cases(
        auth_token=auth_token, 
        token_type=token_type,
        lat_range=conf.simulation.lat_range,
        lon_range=conf.simulation.lon_range,
        endpoint=conf.simulation.endpoint,
        count=conf.simulation.count,
    )

    for response in responses:
        assert response.status_code == 200


if __name__ == '__main__':
    app()

import simulation
import requests


def app():
    responses = simulation.send_new_cases()
    for response in responses:
        assert response.status_code == 200


if __name__ == '__main__':
    app()

import requests
import pytest

def test_status_code():
    base_url= 'https://pokemonbattle.me:9104/'
    response = requests.get(f'{base_url}trainers', params= {'trainer_id' : 3859})
    assert response.status_code == 200

def test_part_of_body():
    base_url= 'https://pokemonbattle.me:9104/'
    response = requests.get(f'{base_url}trainers', params= {'trainer_id' : 3859})
    assert response.json()['trainer_name'] == 'Gaumarjos'
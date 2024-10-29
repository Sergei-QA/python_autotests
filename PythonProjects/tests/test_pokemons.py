import requests
import pytest



URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='f7f8202d09d6c3a306299eeddf77a8aa'
HEADER ={'Content-type' : 'application/json', 'trainer_token':TOKEN}
TREINER_ID='7720'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers',params ={'trainer_id':TREINER_ID})
    assert response.status_code==200

def test_part_of_response():
    response_get=requests.get(url=f'{URL}/trainers',params ={'trainer_id':TREINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'HIMIK'

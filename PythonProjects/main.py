import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='f7f8202d09d6c3a306299eeddf77a8aa'
HEADER ={'Content-type' : 'application/json', 'trainer_token':TOKEN}
body_pokemons= {
    "name": "Бульба",
    "photo_id": 1
}

body_pokemons_put={
    "pokemon_id": "117187",
    "name": "nori",
    "photo_id": 3
}

body_pokemons_in_pokeball={
    "pokemon_id": "117187"
}

'''respons=requests.post(url= f'{URL}/pokemons',headers= HEADER,json=body_pokemons)
print(respons.text)'''

'''response_create = requests.post(url= f'{URL}/pokemons',headers= HEADER,json=body_pokemons)
print(response_create.text)'''


'''put_pockemons=requests.put(url=f'{URL}/pokemons',headers=HEADER,json=body_pokemons_put)
print(put_pockemons.text)'''

pokemon_in_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_pokemons_in_pokeball)
print(pokemon_in_pokeball.text)
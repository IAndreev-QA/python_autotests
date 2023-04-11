import requests

base_url= 'https://pokemonbattle.me:9104/'
token = '85a9f4253a85411cf964505d6e643b8f'

response_add_pokemon = requests.post(f'{base_url}pokemons', headers={'trainer_token' : token}, json={
    "name": "Вахтанг",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}) 

print(response_add_pokemon.text)


response_change_name = requests.put(f'{base_url}pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": "8979",
    "name": "Гурген",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response_change_name.text)

response_add_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": "8979"
}) 

print(response_add_pokeball.text)

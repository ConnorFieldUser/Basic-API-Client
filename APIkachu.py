import requests

# url =


def get_data(endpoint, lookup="!!lookup,name??"):
    url = "http://pokeapi.co/api/v2/{}/".format(endpoint)
    while url:
        result = requests.get(url)
        json_result = result.json()

        for pokemon in json_result["results"]:
            print(pokemon[lookup])

        if input("Press enter to keep going, "):
            break

        url = json_result["next"]

while True:
    value = input("Search: ")
    get_data(value)

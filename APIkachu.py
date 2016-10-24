import requests


# LIST
def get_list_data(endpoint, lookup="name"):
    url = "http://pokeapi.co/api/v2/{}/".format(endpoint)
    print("URL: {}".format(url))
    while url:
        result = requests.get(url)
        json_result = result.json()
        for pokemon in json_result["results"]:
            print(pokemon[lookup])

        if input("Press enter to keep going, submit anything else to quit  "):
            break

        url = json_result["next"]

# while True:
#     value = input("Search: pokemon, generation, item: ").lower()
#     get_list_data(value)


# POKEMON
def get_pokemon_detail_data(endpoint, lookup="name"):
    url = "http://pokeapi.co/api/v2/pokemon/{}/".format(endpoint)
    print(url)
    while url:
        result = requests.get(url)
        json_result = result.json()
        print(json_result['name'])

        if not input("Press enter to search again, or type something to cancel "):
            url = "http://pokeapi.co/api/v2/pokemon/{}/".format(endpoint)
        else:
            return True

        url = json_result["next"]

# while True:
#     value = input("Search: ")
#     get_pokemon_detail_data(value)


# ITEM
def get_item_detail_data(endpoint, lookup="name"):
    url = "http://pokeapi.co/api/v2/item/{}/".format(endpoint)
    print(url)
    while url:
        result = requests.get(url)
        json_result = result.json()
        print(json_result['name'])

        # if input("Press enter to keep going, "):
        #     break

        if not input("Press enter to search again, or type something to cancel "):
            url = "http://pokeapi.co/api/v2/item/{}/".format(endpoint)
        else:
            return True

        url = json_result["next"]

# while True:
#     value = input("Search: ")
#     get_item_detail_data(value)


# Generation
def get_version_detail_data(endpoint, lookup="name"):
    url = "http://pokeapi.co/api/v2/generation/{}/".format(endpoint)
    print(url)
    while url:
        result = requests.get(url)
        json_result = result.json()
        print(json_result['name'])

        # if input("Press enter to keep going, "):
        #     break

        if not input("Press enter to search again, or type something to cancel "):
            url = "http://pokeapi.co/api/v2/generation/{}/".format(endpoint)
        else:
            return True

        url = json_result["next"]
#
# while True:
#     value = input("Search: ")
#     get_version_detail_data(value)


def user_input():
    user_choice = input("Browse the full (LIST)s, or seach for a (POKEMON) an, (ITEM), or a (GENERATION): ").lower()
    if user_choice == "list":
        print("list")
        value = input("List of: pokemon, generation, item: ").lower()
        get_list_data(value)

    elif user_choice == "pokemon":
        print("pokemon")
        value = input("Type the id or name: ")
        get_pokemon_detail_data(value)

    elif user_choice == "item":
        print("item")
        value = input("Type the id or name: ")
        get_item_detail_data(value)

    elif user_choice == "generation":
        print("generation")

    else:
        print(user_choice)
        print("End Program")

user_input()

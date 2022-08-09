import requests
import json
import os

class Cards:
    def __init__(self, id, name, listName = 'To Do'):
        self.id = id
        self.name = name
        self.listName = listName

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list)


def get_todo():
    lists = get_lists()
    # Get the TO DO list id
    idLists = {}
    for list in lists:
        idLists[list['id']] = list['name']

    url = "https://api.trello.com/1/boards/{}/cards".format(os.getenv('TROLLO_BOARD_ID'))

    query = {
        'key': os.getenv('TRELLO_KEY'),
        'token': os.getenv('TROLLO_TOKEN'),
        'cards': 'open'
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )
    response = json.loads(response.text)
    returnData = []
    for card in response:
        toDoItem = Cards.from_trello_card(card, idLists[card['idList']])
        returnData.append(toDoItem)
    return returnData

def get_lists():
    url = "https://api.trello.com/1/boards/{}/lists".format(os.getenv('TROLLO_BOARD_ID'))

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': os.getenv('TRELLO_KEY'),
        'token': os.getenv('TROLLO_TOKEN')
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    return json.loads(response.text)


def add_todo(item):
    lists = get_lists()
    # Get the TO DO list id
    for list in lists:
        if list['name'] == "To Do":
            id = list['id']

    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': id,
        'key': os.getenv('TRELLO_KEY'),
        'token': os.getenv('TROLLO_TOKEN'),
        'name': item
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

def update_itemList(cardId,current):
    lists = get_lists()
    # Get the TO DO list id
    idLists = {}
    for list in lists:
        idLists[list['name']] = list['id']

    if current == 'To Do':
        id = idLists['Done']
    else:
        id = idLists['To Do']

    url = "https://api.trello.com/1/cards/{id}".format(id=cardId)

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': os.getenv('TRELLO_KEY'),
        'token': os.getenv('TROLLO_TOKEN'),
        'idList': id
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )


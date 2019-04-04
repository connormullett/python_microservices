
from flask_injector import inject
from services.provider import ItemsProvider


@inject(data_provider=ItemsProvider)
def search(data_provider) -> list:
    return data_provider.get()


def get_message(message) -> str:
    return message, 200

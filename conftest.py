import allure
import pytest
from clients.http_client import get_http_client
from clients.pets_client import PetsClient
from models.pet import Pet


@pytest.fixture(scope="class")
def class_pets_client():
    http_client = get_http_client()
    client = PetsClient(client=http_client)
    yield client
    http_client.close()


@pytest.fixture(scope="function")
def function_pet(class_pets_client: PetsClient) -> Pet:
    with allure.step("Setup: create pet"):
        pet = class_pets_client.create_pet()
    yield pet
    with allure.step(f"Teardown: delete pet {pet.id}"):
        class_pets_client.delete_pet(pet.id)
import allure
import pytest
from allure_commons.types import Severity
from clients.pets_client import PetsClient
from models.pet import Pet, PetStatus
from utils.assertions import assert_pet, assert_pet_json_schema, assert_status_code


@allure.epic("Petstore API")
@allure.feature("Pets")
class TestPets:

    @allure.story("Create pet")
    @allure.title("Создание нового питомца")
    @allure.severity(Severity.CRITICAL)
    def test_create_pet(self, class_pets_client: PetsClient):
        pet = Pet()
        response = class_pets_client.create_pet_api(pet)
        assert_status_code(response, 200)
        assert_pet_json_schema(response)
        created = Pet(**response.json())
        assert_pet(created, pet)

    @allure.story("Get pet")
    @allure.title("Получение питомца по id")
    @allure.severity(Severity.CRITICAL)
    def test_get_pet_by_id(self, class_pets_client: PetsClient, function_pet: Pet):
        response = class_pets_client.get_pet_api(function_pet.id)
        assert_status_code(response, 200)
        assert_pet_json_schema(response)
        fetched = Pet(**response.json())
        assert_pet(fetched, function_pet)

    @allure.story("Update pet")
    @allure.title("Обновление имени и статуса")
    @allure.severity(Severity.NORMAL)
    def test_update_pet(self, class_pets_client: PetsClient, function_pet: Pet):
        function_pet.name = "UpdatedName"
        function_pet.status = PetStatus.SOLD
        response = class_pets_client.update_pet_api(function_pet)
        assert_status_code(response, 200)
        updated = Pet(**response.json())
        assert updated.name == "UpdatedName"
        assert updated.status == PetStatus.SOLD

    @allure.story("Delete pet")
    @allure.title("Удаление питомца и проверка 404")
    @allure.severity(Severity.CRITICAL)
    def test_delete_pet(self, class_pets_client: PetsClient, function_pet: Pet):
        response = class_pets_client.delete_pet_api(function_pet.id)
        assert_status_code(response, 200)
        check = class_pets_client.get_pet_api(function_pet.id)
        assert_status_code(check, 404)

    @allure.story("Find pets")
    @allure.title("Поиск по статусу: {status}")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("status", list(PetStatus))
    def test_find_by_status(self, class_pets_client: PetsClient, status: PetStatus):
        response = class_pets_client.find_by_status_api(status)
        assert_status_code(response, 200)
        assert isinstance(response.json(), list)

    @allure.story("Negative")
    @allure.title("Получение несуществующего питомца")
    @allure.severity(Severity.MINOR)
    @allure.tag("negative")
    def test_get_nonexistent_pet(self, class_pets_client: PetsClient):
        response = class_pets_client.get_pet_api(999_999_999)
        assert_status_code(response, 404)
        
        # Универсальная проверка: и для JSON, и для текста
        try:
            message = response.json().get("message")
        except Exception:
            message = response.text
            
        assert message == "Pet not found", f"Unexpected message: {message}"
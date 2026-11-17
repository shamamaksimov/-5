import allure
from httpx import Response
from clients.http_client import HTTPClient
from models.pet import ApiResponse, Pet


class PetsClient:
    def __init__(self, client: HTTPClient):
        self.client = client

    @allure.step("Create pet via API")
    def create_pet_api(self, pet: Pet) -> Response:
        return self.client.post("/pet", json=pet.model_dump(by_alias=True, mode="json"))

    @allure.step("Get pet by id {pet_id}")
    def get_pet_api(self, pet_id: int) -> Response:
        return self.client.get(f"/pet/{pet_id}")

    @allure.step("Update pet via API")
    def update_pet_api(self, pet: Pet) -> Response:
        return self.client.put("/pet", json=pet.model_dump(by_alias=True, mode="json"))

    @allure.step("Delete pet by id {pet_id}")
    def delete_pet_api(self, pet_id: int) -> Response:
        return self.client.delete(f"/pet/{pet_id}")

    @allure.step("Find pets by status {status}")
    def find_by_status_api(self, status: str) -> Response:
        status_value = status.value if hasattr(status, "value") else status
        return self.client.get("/pet/findByStatus", params={"status": status_value})

    @allure.step("Create pet and return model")
    def create_pet(self, pet: Pet | None = None) -> Pet:
        pet = pet or Pet()
        response = self.create_pet_api(pet)
        response.raise_for_status()
        return Pet(**response.json())

    @allure.step("Delete pet {pet_id} and return ApiResponse")
    def delete_pet(self, pet_id: int) -> ApiResponse:
        response = self.delete_pet_api(pet_id)
        response.raise_for_status()
        # Локальный сервер может вернуть просто текст
        try:
            data = response.json()
            return ApiResponse(**data)
        except Exception:
            return ApiResponse(code=200, type="string", message=response.text)
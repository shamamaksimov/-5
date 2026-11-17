import allure
from httpx import Response
from jsonschema import validate
from models.pet import Pet


@allure.step("Assert status code == {expected}")
def assert_status_code(response: Response, expected: int) -> None:
    assert response.status_code == expected, (
        f"Expected {expected}, got {response.status_code}. Body: {response.text}"
    )


@allure.step("Assert response matches Pet JSON-schema")
def assert_pet_json_schema(response: Response) -> None:
    schema = Pet.model_json_schema(by_alias=True)
    validate(instance=response.json(), schema=schema)


@allure.step("Assert pet fields match expected model")
def assert_pet(actual: Pet, expected: Pet) -> None:
    assert actual.id == expected.id
    assert actual.name == expected.name
    assert actual.status == expected.status
    assert actual.category == expected.category
    assert actual.photo_urls == expected.photo_urls
    assert actual.tags == expected.tags
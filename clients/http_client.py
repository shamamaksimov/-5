import json
import allure
from httpx import Client, Response
from config import settings

def attach_request_response(response: Response) -> None:
    """Хук для прикрепления запроса и ответа в Allure."""
    response.read()

    request = response.request
    req_body = request.content.decode("utf-8", errors="replace") if request.content else ""
    req_text = f"{request.method} {request.url}\n\n{req_body}"
    allure.attach(req_text, name=f"Request {request.method}", attachment_type=allure.attachment_type.JSON)

    try:
        res_body = json.dumps(response.json(), indent=2, ensure_ascii=False)
    except Exception:
        res_body = response.text
    allure.attach(res_body, name=f"Response {response.status_code}", attachment_type=allure.attachment_type.JSON)

class HTTPClient(Client):
    @allure.step("Make GET request to {url}")
    def get(self, url: str, **kwargs) -> Response:
        return super().get(url, **kwargs)

    @allure.step("Make POST request to {url}")
    def post(self, url: str, **kwargs) -> Response:
        return super().post(url, **kwargs)

    @allure.step("Make PUT request to {url}")
    def put(self, url: str, **kwargs) -> Response:
        return super().put(url, **kwargs)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: str, **kwargs) -> Response:
        return super().delete(url, **kwargs)

def get_http_client() -> HTTPClient:
    return HTTPClient(
        base_url=settings.base_url,
        timeout=settings.timeout,
        headers=settings.headers,
        event_hooks={"response": [attach_request_response]},
    )
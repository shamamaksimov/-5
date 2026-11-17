# КТ №5. Allure + Pydantic для API-тестов Petstore (шаблон)

Заготовка проекта. Места, которые нужно дописать, помечены `TODO 1` ... `TODO 8`.
Подробная инструкция находится в файле «Задание_КТ5.pdf».

## Установка
```
python -m venv .venv
.venv\Scripts\activate          # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```
Для отчёта нужна программа Allure Commandline (и Java): `scoop install allure` или `brew install allure`.

## Запуск
```
pytest
allure serve allure-results
python show_schema.py
```

## Порядок работы
1. `models/pet.py` (TODO 1)
2. `clients/http_client.py` (TODO 2-4)
3. `clients/pets_client.py` (TODO 5)
4. `utils/assertions.py` (TODO 6)
5. `conftest.py` (TODO 7)
6. `tests/test_pets.py` (TODO 8)

Перед сдачей замените этот README описанием вашей работы: как запустить и что реализовано.

> Пока вы не выполнили TODO 1 (модели), `pytest` и `show_schema.py` будут выдавать `ImportError`. Это нормально: после описания моделей ошибка исчезнет.

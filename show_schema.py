"""Печатает пример JSON и JSON-схему, сгенерированные Pydantic (для скриншота в отчёт)"""
import json
from models.pet import Pet

print('--- Пример тела запроса: Pet().model_dump(by_alias=True, mode="json")')
print(json.dumps(Pet().model_dump(by_alias=True, mode='json'), indent=2, ensure_ascii=False))
print('\n--- JSON-схема: Pet.model_json_schema(by_alias=True)')
print(json.dumps(Pet.model_json_schema(by_alias=True), indent=2, ensure_ascii=False))
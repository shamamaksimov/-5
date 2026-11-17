from random import choice, randint
from string import ascii_letters, digits

def random_number(start: int = 1_000_000, end: int = 9_999_999) -> int:
    return randint(start, end)

def random_string(start: int = 6, end: int = 12) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))

def random_photo_urls() -> list[str]:
    return [f'https://example.com/{random_string()}.jpg']
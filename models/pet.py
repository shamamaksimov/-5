from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from utils.fakers import random_number, random_photo_urls, random_string

class PetStatus(str, Enum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

class Category(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int = Field(default_factory=random_number)
    name: str = Field(default_factory=random_string)

class Tag(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int = Field(default_factory=random_number)
    name: str = Field(default_factory=random_string)

class Pet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int = Field(default_factory=random_number)
    name: str = Field(default_factory=random_string)
    photo_urls: list[str] = Field(alias="photoUrls", default_factory=random_photo_urls)
    category: Category | None = None
    tags: list[Tag] | None = None
    status: PetStatus = PetStatus.AVAILABLE

class ApiResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    code: int
    type: str | None = None
    message: str | None = None
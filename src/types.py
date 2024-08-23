from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SectionCreate(BaseModel):
    name: str
    description: str

class SectionResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime]
    is_deleted: bool

    class Config:
        orm_mode = True

class SectionContentCreate(BaseModel):
    content: str

class SectionContentResponse(BaseModel):
    id: int
    section_id: int
    content: str
    created_at: datetime
    updated_at: Optional[datetime]
    is_deleted: bool

    class Config:
        orm_mode = True

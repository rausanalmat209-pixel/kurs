from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class UniversityBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=200, description="Университет атауы")
    description: Optional[str] = Field(None, max_length=1000, description="Университет туралы қысқаша ақпарат")
    city: str = Field(..., min_length=2, max_length=100, description="Орналасқан қаласы")


class UniversityCreate(UniversityBase):
    """Клиенттен қабылданатын деректер.
    Шектеу: id, owner, status өрістері клиентке қолжетімді ЕМЕС.
    """
    pass


class UniversityUpdate(BaseModel):
    """Барлық өрістер міндетті емес (необязательные)."""
    name: Optional[str] = Field(None, min_length=2, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    city: Optional[str] = Field(None, min_length=2, max_length=100)


class UniversityRead(UniversityBase):
    """Жауап форматы (from_attributes=True / attributes=True)."""
    id: int
    owner: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

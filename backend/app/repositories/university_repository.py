from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.university import UniversityModel
from app.schemas.university import UniversityCreate


class UniversityRepository:
    """Repository қабаты:
    Тек SQLAlchemy арқылы дерекқормен жұмыс жасайды.
    Мұнда HTTPException және бизнес-ережелер ЖОҚ.
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def list(self, skip: int = 0, limit: int = 100) -> Sequence[UniversityModel]:
        """Университеттер тізімін алу (пагинациямен)."""
        stmt = select(UniversityModel).offset(skip).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get(self, university_id: int) -> UniversityModel | None:
        """ID бойынша университетті алу."""
        return await self.session.get(UniversityModel, university_id)

    async def create(
        self,
        data: UniversityCreate,
        owner: str = "system",
        status: str = "draft",
    ) -> UniversityModel:
        """Жаңа университет жазбасын құру (id, owner, status ішкі деңгейде беріледі)."""
        instance = UniversityModel(
            name=data.name,
            description=data.description,
            city=data.city,
            owner=owner,
            status=status,
        )
        self.session.add(instance)
        await self.session.flush()
        await self.session.refresh(instance)
        return instance

    async def save(self, instance: UniversityModel) -> UniversityModel:
        """Өзгертілген объектіні сақтау."""
        self.session.add(instance)
        await self.session.flush()
        await self.session.refresh(instance)
        return instance

    async def delete(self, instance: UniversityModel) -> None:
        """Университетті дерекқордан өшіру."""
        await self.session.delete(instance)
        await self.session.flush()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import Section, SectionContent
from src.db import get_db
from src.types import SectionCreate, SectionResponse, SectionContentCreate, SectionContentResponse

router = APIRouter()


@router.post("/sections/", status_code=201, response_model=SectionResponse)
async def add_section(section_data: SectionCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new section.
    """
    new_section = Section(name=section_data.name, description=section_data.description)
    db.add(new_section)
    await db.commit()
    await db.refresh(new_section)
    return new_section


@router.post("/sections/{section_id}/content/", status_code=201, response_model=SectionContentResponse)
async def add_section_content_item(section_id: int, content_data: SectionContentCreate, db: AsyncSession = Depends(get_db)):
    """
    Add content to a specific section.
    """
    # Verify the section exists and is not deleted
    result = await db.execute(select(Section).filter(Section.id == section_id, Section.is_deleted == False))
    section = result.scalar_one_or_none()
    if not section:
        raise HTTPException(status_code=404, detail="Section not found or is deleted")
    
    content_item = SectionContent(section_id=section_id, content=content_data.content)
    db.add(content_item)
    await db.commit()
    await db.refresh(content_item)
    return content_item


@router.get("/sections/{section_id}/content/", response_model=list[SectionContentResponse])
async def get_section_content(section_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get all content items for a specific section.
    """
    # Verify the section exists and is not deleted
    result = await db.execute(select(Section).filter(Section.id == section_id, Section.is_deleted == False))
    section = result.scalar_one_or_none()
    if not section:
        raise HTTPException(status_code=404, detail="Section not found or is deleted")

    # Fetch the content items for this section
    result = await db.execute(
        select(SectionContent).filter(SectionContent.section_id == section_id, SectionContent.is_deleted == False)
    )
    content_items = result.scalars().all()

    return content_items

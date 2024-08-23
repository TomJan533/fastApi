from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()

class Section(Base):
    __tablename__ = 'sections'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)

    # Relationship to SectionContent
    contents = relationship("SectionContent", back_populates="section", cascade="all, delete-orphan")


class SectionContent(Base):
    __tablename__ = 'section_contents'

    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey('sections.id'), nullable=False)
    content = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)

    # Define relationship to Section
    section = relationship("Section", back_populates="contents")


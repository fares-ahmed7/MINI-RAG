from .minirag_base import SQLAlchemyBase
from sqlalchemy import Column, Integer, func, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Project(SQLAlchemyBase):

    __tablename__ = "projects"
    Project_id = Column(Integer, primary_key=True, autoincrement=True)
    Project_uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    
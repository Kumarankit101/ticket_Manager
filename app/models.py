import uuid
from sqlalchemy import Column, String, Enum, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .database import Base


# Ticket Model
class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(
        Enum("open", "in_progress", "resolved", "closed", name="ticket_status"),
        nullable=False,
        default="open",
    )
    priority = Column(
        Enum("low", "medium", "high", "urgent", name="ticket_priority"),
        nullable=False,
        default="medium",
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    assigned_to = Column(UUID(as_uuid=True), ForeignKey("agents.id"), nullable=True)


# Agent Model
class Agent(Base):
    __tablename__ = "agents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

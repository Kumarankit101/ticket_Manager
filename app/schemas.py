from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
from datetime import datetime


# Ticket Create
class TicketCreate(BaseModel):
    title: str
    description: str
    status: str
    priority: str
    assigned_to: Optional[uuid.UUID] = None


# Ticket Response
class TicketResponse(TicketCreate):
    id: uuid.UUID
    status: str
    created_at: datetime
    updated_at: datetime
    assigned_to: Optional[uuid.UUID]


# Agent Create
class AgentCreate(BaseModel):
    name: str
    email: EmailStr


# Agent Response
class AgentResponse(AgentCreate):
    id: uuid.UUID
    created_at: datetime

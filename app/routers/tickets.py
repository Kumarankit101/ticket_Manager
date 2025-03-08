from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import (
    create_ticket,
    get_tickets,
    get_ticket_by_id,
    update_ticket,
    delete_ticket,
)
from ..schemas import TicketCreate, TicketResponse
from uuid import UUID
from ..realtime import publish_update  # Import Ably function


router = APIRouter()


# CREATE Ticket
@router.post("/tickets", response_model=TicketResponse)
def create_new_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db, ticket)


# GET Tickets
@router.get("/tickets")
def list_tickets(db: Session = Depends(get_db)):
    return get_tickets(db)


# GET Ticket by ID
@router.get("/tickets/{id}", response_model=TicketResponse)
def read_ticket(id: UUID, db: Session = Depends(get_db)):
    return get_ticket_by_id(db, id)


# PATCH Ticket
@router.patch("/tickets/{id}", response_model=TicketResponse)
async def modify_ticket(id: UUID, update_data: dict, db: Session = Depends(get_db)):
    return await update_ticket(db, id, update_data, publish_update)


# DELETE Ticket
@router.delete("/tickets/{id}")
def remove_ticket(id: UUID, db: Session = Depends(get_db)):
    return delete_ticket(db, id)

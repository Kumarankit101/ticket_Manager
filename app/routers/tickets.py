from fastapi import APIRouter, Depends, HTTPException
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
    try:
        return create_ticket(db, ticket)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


# GET Tickets
@router.get("/tickets")
def list_tickets(db: Session = Depends(get_db)):
    try:
        return get_tickets(db)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


# GET Ticket by ID
@router.get("/tickets/{id}", response_model=TicketResponse)
def read_ticket(id: UUID, db: Session = Depends(get_db)):
    try:
        return get_ticket_by_id(db, id)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


# PATCH Ticket
@router.patch("/tickets/{id}", response_model=TicketResponse)
async def modify_ticket(id: UUID, update_data: dict, db: Session = Depends(get_db)):
    try:
        return await update_ticket(db, id, update_data, publish_update)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


# DELETE Ticket
@router.delete("/tickets/{id}")
def remove_ticket(id: UUID, db: Session = Depends(get_db)):
    try:
        return delete_ticket(db, id)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )

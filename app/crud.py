from sqlalchemy.orm import Session
from .models import Ticket, Agent
from .schemas import TicketCreate, AgentCreate
from fastapi import HTTPException
from uuid import UUID


# CREATE Ticket
def create_ticket(db: Session, ticket: TicketCreate):
    if ticket.assigned_to is not None:  # ✅ Check only if assigned_to is provided
        agent = db.query(Agent).filter(Agent.id == ticket.assigned_to).first()
        if not agent:
            raise HTTPException(status_code=400, detail="Assigned agent does not exist")
    new_ticket = Ticket(**ticket.model_dump())
    print(new_ticket.__dict__)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


# GET Tickets
def get_tickets(db: Session):
    return db.query(Ticket).all()


# GET Ticket by ID
def get_ticket_by_id(db: Session, ticket_id: UUID):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


# UPDATE Ticket
async def update_ticket(
    db: Session, ticket_id: UUID, update_data: dict, publish_update
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    # Validate assigned_to if provided
    if "assigned_to" in update_data and update_data["assigned_to"] is not None:
        agent = db.query(Agent).filter(Agent.id == update_data["assigned_to"]).first()
        if not agent:
            raise HTTPException(status_code=400, detail="Assigned agent does not exist")

    # Update ticket fields dynamically
    for key, value in update_data.items():
        setattr(ticket, key, value)

    db.commit()
    db.refresh(ticket)

    # Broadcast real-time update when status changes
    if "status" in update_data:
        await publish_update(
            "ticket_updated", {"id": str(ticket.id), "status": ticket.status}
        )

    return ticket


# DELETE Ticket
def delete_ticket(db: Session, ticket_id: UUID):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    db.delete(ticket)
    db.commit()

    return {"detail": "Ticket deleted successfully"}

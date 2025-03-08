from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from ..database import get_db
from ..models import Agent
from ..schemas import AgentCreate, AgentResponse

router = APIRouter()


# CREATE Agent
@router.post("/agents", response_model=AgentResponse)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    existing_agent = db.query(Agent).filter(Agent.email == agent.email).first()
    if existing_agent:
        raise HTTPException(
            status_code=400, detail="Agent with this email already exists"
        )

    new_agent = Agent(name=agent.name, email=agent.email)
    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)
    return new_agent


# GET Agents
@router.get("/agents", response_model=list[AgentResponse])
def list_agents(db: Session = Depends(get_db)):
    return db.query(Agent).all()

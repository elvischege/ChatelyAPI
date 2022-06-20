
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud


from app.schemas import chat as message_schema
from app.api.deps import get_db

router = APIRouter()


@router.get("", response_model=List[message_schema.Message])
def read_messages(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all messages.
    """
    print(db)
    messages = crud.messages.get_multi(db, skip=skip, limit=limit)
    return messages

@router.post("", response_model=message_schema.Message)
def create_message(*, db: Session = Depends(get_db), message_in: message_schema.Message) -> Any:
    """
    Create new messages.
    """
    message = crud.message.create(db, obj_in=message_in)
    return message
from pydantic import BaseModel, EmailStr # type: ignore
from datetime import datetime

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(BaseModel):
    class_id: int
    class_name: str
    client_name: str
    client_email: str
    booked_at: datetime

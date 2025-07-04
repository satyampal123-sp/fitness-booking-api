from fastapi import FastAPI, HTTPException, Query # type: ignore
from pydantic import EmailStr # type: ignore
from typing import Optional

from models import BookingRequest, BookingResponse
from database import classes, bookings
from crud import get_all_classes, create_booking, get_bookings_by_email

app = FastAPI()


@app.get("/classes")
def get_classes(timezone: Optional[str] = Query("Asia/Tokyo")):
    return get_all_classes(timezone)


@app.post("/book", response_model=BookingResponse)
def book_class(request: BookingRequest):
    return create_booking(request)


@app.get("/bookings")
def get_bookings(email: EmailStr):
    return get_bookings_by_email(email)

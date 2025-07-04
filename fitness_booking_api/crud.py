from fastapi import HTTPException # type: ignore
from datetime import datetime
import pytz # type: ignore

from database import classes, bookings
from utils import convert_to_timezone
from models import BookingRequest

def get_all_classes(timezone: str):
    try:
        return [
            {
                "id": c["id"],
                "name": c["name"],
                "datetime": convert_to_timezone(c["datetime"], timezone).isoformat(),
                "instructor": c["instructor"],
                "available_slots": c["available_slots"]
            }
            for c in classes
        ]
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail="Invalid timezone")

def create_booking(request: BookingRequest):
    for c in classes:
        if c["id"] == request.class_id:
            if c["available_slots"] <= 0:
                raise HTTPException(status_code=400, detail="No slots available")
            c["available_slots"] -= 1
            booking = {
                "class_id": c["id"],
                "class_name": c["name"],
                "client_name": request.client_name,
                "client_email": request.client_email,
                "booked_at": datetime.now(pytz.utc)
            }
            bookings.append(booking)
            return booking
    raise HTTPException(status_code=404, detail="Class not found")

def get_bookings_by_email(email: str):
    return [b for b in bookings if b["client_email"] == email]

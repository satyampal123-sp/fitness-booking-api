from datetime import datetime
import pytz # type: ignore

IST = pytz.timezone("Asia/Kolkata")

classes = [
    {
        "id": 1,
        "name": "Yoga",
        "datetime": IST.localize(datetime(2025, 7, 4, 8, 0)),
        "instructor": "Satyam Pal",
        "available_slots": 10
    },
    {
        "id": 2,
        "name": "Zumba",
        "datetime": IST.localize(datetime(2025, 7, 4, 18, 0)),
        "instructor": "Soumabrata Sain",
        "available_slots": 5
    },
    {
        "id": 3,
        "name": "HIIT",
        "datetime": IST.localize(datetime(2025, 7, 5, 7, 0)),
        "instructor": "Avijit Pal",
        "available_slots": 8
    }
]

bookings = []

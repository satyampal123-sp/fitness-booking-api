# 🏋️ Fitness Booking API

A simple FastAPI backend for a fitness studio offering classes like Yoga, Zumba, and HIIT.

## 🚀 Features

- View available classes (`GET /classes`)
- Book a class (`POST /book`)
- View bookings by email (`GET /bookings`)
- Timezone-aware schedule support

## 🔧 Setup

pip install -r requirements.txt
uvicorn main:app --reload

Visit Swagger docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📌 API Example

### `GET /classes`

Optional: `?timezone=Asia/Kolkata`

### `POST /book`

```json
{
  "class_id": 1,
  "client_name": "Satyam",
  "client_email": "satyam@example.com"
}
```

### `GET /bookings?email=satyam@example.com`

## 🧪 Run Tests

pytest test_app.py

## 🎥 Loom Demo

[Watch Demo](https://loom.com/your-demo-link)

Built with ❤️ by **Satyam Pal**


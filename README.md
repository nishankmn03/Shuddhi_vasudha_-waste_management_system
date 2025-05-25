# Shuddhi Waste Management Web App

A full-stack waste booking and tracking system for Karnataka municipalities.

## Features

- User Signup/Login
- Waste booking (e-waste, scrap, disposal, etc.)
- Select pickup date and time
- View bookings
- Live tracking via Google Maps
- REST API for frontend integration

## Technologies Used

- Frontend: HTML, CSS, JavaScript (for Netlify)
- Backend: Python Flask (for Render or Railway)
- Database: SQLite (built-in)
- Google Maps API

---

## Project Structure

```
shuddhi_waste_management_app/
├── frontend/              # Netlify frontend
│   ├── index.html
│   └── static/
│       └── style.css
├── backend/               # Flask backend
│   ├── app.py
│   ├── templates/
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   └── tracking.html
```

---

## Deployment Instructions

### Backend (Render/Railway)

1. Push `backend/` folder to GitHub
2. On [Render](https://render.com):
   - New → Web Service
   - Connect your GitHub repo
   - Build Command: `pip install -r requirements.txt` (you may add this manually)
   - Start Command: `python app.py`
   - Set environment variable: `SECRET_KEY` (optional)

3. Save and deploy → Copy the backend URL

### Frontend (Netlify)

1. Log in to [Netlify](https://netlify.com)
2. Drag and drop `frontend/` folder into the deploy box
3. After upload, visit your live frontend URL

> Update frontend JS fetch URLs to use your Render backend domain

---

## API Endpoints

Base URL: `https://your-backend.onrender.com`

| Method | Endpoint         | Description                  |
|--------|------------------|------------------------------|
| POST   | `/signup`        | User registration (form)     |
| POST   | `/login`         | User login (form)            |
| GET    | `/dashboard`     | Booking form + dashboard     |
| POST   | `/dashboard`     | Create booking               |
| GET    | `/tracking`      | Live map view                |
| GET    | `/api/bookings`  | Returns JSON list of bookings for user |

---

## Google Maps Setup

In `tracking.html`, replace:

```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
```

with your actual API key from [Google Cloud Console](https://console.cloud.google.com/)

---

## Notes

- Ensure CORS is enabled in Flask (`from flask_cors import CORS; CORS(app)`)
- You may extend it with notifications, admin panel, etc.

---

Created by ChatGPT for your custom project needs.
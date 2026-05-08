# Real-Time Face Detection Video Streaming System

## Overview

A real-time face detection and video streaming system built using FastAPI, React, PostgreSQL, WebSockets, and MediaPipe.

The application accepts live video frames from the frontend, processes them on the backend to detect faces, draws ROI (Region of Interest) bounding boxes without using OpenCV for rendering, stores ROI metadata in PostgreSQL, and streams processed frames back to the frontend in real time.

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- MediaPipe
- WebSockets
- Pillow (PIL)

## Frontend

- React.js
- Vite
- react-webcam

## DevOps

- Docker
- Docker Compose

---

# Features

- Real-time face detection
- WebSocket-based live video streaming
- ROI (Region of Interest) extraction and storage
- Bounding box rendering without OpenCV drawing utilities
- PostgreSQL integration for ROI persistence
- Responsive React frontend UI
- Dockerized multi-service setup
- Environment variable-based configuration

---

# Project Structure

```bash
face-detection-system/
│
├── backend/
│   ├── app/
│   │   ├── database.py
│   │   ├── face_detection.py
│   │   ├── image_utils.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── websocket.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   └── App.jsx
│   │
│   ├── Dockerfile
│   └── package.json
│
└── docker-compose.yml
```

---

# Backend Setup

## 1. Navigate to Backend

```bash
cd backend
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file inside `backend/`

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/face_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

---

## 5. Create PostgreSQL Database

Create database:

```sql
CREATE DATABASE face_db;
```

---

## 6. Run Backend Server

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup

## 1. Navigate to Frontend

```bash
cd frontend
```

---

## 2. Install Dependencies

```bash
npm install
```

---

## 3. Run Frontend

```bash
npm run dev
```

Frontend runs at:

```bash
http://localhost:5173
```

---

# Docker Setup

## Start Full Application

From project root:

```bash
docker compose up --build
```

---

# API Endpoints

## REST Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "Backend is running 🚀"
}
```

---

### Get ROI Data

```http
GET /roi
```

Returns all stored ROI metadata.

---

## WebSocket Endpoint

### Video Streaming

```txt
ws://127.0.0.1:8000/ws/video
```

Accepts:

- image frames from frontend

Returns:

- processed frames with ROI bounding box overlays

---

# Database Schema

## ROI Table

| Field     | Type     |
| --------- | -------- |
| id        | Integer  |
| x         | Integer  |
| y         | Integer  |
| width     | Integer  |
| height    | Integer  |
| timestamp | DateTime |

---

# Architecture

```text
Frontend (React)
        │
        │ WebSocket Frames
        ▼
Backend (FastAPI)
        │
        ├── Face Detection (MediaPipe)
        ├── ROI Rendering
        └── PostgreSQL Storage
        │
        ▼
Processed Frames + ROI Data
```

---

# Error Handling

The system includes:

- WebSocket connection validation
- Empty frame checks
- Database session handling
- Face detection fallback handling when no face is detected

---

# Security Practices

- Environment variable-based credential management
- `.env` excluded from Git tracking
- Database credentials not hardcoded
- Service separation through Docker containers

---

# Testing

## Manual End-to-End Testing

Tested workflow:

```text
Frontend Webcam Feed
        ↓
WebSocket Streaming
        ↓
Backend Frame Processing
        ↓
Face Detection
        ↓
ROI Storage in PostgreSQL
        ↓
Processed Frame Rendering
```

Verified:

- live frame transmission
- ROI detection
- ROI persistence
- processed image streaming
- frontend-backend connectivity

---

# AI Usage Attestation

AI tools were used during development for:

- project planning
- debugging assistance
- Docker setup guidance
- README drafting
- frontend UI improvements
- architecture discussions

All implementation decisions, integration, testing, and code understanding were performed manually.

---

# Future Improvements

- Multiple face detection support
- Authentication and access control
- Video upload support
- Automated unit/integration tests
- ROI analytics dashboard
- Cloud deployment

---

# Author

Dinesh Kharah

# Chemical Equipment Parameter Visualizer
## Hybrid Web + Desktop Application

---

## 📌 Project Overview

The **Chemical Equipment Parameter Visualizer** is a hybrid application designed to analyze and visualize operational parameters of chemical equipment using a unified backend architecture.

The system supports both **Web** and **Desktop** clients, enabling consistent data processing, analytics, and visualization across platforms.

Users can upload CSV datasets containing chemical equipment parameters such as **flowrate, pressure, and temperature**. The backend processes the data, generates analytical summaries, and exposes results through REST APIs consumed by both frontends.

---

## 🏗️ System Architecture

CSV Dataset  
→ Django REST API (Backend)  
→ React Web Application (Charts + Tables)  
→ PyQt5 Desktop Application (Charts + Tables)

---

## ✨ Key Features

- CSV file upload via Web and Desktop applications
- Automated data analysis using Pandas
- Summary statistics:
  - Total equipment count
  - Average flowrate, pressure, and temperature
  - Equipment type distribution
- Interactive data visualization
  - Web: Chart.js
  - Desktop: Matplotlib
- Dataset history management (last 5 uploads)
- Secure REST APIs using Basic Authentication

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- Pandas
- SQLite

### Web Frontend
- React.js
- Axios
- Chart.js

### Desktop Frontend
- PyQt5
- Matplotlib
- Requests

### Other Tools
- Git & GitHub

---

## 📁 Project Structure

chemical-equipment-visualizer/
├── backend/
│   └── server/
│       ├── equipment/
│       ├── server/
│       └── manage.py
├── web-frontend/
│   └── equipment-web/
├── desktop-frontend/
│   └── app.py
├── sample_equipment_data.csv
├── screenshots/
├── README.md
└── .gitignore

---

## ⚙️ Setup Instructions

### 1️⃣ Backend Setup

cd backend  
python -m venv venv  
venv\Scripts\activate  
pip install django djangorestframework pandas django-cors-headers  
cd server  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  

Backend URL:  
http://127.0.0.1:8000

---

### 2️⃣ Web Frontend Setup

cd web-frontend/equipment-web  
npm install  
npm start  

Web Application URL:  
http://localhost:3000

---

### 3️⃣ Desktop Application Setup

cd desktop-frontend  
python -m venv venv  
venv\Scripts\activate  
pip install pyqt5 matplotlib pandas requests  
python app.py  

---

## 🔌 API Endpoints

Method | Endpoint        | Description
------ | --------------- | ------------------------------
POST   | /api/upload/    | Upload CSV and generate analytics
GET    | /api/history/   | Retrieve last 5 dataset summaries

---

## 📄 Sample Dataset

A sample CSV file **sample_equipment_data.csv** is provided for testing.

Expected columns:
- Equipment Name
- Type
- Flowrate
- Pressure
- Temperature

---

## 🖼️ Screenshots

Web Application – Dashboard  
screenshots/web_dashboard.png

Desktop Application – Interface  
screenshots/desktop_app.png

---

## 🎯 Learning Outcomes

- Hybrid application architecture
- REST API development
- Frontend–backend integration
- Data analytics using Pandas
- Cross-platform visualization

---

## 📜 License

This project is intended for academic and educational use.

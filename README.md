Chemical Equipment Parameter Visualizer

Hybrid Web + Desktop Application

Project Overview

The Chemical Equipment Parameter Visualizer is a hybrid application designed to analyze and visualize operational parameters of chemical equipment using a unified backend architecture. The system supports both Web and Desktop clients, enabling consistent data processing, analytics, and visualization across platforms.

Users can upload CSV datasets containing chemical equipment parameters such as flowrate, pressure, and temperature. The backend processes the data, generates analytical summaries, and exposes the results through REST APIs consumed by both frontends.

System Architecture
CSV Dataset
     │
     ▼
Django REST API (Backend)
     │
     ├── React Web Application (Charts + Tables)
     │
     └── PyQt5 Desktop Application (Charts + Tables)


Single backend

Multiple frontends

Consistent analytics and visualization

Key Features

CSV file upload via Web and Desktop applications

Automated data analysis using Pandas

Summary statistics:

Total equipment count

Average flowrate, pressure, and temperature

Equipment type distribution

Interactive data visualization:

Web: Chart.js

Desktop: Matplotlib

Dataset history management (last 5 uploads stored)

PDF report generation

Basic authentication for secured API access

Tech Stack
Backend

Python

Django

Django REST Framework

Pandas

SQLite

Web Frontend

React.js

Axios

Chart.js

Desktop Frontend

PyQt5

Matplotlib

Requests

Other Tools

Git & GitHub

ReportLab (PDF generation)

Project Structure
chemical-equipment-visualizer/
│
├── backend/
│   └── server/
│       ├── equipment/
│       ├── server/
│       └── manage.py
│
├── web-frontend/
│   └── equipment-web/
│
├── desktop-frontend/
│   └── app.py
│
├── sample_equipment_data.csv
├── README.md
├── .gitignore

Setup Instructions
1. Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework pandas reportlab django-cors-headers
cd server
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Backend runs at:

http://127.0.0.1:8000

2. Web Frontend Setup
cd web-frontend/equipment-web
npm install
npm start


Web app runs at:

http://localhost:3000

3. Desktop Application Setup
cd desktop-frontend
python -m venv venv
venv\Scripts\activate
pip install pyqt5 matplotlib pandas requests
python app.py

API Endpoints
Method	Endpoint	Description
POST	/api/upload/	Upload CSV and generate analytics
GET	/api/history/	Retrieve last 5 dataset summaries
GET	/api/report/	Download PDF report

All endpoints are protected using Basic Authentication.

Sample Dataset

A sample CSV file sample_equipment_data.csv is provided for testing and demonstration purposes.

Expected columns:

Equipment Name

Type

Flowrate

Pressure

Temperature


Learning Outcomes

Hybrid application architecture

REST API development

Frontend-backend integration

Data analytics using Pandas

Data visualization across platforms

Secure API access

Screenshots
Web Application – CSV Upload & Dashboard

CSV file upload interface

Summary statistics displayed using cards

Interactive data visualization for equipment parameters

![Web Dashboard](screenshots/web_dashboard.png)

Web Application – Dataset History

Displays the last five uploaded datasets

Shows upload timestamp and total equipment count

![Web History](screenshots/web_history.png)

Desktop Application – PyQt5 Interface

CSV upload via desktop client

Tabular data display

Equipment type distribution visualized using Matplotlib

![Desktop Application](screenshots/desktop_app.png)

PDF Report Generation

Automatically generated summary report

Includes dataset statistics and timestamp

![PDF Report](screenshots/pdf_report.png)

# POS Device & Service Management App

A full-stack **Python Django** application styled with **Tailwind CSS**, built to manage and monitor **POS (Point of Sale) devices**, **clients**, and **technician service requests**.

---

## 🚀 Features

- 🔒 Custom user roles: **Technicians** and **Clients**
- 🛠️ Technicians can:
  - Manage all devices
  - Assign devices to clients
  - Track and complete service requests
  - View dashboard with stats
- 👨‍💼 Clients can:
  - Monitor their own devices
  - Request services for a specific device
  - Cancel a pending service request
- 📆 Yearly service tracking
- 📬 Login with role selection
- 🧾 Success & error messages with Tailwind styling
- ✅ Clean and responsive UI using **Tailwind CSS CDN**

---

## 🏗️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Tailwind CSS (CDN-based)
- **Database**: SQLite (default, can be swapped for PostgreSQL/MySQL)
- **Templates**: Django Template Engine
- **Authentication**: Custom user model with role-based access

---

## 📁 Project Structure

pos_service/
├── devices/ # Device models, views, and forms
├── services/ # Service tracking logic
├── users/ # Custom user model and authentication
├── home/ # Base templates and homepage
├── static/ # CSS, JS, images
├── templates/
│ ├── home/
│ ├── devices/
│ ├── services/
│ └── users/
├── db.sqlite3
├── manage.py
└── README.md

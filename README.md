# 💳 Raseed | رصيد

![Project Status](https://img.shields.io/badge/Status-Stable_V2.0-emerald?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Tailwind](https://img.shields.io/badge/Frontend-Tailwind_CSS-38bdf8?style=for-the-badge&logo=tailwindcss)

> **A Secure, Cloud-Ready Rental Management SaaS Platform.**
> Raseed V2.0 transforms property management with a multi-user authentication system, PostgreSQL support, and a modern dark-themed interface.

---

## 📸 Screenshots
*(Screenshots coming soon...)*

---

## ⚡ Key Features (v2.0)

### 🔐 Security & Access
- **Multi-User System:** 👤 Complete isolation between users. Your data is private and visible only to you.
- **Secure Authentication:** Built-in Login & Signup system with hashed passwords using `Werkzeug` & `Flask-Login`.
- **Smart Routing:** Protected dashboard routes; unauthorized users are redirected to the landing page.

### 🏢 SaaS-Ready Architecture
- **Hybrid Database Engine:** 🔄 Automatically switches between **SQLite** (Local Development) and **PostgreSQL** (Production/Render).
- **Production Ready:** Configured with `Gunicorn` and `Procfile` for seamless cloud deployment.

### 💰 Financial Management
- **Smart Ledger:** Track paid/remaining installments with color-coded indicators.
- **Excel Integration:** 📂 Bulk upload payment schedules via `.xlsx`.
- **Alert System:** ⚠️ Auto-notifications for payments due within 15 days.

### 🌐 Modern Experience
- **Landing Page:** A professional, responsive home page for marketing the platform.
- **Dark Mode UI:** 🌑 A unified, sleek dark theme (Slate-900) for better visual comfort.
- **Dynamic Navbar:** Context-aware navigation (shows "Login" for guests, "Dashboard/Logout" for users).

---

## 🛠️ Tech Stack

* **Core:** Python, Flask, Jinja2.
* **Database:** SQLAlchemy (ORM), SQLite / PostgreSQL.
* **Frontend:** HTML5, Tailwind CSS (CDN).
* **Security:** Flask-Login, Werkzeug Security.
* **Deployment:** Gunicorn, Render.

---

## 🚀 How to Run (Locally)

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KhalidExe/Raseed.git](https://github.com/KhalidExe/Raseed.git)
    cd Raseed
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```
    *The app will automatically create a local `raseed_v2.db` database.*

4.  **Access the Platform:**
    Open your browser and go to: `http://127.0.0.1:5000`

---

## 📂 Project Structure

```text
Raseed/
│
├── app.py                 # Main Application Controller
├── database.py            # Database Models & Logic (SQLAlchemy)
├── requirements.txt       # Project Dependencies
├── Procfile               # Production Entry Point (Gunicorn)
├── build.sh               # Build Script for Render
│
├── templates/             # Frontend Views
│   ├── landing.html       # Home/Marketing Page
│   ├── login.html         # User Authentication
│   ├── signup.html        # User Registration
│   ├── index.html         # Dashboard & Alerts
│   ├── tenant.html        # Tenant Ledger
│   └── base.html          # Main Layout
│
└── raseed_v2.db           # (Local Dev Database - Auto Generated)
```
---

## 📝 Data Formatting Guide (Excel)

To import a schedule for a tenant, upload an Excel file with **two columns** (Date & Amount).

> **💡 Quick Test:** You can use the ready-made sample file included in this project: [Download tryme.xlsx](tryme.xlsx)

| Date (التاريخ) | Amount (المبلغ) |
| :--- | :--- |
| 2026-01-01 | 5000 |
| 2026-04-01 | 5000 |
| ... | ... |

--- 

## 🔮 Future Roadmap
- [ ] 📧 Email Notifications: Send PDF receipts to tenants automatically.

- [ ] 📊 Advanced Analytics: Visual charts for yearly revenue.

- [ ] 📱 PWA Support: Install the app on mobile devices.

---

*Developed by **KhalidExe** © 2026*


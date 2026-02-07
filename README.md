# 💳 Raseed | رصيد

![Project Status](https://img.shields.io/badge/Status-Stable_V2.1-emerald?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Tailwind](https://img.shields.io/badge/Frontend-Tailwind_CSS-38bdf8?style=for-the-badge&logo=tailwindcss)

> **A Bilingual, Cloud-Ready Rental Management SaaS Platform.**
> Raseed V2.1 transforms property management with a fully localized interface (Arabic/English), visual financial analytics, and a secure multi-user architecture.

---

## 📸 Screenshots
*(Screenshots coming soon...)*

---

## ⚡ Key Features (v2.1)

### 🌍 Bilingual & Visual Experience (New)
- **Full Localization:** 🇸🇦/🇺🇸 Switch instantly between **Arabic (RTL)** and **English (LTR)**.
- **Interactive Charts:** 📊 Visual doughnut charts powered by **Chart.js** to track Paid vs. Remaining balances instantly.
- **Dynamic UI:** Interface automatically adapts direction (RTL/LTR) based on selected language.

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

---

## 🛠️ Tech Stack

* **Core:** Python, Flask, Jinja2.
* **Database:** SQLAlchemy (ORM), SQLite / PostgreSQL.
* **Frontend:** HTML5, Tailwind CSS (CDN), Chart.js.
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
├── database.py            # Database Models & Logic
├── translations.py        # 🌍 Localization Dictionary (Ar/En)
├── requirements.txt       # Project Dependencies
├── Procfile               # Production Entry Point
│
├── templates/             # Frontend Views
│   ├── landing.html       # Marketing Page
│   ├── login.html         # Auth Pages
│   ├── index.html         # Dashboard & Charts
│   ├── tenant.html        # Tenant Ledger
│   └── base.html          # Layout & Navbar
│
└── raseed_v2.db           # (Local Dev Database)
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
- [x] 🌍 Bilingual Support (Arabic/English).

- [x] 📊 Visual Analytics (Charts).

- [ ] 📧 Email Notifications: Send PDF receipts to tenants automatically.

- [ ] 📱 PWA Support: Install the app on mobile devices.

---

*Developed by **KhalidExe** © 2026*


# 💳 Raseed | رصيد

![Version](https://img.shields.io/badge/Release-v2.2.0-teal?style=for-the-badge)
![Theme](https://img.shields.io/badge/Theme-Light%20%26%20Dark-0f172a?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Tailwind](https://img.shields.io/badge/Frontend-Tailwind_CSS-38bdf8?style=for-the-badge&logo=tailwindcss)

> **A Modern, Bilingual Property Management SaaS.**
> Raseed v2.2 introduces a complete UI overhaul with a dual-theme engine (Light/Dark), smart financial alerts, and a brand-new visual identity.

---

## 📸 Screenshots
*(Screenshots coming soon...)*

---

## ⚡ Key Features (v2.2)

### 🎨 Dual-Theme UI (New)
* **Adaptive Interface:** 🌗 The entire platform now supports **Light Mode** (Clean White/Gray) for daytime productivity and **Dark Mode** (Deep Navy/Slate) for night usage.
* **Smart Toggle:** Automatically detects system preference or can be toggled manually.
* **New Branding:** Refreshed identity with **Teal** (Primary) and **Orange** (Accents) colors.

### 🔔 Smart Notification Center (New)
* **Context-Aware Alerts:**
    * 🔴 **Overdue:** Highlights missed payments in Red with a "Days Overdue" counter.
    * 🟠 **Upcoming:** Warns about payments due within 15 days in Orange.
* **Visual Badges:** Clear status indicators for immediate action.

### 🌍 Bilingual & Visual Experience
* **Full Localization:** 🇸🇦/🇺🇸 Switch instantly between **Arabic (RTL)** and **English (LTR)**.
* **Interactive Charts:** 📊 Visual doughnut charts powered by **Chart.js** (updated with new brand colors) to track Paid vs. Remaining balances.

### 🔐 Security & Access
* **Multi-User System:** 👤 Complete isolation between users. Your data is private and visible only to you.
* **Secure Authentication:** Built-in Login & Signup system with hashed passwords using `Werkzeug` & `Flask-Login`.

### 🏢 SaaS-Ready Architecture
* **Hybrid Database Engine:** 🔄 Automatically switches between **SQLite** (Local Development) and **PostgreSQL** (Production/Render).
* **Production Ready:** Configured with `Gunicorn` and `Procfile` for seamless cloud deployment.

### 💰 Financial Management
* **Smart Ledger:** Track paid/remaining installments with color-coded badges.
* **Excel Integration:** 📂 Bulk upload payment schedules via `.xlsx`.

---

## 🛠️ Tech Stack

* **Core:** Python, Flask, Jinja2.
* **Database:** SQLAlchemy (ORM), SQLite / PostgreSQL.
* **Frontend:** HTML5, Tailwind CSS (v3.4), Chart.js.
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
├── templates/             # Frontend Views (Jinja2)
│   ├── base.html          # Layout & Theme Logic
│   ├── index.html         # Dashboard & Smart Alerts
│   ├── tenant.html        # Tenant Ledger
│   └── ...
│
└── raseed_v2.db           # (Local Dev Database - GitIgnored)
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

- [x] 🎨 Dual-Theme Support (Light/Dark).

- [ ] 📧 Email Notifications: Send PDF receipts to tenants automatically.

- [ ] 📱 PWA Support: Install the app on mobile devices.

---

*Developed by **KhalidExe** © 2026*


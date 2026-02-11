# 💳 Raseed | رصيد

![Version](https://img.shields.io/badge/Release-v2.3.0-teal?style=for-the-badge)
![PWA](https://img.shields.io/badge/PWA-Ready-purple?style=for-the-badge&logo=pwa&logoColor=white)
![Theme](https://img.shields.io/badge/Theme-Light%20%26%20Dark-0f172a?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

> **A Modern, Bilingual Property Management SaaS.**
> Raseed v2.3 transforms into a **Progressive Web App (PWA)**, allowing users to install it on mobile devices. It also features a refined UI with infinite animations and a polished visual identity.

---

## 📸 Screenshots
*(Screenshots coming soon...)*

---

## ⚡ Key Features (v2.3)

### 📱 Mobile App Experience (PWA) - **New!**
* **Installable:** Add Raseed to your phone's home screen just like a native app.
* **App-Like Feel:** Runs in standalone mode without the browser address bar.
* **Custom Icons:** High-quality icons for iOS and Android home screens.

### 🎨 Visual & UI Enhancements - **New!**
* **Infinite Marquee:** A dynamic, auto-scrolling feature strip on the landing page.
* **Branded Favicon:** Custom **RJ** logo in the browser tab for a professional look.
* **Dual-Theme UI:** 🌗 Adaptive **Light Mode** & **Dark Mode** support.

### 🔔 Smart Notification Center
* **Context-Aware Alerts:**
    * 🔴 **Overdue:** Highlights missed payments in Red with a "Days Overdue" counter.
    * 🟠 **Upcoming:** Warns about payments due within 15 days in Orange.

### 🌍 Bilingual & Visual Experience
* **Full Localization:** 🇸🇦/🇺🇸 Switch instantly between **Arabic (RTL)** and **English (LTR)**.
* **Interactive Charts:** 📊 Visual doughnut charts powered by **Chart.js** to track Paid vs. Remaining balances.

### 🔐 Security & Access
* **Multi-User System:** 👤 Complete isolation between users. Your data is private.
* **Secure Authentication:** Built-in Login & Signup system with hashed passwords.

---

## 🛠️ Tech Stack

* **Core:** Python, Flask, Jinja2.
* **Frontend:** HTML5, Tailwind CSS (v3.4), Chart.js.
* **PWA:** Service Workers, Web Manifest.
* **Database:** SQLAlchemy (ORM), SQLite / PostgreSQL.
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
    Open your browser at: `http://127.0.0.1:5000`

---

## 📂 Project Structure

```text
Raseed/
│
├── app.py                 # Main Application Controller
├── database.py            # Database Models & Logic
├── translations.py        # 🌍 Localization Dictionary
├── static/
│   ├── manifest.json      # PWA Configuration
│   ├── sw.js              # Service Worker
│   ├── favicon.png        # Site Icon
│   └── icons/             # Mobile App Icons
│
├── templates/             # Frontend Views
│   ├── base.html          # Layout, Theme & PWA Logic
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

- [x] 📱 PWA Support: Install the app on mobile devices.

- [ ] 📧 Email Notifications: Send PDF receipts to tenants automatically.

- [ ] 🤖 AI Insights: Predict rental income trends.

---

*Developed by **KhalidExe** © 2026*


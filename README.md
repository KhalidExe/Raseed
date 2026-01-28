# 💳 Raseed | رصيد

![Project Status](https://img.shields.io/badge/Status-Beta_V1.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Tailwind](https://img.shields.io/badge/Frontend-Tailwind_CSS-38bdf8?style=for-the-badge&logo=tailwindcss)

> **A Smart Rental Management System for Modern Investors.**
> Raseed helps landlords track installments, manage tenant ledgers, and monitor cash flow through a bilingual, high-performance dashboard.

---

## 📸 Screenshots
*(Add your screenshots here later)*
---

## ⚡ Key Features

### 🏢 Property Management
- **Tenant Profiles:** Create and manage profiles with unit details.
- **Excel Integration:** 📂 Upload bulk installment schedules via `.xlsx` files (Date & Amount columns).
- **Smart Archives:** Automatically stores and organizes data for each tenant separately.

### 💰 Financial Engine
- **Digital Ledger:** A detailed view of every installment (Paid, Remaining, Overdue).
- **Partial Payments:** Flexibility to record full or partial payments for any specific month.
- **Contract Adjustment:** Ability to modify contract values dynamically if discounts are applied.

### 🌐 User Experience
- **Bilingual UI:** 🌍 Full support for **Arabic (RTL)** and **English (LTR)** with one-click toggle.
- **Smart Alerts:** ⚠️ Automatic dashboard warnings for payments due within **15 days**.
- **Clean Design:** Built with **Tailwind CSS** for a responsive and professional look.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, SQLite.
* **Frontend:** HTML5, Tailwind CSS (CDN), Jinja2.
* **Data Processing:** Pandas, OpenPyXL.

---

## 🚀 How to Run

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

4.  **Access the Dashboard:**
    Open your browser and go to: `http://127.0.0.1:5000`

---

## 📂 Project Structure

```text
Raseed/
│
├── app.py                 # The Flask Server & Logic
├── database.py            # Database Controller (SQLite)
├── requirements.txt       # Dependencies
│
├── templates/             # HTML Templates
│   ├── base.html          # Layout & Navbar
│   ├── index.html         # Dashboard & Alerts
│   └── tenant.html        # Ledger & Excel Upload
│
└── real_estate.db         # Auto-generated Database
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
- [ ] 🔐 Authentication System: Multi-user support for different landlords.

- [ ] 📄 PDF Export: Generate official payment receipts.

- [ ] 📊 Analytics: Charts for monthly income vs. expected income.

---

*Developed by **KhalidExe** © 2026*


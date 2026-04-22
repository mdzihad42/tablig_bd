# Tablig Management System (Tablig BD)

A comprehensive Django-based management system designed to track and organize Tablig activities. This system helps in managing members, areas, religious activities (Gasht, Talim), financial records, and Jamat schedules.
notun item jog hobe 
## 🚀 Features

- **Member Management**: Track active and inactive members with detailed profiles.
- **Area Tracking**: Organize activities by specific geographic areas or mosques.
- **Gasht Activities**: Record both Umumi (Public) and Khususi (Personal) Gasht with designated roles (Amir, Rahbar, Mutakallim).
- **Talim Records**: Log daily or periodic religious teachings and book readings.
- **Finance Management**: Manage mosque or group funds with detailed income and expense tracking.
- **Jamat Scheduling**: Keep track of members going out in Jamat (3 days, 10 days, 40 days, 4 months).
- **Dashboard & Reporting**: (Future/Current) Visual representation of activities and growth.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (Default, can be migrated to PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript (Django Templates)

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mdzihad42/tablig_bd.git
   cd tablig_bd
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## 📂 Project Structure

- `tablig/`: Core application containing models for Area, Member, Gasht, Talim, Finance, and Jamat.
- `tablig_project/`: Project configuration and settings.
- `media/`: User-uploaded files (if any).
- `static/`: CSS, JS, and image files.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---
Developed for managing Tablig activities efficiently.

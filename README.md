# SUN_Maintenance

**Desktop application for structured maintenance management of PV service operations.**

Built with Python and PyQt5, SUN_Maintenance is a multi-user desktop tool for managing articles, projects, manufacturers, and addresses in a PV service environment. It includes a full login and user role system, database-backed data management, and a modular PyQt5 GUI.

> ⚠️ This project is currently under active development. Structure and functionality may change at any time.

---

## What it does

SUN_Maintenance provides a structured interface for managing service-related master data across multiple entity types:

- **Articles** – manage and attribute component data
- **Projects** – track and manage service projects
- **Manufacturers** – maintain manufacturer reference data
- **Addresses** – manage address records linked to entities
- **Users** – user accounts with role-based access control

The application starts with a **login screen** and supports **user registration**, ensuring data access is controlled per user role.

---

## Tech Stack

| Layer | Technology |
|---|---|
| GUI | PyQt5 5.15 + Qt Designer (`.ui` files) |
| ORM / Database | SQLAlchemy 2.0 (local SQLite) |
| Data processing | Pandas 2.0, NumPy 1.24 |
| File handling | openpyxl (Excel .xlsx), odfpy (ODS / LibreOffice) |
| Password handling | Hashed credentials via `u_pwd.py` |
| Data import | Custom import logic (`data/import_data.py`) |
| XML handling | defusedxml (secure XML parsing) |
| Styling | Custom QSS stylesheet |
| Packaging | PyInstaller-ready (`build.py`) |

---

## Project Structure

```
SUN_Maintenance/
│
├── src/
│   ├── main.py                        # Entry point – initialises DB, starts login form
│   ├── build.py                       # PyInstaller build script
│   │
│   ├── data/
│   │   └── import_data.py             # Data import logic
│   │
│   ├── database/
│   │   ├── classes/
│   │   │   ├── _initializer.py        # DB initialisation
│   │   │   ├── cls_article_data.py    # Article ORM model
│   │   │   ├── cls_project_data.py    # Project ORM model
│   │   │   ├── cls_user_role_system.py# User & role ORM models
│   │   │   └── cls_enums.py           # Shared enumerations
│   │   ├── constants/
│   │   │   ├── c_db_classes.py        # DB class constants
│   │   │   └── c_role_system.py       # Role system constants
│   │   ├── queries/
│   │   │   ├── q_ref_data.py          # Reference data queries
│   │   │   ├── q_role_system.py       # Role system queries
│   │   │   └── q_users.py             # User queries
│   │   └── utils/
│   │       ├── u_db_sess.py           # Session management
│   │       ├── u_pwd.py               # Password hashing & verification
│   │       └── u_queries.py           # Query utilities
│   │
│   ├── directories/
│   │   ├── constants/
│   │   │   └── c_directories.py       # Path constants
│   │   ├── decorators/
│   │   │   └── d_directories.py       # Path-related decorators
│   │   └── directories_handler.py     # Static directory setup
│   │
│   ├── styles/
│   │   ├── constants.py               # Style constants
│   │   ├── styles_Handler.py          # Style initialisation
│   │   └── stylesheet.qss             # Custom QSS stylesheet
│   │
│   └── ui/
│       ├── buttons/                   # Button creation & customisation
│       ├── classes/
│       │   ├── app_context.py         # Application context
│       │   ├── login_form.py          # Login window logic
│       │   ├── register_form.py       # Registration window logic
│       │   ├── main_window.py         # Main window logic
│       │   ├── dlg_article.py         # Article dialog
│       │   ├── dlg_project.py         # Project dialog
│       │   ├── dlg_manufacturer.py    # Manufacturer dialog
│       │   ├── dlg_address.py         # Address dialog
│       │   └── dlg_user.py            # User dialog
│       ├── constants/                 # UI constants (buttons, tables)
│       ├── forms/                     # Qt Designer .ui files + generated Python
│       ├── icons/                     # PNG icon assets
│       ├── main_body/
│       │   └── usr_overview.py        # User overview panel
│       ├── tables/                    # Table population & utilities
│       └── utils/                     # UI helper functions
│
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

---

## Background

SUN_Maintenance is a follow-up project to [SUN_DOC](https://github.com/creativeSloth/SUN_DOC), developed to address more complex data management needs in PV service operations. Compared to SUN_DOC, this project introduces a proper multi-user architecture with login, registration, and role-based access — all implemented independently without formal software engineering guidance.

---

## Requirements

```
Python 3.10+
PyQt5==5.15.11
SQLAlchemy==2.0.32
pandas==2.0.3
numpy==1.24.4
openpyxl==3.1.5
odfpy==1.4.1
defusedxml==0.7.1
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
cd src
python main.py
```

---

## Status

Active development — not yet intended for production use. Core UI and database structure are functional; further features are still being added.

---

## Author

GitHub: [creativeSloth](https://github.com/creativeSloth)

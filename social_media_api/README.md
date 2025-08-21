# Django REST Framework Authentication (Custom User Model)

This project demonstrates a Django REST Framework (DRF) setup with a **Custom User model** (`CustomUser`) that extends Django’s `AbstractUser`.  
Authentication is handled via **DRF Token Authentication**.

---

## 🚀 Features
- Custom user model with:
  - `bio`
  - `profile_picture`
  - `followers` (self-referential ManyToMany, asymmetrical)
- Token-based authentication
- Endpoints for:
  - User registration (`/accounts/register/`)
  - Login (`/accounts/login/`)
  - Profile management (`/accounts/profile/`)

---

## 📦 Installation

### 1. Clone repository & create virtual environment
```bash
git clone <your-repo-url>
cd myproject
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

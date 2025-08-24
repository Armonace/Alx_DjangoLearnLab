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

Endpoints
Endpoint	Method	Description	Auth Required
/accounts/follow/<id>/	POST	Follow a user	✅ Yes
/accounts/unfollow/<id>/	POST	Unfollow a user	✅ Yes
/api/feed/	GET	Get posts from followed users	✅ Yes

✅ Deliverables included:

Like a Post
POST /posts/{post_id}/like/
→ { "detail": "Post liked!" }

Unlike a Post
POST /posts/{post_id}/unlike/
→ { "detail": "Post unliked." }

Get Notifications
GET /notifications/
→ returns list of notifications, with newest first
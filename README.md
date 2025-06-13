# 🏥 Django Healthcare Backend API

A full-featured backend system for a Healthcare Management Application built with **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT authentication**.

---

## 🚀 Features

- ✅ User Registration & JWT-based Authentication
- 👩‍⚕️ Doctor Management (CRUD)
- 🧑‍🦱 Patient Management (CRUD)
- 🔁 Patient–Doctor Mapping
- 🔒 Token Refresh Support
- 🌱 PostgreSQL Integration
- 📦 Clean & Modular Code

---

## 📂 Project Structure
```
healthcare_backend/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── healthcare_backend/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt
└── .env
```

---

## 🔧 Setup Instructions



### 2. Create Virtual Environment
```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` File
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=your_db
DATABASE_USER=your_user
DATABASE_PASSWORD=your_pass
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5. Migrate & Run Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🔐 API Authentication
We use `JWT` (JSON Web Token) for secure authentication using `djangorestframework-simplejwt`.

- **Register**: `POST /api/auth/register/`
- **Login**: `POST /api/auth/login/`
- **Refresh Token**: `POST /api/auth/token/refresh/`

Include this header for authenticated requests:
```http
Authorization: Bearer <access_token>
```

---

## 📬 API Endpoints Summary

### 🔑 Auth APIs
| Method | Endpoint                 | Description          |
|--------|--------------------------|----------------------|
| POST   | /api/auth/register/      | Register User        |
| POST   | /api/auth/login/         | Login & Get Token    |
| POST   | /api/auth/token/refresh/ | Refresh Access Token |

### 🧑 Patient APIs
| Method | Endpoint            | Description               |
|--------|---------------------|---------------------------|
| POST   | /api/patients/      | Create Patient            |
| GET    | /api/patients/      | List All Patients         |
| GET    | /api/patients/<id>/ | Get Patient Details       |
| PUT    | /api/patients/<id>/ | Update Patient Info       |
| DELETE | /api/patients/<id>/ | Delete Patient            |

### 👨‍⚕️ Doctor APIs
| Method | Endpoint           | Description               |
|--------|--------------------|---------------------------|
| POST   | /api/doctors/      | Create Doctor             |
| GET    | /api/doctors/      | List All Doctors          |
| GET    | /api/doctors/<id>/ | Get Doctor Details        |
| PUT    | /api/doctors/<id>/ | Update Doctor Info        |
| DELETE | /api/doctors/<id>/ | Delete Doctor             |

### 🔄 Patient-Doctor Mapping APIs
| Method | Endpoint                    | Description                      |
|--------|-----------------------------|----------------------------------|
| POST   | /api/mappings/              | Assign Doctor to Patient         |
| GET    | /api/mappings/              | List All Mappings                |
| GET    | /api/mappings/<patient_id>/ | Get Patient's Assigned Doctors   |
| DELETE | /api/mappings/<id>/delete/  | Remove Mapping                   |

---

## 🧪 Testing with `curl`
Example for creating a patient:
```bash
curl -X POST http://localhost:8000/api/patients/ \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{"name": "Alice", "age": 30, "gender": "Female"}'
```

---

## 📮 Postman Collection
> 🔗 [Available on Request] — Exported Postman collection to test all endpoints

---

## 💡 Future Improvements
- Pagination, Filtering, Search
- Admin dashboard UI
- Role-based access control (Doctor/Staff/Admin)
- API rate-limiting

---

## 🧑‍💻 Author
Made with ❤️ by Mayur Sonar

---


# 📌 Church API

REST API built with **Django** + **Django REST Framework** for managing churches, members, and related activities.

---

## 🚀 Features

* **👥 Member management** - Complete CRUD for church members.
* **⛪ Church management** - Manage different church branches.
* **💰 Financial control** - Track tithes, offerings, and expenses.
* **📅 Events (Occasions)** - Schedule and manage church events.
* **🙏 Prayer requests** - System for managing prayer petitions.
* **📚 Studies** - Repository for biblical studies and materials.
* **🔗 Relationship** - One church has many members.
* **🔍 Filtering and pagination** - Built-in search and optimized results.
* **📡 Fully functional REST API** - Easy integration with any frontend or mobile app.

---

## 🛠️ Technologies

* **Python**
* **Django**
* **Django REST Framework**
* **PostgreSQL**
* **Django-filter**

---

## 📂 API Structure

### Main endpoints:
* `/members/`
* `/churches/`
* `/financial/`
* `/occasions/`
* `/prayers/`
* `/studies/`

### 🔥 Special endpoint:
`GET /churches/{id}/members/`
> Returns all members of a specific church.

---

## ⚙️ How to run the project

### 🔹 1. Clone the repository
```bash
git clone [https://github.com/your-username/church-api.git](https://github.com/your-username/church-api.git)
cd church-api
```
### 🔹 2. Create virtual environment
```Bash
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Windows:
# venv\Scripts\activate
```
### 🔹 3. Install dependencies
```Bash
pip install -r requirements.txt
```
If you don’t have the file:
```Bash
pip install django djangorestframework psycopg2-binary django-filter
```
### 🔹 4. Configure database
Edit settings.py:
```
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'church_api',
       'USER': 'postgres',
       'PASSWORD': '12345',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}
```
### 🔹 5. Run migrations

```Bash
python manage.py makemigrations
python manage.py migrate
```

###🔹 6. Create superuser
```Bash
python manage.py createsuperuser
```

### 🔹 7. Run the server
```Bash
python manage.py runserver
```
### 🌐 Access
Admin panel: http://127.0.0.1:8000/admin/

API Root: http://127.0.0.1:8000/

### 📦 Example (Postman/JSON)
POST /members/
```
{
  "church": 1,
  "status": "active",
  "role": "member",
  "baptismdate": "2020-05-10",
  "addmission": "transfer",
  "name": "John Silva",
  "gender": "male",
  "birthdate": "1995-08-15",
  "address": "Street A",
  "state": "PB",
  "occupation": "Teacher"
}
```

Instalación backend


1. pip install virtualenv
2. python -m venv venv
3. venv\Scripts\activate.bat
   pip install django
   pip install --upgrade pip
4. django-admin startproject myproject .
5. python manage.py startapp myapp
   pip install django djangorestframework

6. 'app'
   'rest_framework'
   pip install django-cors-headers
   'corsheaders',
   'corsheaders.middleware.CorsMiddleware',
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

7. python manage.py makemigrations
8. python manage.py migrate
9. python manage.py createsuperuser

   python manage.py runserver

Instalación frontend


1. npm install -g @vue/cli
2. npm i bootstrap@5.3.3
3. npm install axios



Link API: 'http://localhost:8000/api/chessproblems/'




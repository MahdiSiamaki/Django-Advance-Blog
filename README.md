# Django Blog App

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Code Quality](https://img.shields.io/badge/code%20quality-A-brightgreen)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Django](https://img.shields.io/badge/django-5.1.5-blue)
![Docker](https://img.shields.io/badge/docker-available-blue)

Django-Blog-App is a comprehensive blogging platform built with Django. It includes features such as user authentication, blog post creation, commenting, and more. The project is designed to be easily extendable and customizable.

## Project Structure
The project structure is as follows:
```
Django-Blog-App/
├── core/
│   ├── accounts/
│   ├── blog/
│   ├── comment/
│   ├── core/
│   ├── static/
│   ├── templates/
│   ├── manage.py
│   └── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## API Endpoints
The available API endpoints are as follows:

### Accounts
- `POST /accounts/api/v1/register/` - Register a new user
- `POST /accounts/api/v1/token/login/` - Login with email and password
- `POST /accounts/api/v1/token/logout/` - Logout
- `POST /accounts/api/v1/jwt/create/` - Create JWT token
- `POST /accounts/api/v1/jwt/refresh/` - Refresh JWT token
- `POST /accounts/api/v1/jwt/verify/` - Verify JWT token
- `POST /accounts/api/v1/change-password/` - Change password
- `POST /accounts/api/v1/test-email/` - Send test email
- `GET /accounts/api/v1/verify-email/<str:token>/` - Verify email
- `POST /accounts/api/v1/resend-verification-email/` - Resend verification email

### Blog
- `GET /blog/api/v1/posts/` - List all posts
- `POST /blog/api/v1/posts/` - Create a new post
- `GET /blog/api/v1/posts/<int:pk>/` - Retrieve a post
- `PUT /blog/api/v1/posts/<int:pk>/` - Update a post
- `DELETE /blog/api/v1/posts/<int:pk>/` - Delete a post
- `GET /blog/api/v1/categories/` - List all categories
- `POST /blog/api/v1/categories/` - Create a new category
- `GET /blog/api/v1/categories/<int:pk>/` - Retrieve a category
- `PUT /blog/api/v1/categories/<int:pk>/` - Update a category
- `DELETE /blog/api/v1/categories/<int:pk>/` - Delete a category

### Comments
- `GET /comments/api/v1/comments/` - List all comments
- `POST /comments/api/v1/comments/` - Create a new comment
- `GET /comments/api/v1/comments/<int:pk>/` - Retrieve a comment
- `PUT /comments/api/v1/comments/<int:pk>/` - Update a comment
- `DELETE /comments/api/v1/comments/<int:pk>/` - Delete a comment

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/MahdiSiamaki/Django-Advance-Blog.git
   cd Django-Advance-Blog
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Running the Project using Docker
To run the project using Docker, follow these steps:

1. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://127.0.0.1:8000/`.

3. Access the admin panel at `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

## Celery Background Processing
The project uses Celery for background processing. To start the Celery worker, follow these steps:

1. Start the Celery worker:
   ```bash
   docker-compose run worker
   ```

2. The Celery worker will now process background tasks.

## Email Settings
The project is configured to use SMTP for sending emails. The email settings are defined in `core/core/settings.py` and `docker-compose.yml`. By default, the project uses `smtp4dev` for local email testing.

## Running Tests using Pytest
To run tests using pytest, follow these steps:

1. Run the tests:
   ```bash
   pytest
   ```

## Usage
To use the project, follow these guidelines:

1. Access the admin panel at `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.
2. Create blog posts, categories, and tags from the admin panel.
3. Visit the homepage at `http://127.0.0.1:8000/` to see the blog posts.
4. Users can register, log in, and comment on blog posts.

## Contribution
To contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of the feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

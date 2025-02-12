# Django-Advance-Blog

## Project Description
Django-Advance-Blog is a comprehensive blogging platform built with Django. It includes features such as user authentication, blog post creation, commenting, and more. The project is designed to be easily extendable and customizable.

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

   [![Set Up Database](https://img.shields.io/badge/Set%20Up%20Database-blue)](python manage.py migrate)

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

   [![Create Superuser](https://img.shields.io/badge/Create%20Superuser-blue)](python manage.py createsuperuser)

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

   [![Run Development Server](https://img.shields.io/badge/Run%20Development%20Server-blue)](python manage.py runserver)

## Running the Project using Docker
To run the project using Docker, follow these steps:

1. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

   [![Run Docker Containers](https://img.shields.io/badge/Run%20Docker%20Containers-blue)](docker-compose up --build)

2. Access the application at `http://127.0.0.1:8000/`.

3. Access the admin panel at `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

## Celery Background Processing
The project uses Celery for background processing. To start the Celery worker, follow these steps:

1. Start the Celery worker:
   ```bash
   docker-compose run worker
   ```

   [![Run Celery Worker](https://img.shields.io/badge/Run%20Celery%20Worker-blue)](docker-compose run worker)

2. The Celery worker will now process background tasks.

## Email Settings
The project is configured to use SMTP for sending emails. The email settings are defined in `core/core/settings.py` and `docker-compose.yml`. By default, the project uses `smtp4dev` for local email testing.

## Running Tests using Pytest
To run tests using pytest, follow these steps:

1. Run the tests:
   ```bash
   pytest
   ```

   [![Run Tests](https://img.shields.io/badge/Run%20Tests-blue)](pytest)

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

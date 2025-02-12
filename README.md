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

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
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

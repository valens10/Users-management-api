# User Management System

This is a user management application whic is built using the Django web framework that allows to create, read, update, and delete user information in a database. It provides API endpoints that enable to manage user accounts, including user authentication, registration, password reset, and profile editing. The system is designed to be scalable, secure, and customizable, making it ideal for applications that require user management functionality.


## Features

- User management(CRUD Operation)
- Notification
- User Verification

## Dependencies

- Python 3.8 or higher
- Django 3.2 or higher
- Django Rest Framework 3.12 or higher
- PostgreSQL 12 or higher

## Installation

1. Clone the repository:
`$ git clone https://github.com/valens10/Users-management-api.git`

2. Install the dependencies:
`$ pip install -r requirements.txt`

3. Set up the database:
`$ python manage.py migrate`

4. $ python manage.py createsuperuser
`$ python manage.py createsuperuser`

5. Run the development server:
`$ python manage.py runserver`


## Usage

- You can access the API endpoints using the following base URL:
`http://localhost:8000/api/v1/`


- To authenticate and access protected endpoints, you need to obtain a JWT token by sending a POST request to the auth/token/ endpoint with your username and password:

```
POST http://localhost:8000/api/v1/auth/token/

{
    "username": "your-username",
    "password": "your-password"
}

```
- The API documentation is available at [http://localhost:8000/api/v1/docs/](here).


## License

This project is licensed under the MIT License - see the [http://localhost:8000/api/v1/licence/](LICENSE file for details).

## Contact

For any questions or suggestions, feel free to contact us at `nsengvalens10@gmail.com`.
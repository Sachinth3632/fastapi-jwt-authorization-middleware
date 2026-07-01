# JWT Authentication Middleware

A FastAPI-based authentication service that supports both Local and Cloud authentication using JWT (JSON Web Tokens). The project demonstrates secure authentication, authorization, middleware-based token validation, and role-based user provisioning.

## Features

- JWT-based authentication
- Local user authentication
- Cloud authentication integration
- Authentication middleware
- Protected APIs
- User provisioning
- Password hashing using bcrypt
- Role-based authorization
- Unit tests using pytest

## Tech Stack

- Python 3
- FastAPI
- Pydantic
- python-jose (JWT)
- Passlib (bcrypt)
- Pytest
- Uvicorn

## Project Structure

```
auth_middleware/
│
├── auth/
│   ├── strategies/
│   │   ├── base.py
│   │   ├── local_strategy.py
│   │   ├── cloud_strategy.py
│   │   └── token_service.py
│
├── middleware/
│   └── auth_middleware.py
│
├── models/
│   └── user.py
│
├── scripts/
│   └── hash_password.py
│
├── tests/
│
├── data/
│   └── users.json
│
├── main.py
├── .env
└── requirements.txt
```

## Installation

Clone the repository

```bash
git clone <repository-url>
cd auth_middleware
```

Create virtual environment

```bash
python -m venv auth_venv
```

Activate environment

Linux/macOS

```bash
source auth_venv/bin/activate
```

Windows

```bash
auth_venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file.

```env
JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRY_MINUTES=30

CLOUD_LOGIN_URL=<cloud_login_url>
```

## Run Server

```bash
uvicorn main:app --reload
```

Server runs at

```
http://127.0.0.1:8000
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /auth/login | Login using Local or Cloud authentication |
| GET | /me | Returns authenticated user details |
| POST | /users/local | Create local user (Cloud Superuser only) |
| GET | /health | Health Check |

## Authentication Flow

1. User submits credentials.
2. Authentication strategy is selected (Local or Cloud).
3. Credentials are validated.
4. JWT Access Token is generated.
5. Client includes token in Authorization header.
6. Middleware validates the token.
7. Protected endpoints receive authenticated user information.

## Testing

Run all tests

```bash
pytest tests/ -v
```

## Security

- Passwords are hashed using bcrypt.
- JWT tokens contain expiration time.
- Middleware validates every protected request.
- Unauthorized requests return appropriate HTTP status codes.

## Future Improvements

- Refresh Token support
- Database integration (MongoDB/PostgreSQL)
- Role-based access control (RBAC)
- Token blacklisting
- Docker support
- CI/CD integration

## Author

Sachin T H

# Fitnessify User Registration API

This is a backend API for user registration developed for the Fitnessify mobile fitness app. The API allows users to register securely and stores their information in a database. The API is built using [insert chosen backend technology] and integrates with [insert chosen database].

## Requirements

To use the Fitnessify User Registration API, you need to meet the following requirements:

- [insert backend technology] installed
- [insert database] installed and configured
- [insert any other requirements]

## User Registration

To register a new user, send a secure POST request to the following endpoint:

## POST /api/user/register

### Request Body

The request body should be in JSON format and include the following fields:

- `username` (string): The desired username for the new user.
- `email` (string): The email address of the new user.
- `password` (string): The password for the new user.

Example:

```json
{
    "username": "john_doe",
    "email": "johndoe@example.com",
    "password": "P@ssw0rd"
}
```


### Response

Upon successful registration, the API will respond with a status code of 201 (Created) and a JSON object containing the user's information.

Example response:

```json
{
    "id": 123,
    "username": "john_doe",
    "email": "johndoe@example.com"
}
```


If there is an error during the registration process (e.g., invalid input, username/email already taken), the API will respond with an appropriate error message and a status code of 400 (Bad Request).

### User Login
To authenticate a user and obtain an access token, send a POST request to the following endpoint:


## POST /api/user/login
Request Body
The request body should be in JSON format and include the following fields:

username (string): The username of the user.
password (string): The password of the user.
Example:

```json
{
    "username": "john_doe",
    "password": "P@ssw0rd"
}
```

### Response
Upon successful login, the API will respond with a status code of 200 (OK) and a JSON object containing the access token and refresh token.

Example response:

```json
{
    "access_token": "eyJhbGciOi...",
    "refresh_token": "eyJhbGciOi..."
}
```


If the login fails (e.g., invalid credentials), the API will respond with an appropriate error message and a status code of 401 (Unauthorized).

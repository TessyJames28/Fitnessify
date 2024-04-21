# Fitnessify

Fitnessify is a fitness tracking application that helps users monitor their workouts, set goals, and stay motivated on their fitness journey.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## About

This is a backend API for user registration developed for the Fitnessify mobile fitness app. The API allows users to register securely and stores their information in a database. The API is built using [Django] and integrates with [SQLite].

## Features

- User registration and login
- Access and refresh token generation with jwt


## Installation

To install and run Fitnessify locally, follow these steps:

1. Clone the repository from [GitHub](https://github.com/TessyJames28/Fitnessify).

2. Navigate to the project directory.

3. Install the necessary dependencies by running the following command:

```pip install```


4. Make mnigration and migrate the database by using the following command:

```python manage.py makemigrations```
```python manage.py migrate```

5. Start the application using the following command:

```python manage.py runserver```

6. Access the application by visiting `http://localhost:8000` in your web browser.
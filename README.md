# onTrack
onTrack was created to provide a way for developers to track issues for their projects.

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/isaacwoodruff/ontrack/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/isaacwoodruff/ontrack/tree/main)

## Table of Contents

1. [UX](#ux)
    - [Goals](#goals)
        - [Business Goals](#simply-sport-science-goals)
        - [Employer Goals](#employer-goals)
        - [Candidate Goals](#candidate-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)
    - [Information Architecture](#information-architecture)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)

# UX
## Goals
### onTrack Goals
The goals of onTrack are to:
- Provide a way for developers to track bugs/issues for their projects
- Monetize the platform by offering extra features to paying customers

The target audiences for this website are:
- Developers who want to manage their projects better

### Developer Goals
- To track issues/bugs in their project
- To stay on track with project goals

## User Stories
### Developer User Stories
A developer using onTrack expects to:
- Be able to register, login, and logout
- Create, read, update or delete their user profile
- Create, read, update or delete an issue
- Easily and securely pay for the extra features

## Design Choices

## Wireframes
The following wireframes were designed with Balsamiq.

[Desktop wireframes](https://github.com/isaacwoodruff/ontrack/blob/main/desktop-wireframes.png)

[Mobile wireframes](https://github.com/isaacwoodruff/ontrack/blob/main/mobile-wireframes.png)

# Information Architecture

## Database Models
#### User Model
The User model for this project is the standard User model provided by Django.

#### Profile Model
Key | Validation | Field Type |
--- | --- | ---
user | User, on_delete=models.CASCADE | OneToOneField
avatar | null=False | ImageField
job_title | max_length=50, null=False | CharField
github | max_length=50, null=False | CharField

#### Issue Model
Key | Validation | Field Type |
--- | --- | ---
id | null=False, unique=True | PrimaryKey
issue | null=False | TextField
issue_type | max_length=50, choices=ISSUE_TYPE_CHOICES | CharField
kanban_type | max_length=50, choices=KANBAN_TYPE_CHOICES | CharField
project | max_length=50, null=False | ForeignKey
user | max_length=50, null=False | ForeignKey
created_date | auto_now_add=True | DateTimeField

#### Project Model
Key | Validation | Field Type |
--- | --- | ---
id | null=False, unique=True | PrimaryKey
project_name | max_length=50, null=False | CharField
created_date | auto_now_add=True | DateTimeField
slug | null=False, unique=True | SlugField

# Features
## Existing Features

##### Sign Up Page
- Shows a registration form
- Has a link at the bottom that redirects to the sign in page if the user already has an account

##### Sign In Page
- Shows a sign in form
- Has a link at the bottom to sign up if the user doesn't have an account
- Has a 'Forgot Password' option

##### User Profile Page
- Displays a form with user profile details. The form is autopopulated from their account in the database
- The user has two options on the page, update their profile or delete their account

##### Delete Account Page
- Asks the user if they are sure they want to delete their profile
- Requires the user to confirm with their email and password

## Features Left To Implement

##### Dashboard
- Shows current issues
- Option to create, read, update, or delete an issue
- Two different views available, Kanban or Scrum

##### Checkout
- A page to upgrade the user account for access to more features
- The checkout uses webhooks to confirm with Stripe API whether the payment is complete or not

# Technologies Used

### Programming Languages
- This project uses **HTML**, **CSS**, **JavaScript** and **Python**.

### Tools
- [Django](https://www.djangoproject.com/) as a python web application framework for faster development.
- [Visual Studio Code](https://code.visualstudio.com/) as the Integrated Development Environment while developing this project.
- [PIP](https://pip.pypa.io/en/stable/installing/) to install the tools needed in this project.
- [Git](https://git-scm.com) for version control during the development process. 
- [GitHub](https://github.com/) for a remote repository.
- [CircleCI](https://circleci.com/) for Continuous Integration.
- [Balsamiq](https://balsamiq.com/) to build wireframes in the planning stage of development.
- [python-dotenv](https://pypi.org/project/python-dotenv/) to make use of environment variables.
- [Pylint-django](https://pypi.org/project/pylint-django/) for improving code analysis when analysing code using Django.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms on the backend.
- [Heroku](https://www.heroku.com/) for hosting and deployment.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) to allow the web app to serve its own static files.
- [Gunicorn](https://pypi.org/project/gunicorn/) a Python Web Server Gateway Interface HTTP server to aid in deployment of the Django project for heroku deployment.

### Databases
- [SQlite3](https://www.sqlite.org/index.html) as the database for the development environment, provided by django.
- [PostgreSQL](https://www.postgresql.org/) as the database for the deployed site, hosted on Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) as a DB API 2.0 compliant PostgreSQL driver for Python.

### Libraries
- [Pillow](https://pypi.org/project/Pillow/) adds image processing capabilities to Python.
- [Bootstrap](https://getbootstrap.com/) to develop responsive and mobile-first pages more easily.

# Testing
### Continuous Integration
CircleCI was used to test integration of the project. Pylint is run during these test to check for errors and enforces a coding standard in the Python language. All unit tests are run during the CircleCI build.

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/isaacwoodruff/ontrack/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/isaacwoodruff/ontrack/tree/main)

### Validation Tools
These tools were used to test the validity of the code for this project:
- [Pylint-django](https://pypi.org/project/pylint-django/) and [Microsofts Python Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python) was used to validate Python.

### Testing Matrix

# Deployment
## Local Deployment

## Heroku Deployment

# Credits
### Content

### Media
- The default user image is from [flaticon](
https://www.flaticon.com/free-icon/user_848043?term=user&page=1&position=33&page=1&position=33&related_id=848043&origin=search)

### Code

### Acknowledgements

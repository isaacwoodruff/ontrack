# onTrack
onTrack was created to provide a way for developers to track bugs/issues for their projects.

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

# Information Architecture

## Database Models

# Features
## Existing Features

## Features Left To Implement
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

##### Dashboard
- Shows current issues
- Option to create, read, update, or delete an issue
- Two different views available, Kanban or Scrum

##### Checkout
- A page to upgrade the user account for access to more features
- The checkout uses webhooks to confirm with Stripe API whether the payment is complete or not

# Technologies Used

### Programming Languages

### Tools

### Databases

### Libraries

# Testing
### Validation Tools

### Testing Matrix

# Deployment
## Local Deployment

## Heroku Deployment

# Credits
### Content

### Media

### Code

### Acknowledgements

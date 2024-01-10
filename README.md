# realestateapplication


# RealEstatePro - Real Estate Management System

RealEstatePro is a web application developed for managing real estate properties and tenants. It provides features for property listing, tenant management, and property details.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/RealEstatePro.git


cd RealEstatePro
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Usage
Create an admin user by navigating to /admin/ and logging in with your credentials.
Use the admin interface to add properties, units, and tenants.
Access the main features of the application through the provided URLs (e.g., /create_property_unit/, /create_tenant/).
Features
Admin User Authentication:

Log in using your email and password.
Property Listing Module:

Create property profiles with details like name, address, location, and features.
View property profiles with associated units and tenant information.
Tenant Management Module:

Create tenant profiles with personal information and document proofs.
Assign tenants to specific units under a property with details like agreement end date and monthly rent date.
Search for units and properties based on features.
Dependencies
Django 5.0
Other dependencies listed in requirements.txt


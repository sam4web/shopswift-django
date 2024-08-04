# SwiftShop: A Simple E-Commerce Website

## Overview

**SwiftShop** is a clean and functional e-commerce website built with Django. This project highlights essential web development techniques and provides a complete online store experience.

## Features

- **Product Listings:** Browse products with detailed descriptions.
- **User Authentication:** Register, log in, and manage profiles.
- **Shopping Cart:** Add items to your cart and checkout seamlessly.
- **Order Management:** View and track your orders.

## Technologies Used

- **[Django](https://www.djangoproject.com/):** High-level Python web framework for rapid development.
- **[TailwindCSS](https://tailwindcss.com/):** Utility-first CSS framework for custom designs.
- **[Alpine.js](https://alpinejs.dev/):** Minimal framework for adding JavaScript behavior to HTML.
- **[SQLite](https://www.sqlite.org/):** Lightweight, disk-based database for managing data.

## Screenshot

![screenshot](./screenshot.png)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:sam4web/shopswift-django.git
    cd shopswift-django
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up the database:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the development server at `http://127.0.0.1:8000/`
- Log in to the admin panel at `http://127.0.0.1:8000/admin/` with the superuser credentials

## Contributing

If you would like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch (`git checkout -b feature/your-feature`).
- Make your changes and commit them (`git commit -m 'Add some feature'`).
- Push to the branch (`git push origin feature/your-feature`).
- Create a new Pull Request.

## Contact

For any inquiries or questions, please contact [sijal.m06@gmail.com](mailto:sijal.m06@gmail.com).

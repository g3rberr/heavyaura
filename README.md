# Store Project 🛒

This is a Django-based e-commerce web application that includes user authentication, product management, order processing, and payment gateway integration. 

## Features 🚀

- User Authentication: Register, login, and manage profiles
- Product Management: Add, view, and manage products
- Shopping Cart: Add items to cart, view cart, and checkout
- Order Processing: Create and track orders
- Payment Integration: Process payments through a payment gateway (Stripe)
- Admin Panel: Manage users, products, and orders through Django's admin interface
- Responsive Design: Optimized for mobile and desktop users

---

## Installation ⚙️

To set up the project locally, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/g3rberr/heavyaura.git
cd store-project

2. Set up a virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

4. Set up the database

Apply migrations to create the database schema:

python manage.py migrate

5. Create a superuser

Create an admin account to access the Django admin panel:

python manage.py createsuperuser

6. Run the development server

python manage.py runserver

Access the application at http://127.0.0.1:8000.
Project Structure 📂

store-project/
│
├── cart/                   # Shopping cart functionality
│   ├── admin.py            # Admin interface for cart
│   ├── models.py           # Cart-related models
│   ├── views.py            # Views to handle cart logic
│   ├── urls.py             # Cart URLs
│   └── templates/cart/     # Templates for cart-related pages
│
├── main/                   # Main app (landing page, product listing)
│   ├── models.py           # Models for products, categories
│   ├── views.py            # Views for rendering products and home page
│   ├── templates/main/     # Templates for the main pages
│   └── static/             # Static files (CSS, JS, images)
│
├── orders/                 # Order-related functionality
│   ├── models.py           # Models for orders
│   ├── views.py            # Views to handle order creation
│   ├── urls.py             # Order URLs
│   └── templates/order/    # Templates for order pages
│
├── payment/                # Payment gateway integration (e.g., Stripe)
│   ├── models.py           # Models related to payment transactions
│   ├── views.py            # Views for payment processing
│   ├── urls.py             # Payment URLs
│   └── templates/payment/  # Templates for payment-related pages
│
├── users/                  # User authentication and profile management
│   ├── models.py           # User-related models (including profile)
│   ├── views.py            # Views for registration, login, and profile
│   ├── urls.py             # User URLs
│   └── templates/users/    # Templates for user pages (login, register)
│
├── store/                  # Core project settings
│   ├── settings.py         # Django settings for the project
│   ├── urls.py             # URL routing for the whole project
│   └── wsgi.py             # WSGI configuration
│
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── media/                  # Media files (product images, user images)
│   └── products/           # Folder for product images
├── static/                 # Static assets (CSS, JS, Bootstrap)
└── templates/              # Global templates (e.g., base layout)

Technologies Used 🛠

    Backend: Django 5.1.4
    Frontend: HTML, CSS, Bootstrap
    Database: SQLite (default, can be switched to PostgreSQL)
    Payment Integration: Stripe (for payment gateway)
    Admin Interface: Django Admin

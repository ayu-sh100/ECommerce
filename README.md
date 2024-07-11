# E-commerce Platform Backend

## Introduction
This project is a backend system for an e-commerce platform, built using Django and Django Rest Framework (DRF). It includes functionalities for user and admin authentication, product management, shopping cart operations, and order processing. Additional features include Google OAuth integration, OTP-based login, Celery for asynchronous tasks, and WebSockets for live updates.

## Project Setup Instructions

### Prerequisites
- Python 3.x
- Redis
- MySQL

### Setup Instructions
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/ecommerce-backend.git
    cd ecommerce-backend
    ```

2. **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Set Up Environment Variables:**
    Create a `.env` file in the project root and add the necessary environment variables:
    ```env
    SECRET_KEY='your_secret_key'
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=mysql://user:password@localhost:3306/ecommerce
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_password
    DEFAULT_FROM_EMAIL=webmaster@example.com
    ```

4. **Set Up Database:**
    Ensure MySQL is running and create the necessary database:
    ```sql
    CREATE DATABASE ecommerce;
    ```

5. **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

8. **Start Celery Workers:**
    ```bash
    celery -A myproject worker -l info
    celery -A myproject beat -l info
    ```
    
## API Documentation

### Authentication Module
- **Login/Signup:**
  - `POST /api/auth/login/` - Login endpoint
  - `POST /api/auth/signup/` - Signup endpoint
- **Google OAuth Integration:**
  - `GET /api/auth/google/` - Google OAuth login
- **OTP-Based Login:**
  - `POST /api/auth/otp-login/` - OTP login endpoint

### Products Module
- **CRUD Operations:**
  - `GET /api/products/` - List all products
  - `POST /api/products/` - Create a new product
  - `GET /api/products/:id/` - Retrieve a product by ID
  - `PUT /api/products/:id/` - Update a product by ID
  - `DELETE /api/products/:id/` - Delete a product by ID
- **Bulk Product Upload:**
  - `POST /api/products/bulk_upload/` - Bulk upload products using Celery
- **Search and Sorting:**
  - `GET /api/products/?search=<query>&ordering=<field>` - Search and sort products

### Shopping Cart Module
- **Cart Operations:**
  - `POST /api/cart/` - Add item to cart
  - `PATCH /api/cart/:id/` - Update cart item
  - `DELETE /api/cart/:id/` - Remove item from cart
  - `GET /api/cart/total/` - Get cart total calculation

### Orders Module
- **Order Operations:**
  - `POST /api/orders/` - Create a new order
  - `GET /api/orders/:id/` - Retrieve an order by ID
  - `DELETE /api/orders/:id/` - Delete an order by ID
  - `PATCH /api/orders/:id/` - Admin: Update order status
- **Email Notifications:**
  - Email notifications are sent on successful order placement

## Additional Information
- **Celery Integration:**
  Celery is used for asynchronous tasks such as bulk product uploads and sending email notifications.
- **WebSockets:**
  WebSockets are used to display live count of sold SKUs for each product.
- **Logging:**
  Proper logging for API responses and errors is implemented.

## Assumptions
- Users and admins have separate login and authentication processes.
- Email service is properly configured to send notifications.
- Redis is used as the message broker for Celery tasks.
- The frontend is responsible for handling the OAuth flow and passing the tokens to the backend.

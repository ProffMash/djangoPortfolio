# DjangoPortfolio

A professional portfolio website built using Django ,CSS3 AND HTML5.

## Features

- **Responsive Design**: Fully responsive and optimized for all devices.
- **Home Page**: Includes a hero section, about section, and a professional footer.
- **Projects Page**: Showcases completed and ongoing projects (optional for this setup).
- **Contact Form**: Users can submit messages, which are saved in a database (optional for this setup).
- **CSS Styling**: Leveraged CSS for modern and clean UI design.

## Project Structure

```plaintext
djangoPortfolio/
├── djangoPortfolio/         # Main project folder
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project-level URLs
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
├── portfolio/               # Portfolio app folder
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   └── portfolio/
│   │       ├── home.html    # Home page template
│   │       └── base.html    # Base layout template
│   ├── static/              # Static files (CSS, JS, Images)
│   │   └── portfolio/
│   │       ├── css/
│   │       │   └── styles.css  # Custom styles
│   │       └── images/        # Images for the website
│   ├── models.py            # Django models
│   ├── views.py             # Django views
│   ├── urls.py              # App-level URLs
│   └── admin.py             # Django admin configuration
├── manage.py                # Django management script
└── db.sqlite3               # SQLite database

Running Migrations:
python manage.py makemigrations
python manage.py migrate

Running development Server:
python manage.py runserver


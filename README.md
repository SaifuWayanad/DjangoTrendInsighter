# TrendInsighter - Professional Django Dashboard

A modern, professional Django application featuring a well-designed sidebar navigation and comprehensive analytics dashboard with interactive charts and real-time data visualization.

![Dashboard Preview](https://img.shields.io/badge/Django-5.0.1-darkgreen)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

## 🌟 Features

- **Professional Sidebar Navigation** - Modern, responsive sidebar with collapsible menu items
- **Interactive Dashboard** - Real-time metrics and key performance indicators
- **Data Visualization** - Chart.js integration for beautiful, interactive charts
- **Sample Data Models** - Pre-built models for Orders, Metrics, and Analytics
- **Admin Panel** - Django admin interface for easy data management
- **Responsive Design** - Mobile-friendly, fully responsive layout
- **Professional UI** - Clean, modern design with smooth animations
- **Multiple Chart Types** - Bar charts, doughnut charts, and more

## 📋 Project Structure

```
TrendInsighter/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # Database (created on first run)
├── trendinsighter/          # Project configuration
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── dashboard/              # Main dashboard app
│   ├── models.py           # Database models (Dashboard, Card, Order, ChartData)
│   ├── views.py            # View logic
│   ├── admin.py            # Admin interface configuration
│   ├── urls.py             # App URL routing
│   ├── apps.py             # App configuration
│   └── management/
│       └── commands/
│           └── populate_data.py  # Command to create sample data
├── static/                 # Static files
│   ├── css/
│   │   └── style.css       # Professional styling and animations
│   └── js/
│       └── script.js       # JavaScript functionality
└── templates/              # HTML templates
    ├── base.html           # Base template with sidebar
    └── dashboard/
        ├── home.html       # Home page
        └── index.html      # Main dashboard
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd TrendInsighter
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

6. **Populate sample data:**
   ```bash
   python manage.py populate_data
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Dashboard: http://localhost:8000/dashboard/
   - Home: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/

## 📊 Database Models

### Dashboard
Main dashboard configuration model.
- `title`: Dashboard title
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Card
Metric cards displayed on the dashboard.
- `dashboard`: Foreign key to Dashboard
- `title`: Card title
- `value`: Display value
- `description`: Card description
- `card_type`: Type of card (metric, chart, list)
- `icon`: Font Awesome icon class
- `color`: Color theme (primary, success, warning, info)
- `position`: Display order

### Order
Sample order data.
- `dashboard`: Foreign key to Dashboard
- `order_id`: Unique order identifier
- `customer_name`: Customer name
- `amount`: Order amount
- `status`: Order status (Pending, Completed, etc.)
- `created_at`: Order creation timestamp

### ChartData
Chart data points for visualization.
- `dashboard`: Foreign key to Dashboard
- `month`: Month label
- `series_a`, `series_b`, `series_c`: Data values
- `position`: Display order

## 🎨 Customization

### Changing Colors
Edit the CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #4C63FF;
    --secondary-color: #6C757D;
    --success-color: #66BB6A;
    --danger-color: #EF5350;
    --warning-color: #FFA726;
    --info-color: #29B6F6;
}
```

### Adding Menu Items
Edit `templates/base.html` and add items to the sidebar navigation:
```html
<li class="nav-item">
    <a class="nav-link" href="{% url 'your-view-name' %}">
        <i class="fas fa-icon-name"></i>
        <span>Menu Item</span>
    </a>
</li>
```

### Adding Chart Data
Use the Django admin panel to create new ChartData entries, or add them programmatically in your management commands.

## 🛠️ Management Commands

### Populate Sample Data
```bash
python manage.py populate_data
```
Creates dashboard, metric cards, sample orders, and chart data.

### Create Superuser
```bash
python manage.py createsuperuser
```
Creates an admin account for accessing the admin panel.

### Make Migrations
```bash
python manage.py makemigrations
```
Create migration files for model changes.

### Run Migrations
```bash
python manage.py migrate
```
Apply database migrations.

## 🌐 URL Routes

| Route | Description |
|-------|-------------|
| `/` | Home page |
| `/dashboard/` | Main dashboard |
| `/admin/` | Django admin panel |

## 📦 Dependencies

- **Django 5.0.1** - Web framework
- **Bootstrap 5.3.0** - CSS framework (via CDN)
- **Chart.js 3.9.1** - Data visualization (via CDN)
- **Font Awesome 6.4.0** - Icons (via CDN)

## 🔐 Security Notes

- Change the `SECRET_KEY` in `settings.py` for production
- Set `DEBUG = False` for production deployment
- Use environment variables for sensitive data
- Configure `ALLOWED_HOSTS` for your domain
- Use a production database (PostgreSQL, MySQL) instead of SQLite

## 🚢 Deployment

For production deployment:

1. **Set environment variables:**
   ```bash
   export SECRET_KEY='your-secret-key'
   export DEBUG=False
   export ALLOWED_HOSTS='yourdomain.com'
   ```

2. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

3. **Use a production server:**
   ```bash
   pip install gunicorn
   gunicorn trendinsighter.wsgi:application
   ```

4. **Use a reverse proxy** (Nginx, Apache)

5. **Set up HTTPS** (Let's Encrypt, etc.)

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📞 Support

For issues and questions, please review the code documentation and comments throughout the project files.

## 🎯 Future Enhancements

- [ ] User authentication system
- [ ] Real-time data updates with WebSockets
- [ ] Email notifications
- [ ] Advanced analytics and reporting
- [ ] Data export (PDF, Excel)
- [ ] Multi-language support
- [ ] Dark mode theme
- [ ] API endpoints (Django REST Framework)

---

**Created with ❤️ using Django and Bootstrap**

*Last Updated: March 2026*

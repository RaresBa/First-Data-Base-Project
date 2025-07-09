# Entertainment Database Management System

## About This Project

This is my first database project for my Database & Web Services class - a web-based entertainment management system built with Flask and MySQL. As a beginner learning database development, I created this application to practice CRUD operations, database design, and web development fundamentals.

## What This Project Does

This is a comprehensive entertainment database system that manages:

- **Movies** - Store movie information (title, studio, release year, runtime, rating)
- **TV Shows** - Track TV series with seasons and end dates
- **Documentaries** - Manage documentary content with research information
- **People** - Database of directors, actors, and producers
- **Search Functionality** - Search across different entertainment types

## Features

### Data Management
- Add new movies, TV shows, documentaries
- Register directors, actors, and producers
- Input validation and error handling
- User feedback system

### Search Capabilities
- Search for specific movies (Inception)
- Search for TV shows (Community)
- Search for specific series (Arrested Development)
- Detailed result views with comprehensive information

### User Interface
- Clean, responsive web interface
- Maintenance login system
- Form-based data entry
- Results display with detailed views

## Technical Stack

- **Backend**: Python Flask
- **Database**: MySQL with SQLAlchemy ORM
- **Frontend**: HTML/CSS with Bootstrap styling
- **Database Driver**: PyMySQL

## Project Structure

```
DataBase Project/
├── app.py                 # Main Flask application
├── database.py           # Database configuration
├── models.py             # SQLAlchemy models
├── templates/            # HTML templates
│   ├── index.html       # Main page
│   ├── movieInput.html  # Movie entry form
│   ├── tvInput.html     # TV show entry form
│   └── ...              # Other templates
├── static/              # CSS and images
└── instance/           # Database files
```

## Database Schema

The system uses several interconnected tables:
- `VisualEntertainment` - Movies and TV shows
- `Director` - Director information
- `Actor` - Actor details
- `Producer` - Producer data
- `UserManagement` - User authentication

## Getting Started

### Prerequisites
- Python 3.x
- MySQL Server
- Required Python packages (see requirements.txt)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "DataBase Project"
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**
   - Install MySQL Server if not already installed
   - Create a new database named `brares_db`
   - Create a MySQL user or use existing credentials

5. **Configure database connection**
   - Open `app.py` and update the database connection string:
   ```python
   app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/brares_db?charset=utf8mb4"
   ```
   - Replace `username` and `password` with your MySQL credentials
   - Also update the connection in `get_db_connection()` function

6. **Initialize the database**
   - Run the application once to create tables:
   ```bash
   python app.py
   ```

### Running the Server

1. **Activate virtual environment** (if using one)
   ```bash
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Start the Flask application**
   ```bash
   python app.py
   ```

3. **Access the application**
   - Open your web browser
   - Navigate to: `http://localhost:5000` or `http://127.0.0.1:5000`
   - The application should now be running!

### Troubleshooting

- **Database connection errors**: Double-check your MySQL credentials and ensure the database exists
- **Missing dependencies**: Run `pip install -r requirements.txt` again
- **Port already in use**: Change the port in `app.py` or stop other services using port 5000
- **Virtual environment issues**: Make sure you're in the correct directory and virtual environment is activated

## Learning Outcomes

As a beginner project, this helped me learn:
- Database design and relationships
- Flask web framework basics
- SQLAlchemy ORM usage
- Form handling and validation
- Basic authentication systems
- Search functionality implementation
- Template rendering and routing

## Future Improvements

Some areas I'd like to enhance as I learn more:
- Better security practices
- API endpoints
- More advanced search features
- User roles and permissions
- Data visualization
- Mobile responsiveness

## Contributors

This project was developed as a collaborative effort by:

- **Baiasu Stefan Rares** (sbaiasu@constructor.university)
- **Jacob Mekdem Asfaw** (jasfaw@constructor.university) 
- **Patrick Horiszny** (phoriszny@vassar.edu)
---

*This project represents my journey into database development and web application creation. It's just a foundation from which I learned.* 

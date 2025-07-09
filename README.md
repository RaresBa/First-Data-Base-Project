# Entertainment Database Management System

## About This Project

This is my first database project - a web-based entertainment management system built with Flask and MySQL. As a beginner learning database development, I created this application to practice CRUD operations, database design, and web development fundamentals.

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

### Installation
1. Clone the repository
2. Set up a MySQL database named `brares_db`
3. Install dependencies: `pip install -r requirements.txt`
4. Configure database connection in `app.py`
5. Run the application: `python app.py`

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

---

*This project represents my journey into database development and web application creation. It's justt a foundation from which I learned.* 
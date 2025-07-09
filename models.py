from flask_sqlalchemy import SQLAlchemy

# Create db instance
db = SQLAlchemy()

# Database models

class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    debut_year = db.Column(db.Integer, nullable=False)

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    debut_year = db.Column(db.Integer, nullable=False)

class Producer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    debut_year = db.Column(db.Integer, nullable=False)

class VisualEntertainment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    studio = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    seasons = db.Column(db.Integer, nullable=True)
    end_year = db.Column(db.Integer, nullable=True)
    runtime = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.String(10), nullable=True)
    topic = db.Column(db.String(100), nullable=True)
    research_body = db.Column(db.String(100), nullable=True)

'''
class TVShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    studio = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    seasons = db.Column(db.Integer, nullable=False)
    end_year = db.Column(db.Integer, nullable=True)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    studio = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    runtime = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String(10), nullable=False)

class Documentary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    studio = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    research_body = db.Column(db.String(100), nullable=False)
'''
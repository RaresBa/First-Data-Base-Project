from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from models import db, Director, Actor, Producer, VisualEntertainment

app = Flask(__name__, template_folder='templates')  
app.secret_key = 'your_secret_key'  
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://brares:12345@localhost/brares_db?charset=utf8mb4"
db.init_app(app)


def get_db_connection():
    return mysql.connector.connect(
        host='---',  
        user='---', 
        password='---',  
        database='---'  
    )  



'''
# Database models
class TVShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    studio = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    seasons = db.Column(db.Integer, nullable=False)
    end_year = db.Column(db.Integer, nullable=True)

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

class Producer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    debut_year = db.Column(db.Integer, nullable=False)
'''

# Routes
@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/imprint')
def imprint():
    return render_template('imprint.html')

@app.route('/maintenanceLogin')
def maintenance_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('All fields are required.')
            return redirect(url_for('maintenace_login'))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Base query
    query = '''
        SELECT username, password 
        FROM UserManagement
        WHERE username = %s AND password = %s
    '''

    params = [username, password]

    # Execute the query
    cursor.execute(query, params)
    output = cursor.fetchall()

    cursor.close()
    connection.close()
    for i in output:
        if(i.username == username and i.password == password):
            return redirect(url_for('maintenance'))

    return render_template('maintenanceLogin.html')

@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')



# Director Input
@app.route('/directorInput', methods=['GET', 'POST'])
def director_input():
    if request.method == 'POST':
        name = request.form.get('name')
        birth_date = request.form.get('birthdate')
        debut_year = request.form.get('ddyear')

        if not name or not birth_date or not debut_year:
            flash('All fields are required.')
            return redirect(url_for('director_input'))

        new_director = Director(
            name=name,
            birth_date=birth_date,
            debut_year=int(debut_year)
        )
        db.session.add(new_director)
        db.session.commit()

        return redirect(url_for('feedback'))

    return render_template('directorInput.html')

# Actor Input
@app.route('/actorInput', methods=['GET', 'POST'])
def actor_input():
    if request.method == 'POST':
        name = request.form.get('name')
        birth_date = request.form.get('birthdate')
        debut_year = request.form.get('adyear')

        if not name or not birth_date or not debut_year:
            flash('All fields are required.')
            return redirect(url_for('actor_input'))

        new_actor = Actor(
            name=name,
            birth_date=birth_date,
            debut_year=int(debut_year)
        )
        db.session.add(new_actor)
        db.session.commit()

        return redirect(url_for('feedback'))

    return render_template('actorInput.html')

# Movie Input
@app.route('/movieInput', methods=['GET', 'POST'])
def movie_input():
    
    if request.method == 'POST':
        title = request.form.get('title')
        studio = request.form.get('studio')
        ryear = request.form.get('ryear')
        runtime = request.form.get('runtime')
        rating = request.form.get('rating')

        if not title or not studio or not ryear or not runtime or not rating:
            flash('All fields are required.')
            return redirect(url_for('movie_input'))

        new_movie = VisualEntertainment(
            title=title,
            studio=studio,
            release_year=int(ryear),
            runtime=int(runtime),
            rating=rating
        )

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Insert data into the database
        query = '''
        INSERT INTO VisualEntertainment (title, studio, release_year, runtime, rating) 
        VALUES (%s, %s, %d, %d, %s)
        '''
        params = [title, studio, ryear, runtime, rating]
        cursor.execute(query, params)
        db.commit()

        # Execute the query
        cursor.execute(query, params)
        people = cursor.fetchall()

        cursor.close()
        connection.close()

        #db.session.add(new_movie)
        #db.session.commit()

        return redirect(url_for('movie_feedback', success = True))

    return render_template('movieInput.html')

# Movie Feedback
@app.route('/movieFeedback', methods=['GET', 'POST'])
def movie_feedback():
    success = request.args.get('success')  # Get success status from query parameter
    return render_template('movieFeedback.html', success=success)

# TV Show Input
@app.route('/tvInput', methods=['GET', 'POST'])
def tv_input():
    if request.method == 'POST':
        title = request.form.get('title')
        studio = request.form.get('studio')
        ryear = request.form.get('ryear')
        seasons = request.form.get('seasons')
        eyear = request.form.get('eyear')

        if not title or not studio or not ryear or not seasons:
            flash('All fields except end year are required.')
            return redirect(url_for('tv_input'))

        new_tv_show = VisualEntertainment(
            title=title,
            studio=studio,
            release_year=int(ryear),
            seasons=int(seasons),
            end_year=int(eyear) if eyear else None
        )
        db.session.add(new_tv_show)
        db.session.commit()

        return redirect(url_for('feedback'))

    return render_template('tvInput.html')

# Documentary Input
@app.route('/documentaryInput', methods=['GET', 'POST'])
def documentary_input():
    if request.method == 'POST':
        title = request.form.get('title')
        studio = request.form.get('studio')
        ryear = request.form.get('ryear')
        topic = request.form.get('topic')
        research_body = request.form.get('rbody')

        if not title or not studio or not ryear or not topic or not research_body:
            flash('All fields are required.')
            return redirect(url_for('documentary_input'))

        new_documentary = VisualEntertainment(
            title=title,
            studio=studio,
            release_year=int(ryear),
            topic=topic,
            research_body=research_body
        )
        db.session.add(new_documentary)
        db.session.commit()

        return redirect(url_for('feedback'))

    return render_template('documentaryInput.html')

# Producer Input
@app.route('/producerInput', methods=['GET', 'POST'])
def producer_input():
    if request.method == 'POST':
        name = request.form.get('name')
        birth_date = request.form.get('birthdate')
        debut_year = request.form.get('pdyear')

        if not name or not birth_date or not debut_year:
            flash('All fields are required.')
            return redirect(url_for('producer_input'))

        new_producer = Producer(
            name=name,
            birth_date=birth_date,
            debut_year=int(debut_year)
        )
        db.session.add(new_producer)
        db.session.commit()

        return redirect(url_for('feedback'))

    return render_template('producerInput.html')

# Feedback Page
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

#Inception
@app.route('/inceptionSearch', methods=['GET', 'POST'])
def inceptionSearch():
    if request.method == 'POST':
        name = request.form.get('name')
        role = request.form.get('role')

        return redirect(url_for('inceptionSearch-results'))
    return render_template('inceptionSearch.html')

@app.route('/inceptionSearch-results', methods=['GET', 'POST'])
def inceptionSearch_results():
    name = request.args.get('name', "")  # Get the 'name' parameter or default to an empty string
    role = request.args.get('role', "")  # Get the 'role' parameter or default to an empty string
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Base query
    query = '''
        SELECT P.name, F.role 
        FROM People P, Features F, VisualEntertainment V 
        WHERE V.name = %s AND F.vid = V.vid AND P.pid = F.pid
    '''
    params = ["Inception"]  # This is the base parameter for the query

    # Dynamically modify the query based on provided filters
    if name and role:
        query += ' AND P.name = %s AND F.role = %s'
        params.append(name)
        params.append(role)
    elif name:
        query += ' AND P.name = %s'
        params.append(name)
    elif role:
        query += ' AND F.role = %s'
        params.append(role)

    # Execute the query
    cursor.execute(query, params)
    inception = cursor.fetchall()

    cursor.close()
    connection.close()

    if request.method == 'POST':
        name = request.form.get('name')

        return redirect(url_for('inceptionSearch-detailedresult'))

    return render_template('inceptionSearch-results.html', inception=inception)

@app.route('/inceptionSearch-detailedresult', methods=['GET', 'POST'])
def inceptionSearch_detailedresult():
    name = request.args.get('name')  

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Base query
    query = '''
        SELECT P.name, P.awards, P.experience, F.role 
        FROM People P, Features F, VisualEntertainment V 
        WHERE V.name = %s AND F.vid = V.vid AND P.pid = F.pid AND P.name = %s
    '''

    params = ["Inception", name]

        # Execute the query
    cursor.execute(query, params)
    people = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('inceptionSearch-detailedresult.html', people=people)

#Community
@app.route('/communitySearch', methods=['GET', 'POST'])
def communitySearch():
    if request.method == 'POST':
        name = request.form.get('name')
        role = request.form.get('role')

        return redirect(url_for('communitySearch-results'))
    return render_template('communitySearch.html')

@app.route('/communitySearch-results', methods=['GET', 'POST'])
def communitySearch_results():
    name = request.args.get('name', "")  # Get the 'name' parameter or default to an empty string
    role = request.args.get('role', "")  # Get the 'role' parameter or default to an empty string
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Base query
    query = '''
        SELECT P.name, F.role 
        FROM People P, Features F, VisualEntertainment V 
        WHERE V.name = %s AND F.vid = V.vid AND P.pid = F.pid
    '''
    params = ["Community"]  # This is the base parameter for the query

    # Dynamically modify the query based on provided filters
    if name and role:
        query += ' AND P.name = %s AND F.role = %s'
        params.append(name)
        params.append(role)
    elif name:
        query += ' AND P.name = %s'
        params.append(name)
    elif role:
        query += ' AND F.role = %s'
        params.append(role)

    # Execute the query
    cursor.execute(query, params)
    community = cursor.fetchall()

    cursor.close()
    connection.close()

    if request.method == 'POST':
        name = request.form.get('name')

        return redirect(url_for('communitySearch-detailedresult'))

    return render_template('communitySearch-results.html', community=community)

@app.route('/communitySearch-detailedresult', methods=['GET', 'POST'])
def communitySearch_detailedresult():
    name = request.args.get('name')  

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Base query
    query = '''
        SELECT P.name, P.awards, P.experience, F.role 
        FROM People P, Features F, VisualEntertainment V 
        WHERE V.name = %s AND F.vid = V.vid AND P.pid = F.pid AND P.name = %s
    '''

    params = ["Community", name]

        # Execute the query
    cursor.execute(query, params)
    people = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('communitySearch-detailedresult.html', people=people)

#Arrested Development
@app.route('/arrestedDevelopmentSearch', methods=['GET', 'POST'])
def arrestedDevelopmentSearch():
    if request.method == 'POST':
        name = request.form.get('name')
        role = request.form.get('role')

        return redirect(url_for('arrestedDevelopmentSearch-results'))
    return render_template('arrestedDevelopmentSearch.html')

@app.route('/arrestedDevelopmentSearch-results', methods=['GET', 'POST'])
def arrestedDevelopmentSearch_results():
    name = request.args.get('name', "")  # Get the 'name' parameter or default to an empty string
    role = request.args.get('role', "")  # Get the 'role' parameter or default to an empty string
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Base query
    query = '''
        SELECT P.name, F.role 
        FROM People P, Features F, VisualEntertainment V 
        WHERE V.name = %s AND F.vid = V.vid AND P.pid = F.pid
    '''
    params = ["Arrested Development"]  # This is the base parameter for the query

    # Dynamically modify the query based on provided filters
    if name and role:
        query += ' AND P.name = %s AND F.role = %s'
        params.append(name)
        params.append(role)
    elif name:
        query += ' AND P.name = %s'
        params.append(name)
    elif role:
        query += ' AND F.role = %s'
        params.append(role)

    # Execute the query
    cursor.execute(query, params)
    arrested = cursor.fetchall()

    cursor.close()
    connection.close()

    if request.method == 'POST':
        name = request.form.get('name')

        return redirect(url_for('arrestedDevelopmentSearch-detailedresult'))

    return render_template('arrestedDevelopmentSearch-results.html', arrested=arrested)

@app.route('/arrestedDevelopmentSearch-detailedresult', methods=['GET', 'POST'])
def arrestedDevelopmentSearch_detailedresult():
    name = request.args.get('name')  

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Base query
    query = '''
        SELECT P.name, P.awards, P.experience, F.role 
        FROM People P, Features F, VisualEntertainment V 
        WHERE V.name = %s AND F.vid = V.vid AND P.pid = F.pid AND P.name = %s
    '''

    params = ["Arrested Development", name]

        # Execute the query
    cursor.execute(query, params)
    people = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('arrestedDevelopmentSearch-detailedresult.html', people=people)

if __name__ == '__main__':
    app.run(debug=True, port=8031, host="0.0.0.0") 


from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm
import datetime
from app.res import add_film, edit_film
from app.models import Film
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User



@app.route('/')
@app.route('/index')
def index():
    filmname = request.args.get('film_name')
    if filmname:
        film = Film.query.filter_by(name=filmname).first()
    else:
        film = False
    galery = Film.query.all()
    today = datetime.datetime.now().strftime("%d %B")
    coming_soon_films = Film.query.all()
    return render_template('home/pages/home.html', galery=galery, today=today, coming_soon_films=coming_soon_films, film=film)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        print(user)
        if user is None or not user.check_password(request.form['password']):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        rememberme = False
        if request.form.getlist("rememberMe"):
            rememberme = True
        login_user(user, remember=rememberme)
        return redirect("/admin")
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    if request.method == 'POST':
        User().create(request.form['username'], request.form['email'], request.form['password'])
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    #db.session.rollback()
    return render_template('500.html'), 500

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    filmname = request.args.get('film_name')
    if filmname:
        film = Film.query.filter_by(name=filmname).first()
    else:
        film = False
    if request.method == 'POST':
        print(request.form)
        if not request.form:
            print("ccccc")
            return redirect(url_for('admin'))
        if 'file' in request.files:
            file = request.files['mainImage']
            image = file.filename
        else:
            print('no file')
            image= request.form['mainImage']
        if '2d' in request.form:
            filmType = '2d'
        else: filmType = '3d'
        film = {'id': request.form['filmId'],'name': request.form['filmName'], 'image': image, 'description': request.form['filmDescription'],
                'type': filmType, 'trailer': request.form['filmTrailer']}
        edit_film(film)
        return redirect(url_for('admin'))
    galery = Film.query.all()
    today = datetime.datetime.now().strftime("%d %B")
    coming_soon_films = Film.query.all()
    return render_template('admin/pages/films.html', galery=galery, today=today, film=film, coming_soon_films=coming_soon_films, user=current_user)


@app.route('/admin/film/new', methods=['GET', 'POST'])
@login_required
def add_new_film():
    film = {'name': '', 'image': '', 'description': '',
            'type': '', 'trailer': ''}
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['mainImage']
            image = file.filename
        else:
            print('no file')
            image= request.form['mainImage']
        if request.form['2d'] == 'on':
            filmType = '2d'
        film = {'name': request.form['filmName'], 'image': image, 'description': request.form['filmDescription'],
                'type': request.form['2d'], 'trailer': request.form['filmTrailer']}
        add_film(film)
        return redirect(url_for('admin'))
    return render_template('admin/pages/films.html', film=film, user=current_user)
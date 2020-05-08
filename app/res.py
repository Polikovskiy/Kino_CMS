from app import db
from app.models import Film, Galery, CEO_Blog
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def add_film(film):
    if film['remouteImage'] == '':
        film['remouteImage'] = 'https://lh3.googleusercontent.com/proxy/5Bk8ufycEoJ8QueSE7l_cPLwH5B7m5aRf1wFTEg-Ij1AvwDYDkHXwoNEFlJox8_XBBOHEgsetfnUt6AF1j31pAVk'
    if film['image'] == '':
        film['image'] = 'https://lh3.googleusercontent.com/proxy/5Bk8ufycEoJ8QueSE7l_cPLwH5B7m5aRf1wFTEg-Ij1AvwDYDkHXwoNEFlJox8_XBBOHEgsetfnUt6AF1j31pAVk'
    if film['trailer'] == '':
        film['trailer'] = 'https://lh3.googleusercontent.com/proxy/5Bk8ufycEoJ8QueSE7l_cPLwH5B7m5aRf1wFTEg-Ij1AvwDYDkHXwoNEFlJox8_XBBOHEgsetfnUt6AF1j31pAVk'
    if film['description'] == '':
        film['description'] = 'some description'
    film = Film(name=film['name'], image=film['image'], description=film['description'],
                type=film['type'], trailer=film['trailer'], remouteImage=film['remouteImage'])
    db.session.add(film)
    db.session.commit()


def edit_film(film):
    print(film)
    db.session.query(Film).filter_by(id=film['id']).update({'name': film['name'], 'image': film['image'], 'description': film['description'],
                'type': film['type'], 'trailer': film['trailer'], 'remouteImage': film['remouteImage']})
    db.session.commit()


def upload_file(request):
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return False
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return False
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('app/static/images/film_images/', filename))
            return os.path.join('images/film_images/', filename)
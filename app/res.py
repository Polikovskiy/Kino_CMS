from app import db
from app.models import Film, Galery, CEO_Blog
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def add_film(film):
    film = Film(name=film['name'], image=film['image'], description=film['description'],
                type=film['type'], trailer=film['trailer'])
    db.session.add(film)
    db.session.commit()

def edit_film(film):
    print(film)
    db.session.query(Film).filter_by(id=film['id']).update({'name': film['name'], 'image': film['image'], 'description': film['description'],
                'type': film['type'], 'trailer': film['trailer']})
    db.session.commit()


def upload_file(request):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return False
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return False
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('app/static/images/film_images/', filename))
            return os.path.join('images/film_images/', filename)
from app import db
from app.models import Film, Galery, CEO_Blog


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
